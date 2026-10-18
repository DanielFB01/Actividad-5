"""
Funciones de limpieza y preparación de datos para Actividad5.
Archivo: datos_prep.py
"""

import os
import pandas as pd


def load_data(path):
    """Carga un archivo CSV como DataFrame.

    Args:
        path (str): Ruta al archivo CSV.

    Returns:
        pd.DataFrame
    """
    return pd.read_csv(path)


def clean_data(df):
    """Ejemplo simple de limpieza:
    - Elimina duplicados
    - Rellena valores NA con la mediana para columnas numéricas

    Args:
        df (pd.DataFrame): DataFrame original

    Returns:
        pd.DataFrame: DataFrame limpio
    """
    df = df.copy()
    df = df.drop_duplicates()
    num_cols = df.select_dtypes(include=['number']).columns
    for col in num_cols:
        median = df[col].median()
        df[col] = df[col].fillna(median)
    return df


def save_clean(df, out_path):
    """Guarda el DataFrame limpio en CSV."""
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    df.to_csv(out_path, index=False)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Preparar y limpiar datos')
    parser.add_argument('--input', required=True, help='Ruta al CSV original')
    parser.add_argument('--output', required=True, help='Ruta de salida para datos limpios')
    args = parser.parse_args()

    df = load_data(args.input)
    df_clean = clean_data(df)
    save_clean(df_clean, args.output)
    print(f"Datos limpios guardados en {args.output}")
