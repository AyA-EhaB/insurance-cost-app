import streamlit as st
import pickle

lr = pickle.load(open('model.pkl', 'rb'))