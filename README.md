# Linear Regression Predictor (FastAPI + Interface Web)

![Python](https://img.shields.io/badge/python-3.10-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📚 Présentation du projet
Ce projet implémente une **régression linéaire simple** et fournit :

- Une **API FastAPI** pour obtenir la prédiction en JSON
- Une **interface web interactive** pour saisir une valeur `x` et afficher `y_pred`

L'objectif est de montrer comment déployer un modèle de machine learning simple et créer une interface utilisateur professionnelle.


 ## 🧠 Logique générale

Le projet suit les étapes suivantes pour entraîner le modèle et effectuer des prédictions :

## 1️⃣ Chargement et préparation des données

Nous utilisons des données synthétiques pour illustrer une régression linéaire simple.

La variable X représente les entrées (valeurs que l’utilisateur peut saisir), et y représente les sorties (valeurs à prédire).

Les données sont générées de manière à illustrer une relation linéaire simple

Chaque élément de X est une liste car scikit-learn attend un tableau 2D pour les entrées.


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

==> 80 % des données sont utilisées pour l’entraînement et 20 % pour le test.

## 3️⃣ Entraînement du modèle

Nous utilisons le modèle LinearRegression de scikit-learn :

model = LinearRegression()
model.fit(X_train, y_train)

Le modèle apprend la relation entre X et y pour pouvoir prédire de nouvelles valeurs.

## 4️⃣ Prédiction

Pour prédire la valeur de y pour une nouvelle entrée x, nous utilisons une fonction predict

## 🔢 Formule utilisée

                                y=a⋅x+b
## 📦 Dépendances principales

  + fastapi

  + uvicorn

  + numpy

  + scikit-learn

  + jinja2

## 🏗️ Architecture du système
Utilisateur
    ↓
Interface Web (Formulaire HTML / Jinja2)
    ↓
FastAPI (Endpoints GET / POST)
    ↓
Modèle LinearRegression (scikit-learn)
    ↓
Calcul de y_pred
    ↓
Résultat affiché sur l’interface / renvoyé en JSON
