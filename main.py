import argparse
from domain_generator import generate_domains
from subdomain_generator import subdomain_creator
from GAN import GAN
import re
import os

def parse_level(level):

    if '-' in level:
        min_dot_count, max_dot_count = level.split('-')
        return int(min_dot_count), int(max_dot_count)
    else:

        return int(level), int(level)

def filter_lines_by_dot_count(input_file, output_file, min_dot_count, max_dot_count):

    with open(input_file, "r", encoding="utf-8") as infile:

        with open(output_file, "w", encoding="utf-8") as outfile:

            for line_number, line in enumerate(infile, start=1):

                dot_count = line.count(".")
                if min_dot_count <= dot_count <= max_dot_count:
                    outfile.write(line) 

def main():

    parser = argparse.ArgumentParser(description="A tool for subdomain and domain generation.")
    parser.add_argument("-u", "--base-domain", required=True, help="Base domain to use, e.g., example.com")
    parser.add_argument("-w", "--words-file", default="data/words.txt", help="Path to the words file (default: words.txt)")
    parser.add_argument("-sub", "--sub-file", required=True, help="Path to the subdomains file")
    parser.add_argument("-o", "--output-file", required=True, help="Path to save the output file")
    parser.add_argument("--level", help="Level of subdomain depth, e.g., '2' or '2-4'", required=True)

    args = parser.parse_args()


    sub_file = args.sub_file
    words_file = args.words_file
    output_file = args.output_file
    base_domain = args.base_domain


    min_dot_count, max_dot_count = parse_level(args.level)


    temp_output_file = "temp" 
    levelsub = (min_dot_count, max_dot_count)
    generated_domains = GAN(sub_file, words_file, levelsub, base_domain)
    subdomain_creator(all_feature=None, sub_file=sub_file, words_file=words_file)
    with open(temp_output_file, 'w') as file:
        with open(sub_file, 'r') as sub_f:
            subdomains = sub_f.readlines()
            file.writelines(subdomains)

    results = generate_domains("data/tld_words.json", sub_file)

    with open(temp_output_file, 'a') as file:
        for result in results:
            file.write(result + '\n')


    with open(temp_output_file, 'a') as file:
        for domain in generated_domains:
            file.write(domain + '\n')

    target_word = args.base_domain

    with open(temp_output_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    lines = list(set(lines))


    with open(words_file, 'r') as file:
        words = file.readlines()
    for word in words:
        subdomain = f"{word.strip()}.{base_domain}"
       

    with open(temp_output_file, 'w') as output_file:
        for subdomain in subdomains:
            output_file.write(subdomain + '\n')

    cleaned_lines = []
    for line in lines:
        line = line.strip()

 
        if not re.match(r'^[a-zA-Z0-9]', line):
            continue

        line = line.replace('..', '.')

        if not line.endswith(target_word):
            continue

        cleaned_lines.append(line)


    with open(temp_output_file, 'w', encoding='utf-8') as file:
        for line in cleaned_lines:
            file.write(line + '\n')

    filter_lines_by_dot_count(temp_output_file, args.output_file, min_dot_count, max_dot_count)
    os.remove(temp_output_file)

if __name__ == "__main__":
    main()

