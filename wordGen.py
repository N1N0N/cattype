import json
import random


def generateWords():
    with open('settings.json', 'r') as infile:
        settings = json.load(infile)

    lang = settings['language']
    wordSet = f'languages/{lang}.json'

    with open(wordSet, 'r') as data:
        words_data = json.load(data)
        words_list = words_data['words']

    generatedWords = ' '.join(random.choice(words_list) for _ in range(300))

    return generatedWords
