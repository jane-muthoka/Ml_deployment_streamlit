import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
#from prediction import predict
#import tensorflow
#from tensorflow import keras
#from tensorflow.keras import Sequential
#from tensorflow.keras.layers import Dense

#loading the model
model = load_model('model.json')  # Load the Keras model


def predict(GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research):
    # Create a DataFrame with the input data
    input_data = pd.DataFrame(
        [[GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research]],
        columns=["GRE Score", "TOEFL Score", "University Rating", "SOP", "LOR", "CGPA", "Research"]
    )

st.title('Predicting Graduate admission')#title
st.markdown('This model predicts the chances of admit into a school')#description

st.header("Prerequisites")

#defining the user inputs

GRE_Score = st.number_input('GRE Score:',min_value=0.1, max_value=340.0, value=1.0)
TOEFL_Score = st.number_input('TOEFL Score:',min_value=0.1, max_value=120.0, value=1.0)
University_Rating = st.number_input('University Rating:',min_value=0.1, max_value=5.0, value=1.0)
SOP = st.number_input('SOP:',min_value=0.1, max_value=5.0, value=1.0)
LOR = st.number_input('LOR:',min_value=0.1, max_value=5.0, value=1.0)
CGPA = st.number_input('CGPA:',min_value=0.1, max_value=10.0, value=1.0)
Research = st.number_input('Research:',min_value=0.1, max_value=1.0, value=1.0)



#button
#if st.button("Predict chance of Admit"):
    #Chance_of_Admit = predict(
        #np.array([["GRE Score", "TOEFL Score", "University Rating", "SOP", "LOR", "CGPA", "Research"]]))
    #st.success(f'The chance of admit is {result[0]:.2f} ')

if st.button("Predict chance of Admit"):
    Chance_of_Admit = predict(
        GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research)
    st.success(f'The chance of admit is {Chance_of_Admit[0][0]:.2f}')
