import re

NUM_COUNT = 3

def load_words_from_file(file_path):
    with open(file_path, "r") as f:
        return f.read().splitlines()

def create_subdomains(parts, words):
    subdomains = []
    for w in words:
        for i in range(len(parts) - 2):
            tmp_parts = parts[:]
            tmp_parts.insert(i, w)
            subdomains.append(".".join(tmp_parts))
    return subdomains

def append_word_at_every_position(parts, words):
    subdomains = []
    for w in words:
        for i in range(len(parts) - 2):
            tmp_parts = parts[:]
            tmp_parts[i] = "{}{}".format(tmp_parts[i], w)
            subdomains.append(".".join(tmp_parts))
            tmp_parts[i] = "{}-{}".format(tmp_parts[i], w)
            subdomains.append(".".join(tmp_parts))
    return subdomains

def prepend_word_at_every_position(parts, words):
    subdomains = []
    for w in words:
        for i in range(len(parts) - 2):
            tmp_parts = parts[:]
            tmp_parts[i] = "{}{}".format(w, tmp_parts[i])
            subdomains.append(".".join(tmp_parts))
            tmp_parts[i] = "{}-{}".format(w, tmp_parts[i])
            subdomains.append(".".join(tmp_parts))
    return subdomains

def adjust_number_in_subdomains(parts):
    subdomains = []
    for i in range(len(parts) - 2):
        digits = re.findall(r"\d{1,3}", parts[i])
        if digits:
            for d in digits:
                for m in range(NUM_COUNT):
                    new_digit = str(int(d) + 1 + m).zfill(len(d))
                    tmp_parts = parts[:]
                    tmp_parts[i] = tmp_parts[i].replace(d, new_digit)
                    subdomains.append(".".join(tmp_parts))

                    new_digit = str(int(d) - 1 - m).zfill(len(d)) if int(d) - 1 - m >= 0 else ''
                    if new_digit:
                        tmp_parts = parts[:]
                        tmp_parts[i] = tmp_parts[i].replace(d, new_digit)
                        subdomains.append(".".join(tmp_parts))

    return subdomains

def split_domain(domain):
    return domain.split(".")

def subdomain_creator(all_feature, sub_file, words_file):

    with open(sub_file, "r") as f:
        domains = f.read().splitlines()

    words = load_words_from_file(words_file)

    wordlist = None
    wordlen = 5
    fast = False

    permutations = [
        create_subdomains,
        prepend_word_at_every_position,
        append_word_at_every_position,
        adjust_number_in_subdomains
    ]
    
    results = set()

    for domain in set(domains):
        parts = split_domain(domain)
        for perm in permutations:
            if perm == adjust_number_in_subdomains:
                for possible_domain in perm(parts):
                    results.add(possible_domain)
            else:
                for possible_domain in perm(parts, words):  
                    results.add(possible_domain)

  
    for result in results:
        print(result)
