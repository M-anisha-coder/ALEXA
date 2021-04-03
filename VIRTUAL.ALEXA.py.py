import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import sys
import webbrowser
import smtplib
 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour =int(datetime.datetime.now().hour)
    if hour>=0and hour<12:
     speak("good morning")
    elif hour>=12 and hour<18:  
     speak("good afternoon")
    elif hour>=18 and hour<21:
     speak("good evening")
    else:
     speak("good night")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print("listening...")
      r.pause_threshold = 1
      audio = r.listen(source)

      try:
          print("recogniting...")
          query = r.recognize_google( audio,language='en-in')
          print(f"user said :{query}\n")
      except Exception as e:
          print("say that again please...")
          return "none"
      return query



          
if __name__=="__main__":
    wishme()
    
    while True:
        query = takecommand().lower()

        if "wikipedia" in query:
            speak(" searching  wikipedia....")
            query =query.replace("wikipedia" ,"")
            result =wikipedia.summary(query, sentences = 4)
            speak("According to wikipedia...")
            print(result)
            speak(result) 
            
        elif "open youtube" in query: 
           speak(" mam what should i search on youtube ")
           cm = takecommand().lower()
           speak("searching ..")
           webbrowser.open(f"https://www.youtube.com/results?search_query={cm}")

        elif "open google" in query:
           speak(" mam what should i search on google ")
           x = takecommand().lower()
           speak("searching ..")
           webbrowser.open(f"https://www.google.com/search?q={x}")

        elif "open instagram" in query:
               speak("opening insta")
               webbrowser.open("https://www.instagram.com")
           
        elif "open google meet" in query:
            speak("opening")
            webbrowser.open("https://meet.google.com")
            
        elif  "open whatsapp" in query:
            speak("opening whatsapp")
            webbrowser.open("https://web.whatsapp.com")
 
        elif "play song" in query:
            speak("playing ..")
            webbrowser.open("https://gaana.com/search/song")

        elif "open my website" in query:
             speak("opening your website")
             webbrowser.open("https://code.sololearn.com/Wpd5BR9Z31lE/?ref=app
              
