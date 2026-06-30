import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        speak("Sorry, I didn't get that.")
        return ""

def process(command):
    if "hello" in command:
        speak("Hello! How can I help you?")

    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak("Today's date is " + today)    
        
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + now)
        
    elif "search" in command:
        query = command.replace("search", "")
        speak("Searching for " + query)
        webbrowser.open("https://www.google.com/search?q=" + query)
        
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False
        
    else:
        speak("I can say hello, tell date and time, or search.")
        
    return True

speak("Assistant started")

while True:
    cmd = listen()
    if cmd:
        if not process(cmd):
            break