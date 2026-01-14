from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_post_prediction():
    # On envoie x = 5
    response = client.post("/", data={"x": 5})
    assert response.status_code == 200
    assert "10.0" in response.text  # Vérifie que la prédiction est affichée
