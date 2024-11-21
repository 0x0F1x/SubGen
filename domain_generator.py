import itertools
import pathlib
import re
import tldextract
import json

word_list = None
num_count = 3

def load_tld_words(tld_file):
    with open(tld_file, "r") as f:
        return json.load(f)

tld_word_map = None

def split_domain_parts(domain):
    ext = tldextract.extract(domain.lower())
    parts = ext.subdomain.split(".") + [ext.registered_domain]
    return parts

def insert_word_at_positions(parts):
    domains = []
    for w in word_list:
        for i in range(len(parts)):
            tmp_parts = parts[:-1]
            tmp_parts.insert(i, w)
            domains.append(".".join(tmp_parts + [parts[-1]]))
    return domains

def increment_numbers_in_domain(parts):
    domains = []
    parts_joined = ".".join(parts[:-1])
    digits = re.findall(r"\d{1,5}", parts_joined)
    for d in digits:
        for m in range(num_count):
            replacement = str(int(d) + 1 + m).zfill(len(d))
            tmp_domain = parts_joined.replace(d, replacement)
            domains.append("{}.{}".format(tmp_domain, parts[-1]))
    return domains

def decrement_numbers_in_domain(parts):
    domains = []
    parts_joined = ".".join(parts[:-1])
    digits = re.findall(r"\d{1,5}", parts_joined)
    for d in digits:
        for m in range(num_count):
            new_digit = int(d) - 1 - m
            if new_digit < 0:
                break
            replacement = str(new_digit).zfill(len(d))
            tmp_domain = parts_joined.replace(d, replacement)
            domains.append("{}.{}".format(tmp_domain, parts[-1]))
    return domains

def prepend_word_to_parts(parts):
    domains = []
    for w in word_list:
        for i in range(len(parts[:-1])):
            tmp_parts = parts[:-1]
            tmp_parts[i] = "{}{}".format(w, tmp_parts[i])
            domains.append(".".join(tmp_parts + [parts[-1]]))
            tmp_parts = parts[:-1]
            tmp_parts[i] = "{}-{}".format(w, tmp_parts[i])
            domains.append(".".join(tmp_parts + [parts[-1]]))
    return domains

def append_word_to_parts(parts):
    domains = []
    for w in word_list:
        for i in range(len(parts[:-1])):
            tmp_parts = parts[:-1]
            tmp_parts[i] = "{}{}".format(tmp_parts[i], w)
            domains.append(".".join(tmp_parts + [parts[-1]]))
            tmp_parts = parts[:-1]
            tmp_parts[i] = "{}-{}".format(tmp_parts[i], w)
            domains.append(".".join(tmp_parts + [parts[-1]]))
    return domains

def replace_word_in_domain(parts):
    domains = []
    for w in word_list:
        if w in ".".join(parts[:-1]):
            for w_alt in word_list:
                if w == w_alt:
                    continue
                domains.append(
                    "{}.{}".format(".".join(parts[:-1]).replace(w, w_alt), parts[-1])
                )
    return domains

def add_words_based_on_domain_length(parts):
    domains = []
    domain_length = len("".join(parts[:-1]))
    for w in word_list:
        if domain_length <= 5:
            domains.append(f"{w}.{'.'.join(parts)}")
        elif 5 < domain_length <= 10:
            domains.append(f"{parts[0]}.{w}.{'.'.join(parts[1:])}")
        else:
            domains.append(f"{w}.{'.'.join(parts[:-1])}.{parts[-1]}")
    return domains

def add_words_based_on_tld_mapping(parts):
    domains = []
    tld = parts[-1].split(".")[-1]
    if tld in tld_word_map:
        for w in tld_word_map[tld]:
            domains.append(f"{w}.{'.'.join(parts)}")
    return domains

def generate_smart_permutations(parts):
    domains = []
    for w in word_list:
        domains.append(f"{w}-{parts[0]}.{'.'.join(parts[1:])}")
        domains.append(f"{parts[0]}-{w}.{'.'.join(parts[1:])}")
        domains.append(f"{parts[0]}.{w}.{'.'.join(parts[1:])}")
    return domains

def extract_custom_tokens_from_domains(domains, wordlen):
    valid_tokens = set()
    for domain in domains:
        partition = split_domain_parts(domain)[:-1]
        tokens = set(itertools.chain(*[word.lower().split("-") for word in partition]))
        tokens = tokens.union({word.lower() for word in partition})
        for t in tokens:
            if len(t) >= wordlen:
                valid_tokens.add(t)
    return valid_tokens

def initialize_word_list(domains, wordlist, wordlen, fast):
    global word_list
    if wordlist is None:
        wordlist = pathlib.Path(__file__).parent / "data/words.txt"
    word_list = open(wordlist).read().splitlines()
    if fast:
        word_list = word_list[:10]
    word_list = list(set(word_list).union(extract_custom_tokens_from_domains(domains, wordlen)))

def generate(domains, wordlist=None, wordlen=5, fast=False, skip_init=False):
    if not skip_init:
        initialize_word_list(domains, wordlist, wordlen, fast)
    permutations = [
        insert_word_at_positions,
        increment_numbers_in_domain,
        decrement_numbers_in_domain,
        prepend_word_to_parts,
        append_word_to_parts,
        replace_word_in_domain,
        add_words_based_on_domain_length,
        add_words_based_on_tld_mapping,
        generate_smart_permutations,
    ]
    for domain in set(domains):
        parts = split_domain_parts(domain)
        for perm in permutations:
            for possible_domain in perm(parts):
                yield possible_domain

def generate_domains(tld_file, sub_file):
    global tld_word_map
    tld_word_map = load_tld_words(tld_file)

    with open(sub_file, "r") as f:
        domains = f.read().splitlines()

    wordlist = None
    wordlen = 5
    fast = False

    results = set(generate(domains, wordlist=wordlist, wordlen=wordlen, fast=fast))
    
    return results
