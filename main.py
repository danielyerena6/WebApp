from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

class Item(BaseModel):
    Medidas: list

@app.get("/")
def home():
    return {"message": "Pagina activa"}

@app.post("/predicciones")
def prediccion1(item: Item):
    medidas = item.Medidas
    arbol = joblib.load('random_forest_entrenado.pkl')
    predicciones = arbol.predict([medidas])
    return {"message": f'El vino corresponde a la clase {predicciones}'}
