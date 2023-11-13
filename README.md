# Proyecto-Numpy 

#Parte 1
Cargar el dataframe de fallas_cardiacas
Seleccionar la columna de edad, y pasarlo a array de NumPy
Sacar el promedio de las edades y hacer print.

#Parte 2

Convertir la estructura Dataset en un DataFrame de Pandas usando pd.DataFrame.
Separar el dataframe en dos diferentes, uno conteniendo las filas con personas que perecieron (is_dead=1) y otro con el complemento.
Calcular los promedios de las edades de cada dataset e imprimir.


#Parte 3

Verificar que los tipos de datos son correctos en cada columna
Crear la columna 'sex' y  'smoking' en el DataFrame
Verificar si las columnas "sex y smoking" existen en DataFrame
Calcular la cantidad de hombres fumadores vs mujeres fumadoras


#Parte 4

Realizar un GET request para descargar los datos necesarios y escribe la respuesta como un archivo de texto plano con extensión csv 
Agrupar el código en una función reutilizable que reciba como argumento la url.


#Parte 5

Verificar que no existan valores faltantes
Verificar que no existan filas repetidas
Verificar si existen valores atípicos y eliminarlos
Crear una columna que categorice por edades
Guardar el resultado como csv


#Parte 6

Descargar el archivo que necesitamos usando los metodos aprendidos en clase (with open as file)
Categorizamos los datos por edad
Automatizamos los pasos anteriores, y hacemos que se pueda usar una url como argumento para que se ejecute nuestro codigo


#Parte 7

Hacemos uso de las librerias de visualizacion y manejo de datos previamente aprendidas
Creamos un histograma con la distribucion de las edades de las personas
Y creamos otro histograma para visualizar los datos de hombres y mujeres que padecen: Anemia, Diabetes, Fuman y Han muerto.


#Parte 8

Usamos los datos de la parte anterior para crear graficos de torta, que nos permitan ver una mejor distribucion con porcentajes,
y usamos los metodos y personalizaciones propias de las librerias.


#Parte 9

Usamos un grafico 3D para visualizar de manera mas detallada la distribucion de las personas que han muerto, 
usando la técnica de reducción de dimensionalidad para tratar de visualizar aproximadamente la estructura de nuestros datos.


#Parte 10

Cargar los datos procesados anteriormente
Eliminar las columnas DEATH_EVENT y age del dataframe para que sea la matriz X
Ajustar una regresión lineal sobre el resto de columnas y usar la columna age como vector y
Predice las edades y compara con las edades reales
Calcula el error cuadrático medio.


#Parte 11

Cargar los datos procesados nuevamente
Verificar si la columna 'smoking' existe en el DataFrame
Eliminar la columna categoria_edad del dataframe para que sea la matriz X
Ajustar una regresión lineal sobre el resto de columnas y usar la columna smoking como vector y
Graficar la distribución de clases
Realizar la division del dataset en conjunto de entrenamiento y test
Ajustar el árbol de decisión
Predecir las clases y comparar con las clases reales
Calculae el accuracy.


#Parte 12

 Ajustar un random forest
 Predecir nuevamente las clases y compara con las clases reales
 Calcular el accuracy.
 Calcular el F1-Score.
 Calcular la matriz de confusión.
 

