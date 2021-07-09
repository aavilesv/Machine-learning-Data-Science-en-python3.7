# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:28:11 2021

@author: ANGELO
"""
#Los numeros aleatorios permite llevar a cabo simulaciones de modelo
#probabilisticos multicasos, rango posible sobre variantes 
#generar dummy con valores basura y hace un muestreo 
import numpy as np
import pandas as pd 
#Generar un numero aleatorio entero entre 1 y 100
data = pd.read_csv("G:/Data Science/Codificación/python-ml-course-master/datasets/customer-churn-model/Customer Churn Model.txt")

aleatorioentero=np.random.randint(1,100)
#la forma mas clasica para generar el numero aleatorio 

randomm=np.random.random()

#Función que genera una lista de n números aleatorios 
#enteros dentro del intervalo [a,c]

def randint_list(n,a,b):
    x=[]
    for i in range(n):
        x.append(np.random.randint(a,b))
    return x

presenta=randint_list(25, 1, 50)
#esta función te ayuda 
#(0,100,7)  esto te dice que tienes que empezar de 0  le pones 100 que sería 
#lo maximo el 7 sería multiplo de 7 te presentará 
#•pero si le poner (1,100,7) el uno le suma por ejemplo se imprime el 7 mas 1 seria 8
import random
randrangee= random.randrange(0,100,7)


#arange(100) es arreglo y range mezclado del rango 0-99
arangee=np.arange(100)

#esto le cambia todo el orden desordena
print(np.random.shuffle(arangee))


#columnas nombres para elegir una 
columna_list=data.columns.values.tolist()
#ahora cogeremos un valor alazar 
#esto nos trae un valor
alazar=np.random.choice(columna_list)

#esto es una semilla para obtener los mismos resultados seed
np.random.seed(2018)
for i in range(5):
    print(np.random.random())
