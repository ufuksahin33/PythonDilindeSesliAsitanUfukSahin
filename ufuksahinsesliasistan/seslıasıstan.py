from cProfile import run
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import date, datetime
import random
from random import choice
from pydub import AudioSegment
import webbrowser

r= sr.Recognizer

#def speeding():
    #in_path = 'answer.mp3'
    #ex_path = 'speed.mp3'
    #sound = AudioSegment.from_file(in_path)
    #slower_sound = speed_swifter(sound, 1.1)
    #slower_sound.export(ex_path, format="mp3")

def speed_swifter(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    return sound_with_altered_frame_rate

def record(ask=False):
   with sr.Microphone()as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice=""
        try:
            voice = r.recognice_google (audio, language= "tr-TR")
        except sr.UnknownValueError:
            print ("Asistan: Demek İstediğinizi Anlayamadım Lütfen Tekrar Eder Misiniz ?")
        except sr.RequestError:
            print ("Asistan: Sistem Kaynaklı Arıza Lütfen Tekrar deneyin !")
        return voice



def response(voice):
    if "Merhaba" in voice:
          speak("Merhaba")
    if "Selam" in voice:
          speak("Selam,Nasıl Yardımcı Olabilirim ?")
    if "Teşekkür Ederim" in voice or "Teşekkürler" in voice:
           speak ("Rica Ederim")
    if "Görüşürüz" in voice:
         speak("Görüşmek Üzere")
         exit() 

    if "Bugün Günlerden Ne" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
          today = "Pazartesi"

        elif today =="Tuesday":
            today= "Salı"

        elif today == "Wednesday":
            today == "Çarşamba"

        elif today == "Thursday":
            today = "Perşembe"

        elif today == "Friday":
            today = "Cuma"

        elif today =="Saturday":
             today ="Cumartesi"

        elif today == "Sunday":
            today = "Pazar"

        speak (today)

    if "Saati Söyler Misin" in voice:
        datetime.datetime.now
        selection = ["Saat Şu An:", "Hemen Bakıyorum Bekleyin Lütfen:"]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice (selection)
        speak (selection + clock)

    if "google'da ara" in voice:
        speak ("Ne Aramamı İstersiniz ?")
        search = record ()
        url= "https://www.google.com/search?q{}" .format(search)
        webbrowser.get().open(url)
        speak ("{} içi Google'da bulabildiklerimi listeliyorum.".format (search))

    if "uygulama aç" in voice:
        speak ("Hangi Uygulamayı Açmamı İstersiniz ?")
        runApp= record()
        runApp =runApp.lower
        if "Visual Studio Code" in runApp:
            os.startfile("D:\Program Files\Visual Studio Code\Microsoft VS Code\Code.exe")
            speak ("İstediğin uygulama yüklü değil. Çalıştıramıyorum.")
        else:
          speak ("İstediğin uygulama çalıştırma listemde yok.")
    if "not olarak tut" in voice:
        speak ("Dosya ismi ne olsun istersiniz?")
        txtFile = record()+".txt"
        speak ("Ne not tutmamı istiyorsunuz?")
        theText = record()
        f = open(txtFile, "w", encoding="utf-8")
        f.writelines(theText)
        f.close()


def speak(string):
    tts= gTTS(text=string, lang="tr")
    file="answer.mp3"
    tts.save(file)
   # speeding()
    playsound("speed.mp3")
    os.remove(file)
   # os.remove("speed.mp3")

def test (wake):
     if"Merhaba Sesli Asistan" in wake: 
       playsound("ases.mp3")
       wake= record()
       if wake != '' :
         voice= wake.lower()
         print (wake.captalize())
         response(voice)

#speak("Merhaba Ben Ufuk Şahin'in yaptığı Sesli asistanım size nasıl yardımcı olabilirim ?")
playsound("ases.mp3")

while True:
    wake = record ()
    if wake !='':
      wake = wake.lower()
      print(wake.capitalize())
      test (wake)

