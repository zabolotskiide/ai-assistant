import pyttsx3, speech_recognition as sr
engine = pyttsx3.init()
def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        return r.recognize_google(audio, language="ru-RU")
    except:
        return ""
