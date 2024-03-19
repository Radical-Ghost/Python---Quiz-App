import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from frames import *

#home frame
def home_frame(QA):
    QA.remove_all_frames()

    global que_button_img, welcome, button_frame
    home_frame = ctk.CTkFrame(root, width=1400, height=850)
    home_frame.place(x=0, y=0)

    QA.reload_frame(home_frame)

    que_button_img = ImageTk.PhotoImage(Image.open("assets/que_button.png"))
    que_button = tk.Button(home_frame, image = que_button_img, width=70, height=70, background='#1a1a1c', activebackground='#1a1a1c', relief='flat', border=0, command=QA.que_edit)
    que_button.place(anchor='center', x=1320, y=40)

    welcome = ImageTk.PhotoImage(Image.open("./assets/welcome_frame.png"))
    welcome_label_bg = tk.Label(home_frame, image=welcome, background='#1a1a1c', relief='flat', border=0)
    welcome_label_bg.place(anchor='center', relx=0.5, rely=0.54)

    welcome_label = ctk.CTkLabel(home_frame, text="Welcome", font=('Comic Sans MS', 70), text_color='white', bg_color='#1a1a1c')
    welcome_label.place(anchor='center', x=700, y=220)

    button_frame = ImageTk.PhotoImage(Image.open("assets/button_frame.png"))
    button_bg_1 = tk.Button(home_frame, image = button_frame, width=520, height=120, background='#1a1a1c', activebackground='#1a1a1c', relief='flat', border=0, command=QA.start)
    button_bg_1.place(anchor='center', x=700, y=420)
    button_bg_2 = tk.Button(home_frame, image = button_frame, width=520, height=120, background='#1a1a1c', activebackground='#1a1a1c', relief='flat', border=0, command=QA.leaderboard)
    button_bg_2.place(anchor='center', x=700, y=620)

    start_label = ctk.CTkLabel(home_frame, text="Start", font=('Comic Sans MS', 50), text_color='white', bg_color='#272728')
    start_label.place(anchor='center', x=700, y=420)

    leaderboard_label = ctk.CTkLabel(home_frame, text="Leaderboard", font=('Comic Sans MS', 50), text_color='white', bg_color='#272728')
    leaderboard_label.place(anchor='center', x=700, y=620)

#initialize window
def initialize_window():
    global root
    root = tk.Tk()
    root.title('Quiz')
    root.geometry('1400x850+260+115')
    QA = QuizApp(root)

    home_frame(QA)

    root.mainloop()

initialize_window()