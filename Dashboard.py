import streamlit as st
import pandas as pd

# set up data
df = pd.read_csv('training_dataset.csv')

# Make Page
st.set_page_config(page_title="OLIST_SLB")
st.title("OLIST_SLB PROJECT")
st.header("Tech Ia Simplon's Final Project")
st.markdown("use of the transformed OlisT dataset and fastAPI to make data visualisation,train and predict with machine learning models")
st.image(image="motherland_flag.jpg", caption="franco_congolese data/ia company") 
