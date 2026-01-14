from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.model import model, predict

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Endpoint racine → interface HTML
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "prediction": None})

# Endpoint POST → calculer la prédiction
@app.post("/", response_class=HTMLResponse)
def calculate_prediction(request: Request, x: float = Form(...)):
    y_pred = predict(model, x)
    return templates.TemplateResponse("index.html", {"request": request, "prediction": y_pred, "x": x})
