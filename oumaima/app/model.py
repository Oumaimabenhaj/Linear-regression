import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Données
X = np.array([[i] for i in range(1, 21)])
y = np.array([2 * i for i in range(1, 21)])

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Entraînement
model = LinearRegression()
model.fit(X_train, y_train)

def predict(model, x: float) -> float:
    x_array = np.array([[x]])
    return float(model.predict(x_array)[0])

