import streamlit as st
import pickle

lr = pickle.load(open('../Artifacts/lr.pkl', 'rb'))
ohe = pickle.load(open('../Artifacts/ohe.pkl', 'rb'))


# make title for the project
st.title('Predict Health Insurance Cost')

# taking number input from user

st.number_input("Age", min_value = 18 ,