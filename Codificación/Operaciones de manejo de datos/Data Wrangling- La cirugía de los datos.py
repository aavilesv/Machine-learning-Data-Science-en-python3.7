# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:00:49 2021

@author: ANGELO
"""

#Data Wrangling- La cirugía de los datos
#solo seleccionar ciertos datos o busquedad
import pandas as pd 
data = pd.read_csv("G:/Data Science/Codificación/python-ml-course-master/datasets/customer-churn-model/Customer Churn Model.txt")
#busquedad
respuesta=data.iloc[0:15]

#Crear un subconjunto de datos 
# esto ayuda a escoger solo los datos que utilices la columna 
#series o vectores son lo valores de la columna seleccionado 
account_length =data['Account Length']
print(type(account_length))

#traer mas 2 columnas 
subset = data[['Account Length','Phone','Eve Charge','Day Calls']]
datos=subset.iloc[0:15]
#creamos un arreglo esto hace lo mismo que el de arriba
desired_columns =['Account Length','Phone','Eve Charge','Day Calls']

subsett =data[desired_columns]
respuesta2=subsett.iloc[0:15]

#Presentar todas las columnas del dataset 
all_columns_List = data.columns.values.tolist()

#poner restrigción en las columnas que no quiero 
sublist =[x for x in all_columns_List if x not in desired_columns]

subconjuntoset= data[sublist]

soloundato=data["Day Mins"]
#usarios con Day mins > 500
data1=data[data["Day Mins"]>300]

#usuarios de nueva york (State =NY")
#donde State es la columna y "NY" es el valor que quiero que traiga 
data2 = data[data['State']=="NY"]

# Veremos como realizar and y or 
# and =& 
dataand=data[(data["Day Mins"]>300) &(data['State']=="NY")]

# or =& 
dataor=data[(data["Day Mins"]>300) | (data['State']=="NY")]
#Donde los datos dayminis superan al nigth calls 
#hacen una comparación
dayminisandnightcalls=data[(data["Day Mins"]>data["Night Calls"])]

#
columns =['State','Phone','Eve Charge','Day Calls','Day Mins']

#◙trae solo los valores hasta el numero 10 

primero10yciertacomluman=data[columns][:10]

#Busquedad o Buscar con iloc
#iloc es para cuando quiera por etiqueta
#iloc nos ayuda a asignar los indice de fila y columna la posicion 
iloc=data.iloc[0:10,3:6]#primeras 10 filas de la 3 a la 6  columnas

#los indices comienzan desde cero[0][0]
iloc1=data.iloc[[1,2,5],[1,6]]#primeras 10 filas de la 3 a la 6  columnas



#loc 
#['State','Phone','Day Mins','Account Length'] tiene que ponerle el nombre de las columnas
#cuando usas .loc
#se presenta 2 variables porque tienen un orden diferentes las columnas 
locc=data.loc[[0,1,2,3],['State','Phone','Day Mins','Account Length']]

locc1=data.loc[[0,1,2,3],['State','Account Length','Phone','Day Mins']]

#Agregar nuevos campos 
#como sumar un valor solo esta sumando datos
data['Total Mins']=data['Day Mins']+data['Eve Mins']+data['Intl Mins']+data['Night Mins']
totalmins=data


data['Total Calls']=data['Day Calls']+data['Eve Calls']+data['Night Calls']

totalcalls=data





