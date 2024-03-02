import json


def settingMenu():
    exit = False
    while exit is False:

        print("1 | Change language")
        print("2 | Change name")
        print("3 | Change test time")
        settingsChoice = int(input("\n"))

        if settingsChoice == 1:
            get_language()
            exit = True
        elif settingsChoice == 2:
            get_name()
            exit = True
        elif settingsChoice == 3:
            get_testtime()
            exit = True
        else:
            exit = True
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

def get_testtime():
    time_entered = False
    while not time_entered:
        testTime = int(input("Enter the test time: "))
        if testTime >= 1:
            with open("settings.json", "r") as infile:
                settings = json.load(infile)
            settings['testtime'] = testTime
            with open('settings.json', 'w') as outfile:
                json.dump(settings, outfile)
            time_entered = True
        else:
            print("Enter a valid time!")
