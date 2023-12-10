'''
This is the main file that will be executed to run the website with similar features as https://tpb.vn/ca-nhan.
'''
import tkinter as tk
from tkinter import ttk
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Website with Similar Features")
        self.geometry("800x600")
        self.create_widgets()
    def create_widgets(self):
        # Create and configure the main frame
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)
        # Create and configure the header label
        header_label = ttk.Label(main_frame, text="Welcome to the Website with Similar Features")
        header_label.pack(pady=10)
        # Create and configure the content frame
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True)
        # Create and configure the content label
        content_label = ttk.Label(content_frame, text="This is the content of the website.")
        content_label.pack(pady=10)
        # Create and configure the footer label
        footer_label = ttk.Label(main_frame, text="© 2022 Website with Similar Features. All rights reserved.")
        footer_label.pack(pady=10)
if __name__ == "__main__":
    app = Application()
    app.mainloop()