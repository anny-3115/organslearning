# Importing necessary modules required
import speech_recognition as spr
from googletrans import Translator
#from gtts import gTTS


import os


from_lang = 'en'
	
	# In which we want to convert, short
	# form of hindi
to_lang = 'kn'
translator = Translator()

text_to_translate = translator.translate("what are you", src= from_lang, dest= to_lang)
text = text_to_translate.text

print(text)
