import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from frames import *

#initialize window
def initialize_window():
    global root
    root = tk.Tk()
    root.title('Quiz')
    root.geometry('1400x850+260+115')
    root.resizable(False, False)
    QA = QuizApp(root, "Soham")

    QA.home_frame()

    root.mainloop()

initialize_window()