import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import pywhatkit
import pyjokes
from playsound import playsound
import os
import g4f
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id  )
engine.setProperty('rate' , 150)


def speak(text):
        engine.say(text)
        engine.runAndWait()
        interrupted = False

def play_start_sound():
    path = os.path.join(os.path.dirname(__file__), "ding_start.mp3")
    playsound(path)

def play_end_sound():
    path = os.path.join(os.path.dirname(__file__), "ding_end.mp3")
    playsound(path)

def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        if response.status_code == 200:
            weather_info = response.text
            speak(f"The weather in {city} is: {weather_info}")
            print(f"{weather_info}")
            
        else:
            speak("Sorry, I couldn't fetch the weather right now.")
    except Exception as e:
        speak("There was an error fetching the weather.")
        print(e)

def interrupt_listener():
    global interrupted
    while True:
        command = listen()
        if "stop" in command or "enough" in command or "exit" in command:
            interrupted = True
            engine.stop()
            speak("Okay, stopping now.")
            break


def listen(lang = "en-IN"):
     print("Listening...")
     with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            
            audio = recognizer.listen(source, timeout=4, phrase_time_limit=10)
            command = recognizer.recognize_google(audio , language = lang)
            print(f"You said: {command}")
            return command.lower()
        except:
            return ""

def extract_first_last_lines(text):
    lines = text.split("\n")
    if len(lines) >= 2:
        return f"{lines[0]}\n{lines[-1]}"
    else:
        return text
    
def aiProcess(command):
    completion = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4o,
        messages=[
            {"role" : "system" , "content" : "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud and also fecth the latest as well old news from all over the world ." },
            {"role" : "user" , "content" : command }
        ]
    )
    return completion

def ask_news_from_ai(command):
    try:
        completion = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=[
                {"role": "system", "content": "You are a helpful assistant who answers latest or old news related queries like Alexa or Google Assistant. You fetch correct updates."},
                {"role": "user", "content": command}
            ]
        )
        answer = completion
        speak(f"Here is your {command} .")
        print(answer)
        speak("shall i read the full news for you ?")
        play_start_sound()
        c = listen(command)
        try :
            if c =="yes":
                speak(answer)
            elif c=="no":
                speak("Okay , here is your news ")
                print(answer)
        except Exception as e:
            speak("sorry , i couldnt get that . please try again")
        
    except Exception as e:
        print("Error:", e)
        speak("Sorry, I couldn't get the news right now.")

def process_command(command):
    if "hello" in command  or "hey" in command:
        speak("Hello , good to see you here .")
        play_end_sound()
   
    elif "how r u" in command or "how are you" in command:
        speak("Hello , i am fine ")
        play_end_sound()

    elif "date" in command:
        date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {date} . Have a nice day .")
        print(f"Date is {date}")
        play_end_sound()

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time} . Have a good day!")
        print(f"The time is {time} .")
        play_end_sound()
    
    elif "google" in command:
        speak("Okay , Oppening Google")
        webbrowser.open("https://www.google.com")
        play_end_sound()

    elif "youtube" in command:
        speak("Okay , Openning Youtube")
        webbrowser.open("https://www.youtube.com")
        play_end_sound()

    elif "facebook" in command:
        speak("Okay , Openning facebook")
        webbrowser.open("https://www.facebook.com")
        play_end_sound()

    elif "instagram" in command:
        speak("Okay , Openning instagram")
        webbrowser.open("https://www.instagram.com")
        play_end_sound()

    elif "linked" in command:
        speak("Okay , Openning linkedin")
        webbrowser.open("https://www.linkedin.com")
        play_end_sound()

    elif "chat" in command:
        speak("Okay , Openning chat G P T")
        webbrowser.open("https://www.chatgpt.com")
        play_end_sound()

    elif "whatsapp" in command:
        speak("Okay , Openning whatsapp")
        webbrowser.open("https://www.whatsapp.com")
        play_end_sound()
       
    elif "spotify" in command:
        speak("Okay , Openning spotify")
        webbrowser.open("https://www.spotify.com")
        play_end_sound()

    elif "amazon" in command:
        speak("Okay , Openning amazom")
        webbrowser.open("https://www.amazon.com")
        play_end_sound()

    elif "flipkart" in command:
        speak("Okay , Openning flipkart")
        webbrowser.open("https://www.flipkart.com")
        play_end_sound()

    elif "exit" in command or "bye" in command :
        speak("Goodbye , Thankyou for using Jarvis , Have a nice day !")
        play_end_sound()
        exit()

    elif "joke" in command :
        joke = pyjokes.get_joke()
        speak(f"{joke}")
        play_end_sound()
        print(f"{joke}")

    elif "search" in command:
        speak("What should I search for?")
        play_start_sound()
        query = listen()
        url = f"https://www.google.com/search?q={query}"
        speak(f"Searching Google for {query}")
        play_end_sound()
        webbrowser.open(url)
    
    elif command.startswith("play") or command == "play":
        song = command.replace("play", "").strip()
        parts = command.split("play", 1)
        song = parts[1].strip() if len(parts) > 1 else ""

        if song:
            speak(f"Okay, playing {song} on YouTube.")
            play_end_sound()
            pywhatkit.playonyt(song)
        else:
            speak("What song do you want to play?")
            play_start_sound()
            song = listen(lang="hi-IN")

            if not song:
                song = listen(lang="en-IN")
            if song:
                speak(f"Playing {song} on YouTube.")
                play_end_sound()
                pywhatkit.playonyt(song)
            else:
                speak("Sorry, I couldn't understand the song name.")
                play_end_sound()

    elif "weather" in command or "temperature" in command:
        speak("Please tell me your city.")
        play_start_sound()
        city = listen()
        get_weather(city)
        play_end_sound()

    elif "news" in command or  "about" in command or "headlines" in command:
        ask_news_from_ai(command)

    else:
        output = aiProcess(command)
        print(output)
        summary = extract_first_last_lines(str(output))
        speak(summary)

        while True :
            play_start_sound()
            command = listen()
            
            try:
                
                if command in ["stop", "exit", "quit", "thanks", "thank you"]:
                    speak("Exiting conversation mode. I'm here if you need me.")
                    play_end_sound()
                    break
                else:
                        output1 = aiProcess(command)
                        print(output1)
                        summary = extract_first_last_lines(str(output1))
                        speak(summary)

            except Exception as e:
                speak(" Sorry, I didn't understand that.")
            play_end_sound()


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        wake_command = listen()
        if "jarvis" in wake_command:
            play_start_sound()
            speak("Yes , how can i help you")
            play_start_sound()

            user_command = listen()
            if user_command:
                process_command(user_command)
            else:
                speak("Sorry, I couldn't understand the command")
                play_end_sound()
