# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 00:00:58 2025

@author: fredb
"""
#
import numpy as np
import matplotlib.pyplot as plt

ventas = np.random.randint(100, size=[6])
meses = [' Enero',' Febrero',' Marzo',' Abril',' Mayo','Junio']
mapeado = range(len(meses))

plt.plot(ventas)                            #Añadimos el gráfico
plt.xticks(mapeado,meses)                   #Mapeamos los valores horizontales
plt.ylim(0, 100)                            #Configuramos el límite verticles
plt.xlim (0, 6)                             #Configuramos el límite horizontal
plt.title("Ventas del primer semestre")     #Configuramos el título
plt.xlabel("Meses")                         #Configuramos la etiqueta del eje X
plt.ylabel("Cantidad en $")                 #Configuramos la etiqueta del eje Y
plt.show()     


numeros=np.random.normal(size = 1200)
plt.hist(numeros, bins = 10, edgecolor='black')
plt.title("Histograma Gaussiano")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()                             #Finalmente lo mostramos