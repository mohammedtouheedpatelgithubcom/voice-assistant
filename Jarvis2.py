#pip install pywin32 for windows user
#pip install pipwin
#pipwin install pyaudio for audio list
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

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
        speak("Good Morning !")
        print('Good Morning !')

    elif hour>=12 and hour<18:
        print("Good Afternoon !")
        speak("Good Afternoon !")



    else:
        print("Good Evening !")
        speak("Good Evening !")

    print('\n Sytem rebooting\n Powering up JARVIS')
    speak("SYSTEM REBOOTING")
    speak("POWERING UP JARVIS")
    print("hello there, this is JARVIS, your personal voice assistant.")
    print("my interface is build by Mr.Mohammed Touheed patel AND Mr.G.nishanth")
    print("i can follow your commands when you ask me to open vscode, google.com, youtube.com")
    print("i can wish you on a specific time, i can tell you what time it is ")
    print("i can send emails to your friends, can search something on wikipedia")
    print("play music, can open stackoverflow.com and can go back to sleep when you ask me to shut down")
    print("THIS IS JARVIS SIR, LET ME KNOW HOW MAY I HELP YOU")
    speak("hello there, this is JARVIS, your personal voice assistant.")
    speak("my interface is build by Mister mohammed tauheed patel AND mister g nishanth ")
    speak("i can follow your commands when you ask me to open vscode, google.com, youtube.com")
    speak("i can wish you on a specific time, i can tell you what time it is ")
    speak("i can send emails to your friends, can search something on wikipedia")
    speak("play music, can open stackoverflow.com and can go back to sleep when you ask me to shut down")
    speak("THIS IS JARVIS SIR, LET ME KNOW HOW MAY I HELP YOU")

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
        print("\n Sorry can you Say that again please.....")
        speak('Sorry can you Say that again please.....')
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mdtouheedpatel786@gmail.com' or 'nishanth.tekken15gmail.com', 'your-password')
    server.sendmail('mdtouheedpatel786@gmail.com' or 'nishanth.tekken15@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            print('Searching on Wikipedia...wait for a minute ')
            speak('Searching on  Wikipedia...wait for a minute')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia...")
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
            speak(f"The time is {strTime}")
            print(f"The time is {strTime}")
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
        elif 'shut down'or "exit" or "quit" in query:
            print("\n Exiting .....")
            print("\n THANKS for using JARVIS 2.0")
            speak("Exiting  THANKS for using JARVIS 2.0")
            break
