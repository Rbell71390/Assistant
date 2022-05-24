# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:17:08 2021

@author: Rachel Bell
"""
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

#changes voice to female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
#greeting from assistant
    engine.say(text)
    engine.runAndWait()
    

def take_command():
#in case mic doesn't work or something goes wrong getting recognition
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass #ignore when exception happens
    return command


def run_assistant():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'info' in command:
        person = command.replace('info', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Sorry, can you repeat that?')
        


run_assistant()