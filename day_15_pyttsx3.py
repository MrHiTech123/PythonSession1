# import os
# 
# os.system('pip install pyttsx3')
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')


# engine.say('Skibidi toilet')
# engine.say('Sigma chad')
# engine.save_to_file('I am really Sigma. Are you ready to grok the backrooms', 'poggers.mp3')
# 
# 
# engine.runAndWait()

voice = voices[1]

engine.setProperty('voice', voice.id)
engine.setProperty('rate', 10000)

engine.say('I am definitely a real human female')
engine.runAndWait()
