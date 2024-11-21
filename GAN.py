import random
import torch
import torch.nn as nn
import torch.optim as optim

class Generator(nn.Module):
    def __init__(self, input_size, output_size):
        super(Generator, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_size, 128),
            nn.ReLU(),
            nn.Linear(128, 256),
            nn.ReLU(),
            nn.Linear(256, output_size),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.fc(x)

class Discriminator(nn.Module):
    def __init__(self, input_size):
        super(Discriminator, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_size, 256),
            nn.LeakyReLU(negative_slope=0.01), 
            nn.Linear(256, 128),
            nn.LeakyReLU(negative_slope=0.01), 
            nn.Linear(128, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.fc(x)


def create_training_data(domains):

    domain_features = []
    for domain in domains:
        parts = domain.split(".")
        features = [len(part) for part in parts]
        domain_features.append(features)

    max_length = max(len(features) for features in domain_features)
    padded_features = [features + [0] * (max_length - len(features)) for features in domain_features]

    return torch.tensor(padded_features, dtype=torch.float32)

def generate_synthetic_data(generator, real_data):
    noise = torch.randn(real_data.size(0), real_data.size(1))
    noise = torch.randn(real_data.size(0), real_data.size(1)) * 10  

    synthetic_data = generator(noise)
    return synthetic_data

def train_gan(real_data, num_epochs=2995):
    generator = Generator(input_size=real_data.size(1), output_size=real_data.size(1))
    discriminator = Discriminator(input_size=real_data.size(1))

    criterion = nn.BCELoss()
    optimizer_g = optim.Adam(generator.parameters(), lr=0.0004, betas=(0.5, 0.999))
    optimizer_d = optim.Adam(discriminator.parameters(), lr=0.0004, betas=(0.5, 0.999))

    for epoch in range(num_epochs):
        optimizer_d.zero_grad()

        real_labels = torch.ones(real_data.size(0), 1)
        fake_labels = torch.zeros(real_data.size(0), 1)

        real_output = discriminator(real_data)
        d_loss_real = criterion(real_output, real_labels)

        fake_data = generate_synthetic_data(generator, real_data)
        fake_output = discriminator(fake_data.detach())
        d_loss_fake = criterion(fake_output, fake_labels)

        d_loss = d_loss_real + d_loss_fake
        d_loss.backward()
        optimizer_d.step()

        optimizer_g.zero_grad()

        fake_output = discriminator(fake_data)
        g_loss = criterion(fake_output, real_labels)
        g_loss.backward()
        optimizer_g.step()

        if epoch % 500 == 0:
            print(f"Epoch [{epoch}/{num_epochs}], D Loss: {d_loss.item()}, G Loss: {g_loss.item()}")

    return generator

def convert_to_domain_format(synthetic_data, base_domain, words, level_range=(1, 5), max_subdomain_length=8):

    words = [word for word in words if len(word) <= max_subdomain_length]

    domain_names = []
    for data in synthetic_data:
        num_subdomains = random.randint(level_range[0], level_range[1])
        subdomains = []

        for _ in range(num_subdomains):
            subdomain = random.choice(words)
            if subdomain not in subdomains:  
                subdomains.append(subdomain)

        full_domain = '.'.join(subdomains) + '.' + base_domain
        domain_names.append(full_domain)
    
    return domain_names


def GAN(sub_file, words_file, level_range, base_domain):
    with open(sub_file, 'r') as f:
        domains = [line.strip() for line in f.readlines()]

    with open(words_file, 'r') as f:
        words = [line.strip() for line in f.readlines()]

    real_data = create_training_data(domains)
    generator = train_gan(real_data, num_epochs=3000)  
    synthetic_data = generate_synthetic_data(generator, real_data.repeat(1000, 1)) 
    new_domains = convert_to_domain_format(synthetic_data, base_domain, words, level_range)
    
    return new_domains
