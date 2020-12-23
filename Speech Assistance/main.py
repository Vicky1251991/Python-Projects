import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        input = command.replace('play', '')
        talk('playing' + input)
        pywhatkit.playonyt(input)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk('Current time is' + time)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d/%m/%Y')
        print(date)
        talk('Current date is' + date)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'joke' in command:
        info = pyjokes.get_joke()
        print(info)
        talk(info)
    else:
        print('Please say the command again.')
        talk('Please say the command again.')


while True:
    run_alexa()
