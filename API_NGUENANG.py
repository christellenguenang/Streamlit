from fastapi import FastAPI
from fastapi.responses import JSONResponse
import matplotlib.dates as mdates
import uvicorn

import pandas as pd
app = FastAPI()


app = Flask(__name__)

@app.route("/fusion")
def get_donnees():
    # Importation des bases achats, clics, et impressions
    achats = pd.read_csv("achats.csv")
    clics = pd.read_csv("clics.csv")
    impressions = pd.read_csv("impressions.csv")

    # On fusionne les 3 bases
    fusion_1 = pd.merge(clics, impressions, on="cookie_id")
    fusion = pd.merge(fusion_1, achats, on="cookie_id")

    return jsonify(fusion)

if __name__=='__API_NGUENANG__':
 uvicorn.run(app, host='127.0.0.1',port=8000)
