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
st.header('Best ML Model Selection - olist_db dataset')
st.markdown('train and score 2 models on your optmised dataset')
st.sidebar.header('choose your ML Model')

options = st.sidebar.radio('Select Model',
                          options=['Logistic Regression',
                                   'RandomForestClassifier with fine tuning',
                                   'Our choice'])