import json


def get_name():
    global name
    name = input("What is your name? ")
    with open("settings.json", "r") as infile:
        settings = json.load(infile)
    settings["name"] = name

    with open("settings.json", "w") as outfile:
        json.dump(settings, outfile)
def get_language():
    lang_entered = False
    while not lang_entered:
        lang = input("Enter your desired language: ")
        lang_list = open('languages\languages.txt').read().splitlines()

        if lang.lower() in lang_list:
            with open('settings.json', 'r') as infile:
                settings = json.load(infile)

            settings['language'] = lang

            with open('settings.json', 'w') as outfile:
                json.dump(settings, outfile)
            lang_entered = True
        else:
            printLangs = input("The entered language is not supported yet. Do you want to see our supported languages? (y/n) ")
            if printLangs.lower() == "y":
                for lang in lang_list:
                    print(lang)


