# Actividad 5

Este repositorio contiene la estructura mínima para la Actividad 5.

Estructura creada:

Actividad5/
├── datos/
│   ├── datos_ini/    # datos originales (colocar aquí los archivos fuente)
│   └── datos_limp/   # datos procesados y listos para entrenar
├── fuentes/
│   ├── entrena.ipynb # notebook de Colab (entrenamiento y evaluación)
│   ├── datos_prep.py # funciones de limpieza
│   └── train.py      # script de entrenamiento y registro en MLflow
├── README.md
└── CHANGELOG.md

Reproducción rápida

1. Coloca los datos originales en `Actividad5/datos/datos_ini/` (ej. CSV).
2. Limpia los datos:
   ```bash
   python Actividad5/fuentes/datos_prep.py --input Actividad5/datos/datos_ini/miarchivo.csv --output Actividad5/datos/datos_limp/miarchivo_limpio.csv
   ```
3. Entrena y registra (opcional MLflow):
   ```bash
   python Actividad5/fuentes/train.py --data Actividad5/datos/datos_limp/miarchivo_limpio.csv --target objetivo --mlflow-experiment Actividad5
   ```

Decisiones principales

- Se deja una estructura modular: separación clara entre datos y código fuente.
- Se incluyen placeholders mínimos para que la actividad sea reproducible.
- `train.py` es un esqueleto que usa scikit-learn y opcionalmente MLflow para registro.
