# ------------------------------------------------------------ #
# INIT

import re
import shutil
import os
import time

import yaml
from colorama import Fore
from pytube import YouTube
from youtubesearchpython import *
# ------------------------------------------------------------ #
# VAR

listLangs = []
lang: yaml
lang = None
# ------------------------------------------------------------ #
# IMPORTING LANG
langs = os.listdir("lang/")
for language in langs:
    name, extension = os.path.splitext(language)
    with open("lang/" + language, encoding='utf8') as f: tempLang = yaml.load(f, Loader=yaml.FullLoader)
    listLangs.append(tempLang)
# ------------------------------------------------------------ #
# LANG CHOICER
def langChoice() -> None:
    global lang
    lang = None
    while (lang == None):
        print("Welcome, please choose your language:")
        for i in range(len(listLangs)):
            print(i, ">", listLangs[i]["displayName"])
        langChoice = int(input("which one do you want to choose? "))
        if (langChoice >= 0 and langChoice <= len(listLangs)):
            lang = listLangs[langChoice]
            print("Language selected.")

langChoice()
# ------------------------------------------------------------ #
# CHAT SETTINGS
def chatEraser() -> None:
    for i in range(100):
        print("")

def chatColorReset() -> None:
    print(Fore.LIGHTWHITE_EX + "")

chatEraser()
# ------------------------------------------------------------ #
# STARTERS
def start() -> None:
    print(Fore.LIGHTCYAN_EX + "---------------------------")
    print(Fore.MAGENTA + "ArtistDownloader " + Fore.LIGHTBLACK_EX + "•" + Fore.WHITE + " Menu")
    print(lang["mainmenu.choice.artistname"])
    print(lang["mainmenu.choice.playlist"])
    print(lang["mainmenu.choice.automode"])
    print(lang["mainmenu.choice.finalfolder"])
    print(lang["mainmenu.choice.langchoice"])
    print(lang["mainmenu.choice.quit"])
    print(Fore.LIGHTCYAN_EX + "---------------------------")
    choice = int(input(Fore.YELLOW + lang["mainmenu.choice.text"]))
    if choice == 1:
        # launch()
        print("t")
    elif choice == 2:
        # playlist()
        print("t")
    elif choice == 3:
        # auto()
        print("t")
    elif choice == 4:
        # copyPaster()
        print("t")
    elif choice == 5:
        chatColorReset()
        langChoice()
        start()
    elif choice == 6:
        print(Fore.MAGENTA + lang["mainmenu.finish"])
    else:
        print(Fore.RED + lang["mainmenu.choice.notexist"])
        print(Fore.MAGENTA + lang["mainmenu.finish"])

print(Fore.MAGENTA + lang["mainmenu.welcome"])
print(Fore.MAGENTA + lang["mainmenu.author"] + " Curiosow.")
chatColorReset()
start()
# ------------------------------------------------------------ #
