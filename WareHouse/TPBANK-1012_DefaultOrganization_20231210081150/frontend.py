'''
This file contains the front-end logic of the website.
'''
import tkinter as tk
class Frontend:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Website")
        self.root.geometry("800x600")
        self.create_widgets()
    def create_widgets(self):
        # Create and configure the widgets here
        self.entry = tk.Entry(self.root)
        self.entry.pack()
    def get_form_data(self):
        return self.entry.get()