from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from model_utils import load_model, prediction

app = FastAPI()

class LanguageInput(BaseModel):
    language : str

class FeaturesInput(BaseModel):
    sepal_length:float
    sepal_width:float
    petal_length:float
    petal_width:float

class PredictionOutput(BaseModel):
    category:int

model = load_model()


@app.post('/predict')
def prediction_root(feature_input:FeaturesInput):
    features = [value for value in feature_input.dict().values()]
    predictions = prediction(model, [features])
    return PredictionOutput(category=predictions)
    

@app.post('/predict/v0')
def prediction_root(feature_input:FeaturesInput):
    features = [feature_input.sepal_length, feature_input.sepal_width, feature_input.petal_length, feature_input.petal_width]
    predictions = prediction(model, [features])
    return PredictionOutput(category=predictions)


@app.post('/language')
def language_root(language_input:LanguageInput):
    if language_input.language.lower() == "english":
        return {"message" : "Hello"}
    elif language_input.language.lower() == "french":
        return {"message" : "Bonjour"}
    else :
        return {"message": "La langue n'est pas pris en charge"}


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}