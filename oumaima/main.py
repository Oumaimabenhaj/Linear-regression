from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return {"message":"hello oumaima"}
@app.post("/predict")
def predict (x):

    return {"message": "hello"}

@app.get("/predict")
def predict_endpoint(x: float):
    y_pred = predict(model, x)
    return {"x": x, "y_pred": y_pred}

         