# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Carga de datos a través de la función read_csv
import pandas as pd 
import os
#import  pandas as np
#esta forma es relativa

mainpath="G:/Data Science/Codificación/python-ml-course-master/datasets"
filename ="titanic/titanic3.csv"
fullpath =os.path.join(mainpath,filename)


#dataframe = pd.read_csv(
#  filepath_or_buffer= fullpath,
#    sep=",")
#dataframe.head()
data2  = pd.read_csv(mainpath+"/"+"customer-churn-model/Customer Churn Model.txt")
data2.head()
# esto ve los nombres de las columnas 
data2.columns.values
print(data2.columns.values)

#cambiar los nombres de las columnas 

data_colmns =pd.read_csv(
    mainpath+"/"+"customer-churn-model/Customer Churn Columns.csv")
#convertir en una lista
data_col_list =data_colmns["Column_Names"].tolist()
print(data_col_list)
data2 =pd.read_csv(
    mainpath+"/"+"customer-churn-model/Customer Churn Model.txt",header=None,
    names=data_col_list)
print(data2.columns.values)

