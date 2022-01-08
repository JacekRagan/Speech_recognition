# Python program to translate
# speech to text and text to speech
import os
from sys import modules
import webbrowser
import keyboard
import speech_recognition as sr
import pyttsx3
import pyautogui as pya
import time
from datetime import datetime
from datetime import date
from playsound import playsound


#sciezki do komend
opgg = 'https://euw.op.gg/summoner/userName=Kaellyneliacel'
yt = 'https://www.youtube.com/'
chess = 'https://lichess.org/'
librus = 'https://portal.librus.pl/rodzina/synergia/loguj'
twitch = 'https://www.twitch.tv/'
github = 'https://github.com/JacekRagan'
PATH = "C:\Program Files\Google\Chrome\Application\chrome.exe"
# Initialize the recognizercls
r = sr.Recognizer()


# Function to convert text to
# speech

def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


SpeakText(f"Witam sluże do usług{os.getlogin()}")
playsound('D:\python\music\sound.mp3')
#komendy ktore ten bot obsluguje 
pya.alert(title="KOMENDY",text=" Youtube, Twitch, Szachy, Librus, Przedstaw sie, Shutdown, Czas, Steam, Szukaj, Github, OPGG, Zamknij")


# Loop infinitely for user to
# speak
while (1):

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # Klawisz pod mowienie
        if keyboard.record(until="Page up"):
            SpeakText(f"Slucham {os.getlogin()}")
            with sr.Microphone() as source2:
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # listens for the user's input
                audio2 = r.listen(source2)

                # Jezyk rozpoznawania glosu
                MyText = r.recognize_google(audio2, language='pl-PL')
                MyText = MyText.lower()
                print(f"did u say {MyText}")
        if MyText == "youtube":
            SpeakText("otwieram youtuba")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(PATH))
            webbrowser.get('chrome').open_new_tab(yt)
        elif MyText == "szachy":
            SpeakText("Otwieram szachy")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(PATH))
            webbrowser.get('chrome').open_new_tab(chess)
        elif MyText == 'librus':
            SpeakText("Otwieram librusa")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(PATH))
            webbrowser.get('chrome').open_new_tab(librus)
        elif MyText == 'twitch':
            SpeakText("Otwieram twitch")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(PATH))
            webbrowser.get('chrome').open_new_tab(twitch)
        elif MyText == 'shutdown':
            SpeakText("Zamykam komputer")
            cos = pya.confirm('Czy napewno chcesz zamknac komputer?', buttons=['Tak', 'Anuluj'])
            if cos == 'Tak':
                os.system("shutdown /s /t 1")
            else:
                continue
        elif MyText == 'czas':
           SpeakText(datetime.now())

        elif MyText == 'przedstaw sie':
            SpeakText('Jestem Glacier')

        elif MyText == 'steam':
            SpeakText("Otwieram Steam")
            os.system("D:\steam\steam.exe")
        elif 'szukaj' in MyText:
            SpeakText("szukam")
            MyText=MyText.replace("szukaj", "")
            url = "google.com/search?q=" + MyText
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(PATH))
            webbrowser.get('chrome').open_new_tab(url)
        elif MyText == 'github':
            SpeakText('Otwieram githuba')
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(PATH))
            webbrowser.get('chrome').open_new_tab(github)
        elif MyText == 'op.gg':
            SpeakText('Otwieram opgg')
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(PATH))
            webbrowser.get('chrome').open_new_tab(opgg)
        elif MyText == 'zamknij':
            SpeakText("Dowidzenia")
            break

        



    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        SpeakText("Nie zrozumiałam możesz powtórzyć?")

    except sr.UnknownValueError:
        print("unknown error occured")
        SpeakText("Błąd")
