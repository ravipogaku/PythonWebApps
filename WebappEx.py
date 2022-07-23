# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 16:32:04 2022

@author: ravip
"""

import streamlit as st
import pandas as pd

st.write("""
# Division App

This app divides first_number by second_number
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    firstNumber = st.number_input("First_Number",min_value=1,max_value=400000 ,step=1)
    secondNumber = st.number_input("Second_Number",min_value=1,max_value=400000 ,step=1)
    thirdNumber = st.number_input("Quotient_Number")
    
    
    data = {
            'First_Number': firstNumber,
            'Second_Number': secondNumber,
            'Quotient_Number': thirdNumber
            
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

df['Quotient_Number'] = df['First_Number']/df['Second_Number']

st.write("Result",df['Quotient_Number'])


    