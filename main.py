from gtts import gTTS
import os
import poplib
import string, random
import StringIO, rfc822
import logging
import speech_recognition as sr
from time import ctime
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import sys
import webbrowser
from PyDictionary import PyDictionary

my_id = { "work" : "nihalghanathe@gmail.com", "personal":"nihal999nez@gmail.com", "test":"testdie9@gmail.com"}
to_id = { "nez" : "nihal999nez@gmail.com", "nikhil" : "nikhilghanathe@gmail.com", "uma": "pratapuma12@gmail.com","gf":"birajdarsandhya@gmail.com","cool":"coolmothi@gmail.com"}

# Speaks
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

# get audio from the microphone                                                                       
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data

# Operates on commands
def JASS(text):
	if text == "are you alright":
		speak("Yes Nez, thank you for asking")

################### ACCESSING GMAIL #############################

	elif text == "do i have any emails":
		SERVER = "pop.gmail.com"
		USER  = "testdie9"
		PASSWORD = "diego_12"
 
		# connect to server
		logging.debug('connecting to ' + SERVER)
		server = poplib.POP3_SSL(SERVER)
		#server = poplib.POP3(SERVER)
 
		# login
		logging.debug('logging in')
		server.user(USER)
		server.pass_(PASSWORD)
 
		# list items on server
		logging.debug('listing emails')
		resp, items, octets = server.list()
 
		# download the first message in the list
		id, size = string.split(items[0])
		resp, text, octets = server.retr(id)
 
		# convert list to Message object
		text = string.join(text, "\n")
		file = StringIO.StringIO(text)
		message = rfc822.Message(file)
 
		# output message
		from1 = message['From']
		subject = message['Subject']
		date = message['Date']

		speak('you have received email from '+from1+' on '+date+' about '+subject)

	elif text == "are you up":
		speak("For you Nez, always")

	elif text == "send an email":
		speak("sure")
		time.sleep(0.5)
		speak("from which email would you like to send?")
		fro = recordAudio()
		print fro
		fro = my_id[str(fro)]
		time.sleep(0.5)
		speak("who would you like to send the email to?")
		to = recordAudio()
		to = to_id[str(to)]
		time.sleep(0.5)
		speak("what would you like the subject to be?")
		time.sleep(0.5)
		sub = recordAudio()
		time.sleep(0.5)
		speak("what email would you like to send?")
		time.sleep(0.5)
		msg = recordAudio()
		email = MIMEMultipart()
		email['From'] = fro
		email['To'] = to
		email['Subject'] = sub
		body = msg
		email.attach(MIMEText(body, 'plain'))
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fro, "diego_12")
		text = email.as_string()
		server.sendmail(fro, to, text)
		server.quit()

	elif text == "what is your name":
		speak("i am JASS")

	elif text == "who are you":
		speak("i am your personal assistant")

	elif text == "thank you":
		speak("no problem nez, happy to help")

	elif text == "how are you":
		speak("i'm fine thank you")

	elif "you take some rest now" in text or "go to sleep" in text:
		speak("Alright, see you soon")
		sys.exit(0)

	elif "what time is it" in text:
		speak(ctime())

	elif "where is" in text:
		text = text.split(" ")
		location = text[2]
		speak("Hold on Nez, I will show you where " + location + " is.")
		os.system("gksu -u nihal google-chrome https://www.google.nl/maps/place/" + location + "/&amp;")

	elif "multiply" in text:
		data = text.split(" ")
		speak(data[1]+" multiplied by "+data[3]+" is "+str(float(data[1])*float(data[3])))

	elif "add" in text:
		data = text.split(" ")
		speak(data[1]+" plus "+data[3]+" is "+str(float(data[1])+float(data[3])))		

	elif "subtract" in text:
		data = text.split(" ")
		speak(data[1]+" minus "+data[3]+" is "+str(float(data[1])-float(data[3])))

	elif "divide" in text:
		data = text.split(" ")
		speak(data[1]+" divided by "+data[3]+" is "+str(float(data[1])/float(data[3])))		

	elif "what is" in text:

		speak("here are the google search results for"+text)
		data = text.replace(" ", "+")
		os.system("gksu -u nihal google-chrome https://www.google.com/search?q=" + data )

	elif "open chrome" in text:
		speak("Sure, are you searching for something in particular?")
		query = recordAudio()
		query = query.lower()
		if "yes" in query:
			speak("what do you want to search about?")
			query = recordAudio()
			query = query.lower()
			speak("here is the google page for your query")
			query = query.replace(" ", "+")
			url = "https://www.google.com/search?q=" + query
			chrome_path = 'gksu -u nihal google-chrome %s'
			webbrowser.get(chrome_path).open(url)

		else: 
			url = "https://www.google.com"
			chrome_path = 'gksu -u nihal google-chrome %s'
			webbrowser.get(chrome_path).open(url)

	elif "define" in text:
		searchstr = text.split(" ")
		searchstr = searchstr[1]
		dictionary=PyDictionary()
		result = dictionary.meaning(searchstr)
		if 'Noun' in result:
			if len(result['Noun']) > 1:
				speak("as a noun "+searchstr+" has "+str(len(result['Noun']))+" definitions ")
				time.sleep(0.5)
				speak("they are")
				for i in result['Noun']:
					speak(i)
					time.sleep(0.5)
			else:
				speak("as a noun "+searchstr+" has the following meaning")
				time.sleep(0.5)
				for i in result['Noun']:
					speak(i)
					time.sleep(0.5)

		if 'Verb' in result:
			if len(result['Verb']) > 1:
				speak("as a verb "+searchstr+" has "+str(len(result['Verb']))+" definitions ")
				time.sleep(0.5)
				speak("they are")
				for i in result['Verb']:
					speak(i)
					time.sleep(0.5)
			else:
				speak("as a verb "+searchstr+" has the following meaning ")
				time.sleep(0.5)
				for i in result['verb']:
					speak(i)
					time.sleep(0.5)

		speak("for more information on "+searchstr+" here is the google page")
		url = "https://www.google.com/search?q=" + searchstr
		chrome_path = 'gksu -u nihal google-chrome %s'
		webbrowser.get(chrome_path).open(url)

	else:
		speak('i\'m sorry i dont understand. Please speak again')
 

# initialization
time.sleep(2)
speak("Hello Nez, what can I do for you?")
while 1:
    data = recordAudio()
    data = data.lower()
    JASS(data)