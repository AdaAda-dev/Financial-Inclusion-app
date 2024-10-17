#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, r2_score, mean_squared_error

#import the streamlit library
import streamlit as st

#give the app a name
st.title("FINANCIAL INCLUSION")

# Import picture
from PIL import Image
image = Image.open("UNUZ4zR - Imgur.JPG")

st.image(image, width = 500)

st.text("The dataset contains demographic information and what financial services are used by \napproximately 33,600 individuals across East Africa. The ML model role is to predict which individuals are most likely to have or use a bank account.\nThe term financial inclusion means:  individuals and businesses have access to useful \nand affordable financial products and services that meet their needs – transactions, \npayments, savings, credit and insurance – delivered in a responsible and sustainable way.")

# Input features with consistent types
country = st.number_input("country", min_value=0, max_value=100, step=1, format="%d")  
year = st.number_input("year", min_value=2000, max_value=2024, step=1, format="%d")
bank_account = st.number_input("bank_account", min_value=0, max_value=1, step=1, format="%d")
location_type = st.number_input("location_type", min_value=0, max_value=30, step=1, format="%d")
cellphone_access = st.number_input("cellphone_access", min_value=0, max_value=10, step=1, format="%d")
household_size = st.number_input("household_size", min_value=0, max_value=100, step=1, format="%d")
age_of_respondent = st.number_input("age_of_respondent", min_value=0, max_value=100, step=1, format="%d")
gender_of_respondent = st.number_input("gender_of_respondent", min_value=0, max_value=1, step=1, format="%d")
relationship_with_head = st.number_input("relationship_with_head", min_value=0, max_value=10, step=1, format="%d")
marital_status = st.number_input("marital_status", min_value=0, max_value=5, step=1, format="%d")
education_level = st.number_input("education_level", min_value=0, max_value=10, step=1, format="%d")
job_type = st.number_input("job_type", min_value=0, max_value=20, step=1, format="%d")


# Once inputs are provided, make a prediction
if st.button("Predict"):
    input_data = pd.DataFrame({
        'country': [country],
        'year': [year],
        'bank_account': [bank_account],
        'location_type': [location_type],
        'cellphone_access': [cellphone_access],
        'household_size': [household_size],
        'age_of_respondent': [age_of_respondent],
        'gender_of_respondent': [gender_of_respondent],
        'relationship_with_head': [relationship_with_head],
        'marital_status': [marital_status],
        'education_level': [education_level],
        'job_type': [job_type],
    })

    # Make a prediction using the loaded model
    prediction = model.predict(input_data)

    # Display the result
    if prediction == 1:
        st.write("The customer needs to have a bank account")
    else:
        st.write("The customer does not need a bank account")

