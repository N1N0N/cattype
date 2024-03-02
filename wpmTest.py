import wordGen
import time
import os
import threading
import json
import keyboard
import math



def load_testtime():
    with open("settings.json", "r") as infile:
        settings = json.load(infile)
    return int(settings.get('testtime'))



def sendSpaceCauseFuckPython():
    testTime = load_testtime()
    time.sleep(testTime)
    keyboard.press_and_release('enter')


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def wpmTest():
    testTime = load_testtime()
    print("The test begins in 3")
    time.sleep(1)
    cls()
    print("The test begins in 2")
    time.sleep(1)
    cls()
    print("The test begins in 1")
    time.sleep(1)
    cls()

    generatedString = wordGen.generateWords()
    print(generatedString + "\n")

    sendEnter = threading.Thread(target=sendSpaceCauseFuckPython)
    sendEnter.start()

    userInput = input()
    wordInput = len(userInput.split())


    correct_characters = sum(
        1 for user_char, generated_char in zip(userInput, generatedString) if user_char == generated_char)
    total_characters = len(userInput)

    accuracy = (correct_characters / total_characters) * 100 if total_characters > 0 else 0
    wpmTime = testTime / 60
    wpm = wordInput / wpmTime

    print(f"Word per Minute: {wpm}")
    print(f"Accuracy: {accuracy:.2f}%")
    with open("statsList.txt", "a") as stats:
        stats.write(f"{wpm}\n")

def checkStats():
    wpmLst = []
    with open("statsList.txt", "r") as statsList:
        for line in statsList:
            wpmLst.append(line)
        wpmLst = list(map(str.strip,wpmLst))
        wpmLst = [float(i) for i in wpmLst]
        averageWpm = math.fsum(wpmLst) / len(wpmLst)
    print(f"Average WPM: {averageWpm}")