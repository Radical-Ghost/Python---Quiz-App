import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from connection import *

class QuizApp:
    def __init__(self, window, Name):
        self.user_name = Name
        self.root = window
        self.bg_img = None
        self.back_bg = None
        self.welcome = None
        self.button_frame = None
        self.lb_bg = None
        self.op_1 = None
        self.op_2 = None
        self.op_3 = None
        self.op_4 = None
        self.q_text_bg_png = None
        self.next = None
        self.skip = None
        self.time_ring = None
        self.answer = None
        self.countdown_time = 30
        self.countdown_id = None

    def update_countdown(self, q_no):
        if self.countdown_time <= 0:
            self.INI.result(q_no, "None")
            self.quiz_start(None)
        elif self.countdown_label.winfo_exists():
            self.countdown_label.configure(text=str(self.countdown_time))
            self.countdown_time -= 1
            self.countdown_id = self.root.after(1000, self.update_countdown, q_no)

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

        self.back_bg = ImageTk.PhotoImage(Image.open("./assets/back.png"))
        back_button = tk.Button(frame, image = self.back_bg, width=30, height=50, background='#1a1a1c', activebackground='#1a1a1c', relief='flat', border=0, command = lambda: self.home_frame())
        back_button.place(anchor='center', x=50, y=35)
        back_button.place(anchor='center', x=50, y=35)

        name_label = ctk.CTkLabel(frame, text="Quiz App", font=('Comic Sans MS', 50), text_color='white', bg_color='#1a1a1c')
        name_label.place(anchor='center', x=700, y=30)

    #home frame
    def home_frame(self):
        self.remove_all_frames()

        home_frame = ctk.CTkFrame(self.root, width=1400, height=850)
        home_frame.place(x=0, y=0)

        self.reload_frame(home_frame)

        self.welcome = ImageTk.PhotoImage(Image.open("./assets/welcome_frame.png"))
        self.button_frame = ImageTk.PhotoImage(Image.open("assets/button_frame.png"))

        welcome_label_bg = tk.Label(home_frame, image=self.welcome, background='#1a1a1c', relief='flat', border=0)
        welcome_label_bg.place(anchor='center', relx=0.5, rely=0.54)
        welcome_label = ctk.CTkLabel(home_frame, text="Welcome", font=('Comic Sans MS', 70), text_color='white', bg_color='#1a1a1c')
        welcome_label.place(anchor='center', x=700, y=220)

        start_button = tk.Button(home_frame, image = self.button_frame, width=520, height=120, background='#1a1a1c', activebackground='#1a1a1c', relief='flat', border=0, command= lambda: self.quiz_start("home"))
        start_button.place(anchor='center', x=700, y=420)
        start_label = ctk.CTkLabel(home_frame, text="Start", font=('Comic Sans MS', 50), text_color='white', bg_color='#272728')
        start_label.place(anchor='center', x=700, y=420)

        leaderboard_button = tk.Button(home_frame, image = self.button_frame, width=520, height=120, background='#1a1a1c', activebackground='#1a1a1c', relief='flat', border=0, command= lambda: self.leaderboard("home"))
        leaderboard_button.place(anchor='center', x=700, y=620)
        leaderboard_label = ctk.CTkLabel(home_frame, text="Leaderboard", font=('Comic Sans MS', 50), text_color='white', bg_color='#272728')
        leaderboard_label.place(anchor='center', x=700, y=620)

    #leaderboard frame
    def leaderboard(self, new):
        if new == "home":
            self.INI = initialize(self)

        calculate_score = self.INI.calculate_score()
        
        self.remove_all_frames()

        lb_frame = ctk.CTkFrame(self.root, width=1400, height=850)
        lb_frame.place(x=0, y=0)

        self.reload_frame(lb_frame)
        
        lb_bg_label = ctk.CTkLabel(lb_frame, image=self.lb_bg, text="Leaderboard", font=('Comic Sans MS', 70), text_color='white', bg_color='#131315')
        lb_bg_label.place(anchor='center', x=700, y=150)

        ur_score = ctk.CTkLabel(lb_frame, text=f"Your Score: {calculate_score}", font=('Comic Sans MS', 40), text_color='white', bg_color='#131315')
        ur_score.place(anchor='center', x=700, y=250)

        heading_lb_1 = ctk.CTkLabel(lb_frame, text="Name", width = 520, height = 40, font=('Comic Sans MS', 40), text_color='white', fg_color='#1d1d26')
        heading_lb_2 = ctk.CTkLabel(lb_frame, text="Score", width = 300, height = 40, font=('Comic Sans MS', 40), text_color='white', fg_color='#1d1d26')
        heading_lb_1.place(anchor='center', x=550, y=355)
        heading_lb_2.place(anchor='center', x=960, y=355)

        leaderboard_box = ctk.CTkScrollableFrame(lb_frame, width=800, height=410, fg_color='#1a1a1c', scrollbar_button_hover_color='#9457ff', scrollbar_button_color='#1a1a1c', label_font=('Comic Sans MS', 30), label_text_color='white')
        leaderboard_box.place(anchor='center', x=700, y=590)

        lb_data = self.INI.fetch_leaderboard()
        for i, (name, score) in enumerate(lb_data):
            name_label = ctk.CTkLabel(leaderboard_box, text=name, width = 520, height = 40, font=('Comic Sans MS', 30), text_color='white', bg_color='#1a1a1c')
            score_label = ctk.CTkLabel(leaderboard_box, text=score, width = 300, height = 40, font=('Comic Sans MS', 30), text_color='white', bg_color='#1a1a1c')
            name_label.grid(row=i, column=0)
            score_label.grid(row=i, column=1)
        
    def ini_answer(self, ans):
        self.answer = ans
    
    #quiz start
    def quiz_start(self, new):
        if new == "home":
            print("Hi")
            self.INI = initialize(self)

        result = self.INI.q_no_fetch()
        if result is None:
            self.leaderboard(None)
            return
        
        #getting all the options
        q_no, q_text, option_1, option_2, option_3, option_4 = result
        self.remove_all_frames()

        q_start = ctk.CTkFrame(self.root, width=1400, height=850)
        q_start.place(x=0, y=0)

        self.reload_frame(q_start)

        # Countdown label 
        self.time_ring = ImageTk.PhotoImage(Image.open("./assets/timer_ring.png"))
        self.countdown_label = ctk.CTkLabel(q_start, image=self.time_ring, text=str(self.countdown_time), font=('Comic Sans MS', 25), text_color='white', bg_color='#1a1a1c')
        self.countdown_label.place(anchor='center', x=1350, y=35)
        if self.countdown_id is not None:
            self.root.after_cancel(self.countdown_id)
        self.countdown_time = 30
        self.countdown_id = self.root.after(1000, self.update_countdown, q_no)

        self.q_text_bg_png = ImageTk.PhotoImage(Image.open("./assets/q_text.png"))
        self.op_1 = ImageTk.PhotoImage(Image.open("assets/option1.png"))
        self.op_2 = ImageTk.PhotoImage(Image.open("assets/option2.png"))
        self.op_3 = ImageTk.PhotoImage(Image.open("assets/option3.png"))
        self.op_4 = ImageTk.PhotoImage(Image.open("assets/option4.png"))
        self.next = ImageTk.PhotoImage(Image.open("assets/next.png"))
        self.skip = ImageTk.PhotoImage(Image.open("assets/skip.png"))

        q_text_bg = tk.Label(q_start, image=self.q_text_bg_png, background='#131315', relief='flat', border=0)
        q_text_bg.place(anchor='center', x=700, y=230)
        label_q_text = ctk.CTkLabel(q_start, text=q_text, font=('Comic Sans MS', 30), text_color='white', bg_color='#272728')
        label_q_text.place(anchor='center', x=700, y=230)

        #1st option
        button_op_1 = tk.Button(q_start, image = self.op_1, width=357, height=120, background='#131315', activebackground='#131315', relief='flat', border=0, command = lambda: self.ini_answer(option_1))
        button_op_1.place(anchor='center', x=400, y=460)
        label_op_1 = ctk.CTkLabel(q_start, text=option_1, font=('Comic Sans MS', 30), text_color='white', bg_color='#7f00ff')
        label_op_1.place(anchor='center', x=400, y=460)

        #2nd option
        button_op_2 = tk.Button(q_start, image = self.op_2, width=357, height=120, background='#131315', activebackground='#131315', relief='flat', border=0, command = lambda: self.ini_answer(option_2))
        button_op_2.place(anchor='center', x=1000, y=460)
        label_op_2 = ctk.CTkLabel(q_start, text=option_2, font=('Comic Sans MS', 30), text_color='white', bg_color='#6400c7')
        label_op_2.place(anchor='center', x=1000, y=460)
        
        #3rd option
        button_op_3 = tk.Button(q_start, image = self.op_3, width=357, height=120, background='#131315', activebackground='#131315', relief='flat', border=0, command = lambda: self.ini_answer(option_3))
        button_op_3.place(anchor='center', x=400, y=610)
        label_op_3 = ctk.CTkLabel(q_start, text=option_3, font=('Comic Sans MS', 30), text_color='white', bg_color='#420084')
        label_op_3.place(anchor='center', x=400, y=610)
        
        #4th option
        button_op_4 = tk.Button(q_start, image = self.op_4, width=357, height=120, background='#131315', activebackground='#131315', relief='flat', border=0, command = lambda: self.ini_answer(option_4))
        button_op_4.place(anchor='center', x=1000, y=610)
        label_op_4 = ctk.CTkLabel(q_start, text=option_4, font=('Comic Sans MS', 30), text_color='white', bg_color='#5300a6')
        label_op_4.place(anchor='center', x=1000, y=610)

        #skip and next button
        button_skip = tk.Button(q_start, image = self.skip, width=357, height=120, background='#131315', activebackground='#131315', relief='flat', border=0, command = lambda:(self.INI.result(q_no, "None"), self.quiz_start(None)))
        button_skip.place(anchor='center', x=495, y=765)
        label_skip = ctk.CTkLabel(q_start, text="SKIP", font=('Comic Sans MS', 30), text_color='white', bg_color='#bb0000')
        label_skip.place(anchor='center', x=495, y=765)

        button_next = tk.Button(q_start, image = self.next, width=357, height=120, background='#131315', activebackground='#131315', relief='flat', border=0, command = lambda: (self.INI.result(q_no, self.answer), self.quiz_start(None)))
        button_next.place(anchor='center', x=905, y=765)
        label_next = ctk.CTkLabel(q_start, text="NEXT", font=('Comic Sans MS', 30), text_color='white', bg_color='#03a400')
        label_next.place(anchor='center', x=905, y=765)