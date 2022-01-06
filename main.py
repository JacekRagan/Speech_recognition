# Python program to translate
# speech to text and text to speech
import webbrowser
import keyboard
import speech_recognition as sr
import pyttsx3

yt = 'https://www.youtube.com/'
chess = 'https://lichess.org/'
librus = 'https://portal.librus.pl/rodzina/synergia/loguj'
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


SpeakText("Witam sluże do usług")
# Loop infinitely for user to
# speak
while (1):

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        if keyboard.record(until="alt"):
            with sr.Microphone() as source2:
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # listens for the user's input
                audio2 = r.listen(source2)

                # Using ggogle to recognize audio
                MyText = r.recognize_google(audio2, language='pl-PL')
                MyText = MyText.lower()
                print(f"did u say {MyText}")
        if MyText == "youtube":
            SpeakText("otwieram youtuba")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(PATH))
            webbrowser.get('chrome').open_new_tab(yt)
        elif MyText == "chess":
            SpeakText("Otwieram szachy")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(PATH))
            webbrowser.get('chrome').open_new_tab(chess)
        elif MyText == 'librus':
            SpeakText("Otwieram librusa")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(PATH))
            webbrowser.get('chrome').open_new_tab(librus)



    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
