import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import subprocess


listener= sr.Recognizer()
engine=pyttsx3.init()
rate=engine.getProperty('rate')
print(rate)
engine.setProperty('rate',120)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'rambo' in command:
                command=command.replace('rambo','')
                print(command)
    except:
        pass
    return command

def run_rambo():
    cmd= take_command()
    print(cmd)
    if 'play' in cmd:
        song=cmd.replace('play','')
        talk('playing'+ song) 
        pywhatkit.playonyt(song)
        
    elif 'time' in cmd:
        time=datetime.datetime.now().strftime('%H:%M:%S %p')
        talk('current time is '+ time)
        print(time)
    elif 'tell me about' in cmd or 'who is' in cmd:
        person=cmd.replace('tell me about','')
        person=cmd.replace('who is','')
        info=wikipedia.summary(person,1) #1 stands for how many lines you want to show or listen
        talk(info)
        print(info)
    elif 'jokes' in cmd or 'joke' in cmd:
        person=cmd.replace('jokes','')
        person=cmd.replace('joke','')
        talk(pyjokes.get_joke())
    elif 'open notepad' in cmd:
        person=cmd.replace('open notepad','')
        talk('opening notepad')
        os.system('notepad.exe')
        
    elif 'open firefox' in cmd:
        talk('opening firefox')
        subprocess.Popen(['C:\Program Files\Mozilla Firefox\\firefox.exe'])
    elif 'open my laptop' in cmd:
        os.system('My Laptop')
    else:
        talk('please say the command again')
        run_rambo()        

run_rambo()        