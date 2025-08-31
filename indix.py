import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def lsn():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = listener.listen(source)

    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, there was an issue with the speech recognition service.")
        return ""

def run_ass():
    speak("Hello! How can I help you today?")

    while True:
        command = lsn()

        if "hello" in command:
            speak("Hello there!")
        elif "time" in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {current_time}")
        elif "date" in command:
            today = datetime.date.today().strftime('%B %d, %Y')
            speak(f"Today's date is {today}")
        elif "search for" in command:
            topic = command.replace("search for", "").strip()
            if topic:
                speak(f"Searching the web for {topic}")
                pywhatkit.search(topic)
            else:
                speak("What do you want me to search for?")
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        elif command:
            speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
    run_ass()