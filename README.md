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
