# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 22:31:44 2021

@author: ANGELO
"""
import numpy as np
#histograma  
import matplotlib.pyplot as plt
#https://www.udemy.com/course/machinelearningpython/learn/lecture/9725328#content
#Haremos un ejemplo de un circulo 
# la probabilidad de caer en un circulo
#generamos dos  números aleatorios x e y entre 0 y 1 en total 1000 veces.
#Calculamos x^x +y^y
#Si el valor es inferior a 1 -> estamos dentro del círculo
#si el valor es superior a 1 ->estamos fuera del círculo 
#Calculamos el numero total de veces que están dentro del círculo y lo dividimos 
#entre el número total de intentos para obtener una aproximación de la probabilidad de caer dentro del circulo
#Usamos dicha probabilidad para aproximar el valor de π
#Repetimos el experimento un número suficiente de veces(por ejemplo 100), para obtener (100) diferentes aproximacions de π.
#Calculamos el promedio de los 100º experimientos anteriores para dar un valor final de π
#4 casos posibles probabilidad
pi_avg=0
n=1000# experimiento 1000 que esten fuera y dentro del circulo puntos
n_experiment=100#y repito ese experimento 100
pi_value_list=[]
for i in range(n_experiment):
    value=0#
    x=np.random.uniform(0,1,n).tolist()#numero aleatorio entre o y 1 y el valor de n y lo convertimos a lista
    y=np.random.uniform(0,1,n).tolist()#numero aleatorio entre o y 1 y el valor de n y lo convertimos a lista
    for j in range(n):#aplicamos la formula que nos dan para aplicar la simulacionde monte de carlo
        z=np.sqrt( x[j]* x[j] + y[j] * y[j]) # sqrt es raiz cuadrada 
        if z<=1:
            value +=1
    float_value=float(value)
    pi_value=float_value*4/n
    pi_value_list.append(pi_value)
    pi_avg+=pi_value
pi=pi_avg/n_experiment
print(pi)
plt.plot(pi_value_list)


def pi_montecarlo(n,n_experiment):
    pi_avg=0
    
    pi_value_list=[]
    for i in range(n_experiment):
        value=0#
        x=np.random.uniform(0,1,n).tolist()#numero aleatorio entre o y 1 y el valor de n y lo convertimos a lista
        y=np.random.uniform(0,1,n).tolist()#numero aleatorio entre o y 1 y el valor de n y lo convertimos a lista
        for j in range(n):#aplicamos la formula que nos dan para aplicar la simulacionde monte de carlo
            z=np.sqrt( x[j]* x[j] + y[j] * y[j]) # sqrt es raiz cuadrada 
            if z<=1:
                value +=1
        float_value=float(value)
        pi_value=float_value*4/n
        pi_value_list.append(pi_value)
        pi_avg+=pi_value
    pi=pi_avg/n_experiment
    fig=plt.plot(pi_value_list)
    return (pi,fig)
