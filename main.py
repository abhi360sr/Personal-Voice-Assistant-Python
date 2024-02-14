#setting up jarvis
import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime
from random import choice 
from utils import opening_text
from functions.offline import notepad,microsoftword,calculator,cmpt
USERNAME=config('USERNAME')
BOTNAME=config('BOTNAME')
engine=pyttsx3.init('sapi5')
engine.setProperty('rate',190)
engine.setProperty('volume',1.0)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#Setting up speak
def speak(text):
    
    engine.say(text)
    engine.runAndWait()
#Greeting function

def greet_user():
    hour=datetime.now().hour
    if (hour>=3) and (hour<12):
        speak(f"Good Morning {USERNAME}")
    elif (hour>=12) and (hour <19):
        speak(f"Good Afternoon{USERNAME}")
    elif(hour>=19)and(hour<24): 
        speak(f"Good eavening{USERNAME}")
    else:
        speak("Hello sir nice to meet you") 
    speak(f"I am {BOTNAME}, Your personal assistant ready to help you")    
    
def take_user_input():
    r=sr.Recognizer() 
    with sr.Microphone() as source1:
        print('Listening...')
        r.pause_threshold=1
        audio=r.listen(source1)
    try:
        print('Recognizing...')
        query=r.recognize_google(audio,language='en-in')
        if(not('exit'in query or 'stop' in query)):
            speak(choice(opening_text))
        else:
            hour=datetime.now().hour
            if hour>=21 and hour< 3:
                speak("Good night sir, take care")
            else:
                speak("Have a good day sir")
            exit()
    except Exception:
        speak('Sorry,I could not understand.Could you please say that again')            
        query=None 
    return query     

if __name__=='__main__':
    greet_user()
    query=take_user_input()
    if ('open notepad' in query):
        notepad()
    elif('open calculator' in query):
       calculator() 
    elif('open word' in query):
        microsoftword()
    