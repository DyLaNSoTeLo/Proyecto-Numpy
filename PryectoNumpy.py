from datasets import load_dataset
import numpy as np
import pandas as pd

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