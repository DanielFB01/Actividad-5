"""
Script de entrenamiento y registro en MLflow (esqueleto).
Archivo: train.py
"""

import argparse
import os
import pandas as pd

try:
    import mlflow
except Exception:
    mlflow = None

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def train(data_path, target_col, mlflow_experiment=None):
    df = pd.read_csv(data_path)
    X = df.drop(columns=[target_col])
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    if mlflow is not None:
        mlflow.set_experiment(mlflow_experiment or 'Actividad5')
        with mlflow.start_run():
            mlflow.log_param('model', 'LogisticRegression')
            mlflow.log_metric('accuracy', float(acc))
            # Para registrar el modelo necesitarías mlflow.sklearn.log_model
    else:
        print('MLflow no está disponible. Se muestra métricas en consola.')

    print(f'Accuracy: {acc:.4f}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Entrenar modelo y (opcional) registrar en MLflow')
    parser.add_argument('--data', required=True, help='Ruta al CSV con datos limpios')
    parser.add_argument('--target', required=True, help='Nombre de la columna objetivo')
    parser.add_argument('--mlflow-experiment', default=None, help='Nombre del experimento MLflow')
    args = parser.parse_args()

    train(args.data, args.target, args.mlflow_experiment)
