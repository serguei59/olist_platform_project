import requests
import streamlit as st
import pandas as pd
import pages_access_filter

# set up data
#df = pd.read_csv('training_dataset.csv')

#Make page
st.set_page_config(page_title='OLIST_SLB')
st.header('Dataset Cleaning - olist_db dataset')
st.markdown('from new datas to  transformed and useable ones.')
st.sidebar.header('clean your data')

data_cleaning = st.sidebar.button("Cleaning")

if data_cleaning:

    url = f"http://localhost:8000/clean_data"

    response  = requests.get(url)
    cleaned_data = 'cleaning succeeded'
        #verif si requete a reussi (statut 200)
    if response.status_code == 200:
        species_pred = response.json()["cleaning"]
        st.success(f"Cleaning result: {cleaned_data}")
    else:
        st.error("Error in cleaning request")


