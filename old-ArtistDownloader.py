# -------------------- #
# INIT
# -------------------- #
import re
from youtubesearchpython import *
import argparse
from pytube import YouTube
import os
import time
from colorama import Fore, Back, Style
import shutil

print(Fore.MAGENTA + "Bienvenue sur ArtistDownloader !")
print(Fore.WHITE + "")

# -------------------- #
# VARS
# -------------------- #
list = []
listInstru = []
listAcapella = []
index = 0
value = ""
AUDIO_DOWNLOAD_DIR = ""
AUDIO_DOWNLOAD_DIR_INSTRU = ""
AUDIO_DOWNLOAD_DIR_ACAPELLA = ""
nbrMusic = 0
isInstru = 0
isAcapella = 0


# -------------------- #
# LAUNCHERS
# -------------------- #
def launch():
    global value
    global nbrMusic
    global isInstru
    global isAcapella

    print(Fore.WHITE + "Écrivez le nom d'un artiste et un dossier va se créer avec vos titres favoris.")
    value = input("Recherche : ")
    nbrMusic = int(input("Nombre de musiques : "))
    isInstru = int(input("Instrumental ? (1 : Oui | 0 : Non) : "))
    isAcapella = int(input("Acapella ? (1 : Oui | 0 : Non) : "))
    nexter()


def playlist():
    global value
    global isInstru
    global isAcapella

    print(
        Fore.WHITE + "Collez le lien de la playlist YouTube (obligatoirement publique), elle se téléchargera dans un dossier.")
    value = input("Lien : ")
    isInstru = int(input("Instrumental ? (1 : Oui | 0 : Non) : "))
    isAcapella = int(input("Acapella ? (1 : Oui | 0 : Non) : "))
    nexterPlaylist()


def auto():
    global AUDIO_DOWNLOAD_DIR
    global AUDIO_DOWNLOAD_DIR_INSTRU
    global AUDIO_DOWNLOAD_DIR_ACAPELLA
    global value
    global list
    global listInstru
    global listAcapella
    global index
    global nbrMusic
    global isInstru
    global isAcapella

    print(Fore.WHITE + "-- AUTO MODE ENABLE --")
    LISTER = ["PLACE HERE YOUR ARTISTS"]
    nbrMusic = 15
    isInstru = 1
    isAcapella = 1
    for i in LISTER:
        time.sleep(5)
        print("--- ARTISTE : ", i, " ---")
        list = []
        listInstru = []
        listAcapella = []
        index = 0
        AUDIO_DOWNLOAD_DIR = ""
        AUDIO_DOWNLOAD_DIR_INSTRU = ""
        AUDIO_DOWNLOAD_DIR_ACAPELLA = ""
        value = i
        nexter()
        print(Fore.WHITE + "--- FIN ARTISTE : ", i, " ---")


def copyPaster():
    global value
    value = input(Fore.WHITE + "Écrivez le nom du dossier que vous voulez : ")

    all_dir = os.path.join("./", value)
    if not os.path.exists(all_dir):
        os.makedirs(all_dir)

    for root, dirs, files in os.walk("./"):
        if "Audio" in dirs:
            audio_dir = os.path.join(root, "Audio")
            for audio_root, audio_dirs, audio_files in os.walk(audio_dir):
                for audio_file in audio_files:
                    if audio_file.lower().endswith(".mp4"):
                        src_path = os.path.join(audio_root, audio_file)
                        dest_path = os.path.join(all_dir, audio_file)
                        print(Fore.LIGHTGREEN_EX + "Téléchargement de : " + src_path + " vers " + dest_path)
                        shutil.copy2(src_path, dest_path)
                        print(Fore.GREEN + "Le titre vient d'être copié.")
    print(Fore.MAGENTA + "Votre téléchargement est terminé, merci !")


