import json


def get_name():
    askName = input("What is your name? ")
    with open("settings.json", "r") as infile:
        settings = json.load(infile)
    settings["name"] = askName

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
            print("The entered language is not supported yet. We support:")
            for lang in lang_list:
                print(lang)




get_language()