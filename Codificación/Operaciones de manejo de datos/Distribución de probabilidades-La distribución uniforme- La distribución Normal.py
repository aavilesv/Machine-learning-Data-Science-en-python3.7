# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:00:31 2021

@author: ANGELO
"""

#Distribución uniforme punto de origen y punto final
# para generar numeros aleatorios una probabilidad constante

import numpy as np
#histograma  
import matplotlib.pyplot as plt
#la formula de distribucion uniforme 1/(b-a)
#a debe ser siempre menor que b 
a=1
b=100
n=2000000#muestras deben ser altas en volumen para poder ver el concepto de uniforme 
data = np.random.uniform(a,b,n)

#tengo que ocultar esta linea para que se pueda ver la grafica 

#%matplotlib inline
#plt.hist(data)


#Distribución normal= la media valor central y la desviación tipica o estandar   
#randm es distrubicion normal
data1=np.random.randn(1000)#cuantos valores aleatorio quiero generar  en mi caso 100 
x=range(1,1001)#siempre pon en randn(1000) lo mismo que en el range 
print(x)
#%matplotlib inline
#plt.plot(x,data1)#x=x , y=data1

#%matplotlib inline
#plt.hist(data1)

#%matplotlib inline
#plt.plot(x,sorted(data1))
#Esto es si quieres ingresar tus propios datos si generar los aleatorios
media=5.5
sddesviicionestandar=2.5 # arriba y abajo
zdistrubicionnormal=np.random.randn(10000)
data2=media+sddesviicionestandar*zdistrubicionnormal #Z=(X-media)/sddesviicionestandar->N(0,1), X=media+sddesvicionestandar*zdistrubicionnormal

%matplotlib inline
plt.hist(data2)

data2=np.random.randn(2,4)
print(data2)



