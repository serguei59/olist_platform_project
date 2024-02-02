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
st.header('Data Visualisation - olist_db dataset')
st.markdown('Data analysis from transformed and useable dataset.')
st.sidebar.header('Visualize your data')

options = st.sidebar.radio('Select visualisation',
                          options=['Geomapping',
                                   'Orders analysis',
                                   'Products analysis',
                                   'Sellers anaysis'])

if options == "Geomapping":
    #je declenche ma data visualisation
    url = f"http://localhost:8000/geomap_data"

     # envoi de requete get et recup de reponse
    response  = requests.get(url)
    geomapper = 'geomapping succeed'
        #verif si requete a reussi (statut 200)
    if response.status_code == 200:
            geomapper = response.json()["geomapping"]
            st.success(f"Geomapping result: {geomapper}")
    else:
        st.error("Error in geomapping request")

    st.image('test.png')

elif options == "Orders analysis":
    #
    st.markdown("repartition des orders par etat")

elif options == "Products analysis":
    st.markdown("top 10 products")

elif options == "Sellers analysis":
    st.markdown=("in progress")


