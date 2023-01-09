import speech_recognition as sr
import pyttsx3 as ttx
import pyaudio

# Apprendre à écouter
listener = sr.Recognizer()
engine = ttx.init()
assistant_voice = engine.getProperty('voices')
# engine.setProperty('voice', assistant_voice[1].id)
engine.setProperty('voice', 'french')


def parler(text):
    engine.say(text)
    engine.runAndWait()


def ecouter():
    try:
        with sr.Microphone() as source:
            print("Parlez maintement")
            voix = listener.listen(source)
            # interpreter la voix
            command = listener.recognize_google(voix, language='fr-FR')
            command = command.lower()
    except:
        pass
    return command


def lancer_assistant():
    command = ecouter()
    print(command)
    if 'bonjour' in command:
        text = 'bonjour , cava?'
        parler(text)

    search = 'mets la chanson de'
    if search in command:
        singer = command.replace(search, '')
        print(singer)
        parler(singer)


lancer_assistant()
