import pyttsx3
import os
pyttsx3.speak("Welcome to my Bot ")
while True:
    print("------------------------------------------------")
    print("Open any softwares as your wish: ",end='')
    p = input()
    if((("run" in p) or ("execute" in p) or ("open" in p)) and (("chrome browser" in p) or ("browser" in p))):
        pyttsx3.speak("Opening the chrome browser")
        os.system("chrome")

    elif((("run" in p) or ("execute" in p) or ("open" in p) or ("play" in p)) and (" media player" in p)):
        pyttsx3.speak("Opening the windows media player")
        os.system("wmplayer")

    elif((("run" in p) or ("execute" in p) or ("open" in p) or ("calc" in p)) and ("calculator" in p)):
        pyttsx3.speak("Opening the Calculator")
        os.system("calc")

    elif((("run" in p) or ("execute" in p) or ("open" in p)) and (("text" in p) or ("notepad" in p) or ("editor" in p))):
        pyttsx3.speak("Opening the notepad IDE")
        os.system("notepad")

    elif((("run" in p) or ("execute" in p) or ("open" in p)) and (("keyboard" in p) or ("osk" in p) or ("on screen keyboard" in p))):
        pyttsx3.speak("Opening the On Screen Keyboard")
        os.system("osk")

    elif((("run" in p) or ("execute" in p) or ("open" in p)) and (("text" in p) or ("DEV C++" in p) or ("editor" in p) or ("IDE" in p))):
        pyttsx3.speak("Opening the Dev C++ IDE")
        os.system("devcpp")

    elif((("run" in p) or ("execute" in p) or ("open" in p)) and (("text" in p) or ("notepad++" in p) or ("editor" in p) or ("IDE" in p))):
        pyttsx3.speak("Opening the notepad++ IDE")
        os.system("notepad++")
    elif("exit" in p) or ("quit" in p):
        break
    else:
        pyttsx3.speak("We Apologise the Programs are not avalilable here but will come soon")
        print("---------------------------------------")
        print("Does not support")
        print("---------------------------------------")