# Importing the dependencies, loading the environment variables and congifuring any models/libraries
import sqlite3
from dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load the Google Gemini Model and provide the response

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text


# Function to retrieve query from the database

def read_sql_query(sql,db):
    con = sqlite3.connect(db)
    cur = con.cursor()
    
    cur.execute(sql)
    
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
        
    return rows