# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:18:37 2021

@author: ANGELO
"""
 #Leer datos desde una url externa 
#primero importamos la librería y hacemos la conexión con la web de los datos


import pandas as pd 
import urllib3 # se utiliza para navegar y obtener información 
import os


medals_url='http://winterolympicsmedals.com/medals.csv'



http = urllib3.PoolManager()

r = http.request('GET', medals_url)
r.status
print("El estado de la respuesta es"+str( r.status))
responde = r.data

#El objeto reponse contiene un string binario aasí que convertimos
#a un string descodificado en UTF-() descodificación estandar se pu
#se puede el utf-8 por otra buscar si fuera el caso
str_data=responde.decode('utf-8')

#Dividimos el string en array de filas
#, separadolo por intros array de String
lines =str_data.split("\n")
#la primera línea contiene la cabecera, así que extramos
#me quedo con el primer elemento y la separado por coma  
#y eso guardamos en una variable 
# luego saber cuantas columnas son 
col_names =lines[0].split(",")
#esta variable solo es para imprimir 
numero_colmuns =len(col_names)
#Generamos un diccionario vacio donde irá la información 
#url externa 
#esta variable counter es para ver la cantidad de filas 
counter=0
#aquí lo que hacemos es guardar esa información en un diccionario pero
# solo las columnas
main_dict ={}
for col in col_names:
    main_dict[col]=[]
# recorre las lineas del dataset

#procesamos fila a fila la información para ir rellenando el diccionario 
#con los datos como hicimos antes 
for line in lines:
    #nos saltamos la priemra linea que es la que contiene 
    #la cabecera y que tenemos procesada 
    if(counter>0):
        #esto separa las lineas por coma
        values= line.strip().split(",")
        #esto lo que hace es añadir a su diccionario a su respectiva columna 
        #Añadimos cada valor a su respectiva columna del diccionario
        for i in range (len(col_names)):
            main_dict[col_names[i]].append(values[i])
        #esto solo es para saber cuantas filas tiene y presentar 
    counter +=1

print("El data set tiene %d filas y %d columnas" % (counter,numero_colmuns))


#Convertimos el diccionario procesado a Data Frame y comprobamos que los datos
#son correctos 
medals_dframe = pd.DataFrame(main_dict)
medals_dframe.head()
mainpath ="G:\Data Science\Codificación"
filename ="Guardar archivos xls,xlsx,txt,json/descargarurlexterno."
fullpath =os.path.join(mainpath,filename)
#guardamos en, excel, json,csv los datos obtenidos por medio de una url 
medals_dframe.to_excel(fullpath+".xls")
medals_dframe.to_csv(fullpath+"csv")
medals_dframe.to_json(fullpath+"json")




