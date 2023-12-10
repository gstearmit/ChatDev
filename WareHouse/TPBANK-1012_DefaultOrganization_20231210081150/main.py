'''
This is the main file of the website.
'''
import tkinter as tk
from tkinter import messagebox
from frontend import Frontend
from backend import Backend
class Website:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Website")
        self.root.geometry("800x600")
        self.frontend = Frontend()
        self.backend = Backend()
        self.create_widgets()
    def create_widgets(self):
        # Create and configure the widgets here
        button = tk.Button(self.root, text="Submit", command=self.handle_submit)
        button.pack()
    def handle_submit(self):
        data = self.frontend.get_form_data()
        if not data:
            messagebox.showerror("Error", "Form data cannot be empty!")
            return
        self.backend.process_form_data(data)
        messagebox.showinfo("Success", "Form submitted successfully!")
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    website = Website()
    website.run()