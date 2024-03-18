import mysql.connector as mysql

conn = mysql.connect(host='localhost', 
                    user='root', 
                    password='root', 
                    database='Quiz')

myc = conn.cursor()

myc.execute("CREATE TABLE questions (id INT AUTO_INCREMENT PRIMARY KEY, question VARCHAR(255), option1 VARCHAR(255), option2 VARCHAR(255), option3 VARCHAR(255), option4 VARCHAR(255), answer VARCHAR(255))")
