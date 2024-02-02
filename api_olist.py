from fastapi import FastAPI
import numpy as np
from traitement_dataset import make_data_cleaning
from visualisation_dataset import geomap

app = FastAPI()
filtre_traitement = bool

@app.get("/")
def read_root():
    print('toto')
    return {"message": "welcome on board"}

@app.get("/clean_data")
def clean_data():
    print('Cleaning in progress')
    make_data_cleaning()
    return {"cleaning": "Cleaning completed"}

@app.get("/geomap_data")
def do_geomapping():    
    print('production de la carte')
    geomap()
    return {"geomapping": ""}
    