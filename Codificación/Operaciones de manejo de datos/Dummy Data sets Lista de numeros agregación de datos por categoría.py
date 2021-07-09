# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 21:32:27 2021

@author: ANGELO
"""
#Agrupación de datos
#dataset o datafraem
import pandas as pd
#estadistica
import numpy as np
import matplotlib.pyplot as plt
gender=['Male','Female']
nivelingresos=['Bajo','Clase Media','Rica']
n=500# nos crea 500 datos aleatorios 
gender_data=[]
nivelingresos_data=[]

for i in range(0,500):
    gender_data.append(np.random.choice(gender))# choice nos crea 500 datos aleatorios 
    nivelingresos_data.append(np.random.choice(nivelingresos))# choice nos crea 500 datos aleatorios 
#print(gender_data)
media=160
sddesviicionestandar=30
altura= media +sddesviicionestandar * np.random.randn(n)#con formula cuantos valores aleatorio quiero generar  en mi caso 10 distrubucion normal
peso =65+25 * np.random.randn(n)#con formula cuantos valores aleatorio quiero generar  en mi caso 10 distrubucion normal
edad=30+12* np.random.randn(n)#con formula cuantos valores aleatorio quiero generar  en mi caso 10 distrubucion normal
nivelingresoss=1800+3500* np.random.randn(n)#con formula cuantos valores aleatorio quiero generar  en mi caso 10 distrubucion normal

data=pd.DataFrame({#DataFrame nos permite crear el diccionario a dataframe dataset 
    "Gender":gender_data,
    "Estado Economico":nivelingresos_data,
    "Altura":altura,
    "Peso":peso,
    "Edad":edad,
    "NivelIngreso":nivelingresoss
    })
#Agrupar Datos 

grupos_gender=data.groupby("Gender")# esto te agrupo los generos pero te trae en valor numero su posicion en el dataframe
#por ejemplo te trae los valores en forma de objeto
grupos_genderr=grupos_gender.groups#esto te trae los valores te los valores en forma de diccionario
#solo presenta
#esto es para cuando solo un grupo
for nombre,grupos in grupos_gender:
    print(nombre)# no puedo imprimir unido
    print(grupos)
print(grupos_gender.groups)

#doble agrupacion
doble_agrupacion=data.groupby(["Gender","Estado Economico"])#te ayuda agrupar los datos de la mejor manera
doble=len(doble_agrupacion)
for nombre,grupos in doble_agrupacion:
    print(grupos)
    print(nombre)

#Operaciones sobre datos agrupados 
print(doble_agrupacion.sum())#suma lo valores agrupados
print(doble_agrupacion.mean())#suma el promedio lo valores agrupados
print(doble_agrupacion.size())#dice el tamaño de cada elemento
print(doble_agrupacion.describe())# esto te describe todo media, promedio, sd desvision estandar


#Agrega agrupa los datos
doble_agrupacion.aggregate(
    {"NivelIngreso" : np.mean,
     "Edad":np.mean,
     "Altura":np.std
    })
doble_agrupacion.aggregate([lambda x: np.mean(x)/np.std(x)])#lambda crea una funcion esto directamente 
#te lleva cuando lleva np hay si te le pones parametro x

doble_agrupacion.aggregate(
    {
     "Edad":np.mean,
         "Altura": lambda a: (np.mean(a))/np.std(a)# se pasa por parametro la a 
    })
print(doble_agrupacion.aggregate([np.sum,np.mean,np.std]))#este valor se va directamente a los valores principales 
#como 
'''
 "Gender":gender_data,
    "Estado Economico":nivelingresos_data,
    "Altura":altura,
    "Peso":peso,
    "Edad":edad,
    "NivelIngreso":nivelingresoss
    '''

#Filtrados de datos

print(doble_agrupacion.sum())
filterr=doble_agrupacion['Edad'].filter(lambda x: x.sum()>2400) #en la columnaa de edad menor a 2400
#devuelve los elementos de la columna
#Transformación de variables
zsore =lambda  x: (x- x.mean())/x.std() #como es funcion le puedes poner mean y std a cualquier valor
#esta x representa a todas las columnas  que tenemos en doble_agrupacion va filaa por fila
transfor=doble_agrupacion.transform(zsore)#transform con lambda cambias los datos 

plt.hist(transfor["Edad"])
# Reemplazar datos

fill_namean= lambda x : x.fillna(x.mean)# esto reemplaza la fila y columnas que este vacia 
print(doble_agrupacion.transform(fill_namean))


# Operaciones diversas muy útiles
print(doble_agrupacion.tail(1))# devuelve todo de abajo hacia arriba


#cogemos el data frame original
data_ordenar =data.sort_values(["Altura","NivelIngreso"])# te ordena los valores las columnas en este

edad_grupo=data_ordenar.groupby("Gender")# esto te agrupo los generos pero te trae en valor numero su posicion en el dataframe
#por ejemplo te trae los valores en forma de objeto
print(edad_grupo.head(1))




