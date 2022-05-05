import phonenumbers
import speech_recognition as sr
import pywhatkit as pw
import pyttsx3
import wikipedia as wiki
import datetime
from datetime import datetime
import phonenumbers as phn
from phonenumbers import geocoder
from phonenumbers import carrier
import webbrowser as wb
import os
import smtplib

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def song(user):
    pw.playonyt(user)


def search(search):
    pw.search(search)


def anything(text1):
    m = wiki.summary(text1, 2)
    talk(m)


def time_re(command):
    talk(command)
    time = datetime.now().strftime("%I:%M %p")
    talk(time)
    print(time)


def location(loc):
    talk("here is your location")
    pw.search(loc)


def truecaller():
    engine.say(
        "hey i am bubai , are you searching for phone number location and details?")
    engine.runAndWait()
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)

            if "yes" in command:
                engine.say(
                    "enter the number in the terminal with proper country code ")
                engine.runAndWait()
                phn = input("enter the phone number here")
                number = phonenumbers.parse(phn, "CH")

                num_location = geocoder.country_name_for_number(number, "en")
                num_des = geocoder.description_for_number(number, "en")
                num_user = carrier.name_for_number(number, "en")

                talk(num_user)
                print(num_user)
                talk(num_location)
                print(num_location)
                talk(num_des)
                print(num_des)

                talk("do you want to search the location???")
                try:
                    with sr.Microphone() as source:
                        print("listening...")
                        voice = listener.listen(source)
                        command = listener.recognize_google(voice)
                        if "yes" in command:
                            talk("ok fine")
                            location(num_des) or location(num_location)
                        elif "no" in command:
                            talk("okay, have a good day")
                            print("closing")
                except:
                    print("sorry!")
                    talk("sorry, unable to recognize")
            elif "no" in command:
                talk("ok fine, have a good day")
    except:
        print("sorry!")
        talk("sorry, unable to recognize")


def open_youtube():
    talk("okay opening")
    wb.open("youtube.com")


def open_google():
    talk("okay opening")
    wb.open("google.com")


def open_facebook():
    talk("okay opening")
    wb.open("facebook.com")


def open_wikipedia():
    talk("okay opening")
    wb.open("wikipedia.com")


def open_calculator():
    talk("opening")
    os.system("calc")


def open_notepad():
    talk("opening")
    os.system("notepad")

def send_msg():
    talk("enter the number you want to send massage ")
    num=input("enter the number here ")
    talk("write massage ")
    msg=input("write here ")
    talk("enter hour ")
    hour=int(input("hour "))
    talk("enter minute ")
    min=int(input("minute "))
    pw.sendwhatmsg(num,msg,hour,min)

def g_mail_msg():
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)

    talk("enter your mail id")
    mail=input("enter your mail id ")
    talk("enter your password")
    password=input("enter your password ")

    server.login(mail,password)

    talk("enter mail id where to send")
    mail_to_the_person=input("enter here ")

    talk("write the message")
    msg=input("write here ")

    server.sendmail(mail,mail_to_the_person,msg)
    server.quit()
    talk("possibly,mail sent")

engine.say("i am bubai, what can i do for you?")
engine.runAndWait()

try:
    with sr.Microphone() as source:
        print("listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        if("play" in command):
            music = command.replace("play", "")
            talk("playing"+music)
            song(command)
            print(command)

        elif("search" in command):
            command = command.replace("search", "")
            a = search(command)
            talk(a)

        elif("do you know" in command):
            engine.say("yes i know")
            engine.say("here are the results")
            engine.runAndWait()
            anything(command)

        elif("time" in command):
            command = "the time is"
            time_re(command)

        elif "send a mail"  in command:
            g_mail_msg()


        elif "open YouTube" in command:
            open_youtube()

        elif ("Wikipedia" in command):
            open_wikipedia()

        elif ("Google" in command):
            open_google()
        elif("Facebook" in command):
            open_facebook()

        elif ("looking for a number" in command):
            truecaller()

        elif "calculator" in command:
            open_calculator()
        elif "note" in command:
            open_notepad()

        elif "send a message" in command:
            send_msg()

        elif "no" in command:
            talk("ok fine, have a good day")
            print("closing")

        else:
            print("sorry -_- i don't know this")
            talk("sorry -_- i don't know this")

except:
    print("sorry!")
    talk("sorry, unable to recognize,try again")
