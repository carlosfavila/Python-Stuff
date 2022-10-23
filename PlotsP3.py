# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 17:26:15 2022

@author: CarlosFavila
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#importa el dataframe de Excel
datos = pd.read_excel('D:\\CARLOS\\UPIITA\\SEXTO SEMESTRE\\Máquinas Eléctricas\\Prácticas\\Práctica 3\\P3 transformador.xlsx', header = None) #Dirección delarchivo de excel usando doble \\

#Elimina las ultimas columas del excel debido a que se anexan unas por la fila  J 
data = datos.drop([0,50,51,52,53,54,55,56,57],axis=0)

fp = data[0].tolist()   # Frecuencia del generador de funciones al primario del Transformador
vspico = data[1].tolist() #Voltaje Pico-Pico del secundario del Transformador
fs = data[2].tolist()   # Frecuencia del Secundario del Transformador
a = data[3].tolist()    # Relación entre el voltaje del primario entre el voltaje del secundario
w = data[4].tolist()    # Velocidad angular de la frecuencia
tf = data[5].tolist()   # Funcion de Transferencia
dB=20*np.log(np.abs(tf))

plt.figure()
plt.semilogx(fp,tf)
plt.xlabel("Frecuencia Hz")
plt.ylabel("Funcion de Transferencia")
plt.title("Función de Transferencia")
plt.grid(True)

plt.figure()
plt.semilogx(w,dB)
plt.xlabel(r"$w - (\frac{rad}{s}$)")
plt.ylabel("Magnitud (dB)")
plt.title(r"Diagrama de Bode. Magnitud en dB= $20log|FT|$")
plt.grid(True)


plt.figure()
plt.semilogx(fp,a)
plt.xlabel("Frecuencia Hz")
plt.ylabel(r"a=$\frac{V_p}{V_s}$")
plt.title("Relación de Transformación")
plt.grid(True)