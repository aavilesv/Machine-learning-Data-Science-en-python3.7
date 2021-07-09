# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 21:34:52 2021

@author: ANGELO
"""

#dataset o datafraem
import pandas as pd
#estadistica
import numpy as np
#histograma  
import matplotlib.pyplot as plt


n=10# experimiento 1000 que esten fuera y dentro del circulo puntos
#son lista dentro diccionarios
media=1.5
sddesviicionestandar=2.5 
data= pd.DataFrame({#.DataFrame nos permite crear el diccionario a dataframe
    'A': np.random.randn(10),#cuantos valores aleatorio quiero generar  en mi caso 10 distrubucion normal 
    'B': media +sddesviicionestandar * np.random.randn(10),#con formula cuantos valores aleatorio quiero generar  en mi caso 10 distrubucion normal
    'C' :np.random.uniform(5,32,n).tolist()#numero aleatorio entre o y 1 y el valor de n y lo convertimos a lista
      })



plt.hist(data)
#plt.hist(data['A'])#normal
#plt.hist(data['B'])#normal 
#plt.hist(data['C'])#uniforme 
dataa =pd.read_csv('G:/Data Science/Codificación/python-ml-course-master/datasets/customer-churn-model/Customer Churn Model.txt')
colum_names=dataa.columns.values.tolist()
ncolumns=len(colum_names) # siempre debe ser el mismo tamaño
new_data =pd.DataFrame({
    'Column Name': colum_names,
    'A': np.random.randn(ncolumns),#cuantos valores aleatorio quiero generar  en mi caso 10 distrubucion normal 
    'B' :np.random.uniform(0,1,ncolumns)#numero aleatorio entre o y 1 y el valor de ncolumns y lo convertimos a lista
    
    },index=range(42,42+ncolumns) # generamos valores entre 42 y 42 mas ncolumnas comienza desde 42 y termina desde ncolumns
    #index es muy util si quieres unir con otros dataframe 
    ) 
print(new_data)

print(data.describe())#describe media, min , max, etc.