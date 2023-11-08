'''
This file handles voice recognition functionality.
'''
import speech_recognition as sr
class VoiceRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()
    def get_voice_input(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            voice_input = self.recognizer.recognize_google(audio, language="vi-VN")
            print("Voice input:", voice_input)
            return voice_input
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return ""