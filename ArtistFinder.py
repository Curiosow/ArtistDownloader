# ------------------------------------------------------------ #
# INIT

import yaml
from colorama import Fore
# ------------------------------------------------------------ #
# VAR

lang: yaml
lang = None
value = None
searchNbrMusic = 0
instrumental = False
acapella = False
# ------------------------------------------------------------ #
def setValues(language: yaml) -> None:
    global lang

    lang = language

def launch() -> None:
    global value,searchNbrMusic,instrumental,acapella

    print(Fore.WHITE + lang['artistfinder.search'])
    value = str(input(lang['valueName']))
    searchNbrMusic = int(input(lang['artistfinder.nbrmusic']))
    instrumental = bool(int(input(lang['artistfinder.instrumental'])))
    acapella = bool(int(input(lang['artistfinder.acapella'])))
# ------------------------------------------------------------ #
