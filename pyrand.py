"""
python3-randword

gets the definition of a random word
created by Connor Ruggles
"""

import json
import random
import requests
import sys

API_KEY = "YOUR API KEY HERE"
BASE_URL = "http://api.wordnik.com:80/v4/word.json/"

def load_words(path):
    try:
        filename = path + "/words_alpha.txt"
        with open(filename, "r") as dictionary:
            words = dictionary.readlines()
            words = [x.strip('\n') for x in words]
            return words
    except Exception as e:
        return str(e)

def get_def(word_list):
    num_word = random.randint(0, 370098)
    params = "/definitions?limit=200&api_key=" + API_KEY
    req = requests.get(BASE_URL + word_list[num_word] + params)
    if req.status_code == 200:
        return json.loads(json.dumps(req.json()))
    else:
        print("error retrieving word; try again later")
        sys.exit(1)

def print_defs(word_info):
    i = 1
    for defin in word_info:
        print(str(i) + ". " + defin["text"])
        i += 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "."
    english_words = load_words(path)
    word_info = get_def(english_words)
    while len(word_info) <= 0:
        word_info = get_def(english_words)
    print_defs(word_info)
