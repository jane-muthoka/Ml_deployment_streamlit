import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

#defining the prediction function
def predict(GRE Score,TOEFL Score,University Rating,SOP,LOR, CGPA,Research):
    prediction = model.predict(pd.DataFrame([[GRE Score,TOEFL Score,University Rating,SOP,LOR, CGPA,Research]], columns=[GRE Score,TOEFL Score,University Rating,SOP,LOR, CGPA,Research]))
    return prediction


st.title('Predicting Graduate admission')#title
st.markdown('This model predicts the chances of admit into a school')#description

st.header("Prerequisites")

#defining the user inputs

GRE Score = st.number_input('GRE Score:',min_value=0.1, max_value=100.0, value=1.0)
TOEFL Score = st.number_input('TOEFL Score:',min_value=0.1, max_value=100.0, value=1.0)
University Rating = st.number_input('University Rating:',min_value=0.1, max_value=100.0, value=1.0)
SOP = st.number_input('SOP:',min_value=0.1, max_value=100.0, value=1.0)
LOR = st.number_input('LOR:',min_value=0.1, max_value=100.0, value=1.0)
CGPA = st.number_input('CGPA:',min_value=0.1, max_value=100.0, value=1.0)
Research = st.number_input('Research:',min_value=0.1, max_value=100.0, value=1.0)



#button
if st.button("Predict chance of Admit"):
    Chance of Admit = predict(
        np.array([[GRE Score,TOEFL Score,University Rating,SOP,LOR, CGPA,Research]]))
    st.success(f'The chance of admit is {result[0]:.2f} ')


