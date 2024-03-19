import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

class QuizApp:
    def __init__(self, window):
        self.root = window
        self.bg_img = None

    #remove all frames
    def remove_all_frames(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()

    #reload frame
    def reload_frame(self, frame):
        self.bg_img = ImageTk.PhotoImage(Image.open("./assets/background.jpeg"))
        bg_label = tk.Label(frame, image = self.bg_img)
        bg_label.place(anchor='center', relx=0.5, rely=0.5)

        name_label = ctk.CTkLabel(frame, text="Quiz App", font=('Comic Sans MS', 50), text_color='white', bg_color='#1a1a1c')
        name_label.place(anchor='center', x=700, y=30)

    #edit question frame
    def que_edit(self):
        self.remove_all_frames()

        que_frame = ctk.CTkFrame(self.root, width=1400, height=850)
        que_frame.place(x=0, y=0)

        self.reload_frame(que_frame)

    #start frame
    def start(self):
        self.remove_all_frames()

        start_frame = ctk.CTkFrame(self.root, width=1400, height=850)
        start_frame.place(x=0, y=0)

        self.reload_frame(start_frame)

    #leaderboard frame
    def leaderboard(self):
        self.remove_all_frames()

        LB_frame = ctk.CTkFrame(self.root, width=1400, height=850)
        LB_frame.place(x=0, y=0)

        self.reload_frame(LB_frame)