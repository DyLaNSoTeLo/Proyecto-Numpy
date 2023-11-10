import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


df = pd.read_csv('datos_procesados_2.csv')


X = df.drop(['DEATH_EVENT', 'categoria_edad'], axis=1)

y = df['age']

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

mse = mean_squared_error(y, y_pred)

print('Error cuadrático medio: ', mse)