# Importing the dependencies
import streamlit as st 
import sqlite3
from src.Text_to_SQL.utils import get_gemini_response,read_sql_query
from src.Text_to_SQL.prompt import prompt
from src.Text_to_SQL.logger import logging

# Creating the Page
st.set_page_config(page_title="Text to SQL Retrieval")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input : ",key="input")

submit = st.button("Ask the question!")


# Running the query
if submit:
    logging.info("----------------------------START------------------------------")
    logging.info("Response Requested")
    
    response = get_gemini_response(question,prompt)
    logging.info("Response Generated")
    print(response)
    
    response = read_sql_query(response,"./data/Student_Data.db")
    logging.info("Response converted as SQL")
    
    
    st.subheader("The response is : ")
    for row in response:
        print(row)
        st.header(row)
    
    logging.info("----------------------------END------------------------------")
    