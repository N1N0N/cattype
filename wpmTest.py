import wordGen
import time
import os
import threading
import json
import keyboard

testTime = 15 # UPDATE LATER


def sendSpaceCauseFuckPython():
    time.sleep(testTime)
    keyboard.press_and_release('enter')
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def wpmTest():
    print("The test begins in 3")
    time.sleep(1)
    cls()
    print("The test begins in 2")
    time.sleep(1)
    cls()
    print("The test begins in 1")
    time.sleep(1)

    timeEnd = time.time() + testTime




    sendEnter = threading.Thread(target=sendSpaceCauseFuckPython)
    sendEnter.start()


    while timeEnd > time.time():
        wordGen.generateWords()
        userInput = input("\n")




wpmTest()

