from fastapi import FastAPI
from fastapi.responses import JSONResponse
import matplotlib.dates as mdates
import uvicorn

import pandas as pd
app = FastAPI()



@app.get("/fusion")
async def merge():
    # Importation des bases achats, clics et impressions

    achats = pd.read_csv("C:/Users/DELL/Desktop/ISE 2/Semestre 2/ML/Streamlit_NGUENANG/achats.csv")
    clics = pd.read_csv("C:/Users/DELL/Desktop/ISE 2/Semestre 2/ML/Streamlit_NGUENANG/clics.csv")
    impressions = pd.read_csv("C:/Users/DELL/Desktop/ISE 2/Semestre 2/ML/Streamlit_NGUENANG/impressions.csv")

    # On fusionne les 3 bases
    fusion_1 = pd.merge(clics, impressions, on="cookie_id")
    fusion = pd.merge(fusion_1, achats, on="cookie_id")
    # changement du type des variables de temps

    fusion['timestamp_x'] = pd.to_datetime(fusion['timestamp_x'], unit='s')
    fusion['date_impressions'] = fusion['timestamp_x'].dt.strftime('01-01-1970 %H:%M:%S')
    fusion['timestamp_y'] = pd.to_datetime(fusion['timestamp_y'], unit='s')
    fusion['date_clics'] = fusion['timestamp_y'].dt.strftime('01-01-1970 %H:%M:%S')
    fusion['timestamp'] = pd.to_datetime(fusion['timestamp'], unit='s')
    fusion['date_achats'] = fusion['timestamp'].dt.strftime('01-01-1970 %H:%M:%S')
    fusion = fusion.fillna("-")
    return fusion.to_dict()
