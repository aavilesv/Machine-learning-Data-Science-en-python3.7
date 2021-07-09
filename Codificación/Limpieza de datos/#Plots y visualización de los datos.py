# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:57:03 2021

@author: ANGELO
"""
#como estas usando el mismo data debes comentar 
#el codigo que ya no uses o crear mas variables
#Plots y visualización de los datos
import pandas as pd
#calculo
import numpy  as np
import matplotlib.pyplot as plt
data =pd.read_csv('G:\Data Science\Codificación\python-ml-course-master\datasets\customer-churn-model\Tab Customer Churn Model.txt ')
presentar=data[0:15]

total=len(data)
#presetar los graficos 
#savefig('path_donde_guardar_im.jpeg')
###Scatter plot 
#vertor x &  y 
%matplotlib inline
data.plot(kind="scatter",x="Day Mins",y="Day Charge")

#Histograma de frecuencia es ver como se distribuye los grupos se agrupan 
#donde se concentran los valores maximo, minimo los datos 
#agrupados 
#bins es para poder repartir entre  bloques o el valor que tu le pongas 
#puede ser numero como 1,2,3,etc o en nuestro caso usaremos estadistica 
#plt.hist(data['Day Calls'],bins=7)
#primero sacomos el regla sturges(k) y con ceil se convierte a entero
k=np.ceil(1+np.log2(len(data)))
plt.hist(data['Day Calls'],bins=int(k))

#xlabel el nombre en x 
plt.xlabel("Numero de llamadas al día")
#ylabel el nombre en y
plt.ylabel("Frecuencia")

#Boxplot, diagrama de caja y bigotes 
plt.boxplot(data['Day Calls']) c
plt.xlabel("Numero de llamadas al día")
#ylabel el nombre en y
plt.ylabel("Frecuencia")
#Rango intercuartil se coje el 25% y el 75% para eso le pones 
#el discrebe()
print(data['Day Calls'].describe())
IQR=data['Day Calls'].quantile(0.75)-data['Day Calls'].quantile(0.25)
print(data['Day Calls'].quantile(0.75)-data['Day Calls'].quantile(0.25))
#figura 
# matriz de 2x2  y pone un panel y lo lo vas llenando
fig, axs = plt.subplots(2,2,sharex=True, sharey=True)


data.plot(kind="scatter",x="Day Mins",y="Day Charge",ax=axs[0][0])
data.plot(kind="scatter",x="Night Mins",y="Night Charge",ax=axs[0][1])
data.plot(kind="scatter",x="Day Calls",y="Night Charge",ax=axs[1][0])
data.plot(kind="scatter",x="Night Calls",y="Night Charge",ax=axs[1][1])





