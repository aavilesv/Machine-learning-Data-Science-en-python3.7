# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:41:59 2021

@author: ANGELO
"""
import pandas as pd 
 
mainpath="G:/Data Science/Codificación/python-ml-course-master/datasets"
filename ="titanic/titanic3.xls"
filename1 ="titanic/titanic3.xlsx"
titanic2 = pd.read_excel(mainpath+"/"+filename,"titanic3")

titanic3 = pd.read_excel(mainpath+"/"+filename1,"titanic3")

#csv crear los datos que he modelado 
# esto permite crear un dataframe 
#esto convierto en archivo  

titanic3.to_csv(mainpath+"/titanic/titanic_customM.csv")
titanic3.to_excel(mainpath+"/titanic/titanic_customM.xls")
titanic3.to_json(mainpath+"/titanic/titanic_customM.json")