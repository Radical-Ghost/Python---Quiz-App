import sqlite3
import random

conn = sqlite3.connect("Quiz.db")
myc = conn.cursor()

myc.execute('''
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                option1 TEXT,
                option2 TEXT,
                option3 TEXT,
                option4 TEXT,
                answer TEXT
            );
        ''')
myc.execute('''
            CREATE TABLE IF NOT EXISTS leaderboard (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                score INTEGER
            );
        ''')
# # List of questions, options, and answers
# data = [
#     ('What is the capital of France?', 'Paris', 'London', 'Berlin', 'Madrid', 'Paris'),
#     ('What is the capital of England?', 'Paris', 'London', 'Berlin', 'Madrid', 'London'),
#     ('What is the capital of Germany?', 'Paris', 'London', 'Berlin', 'Madrid', 'Berlin'),
#     ('What is the capital of Spain?', 'Paris', 'London', 'Berlin', 'Madrid', 'Madrid'),
#     ('What is the capital of Italy?', 'Paris', 'Rome', 'Berlin', 'Madrid', 'Rome'),
#     ('What is the capital of Canada?', 'Ottawa', 'London', 'Berlin', 'Madrid', 'Ottawa'),
#     ('What is the capital of Australia?', 'Paris', 'London', 'Canberra', 'Madrid', 'Canberra'),
#     ('What is the capital of India?', 'Paris', 'London', 'Berlin', 'New Delhi', 'New Delhi'),
#     ('What is the capital of Japan?', 'Paris', 'London', 'Berlin', 'Tokyo', 'Tokyo'),
#     ('What is the capital of Russia?', 'Paris', 'London', 'Moscow', 'Madrid', 'Moscow'),
# ]
# # Insert records into the questions table
# for item in data:
#     myc.execute('''
#         INSERT INTO questions (question, option1, option2, option3, option4, answer)
#         VALUES (?, ?, ?, ?, ?, ?);
#     ''', item)
# myc.execute("DELETE FROM leaderboard")
conn.commit()

class initialize:
    def __init__(self, QA):
        self.QA = QA
        self.selected_no = {}
        myc.execute("SELECT COUNT(id) FROM questions")
        self.total_ids = myc.fetchone()[0]
        self.id_list = list(range(1, self.total_ids + 1))
        random.shuffle(self.id_list)
        self.score = 0

    def result(self, q_no, ans):
        self.selected_no[q_no] = ans

    def q_no_fetch(self):
        if not self.id_list:   
            return None
    
        id_no = self.id_list.pop()

        myc.execute("SELECT id, question, option1, option2, option3, option4 FROM questions WHERE id = ?", (id_no,))
        row = myc.fetchone()
        return row
    
    def calculate_score(self):
        for q_no, selected_answer in self.selected_no.items():
            myc.execute("SELECT answer FROM questions WHERE id = ?", (q_no,))
            correct_answer = myc.fetchone()[0]
            if selected_answer is None:
                continue
            elif selected_answer == correct_answer:
                self.score += 5
            else:
                self.score -= 3
        
        if self.score <= 0:
            return self.score
        else:
            myc.execute("INSERT INTO leaderboard (name, score) VALUES (?, ?)", (self.QA.user_name, self.score))
            conn.commit()
            return self.score

    def fetch_leaderboard(self):
        myc.execute("SELECT name, score FROM leaderboard ORDER BY score DESC")
        return myc.fetchall()