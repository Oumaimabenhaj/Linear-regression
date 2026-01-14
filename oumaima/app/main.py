from fastapi import FastAPI
from app.model import model, predict

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Linear Regression API"}

@app.get("/predict")
def predict_endpoint(x: float):
    y_pred = predict(model, x)
    return {
        "x": x,
        "y_pred": y_pred
    }
