import speech_recognition as sr
import webbrowser
import pyttsx3

r = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("Say command now...")
    audio = r.listen(source, timeout=6, phrase_time_limit=6)

try:
    text = r.recognize_google(audio).lower()
    print("Heard:", text)

    if "google" in text:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "youtube" in text:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

except Exception as e:
    print("Error:", e)
