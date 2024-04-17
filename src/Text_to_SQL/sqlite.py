# Importing the dependencies and connecting to SQLITE DataBase
import sqlite3
import random
connection = sqlite3.connect("./data/Student_Data.db")

# Creating a cursor object to create tables

cursor = connection.cursor()

# Basic college student information table
table_info = """ 
Create table STUDENT(
    NAME VARCHAR(25),
    YEAR INT,
    DEPARTMENT VARCHAR(25),
    SECTION VARCHAR(25),
    CGPA FLOAT,
    PROJECTS INT
);
"""

cursor.execute(table_info)

# Inserting some records

cursor.execute(''' Insert Into STUDENT values('Dhruv Pamneja', 3,'CSE','A',8.13,3)''')

names = [
    "Aarav", "Vihaan", "Advik", "Aadi", "Reyansh", "Mohammed", "Arnav", "Shaan", "Ayaan", "Krishna", 
    "Mitansh", "Atharva", "Vivaan", "Aaryan", "Ishaan", "Rudra", "Shaurya", "Darsh", "Rishabh", "Kabir",
    "Yuvan", "Ishan", "Vedant", "Sai", "Arush", "Aryan", "Aadi", "Viraj", "Advait", "Rishi",
    "Aarush", "Siddharth", "Rohan", "Aryan", "Aahan", "Vihaan", "Ayaan", "Dev", "Yuvraj", "Ritvik",
    "Tanish", "Veer", "Yash", "Samarth", "Rudransh", "Parth", "Ansh", "Vihan", "Kiaan"
]

def generate_random_data(names):
    random_data = []
    for _ in range(len(names)):
        # Ensuring to add unique names
        name = random.choice(names)
        names.remove(name)
        
        year = random.randint(1, 4)
        department = random.choice(['CSE', 'EE', 'CE', 'BE', 'PE', 'GE'])
        section = random.choice(['A', 'B', 'C', 'D', 'E'])
        cgpa = round(random.uniform(6.00, 10.00), 2)
        projects = random.randint(0, 10) 
        random_data.append((name, year, department, section, cgpa, projects))
    return random_data


random_data = generate_random_data(names)
for data in random_data:
    cursor.execute('''INSERT INTO STUDENT VALUES(?, ?, ?, ?, ?, ?)''', data)  
    
connection.commit()
    









