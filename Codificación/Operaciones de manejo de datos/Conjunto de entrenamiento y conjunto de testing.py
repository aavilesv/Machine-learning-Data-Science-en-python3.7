# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 22:28:22 2021
@author: ANGELO
"""
#Conjunto de entranamiento y conjunto de testing
import pandas as pd
#estadistica y probalidad
import numpy as np
#histogramas
import matplotlib.pyplot as plt
## Con la libreria sklearn estadistica praa hacer testeo
from sklearn.model_selection import train_test_split
data =pd.read_csv('G:/Data Science/Codificación/python-ml-course-master/datasets/customer-churn-model/Customer Churn Model.txt')
print(len(data))

#Dividir utilizando la distribución normal
a= np.random.random(len(data))
print(a)
#plt.hist(a)

check =(a<0.8)# de todos los numeros aleatorios de la normal se que por debajo del 80=0.8
#tambien puedes hacerlo despendiendo cual quieres hacer el testigin por ejemplo aqui es el %80
check=check.astype(int)
plt.hist(check.astype(int))#convirtiendo el array de valores Booleanos a Enteros.

# Con la libreria sklearn

entramiento, testing =train_test_split(data,test_size = 0.2)#☻ el 0.2 será utiliza para hacer test
#esto te hace poder analizar datos tanto si quieres para testign o para entramiento

# Usaremos un función de shuffle 
#para hacer el entramiento y el testing  nos basamos en la porción de datos
import sklearn
data = sklearn.utils.shuffle(data)#Esto te guarda todo mezclado los datos lo volvemos a poner en data
corte_id =int(0.75*len(data))
entranamien_data= data[:corte_id]
testing_data= data[corte_id:]
print(len(entranamien_data))#esta
print(len(testing_data))