# -------------------- #
# NEXTERS
# -------------------- #
def nexterPlaylist():
    global AUDIO_DOWNLOAD_DIR
    global AUDIO_DOWNLOAD_DIR_INSTRU
    global AUDIO_DOWNLOAD_DIR_ACAPELLA
    global value
    global list
    global listInstru
    global listAcapella

    playlist = Playlist(value)
    while playlist.hasMoreVideos:
        playlist.getNextVideos()

    value = playlist.getInfo(value)['title']
    AUDIO_DOWNLOAD_DIR = "./" + value + "/Audio"
    AUDIO_DOWNLOAD_DIR_INSTRU = "./" + value + "/Instrumental"
    AUDIO_DOWNLOAD_DIR_ACAPELLA = "./" + value + "/Acapella"

    print("Lancement de la récupération des musiques en cours...\nCela prendra plusieurs minutes, soyez patient :)")
    for i in playlist.videos:
        hasIt = False
        hasItInstru = False
        hasItAcapella = False
        fullTitle = remove_parentheses(i['title'])

        title = fullTitle + " audio"
        videosSearchAudio = VideosSearch(title, limit=10)
        json_audio = videosSearchAudio.result()
        for i in json_audio['result']:
            if hasIt == False:
                titleAudio = i['title']
                if check_word_in_string("audio", titleAudio):
                    if not check_word_in_string("8D", titleAudio):
                        hasIt = True
                        linkAudio = i['link']
                        list.append([titleAudio, linkAudio])

        if isInstru == 1:
            titleInstru = fullTitle + " instrumental"
            videosSearchInstru = VideosSearch(titleInstru, limit=10)
            json_instru = videosSearchInstru.result()
            for i in json_instru['result']:
                if hasItInstru == False:
                    titleAudioInstru = i['title']
                    if check_word_in_string("instrumental", titleAudioInstru):
                        if not check_word_in_string("8D", titleAudioInstru):
                            hasItInstru = True
                            linkInstru = i['link']
                            listInstru.append([titleAudioInstru, linkInstru])

        if isAcapella == 1:
            titleAcapella = fullTitle + " acapella"
            videosSearchAcapella = VideosSearch(titleAcapella, limit=10)
            json_acapella = videosSearchAcapella.result()
            for i in json_acapella['result']:
                if hasItAcapella == False:
                    titleAudioAcapella = i['title']
                    if check_word_in_string("acapella", titleAudioAcapella):
                        if not check_word_in_string("8D", titleAudioAcapella):
                            hasItAcapella = True
                            linkAcapella = i['link']
                            listAcapella.append([titleAudioAcapella, linkAcapella])
    nexterer()


def nexter():
    global AUDIO_DOWNLOAD_DIR
    global AUDIO_DOWNLOAD_DIR_INSTRU
    global AUDIO_DOWNLOAD_DIR_ACAPELLA
    global value
    global list
    global listInstru
    global listAcapella
    global index
    global nbrMusic
    global isInstru
    global isAcapella

    AUDIO_DOWNLOAD_DIR = "./" + value + "/Audio"
    AUDIO_DOWNLOAD_DIR_INSTRU = "./" + value + "/Instrumental"
    AUDIO_DOWNLOAD_DIR_ACAPELLA = "./" + value + "/Acapella"
    print("Lancement de la recherche en cours...\nCela prendra plusieurs minutes, soyez patient :)")
    videosSearch = VideosSearch(value)
    json_text = videosSearch.result()
    while len(list) < nbrMusic:
        hasIt = False
        hasItInstru = False
        hasItAcapella = False
        item = get_result_at_index(json_text, index)
        if not item == None:
            if remove_after_colon(item['duration']) != "TOO LONG":
                duration = int(remove_after_colon(item['duration']))
                if duration < 8:
                    fullTitle = remove_parentheses(item['title'])
                    title = fullTitle + " audio"
                    videosSearchAudio = VideosSearch(title, limit=10)
                    json_audio = videosSearchAudio.result()
                    for i in json_audio['result']:
                        if hasIt == False:
                            titleAudio = i['title']
                            if check_word_in_string("audio", titleAudio):
                                if not check_word_in_string("8D", titleAudio):
                                    hasIt = True
                                    linkAudio = i['link']
                                    list.append([titleAudio, linkAudio])
                    if isInstru == 1:
                        titleInstru = fullTitle + " instrumental"
                        videosSearchInstru = VideosSearch(titleInstru, limit=10)
                        json_instru = videosSearchInstru.result()
                        for i in json_instru['result']:
                            if hasItInstru == False:
                                titleInstru = i['title']
                                if check_word_in_string("instrumental", titleInstru):
                                    if not check_word_in_string("8D", titleInstru):
                                        hasItInstru = True
                                        linkInstru = i['link']
                                        listInstru.append([titleInstru, linkInstru])
                    if isAcapella == 1:
                        titleAcapella = fullTitle + " acapella"
                        videosSearchAcapella = VideosSearch(titleAcapella, limit=10)
                        json_acapella = videosSearchAcapella.result()
                        for i in json_acapella['result']:
                            if hasItAcapella == False:
                                titleAcapella = i['title']
                                if check_word_in_string("acapella", titleAcapella):
                                    if not check_word_in_string("8D", titleAcapella):
                                        hasItAcapella = True
                                        linkAcapella = i['link']
                                        listAcapella.append([titleAcapella, linkAcapella])
        else:
            print(Fore.RED + "La recherche n'a pas aboutit à assez de résultats, passons au téléchargement.")
            break
        index += 1
    nexterer()


