import speech_recognition as sr
import webbrowser
import time
import musiclib

r = sr.Recognizer()

def speak(text): 
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("voice",
    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0")
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def processCommand(voicecmd):
    voicecmd = voicecmd.lower()
    print(voicecmd)
    if "open youtube" in voicecmd:
        speak("Opening Youtube")
        webbrowser.open_new_tab("https://youtube.com")
    elif "open google" in voicecmd:
        speak("Opening Google")
        webbrowser.open_new_tab("https://google.com")   
    elif "open linkedin" in voicecmd:
        speak("Opening LinkedIn")
        webbrowser.open_new_tab("https://linkedin.com")     
    elif "open instagram" in voicecmd:
        speak("Opening Instagram")
        webbrowser.open_new_tab("https://instagram.com")
    elif "open facebook" in voicecmd:
        speak("Opening Facebook")
        webbrowser.open_new_tab("https://facebook.com")  
    elif voicecmd.lower().startswith("play"):
       songs = voicecmd.lower().replace("play","").strip()
       if songs in musiclib.song:
           link = musiclib.song[songs]
           speak(f"Playing {songs}")
           webbrowser.open_new_tab(link)


  

if __name__ == "__main__":
        speak("Intializing Iris")
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
       
      
        while(True):    
            try:
                with sr.Microphone() as source:
                    print("Listening....")
                    audio = r.listen(source,timeout=5,phrase_time_limit=3)
                
                word = r.recognize_google(audio).lower()
                print(word)

                if "iris" in word:
                    speak("Yes") 
                    time.sleep(0.2)
                    with sr.Microphone() as source:
                       
                       print("Iris Activate")
                       audio = r.listen(source, timeout=5, phrase_time_limit=3)

                    command = r.recognize_google(audio)
                    processCommand(command)
                    
            except sr.WaitTimeoutError:
                print("No speech detected")

            except sr.UnknownValueError:
                print("Could not understand audio")

            except sr.RequestError as e:
                print("Internet error:", e)

            except Exception as e:
                print("Unexpected error:", repr(e))

            time.sleep(0.5)    