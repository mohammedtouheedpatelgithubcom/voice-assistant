# @author of code date:24/06/2020
# mohammed touheed patel
# roll no: 1601-19-737-098
# IT-2 SEM-2 
# CBIT  hyderabad
#project title jarvis-an AI bot which can be enhanced much more
#features please help to enhance more functionalities
#in this we can use our voice like google and youtube to perform
#tasks like 1.open vscode 2.google.com 3.youtube.com 
# 4.wish U according to time 5.tell U time
# 6.send email 7.search something on wikipedia
# 8. play music 9. open stackoverflow.com 10.quit 


import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
#pip install pywin32 for windows user
#pip install pipwin 
#pipwin install pyaudio for audio list

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)#for male version 
engine.setProperty('voice', voices[0].id)#female version check by just printing

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")   

    else:
        speak("Good Evening Sir!")  

    speak("I am Jarvis 2.0 Sir  my introduction i am built by  mohammed  touheed  patel ")
    speak("i can perform tasks like 1 open vscode 2 google.com 3  youtube.com  ") 
    speak("4  wish U according to time  5  tell U time")
    speak(" 6  send email 7  search something on wikipedia")
    speak("8  play music 9  open stackoverflow.com 10  quit ")
    speak("I am Jarvis Sir  Please tell me how may I help you") 
    print("\nI am Jarvis 2.0 Sir  my introduction i am built by  mohammed  touheed  patel ")      
    print("\ni can perform tasks like 1 open vscode 2 google.com 3  youtube.com ")
    print("\n4  wish U according to time  5  tell U time")
    print("\n6  send email 7  search something on wikipedia ")
    print("\n8  play music 9  open stackoverflow.com 10  quit  ")
    print("\n I am Jarvis Sir  Please tell me how may I help you")
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("\nRecognizing......")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e) 
        speak("Sorry can you Say that again please....")   
        print("\n Sorry can you Say that again please.....")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mdtouheedpatel786@gmail.com', 'your-password')
    server.sendmail('mdtouheedpatel786@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
# we can like this open any website 
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

# for playing music U need to change directory where musics are
        elif 'play music' in query:
            music_dir = 'C:\\Users\\R computer\\Music\\Playlists'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
# displays and speak what's time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")
#using this You can open any file or application by replacing codepath by that app path
        elif 'open code' in query:
            codePath = "C:\\Users\\R computer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
#using this you can send email to a particular person by providing email
#for using this you need to login using you id and password
#And allow less secure app to send email
        elif 'email to touheed' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mdtouheedpatel786@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend touheed bro. I am not able to send this email")  
        elif 'quit' in query:
            print("\n Exiting .....")
            print("\n THANKS for using JARVIS 2.0 built by mr mohammed touheed patel")
            speak("Exiting  THANKS for using JARVIS 2.0 built by mr mohammed tauheed patel")  
            break      