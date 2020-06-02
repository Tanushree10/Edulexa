import speech_recognition as sr
from gtts import gTTS
import time
import os
def stt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("please say something...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        return(text)  
def tts(mytext):
    output=gTTS(text=mytext,lang="en",slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")
    time.sleep(3) 