def nexterer():
    check_and_create_folder(value)
    print("\n" + Fore.GREEN + "Début de téléchargement des Audios...")
    for i in list:
        print(Fore.LIGHTGREEN_EX + "Téléchargement de : ", i[0])
        YoutubeAudioDownload(i[1])
        time.sleep(1)

    if isInstru == 1:
        print("" + Fore.GREEN + "\nDébut de téléchargement des Instrumentals...")
        for i in listInstru:
            print(Fore.LIGHTGREEN_EX + "Téléchargement de : ", i[0])
            YoutubeAudioDownload_INSTRU(i[1])
            time.sleep(1)

    if isAcapella == 1:
        print("" + Fore.GREEN + "\nDébut de téléchargement des Acapellas...")
        for i in listAcapella:
            print(Fore.LIGHTGREEN_EX + "Téléchargement de : ", i[0])
            YoutubeAudioDownload_ACAPELLA(i[1])
            time.sleep(1)

    print(Fore.MAGENTA + "Votre téléchargement est terminé, merci !")


# -------------------- #
# FUNCS
# -------------------- #
def remove_parentheses(text):
    pattern = "\([^)]*\)"
    cleaned_text = re.sub(pattern, "", text)
    return cleaned_text.strip()


def remove_after_colon(text):
    if text.count(":") == 2:
        return "TOO LONG"
    cleaned_text = text.split(":", 1)[0]
    return cleaned_text.strip()


def get_result_at_index(json_data, index):
    try:
        index = int(index)
        return json_data['result'][index]
    except (IndexError, ValueError):
        return None


def check_word_in_string(word, input_string):
    return word.lower() in input_string.lower()


def check_and_create_folder(folder_name):
    global isInstru
    global isAcapella

    current_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(current_dir, folder_name)
    folder_path_audio = os.path.join(current_dir + "/" + folder_name, "Audio")
    folder_path_instrumental = os.path.join(current_dir + "/" + folder_name, "Instrumental")
    folder_path_acapella = os.path.join(current_dir + "/" + folder_name, "Acapella")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        os.makedirs(folder_path_audio)
        if isInstru == 1:
            os.makedirs(folder_path_instrumental)
        if isAcapella == 1:
            os.makedirs(folder_path_acapella)
        print(Fore.GREEN + f"Le dossier '{folder_name}' a été créé avec succès.")
    else:
        print(Fore.YELLOW + f"Le dossier '{folder_name}' existe déjà.")


def checkAge(video_url):
    video = YouTube(video_url)
    try:
        audio = video.streams.filter(only_audio=True).first()
        return True
    except:
        return False


def YoutubeAudioDownload(video_url):
    video = YouTube(video_url)
    if checkAge(video_url) == True:
        audio = video.streams.filter(only_audio=True).first()
        try:
            audio.download(AUDIO_DOWNLOAD_DIR)
        except:
            print(Fore.RED + "Failed to download audio")
        print(Fore.GREEN + "Le titre vient d'être téléchargé.")
    else:
        print(Fore.RED + "Cette vidéo est en `Age Restricted`.")


def YoutubeAudioDownload_INSTRU(video_url):
    video = YouTube(video_url)
    if checkAge(video_url) == True:
        audio = video.streams.filter(only_audio=True).first()
        try:
            audio.download(AUDIO_DOWNLOAD_DIR_INSTRU)
        except:
            print(Fore.RED + "Failed to download audio")
        print(Fore.GREEN + "Le titre vient d'être téléchargé.")
    else:
        print(Fore.RED + "Cette vidéo est en `Age Restricted`.")


def YoutubeAudioDownload_ACAPELLA(video_url):
    video = YouTube(video_url)
    if checkAge(video_url) == True:
        audio = video.streams.filter(only_audio=True).first()
        try:
            audio.download(AUDIO_DOWNLOAD_DIR_ACAPELLA)
        except:
            print(Fore.RED + "Failed to download audio")
        print(Fore.GREEN + "Le titre vient d'être téléchargé.")
    else:
        print(Fore.RED + "Cette vidéo est en `Age Restricted`.")


# -------------------- #
# STARTERS
# -------------------- #
print(Fore.LIGHTCYAN_EX + "---------------------------")
print(Fore.MAGENTA + "ArtistDownloader " + Fore.LIGHTBLACK_EX + "•" + Fore.WHITE + " Menu")
print("1 » Télécharger avec le nom d'un artiste.")
print("2 » Télécharger une playlist avec son lien.")
print("3 » Lancer le mode automatique.")
print("4 » Copier tout les dossiers Audio et les mettre dans un dossier final.")
print("5 » Quitter l'application.")
print(Fore.LIGHTCYAN_EX + "---------------------------")
choice = int(input(Fore.YELLOW + "Faites votre choix : "))
if choice == 1:
    launch()
elif choice == 2:
    playlist()
elif choice == 3:
    auto()
elif choice == 4:
    copyPaster()
elif choice == 5:
    print(Fore.MAGENTA + "Votre téléchargement est terminé, merci !")
else:
    print(Fore.RED + "Ce choix n'existe pas.")
    print(Fore.MAGENTA + "Votre téléchargement est terminé, merci !")
