'''
This is the main file of the Vietnamese voice assistant application.
'''
import tkinter as tk
from voice_recognition import VoiceRecognition
from text_to_speech import TextToSpeech
from command_processor import CommandProcessor
class VoiceAssistantApp:
    def __init__(self):
        self.voice_recognition = VoiceRecognition()
        self.text_to_speech = TextToSpeech()
        self.command_processor = CommandProcessor()
    def run(self):
        # Create the main application window
        self.window = tk.Tk()
        self.window.title("Vietnamese Voice Assistant")
        # Create and configure GUI elements
        self.label = tk.Label(self.window, text="Say something:")
        self.label.pack()
        self.text_box = tk.Text(self.window, height=10, width=50)
        self.text_box.pack()
        self.button = tk.Button(self.window, text="Submit", command=self.process_command)
        self.button.pack()
        # Start the main event loop
        self.window.mainloop()
    def process_command(self):
        # Get the user's voice input
        voice_input = self.voice_recognition.get_voice_input()
        # Process the voice command
        response = self.command_processor.process_command(voice_input)
        # Convert the response to speech
        self.text_to_speech.convert_to_speech(response)
        # Display the response in the GUI
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, response)
if __name__ == "__main__":
    app = VoiceAssistantApp()
    app.run()