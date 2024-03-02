import json

def get_language():
    lang = input("Enter your desired language: ")
    lang_list = json.loads(open("languages\languages.json").read())


get_language()

