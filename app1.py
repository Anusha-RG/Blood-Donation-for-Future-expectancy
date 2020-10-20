import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_note_authentication(recency,frequency,monetary,time):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: recency
        in: query
        type: number
        required: true
      - name: frequency
        in: query
        type: number
        required: true
      - name: monetery
        in: query
        type: number
        required: true
      - name: time
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[recency,frequency,monetary,time]])
    print(prediction)
    return prediction



def main():
    st.title("TRANSFUSION")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> Blood donation for future expectancy </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    recency = st.text_input("Recency (months)","Type Here")
    frequency = st.text_input("Frequency (times)","Type Here")
    monetary = st.text_input("Monetary (c.c. blood)","Type Here")
    time = st.text_input("Time (months)","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(recency,frequency,monetary,time)
    st.success('Donation in March 2007 {}'.format(result))

if __name__=='__main__':
    main()
