import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import os
import yfinance as yf
import pyjokes
import pyaudio
import wikipedia
                       
# listen to my mic and return the audio as text using google

def convert():
    r = sr.Recognizer()
    with sr.Microphone() as origin:
        r.pause_threshold = 1.25
        deliver = r.listen(origin)
        try:
            print("Listening...")
            q = r.recognize_google(deliver, language="en")
            return q
        except sr.UnknownValueError:
            print("Sorry, I did not understand, please repeat")
            return "Waiting..."
        except sr.RequestError:
            print("Sorry, the service is down")
            return "Waiting..."
        except:
            return "Waiting..."

convert()

def vocalize(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

# voice

engine = pyttsx3.init()
for voice in engine.getProperty("voices"):
    print(voice)

id ='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty("voice", id)
# engine.say("Hello World")
engine.runAndWait

# tells the name of the day

def query_day():
    day = datetime.date.today()
    # print(day)
    weekday = day.weekday()
    # print(weekday)
    mapping = {
        0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"
    }
    try:
        vocalize(f"Today's date is {mapping[weekday]}")
    except:
        pass

# query_day()

# tells the time

def query_time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    vocalize(f"It is {time[0:2]} o'clock and {time[3:5]} minutes")

# query_time()

# Greeting at the beginning
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        vocalize("Hello, Good Morning")

    elif hour>= 12 and hour<18:
        vocalize("Hello, Good Afternoon")

    else:
        vocalize("Hello, Good Evening")

wishMe()


def greetings():
    vocalize("My name is Akana. I am your personal virtual assistant. How may I help you?")

greetings()

# The brain. It takes requests and completes them

def inquire():
    # greetings()
    start = True
    while(start):
        q = convert().lower()

        if "open youtube" in q or "youtube" in q:
            vocalize("I am starting youtube. Just a second.")
            webbrowser.open("https://www.youtube.com")
            continue

        elif "open web browser" in q or "web browser" in q:
            vocalize("I am opening web browser. Just a second.")
            webbrowser.open("https://www.google.com")
            continue

        elif "what day is it" in q:
            query_day()
            continue

        elif "what time is it" in q:
            query_time()
            continue

        elif "stop" in q or "shut down" in q:
            vocalize("OK I am shutting down. Goodbye.")
            break

        elif "from wikipedia" in q or "wikipedia" in q:
            vocalize("I am checking wikipedia. Just a second.")
            q = q.replace("wikipedia","")
            result = wikipedia.summary(q,sentences=2)
            vocalize("found on wikipedia")
            vocalize(result)
            continue
        
        elif "your name" in q:
            vocalize("My name is Akana. Your personal virtual assistant")
            continue

        elif "search the web" in q:
            pywhatkit.search(q)
            vocalize("this is what I found on the web")
            continue

        elif "play" in q:
            vocalize(f"playing {q}")
            pywhatkit.playonyt(q)
            continue

        elif "joke" in q:
            vocalize(pyjokes.get_joke())
            continue
        
        elif "thank you" in q:
            vocalize("you are welcome, is there anything else I can help you with?")
            continue

        elif "yes" in q:
            vocalize("what is it?")
            continue

        elif "no" in q or "nope" in q:
            vocalize("OK. Goodbye.")
            break

        elif "stock price" in q:
            search = q.split("of")[-1].strip()
            lookup = {"apple":"AAPL",
                     "tesla":"TSLA",
                     "google":"GOOGL",
                     "amazon":"AMZN",}
            try:
                stock = lookup[search]
                stock = yf.Ticker(stock)
                currentprice = stock.info["regularMarketPrice"]
                vocalize(f"OK, found it, the price for {search} is {currentprice}")
                continue
            except:
                vocalize(f"sorry, I have no data for {search}")
            continue

        elif "how are you" in q:
            vocalize("I am fine, thank you, how are you?")
            continue

        elif "fine" in q or "good" in q:
            vocalize("It is good to hear that you are fine")
            continue
        
inquire()