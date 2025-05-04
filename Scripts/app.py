import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os 


base_path = os.path.dirname(os.path.dirname(__file__))  # Go up from Scripts/
lr_path = os.path.join(base_path, 'Artifacts', 'lr.pkl')
ohe_path = os.path.join(base_path, 'Artifacts', 'ohe.pkl')

lr = pickle.load(open(lr_path, 'rb'))
ohe = pickle.load(open(ohe_path, 'rb'))
# Page configuration
st.set_page_config(page_title="Health Insurance Cost Predictor", page_icon="💸", layout="centered")

# Main title
st.markdown("<h1 style='text-align: center; color: teal;'>💸 Predict Health Insurance Cost</h1>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar for input
st.sidebar.header("Input Information")

age = st.sidebar.number_input("Age", min_value=18.0, max_value=64.0, step=1.0)
bmi = st.sidebar.number_input("BMI", min_value=15.0, max_value=47.0, step=0.1)
child = st.sidebar.number_input("Number of Children", min_value=0, max_value=5, step=1)

sex = st.sidebar.selectbox("Gender", ('male', 'female'))
smoker = st.sidebar.selectbox("Smoker", ('no', 'yes'))
region = st.sidebar.selectbox("Region", ('northeast', 'southeast', 'southwest', 'northwest'))

# Prediction button
if st.sidebar.button("Predict Cost"):
    # Encode categorical data
    temp = ohe.transform([[sex, region, smoker]]).toarray()
    data = [age, bmi, child]
    data.extend(temp[0])
    
    # Make prediction
    pred = lr.predict([data])
    cost = np.exp(pred)[0]

    # Show result
    st.success("✅ Prediction Completed!")
    st.markdown(f"<h3 style='text-align: center;'>Estimated Annual Insurance Cost:</h3>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center; color: green;'>${cost:,.2f}</h2>", unsafe_allow_html=True)
