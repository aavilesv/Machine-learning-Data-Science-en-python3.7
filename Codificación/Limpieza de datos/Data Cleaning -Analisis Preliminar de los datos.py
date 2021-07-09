# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 19:29:25 2021

@author: ANGELO
"""

#Resumen de los datos, dimensiones y estrcuturas 
import pandas as pd
import os
mainpath="G:/Data Science/Codificación/python-ml-course-master/datasets"
filename ="titanic/titanic3.csv"
fullpath =os.path.join(mainpath,filename)
urldata ="https://raw.githubusercontent.com/joanby/python-ml-course/master/datasets/titanic/titanic3.csv"
data = pd.read_csv(urldata)
data.head(10)
#solo nos traera las primeras 15 filas 
respon=data.iloc[0:15]
# esto nos dice la cantidad de datos que queremos por ejemplo 
#de 0:15 serían las filas sería 0:2  en este caso le digo que solo quiero esas columnas la primera y la segunda 

responde = data.iloc[0:15,0:2]
#esto data,info ayuda y muestra los tipos de datos que estan como 
# int, object,float64, etc.
print(data.info())

#trae el conteo de filas y columnas que estan llenos 
ver=data.shape
#tail() nos presenta los 5 ultimos de la lista si no le pones nada pero en 
#nuestro cosa le ponemos los 10 ultimos de la lista 
ultimo = data.tail(10)

#trae el nombre de las columnas
print(data.columns.values)
#Vamos hacer un resumen de los estadiscticos basicos de #las variables numericas dentro de la data set las columnas #te analiza todas las columnas numericas y te da la media desviación estandar
#min y max en porcentaje en nuestro caso muertos, edad, sobreviviente 
#describir
objecto=data.describe()
print(data.describe())
#nos dice de que tiene son las columnas
#es lo mismo que info()
print(data.dtypes)
#se comprueba si todos los valores de una columna
isnulls = pd.isnull(data["body"])
# y diferente a null 
notnulls = pd.notnull(data["body"])
#solo si tienen valores suman con ravel() y nos dicen cuales 
# cuantos datos tenemos nulos 
ravel = pd.isnull(data["body"]).values.ravel().sum()
# los valores que faltan en un data set #pueden ser  por 2 razones # extracción de las datos #puede ser problemas de compactibilidad 
#Recolección de los datos 
#en algunos casos no dejan introducir los valores en # la base de datos # como por ejemplo datos sensibles #que los usuarios no suelen contestar o guardarlos 
#Borrar los valores que faltan o en blanco
#si axis es igual a 1 borra las columnas y si es 0 elimina las filas 

#how nos dice que fila debe de borrar debes
#pueden ser todas "all", 
#"any" esto dice que al menos una fila # tiene un valor en blanco no lo tomará 
#
data.dropna(axis=0, how="all")

# Computo de los valores faltantes 
data3=data
#añade o reemplazar por otro valores cuando este en blanco 
#fillna añade el valor de cualquier tipo # numerico o string  en el dataset con el cero en este caso 
data3.fillna(0)
#vamos a decir con que tipo de datos regeñando  las filas debes poner la columna asi como esta en el ejemplo
#debes volver a ponerle en la variable o inicializar la 
data5=data 
data5['body']=data5['body'].fillna(0)
data5['home.dest']=data5['home.dest'].fillna('Desconocido')
data5['age']=data5['age'].fillna(data5['age'].mean())
tengo=data5
#este función pone un valor a la columna vacia pero
#el valor que esta antes con ffill en nuestro caso ya tenemos llena la función con data5['age']=data5['age'].fillna(data5['age'].mean())

ffill=data5['age'].fillna(method="ffill")



#este función pone un valor a la columna vacia pero
#el valor que esta despues  con backfill en nuestro caso ya tenemos llena la función con data5['age']=data5['age'].fillna(data5['age'].mean())

backfill=data5['age'].fillna(method="backfill")

#Variables dummy convertir esa categoria en unaa colmna 
#sex es una columna que tiene female y male(masculino)
print(data['sex'])
#esto nos trae un cero y uno en vez de female y male y 
#nos sera en 2 columnas como sex_famele sex_male 
# y te trae valores de 1 y 0 
dummy_sex=pd.get_dummies(data['sex'],prefix='sex')
#presentar los nombres de la columna 
column_name=data.columns.values.tolist()
#Eliminar una column con drop (1) es columna 
eliminar =data.drop(['sex'],axis=1)
# para concatener datos  a la columna
concatener=pd.concat([data,dummy_sex],axis=1)
#recorrar todo hacer por función
def createdummies(df, var_name):
    dummy=pd.get_dummies(df[var_name],prefix=var_name)
    df =data.drop(var_name,axis=1)
    df=pd.concat([df,dummy],axis=1)
    return df
devuelver=createdummies(data,'sex')