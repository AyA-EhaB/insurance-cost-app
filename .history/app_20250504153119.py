import streamlit as st
import pickle

lr = pickle.load(open('../Artifacts/lr.pkl', 'rb'))
ohe = pickle.load(open('../Artifacts/ohe.pkl', 'rb'))