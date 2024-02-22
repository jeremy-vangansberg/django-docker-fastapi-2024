from fastapi import FastAPI
from pydantic import BaseModel
from model_utils import load_model, predict_prod

model = load_model()

app = FastAPI()

# Modèle Pydantic pour la structure de données d'entrée
class FeaturesInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class PredictionOut(BaseModel):
    predictions : float

@app.post("/predict")
async def predict(payload: FeaturesInput):
    features = [value for value in payload.dict().values()]
    predictions = predict_prod(model, [features])
    return PredictionOut(predictions=predictions)