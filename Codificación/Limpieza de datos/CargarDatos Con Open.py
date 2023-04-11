# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:52:06 2021

@author: ANGELO
"""
#Cargar datos a través de la función de open,
# esto te lee linea a linea 
mainpath="G:/Data Science/Codificación/python-ml-course-master/datasets"

#"r" significa que va solo es a leer 
"""
Hay que tener cuidado al abrir un fichero en 
modo "w" (escritura) ya que esto hará que dicho fichero pierda su
 contenido (en caso de tenerlo y querer conservarlo). Si por
 algún motivo se quiere agregar contenido a este es recomendable 
 abrirlo en modo "a" (append), lo cual posicionará el cursor al 
 final y no borrará el contenido del mismo.
"""
import pandas as pd 

data = open(mainpath
            +"/"+"customer-churn-model/Customer Churn Model.txt","r")
#strip elimina espacios en blanco al inicio o al final de la linea

columns =data.readline().strip().split(",")
n_columns =len(columns)
print(columns)

counter =0 
main_dict ={}
for col in columns:
    main_dict[col]=[]
# recorre las lineas del dataset
for line in data:
    #esto separa las lineas por coma
    values= line.strip().split(",")
    #esto lo que hace es añadir a su diccionario a su respectiva columna 
    
    for i in range (len(columns)):
        main_dict[columns[i]].append(values[i])
    #esto solo es para saber cuantas filas tiene y presentar 
    counter +=1
print("El data set tiene %d filas y %d columnas" % (counter,n_columns))


# eso hace cambiar la separación en nuestro es una coma le ponemos un tabulador
# "/t"
#lectura y escritura  de ficheros

infile =mainpath+"/"+"customer-churn-model/Customer Churn Model.txt"
outfile =mainpath+"/"+"customer-churn-model/Tab Customer Churn Model.txt"
with  open(infile,"r") as infile1:
    with  open(outfile,"w") as outfile1:
        for line in infile1:
            fileds=line.strip().split(",")# es la división
            #join hace la funcion de unir 
            outfile1.write("/t".join(fileds))#
            outfile1.write("\n")#salto de linea
            
dt4 = pd.read_csv(outfile,sep="/t")
dt4.head()

    
