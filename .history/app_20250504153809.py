import streamlit as st
import pickle

lr = pickle.load(open('../Artifacts/lr.pkl', 'rb'))
ohe = pickle.load(open('../Artifacts/ohe.pkl', 'rb'))


# make title for the project
st.title('Predict Health Insurance Cost')

# taking number input from user

age = st.number_input("Age", min_value = 18.0 ,max_value = 64.0)
child = st.number_input("Number of Children", min_value = 0,max_value = 5)
bmi = st.number_input("BMI", min_value = 15.0 ,max_value = 47.0)

# taking categorical input from user
