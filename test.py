import pyttsx3
import time

engine = pyttsx3.init()

for i in range(3):
    print("Speaking", i + 1)
    engine.say(f"Test number {i + 1}")
    engine.runAndWait()
    time.sleep(1)
