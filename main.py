from voice import speak, listen
from agent import process

speak("JARVIS PRO FINAL запущен")

while True:
    text = listen()
    if text:
        if text.lower() in ["exit","quit","выход"]:
            break
        answer = process(text)
        speak(answer)
