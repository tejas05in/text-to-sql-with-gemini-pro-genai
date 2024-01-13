import google.generativeai as genai
import sqlite3
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()  # load all the environment variables


# configure genai
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


# function to load the google gemini model and provide queries as reponse
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text


# function to retrieve queries from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    print(rows)
    for row in rows:
        print(row)
    return rows


# Define Your prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION, MARKS \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]
# Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini APP to retrieve SQL Data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask this Question")

# if submit is clicked,

if submit:
    query = get_gemini_response(question, prompt)
    response = read_sql_query(query, "student.db")
    st.subheader("The response is: ")
    for row in response:
        print(row)
        st.write(row)
