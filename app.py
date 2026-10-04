from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load trained model
model = joblib.load("car_price_model.pkl")

app = FastAPI(
    title="Used Car Price Appraiser API",
    description="API for predicting used car selling prices",
    version="1.0"
)


class CarData(BaseModel):
    make: str
    model: str
    trim: str
    body: str
    transmission: str
    state: str
    condition: float
    odometer: float
    color: str
    interior: str
    car_age: int


@app.get("/")
def home():
    return {
        "message": "Used Car Price Appraiser API is running"
    }


@app.post("/predict")
def predict_price(car: CarData):

    input_data = {
        "make": car.make,
        "model": car.model,
        "trim": car.trim,
        "body": car.body,
        "transmission": car.transmission,
        "state": car.state,
        "condition": car.condition,
        "odometer": car.odometer,
        "color": car.color,
        "interior": car.interior,
        "car_age": car.car_age
    }

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]

    return {
        "predicted_price": round(float(prediction), 2),
        "currency": "USD"
    }