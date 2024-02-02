import requests
import streamlit as st
import pandas as pd
import sqlite3

# set up data
#df = pd.read_csv('training_dataset.csv')
#connection = sqlite3.connect('olist_db.db')
#df = pd.read_sql_query("SELECT * FROM TrainingDataset",connection)

#Make page
st.set_page_config(page_title='OLIST_SLB')
st.header('Prediction - olist_db dataset')
st.markdown('make predictions using the best MLmodel tested')
st.sidebar.header('Make prediction')
 # a adapter avec mes variables entrantes choisies ex latitude et longitude
""" sep_len = st.sidebar.text_input("Sepal Length")
sep_wid = st.sidebar.text_input("Sepal Width")
pet_len = st.sidebar.text_input("Petal Length")
pet_wid = st.sidebar.text_input("Petal Width") """

predict = st.sidebar.button("Predict")

