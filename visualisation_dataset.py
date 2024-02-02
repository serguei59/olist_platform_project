import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.basemap import Basemap
from datetime import datetime
import streamlit as st

# je choisis de travailler sur ma table training dataset en base elle est nettoyée et disponible
# ou je fournit précisément au plus efficacepour un besoin client => geolocation_dataset est une version nettoyée du fichier csv
# set up data


#geomap

def geomap():

    connection = sqlite3.connect("olist_db.db")
    df_geolocation = pd.read_sql_query("SELECT * FROM Geolocation",connection)

    lat = df_geolocation['geolocation_lat']
    lon = df_geolocation['geolocation_lng']

    fig = plt.figure(figsize=(15,15))

    m = Basemap(llcrnrlat=-55.401805,llcrnrlon=-92.269176,urcrnrlat=13.884615,urcrnrlon=-27.581676)
    m.bluemarble()
    m.drawmapboundary(fill_color='#46bcec') # Make your map into any style you like
    m.fillcontinents(color='#f2f2f2',lake_color='#46bcec') # Make your map into any style you like
    #m.drawcoastlines()
    m.drawcountries()
    m.scatter(lon, lat,zorder=10,alpha=0.5,color='tomato')

    plt.savefig('test.png')
    print('test_savefig')

    connection.commit()


# orders par etat
