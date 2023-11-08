'''
This file handles text to speech functionality.
'''
import pyttsx3
class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
    def convert_to_speech(self, text):
        self.engine.say(text)
        self.engine.runAndWait()