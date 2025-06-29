# pip install speechrecognition pyaudio
# pip install setuptools
# pip install pyttsx3
# pip install pocketsphinx

# import google.generativeai as genai

# # Load your API key from file
# with open(r'C:\Users\Asus\Documents\LLM\GeminiapiKey.env') as f:
#     api_key = f.read().strip()

# genai.configure(api_key=api_key)
# model = genai.GenerativeModel('gemini-1.5-flash')


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
        pass
        # response = model.generate_content(c)
        # reply = response.text
        # print("Gemini:", reply)
        # speak(reply)
if __name__ =="__main__":
    speak("Hello, I am Radha, your personal assistant. How can I help you?")
    while True:
        # listen for the wake world "jarvis"
        # obtain audio from the microphone
        r =sr.Recognizer()

        print("recognizing..")

        # recognize speech using sphinx
        try:
            with sr.Microphone() as source:
                print("Listining...")
                audio = r.listen(source , timeout=5, phrase_time_limit=5)
            command = r.recognize_google(audio)
            if "radha" in command.lower():
                speak("ya ")
                with sr.Microphone() as source:
                    print("Radha Active...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    processcommand(command)

        except Exception as e:
            print("Error; {0}".format(e))







