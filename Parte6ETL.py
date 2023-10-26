import pandas as pd
import requests
import numpy as np
import sys

def download_csv(url):
    response =  requests.get(url)
    name_file = 'datos_procesados.csv'

    with open(name_file, 'w', encoding='utf-8') as archivo:
        archivo.write(response.text)

    return pd.read_csv(name_file)

def clasificar_datos(df): 
    bins = [0, 12, 19, 39, 59, np.inf]
    labels = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    df['categoria_edad'] = pd.cut(df['age'], bins=bins, labels=labels)

    return df

def main():
    url = sys.argv[1]

    df = download_csv(url)

    df_clasificado = clasificar_datos(df)

    df_clasificado.to_csv('datos_procesados_2.csv', index=False)

if __name__ == '__main__':
    main()

# python Parte6ETL.py https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv