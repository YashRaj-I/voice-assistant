# pip install speechrecognition pyaudio
# pip install setuptools
# pip install pyttsx3
# pip install pocketsphinx
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary



recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song =c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    else:
        # let OpenAI handle the request
        pass

if __name__ =="__main__":
    speak("your son ujjwal is here...")
    while True:
        # listen for the wake world "jarvis"
        # obtain audio from the microphone
        r =sr.Recognizer()

        print("recognizing..")

        # recognize speech using sphinx
        try:
            with sr.Microphone() as source:
                print("Listining...")
                audio = r.listen(source , timeout=2, phrase_time_limit=2)
            command = r.recognize_google(audio)
            if (command.lower() == "ujjwal"):
                speak("yes papa")
                # listen this command
                with sr.Microphone() as source:
                    print("radha Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processcommand(command)

        except Exception as e:
            print("Error; {0}".format(e))







