import json
import random


def generateWords():
    lst = []
    with open('settings.json', 'r') as infile:
        settings = json.load(infile)

    lang = settings['language']

    wordSet = f'languages/{lang}.json'

    with open(wordSet, 'r') as data:
        words_data = json.load(data)
        words_list = words_data['words']


    for i in range(500):
        random_word = random.choice(words_list)
        print(random_word, end=" ")
        lst.append(random_word)
