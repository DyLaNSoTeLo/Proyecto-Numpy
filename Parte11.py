import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('datos_procesados_2.csv')

if 'smoking' in df.columns:
    
    X = df.drop(['categoria_edad'], axis=1)
    y = df['smoking']

    # Usando seaborn para el histograma
    sns.histplot(y, kde=False)
    plt.show()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)

    print('Accuracy: ', acc)
