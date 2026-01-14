import pytest
import numpy as np
from app.model import model, predict

def test_predict_basic():
    # Test simple : x = 5 → y = 10
    x = 5
    expected = 10
    result = predict(model, x)
    assert result == expected, f"Expected {expected}, got {result}"

def test_predict_float():
    # Test avec un float
    x = 3.5
    expected = 7
    result = predict(model, x)
    assert result == expected, f"Expected {expected}, got {result}"
