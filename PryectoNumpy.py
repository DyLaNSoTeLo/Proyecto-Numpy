from datasets import load_dataset
import numpy as np
import pandas as pd
import requests

#Parte 1

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]
edades = np.array(data['age'])
promedio_edad = np.mean(edades)

print(f"El promedio de edad de las personas que participaron en el estudio es: {promedio_edad}")

#Parte 2

df = pd.DataFrame(data)

df_muertos = df[df['is_dead'] == 1]
df_vivos = df[df['is_dead'] == 0]

promedio_edad_muertos = df_muertos['age'].mean()
promedio_edad_vivos = df_vivos['age'].mean()

print(f"El promedio de edad de las personas que fallecieron en el estudio es: {promedio_edad_muertos}")
print(f"El promedio de edad de las personas que sobrevivieron en el estudio es: {promedio_edad_vivos}")

#Parte 3

print(df.dtypes)

cantidad_gente_smoker = df.groupby(['is_male', 'is_smoker']).size()

hombres_fumadores = cantidad_gente_smoker[True, True]
mujeres_fumadoras = cantidad_gente_smoker[False, True]


print(f"La cantidad de hombres fumadores es: {hombres_fumadores}")
print(f"La cantidad de mujeres fumadoras es: {mujeres_fumadoras}")

#Parte 4 Apis

def download_csv(url):
    response = requests.get(url)
    name_new_csv = url.split("/")[-1] 

    with open(name_new_csv , 'w') as archivo:
        archivo.write(response.text)


download_csv('https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv')

#Parte 5 Clean data

def process_data(df):
    
    try:
        valores_faltantes = df.isnull().sum().sum()
        if valores_faltantes > 0:
            raise ValueError(f"El DataFrame tiene {valores_faltantes} valores faltantes.")
    except ValueError as e:
        print(e)

    try:
        filas_repetidas = df.duplicated().sum()
        if filas_repetidas > 0:
            raise ValueError(f"El DataFrame tiene {filas_repetidas} filas duplicadas.")
    except ValueError as e:
        print(e)

    
    Q1 = df['age'].quantile(0.25)
    Q3 = df['age'].quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df['age'] < (Q1 - 1.5 * IQR)) | (df['age'] > (Q3 + 1.5 * IQR)))]

    
    bins = [0, 12, 19, 39, 59, np.inf]
    labels = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    df['categoria_edad'] = pd.cut(df['age'], bins=bins, labels=labels)

    
    df.to_csv('datos_procesados.csv', index=False)
    return df


df_procesado = process_data(df)

#Parte 6 ETL

