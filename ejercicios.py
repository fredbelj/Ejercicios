import os

#BORRAR LA CONSOLA
#borrar = lambda: os.system('cls')
#borrar()

# from io import open
# # print('prueba')

# class Cliente:
#   def __init__(self):
#     self.__archivo = open(r"clientes.txt", "w", encoding="utf8")
#     self.__registros = self.__archivo.readlines()
    
#   def leer (self):
#     print("id nombre apellido telefono correo")
#     clientes = []
#     for registro in self.__registros:
#       #Se borran los saltos de línea y las comas del archivo
#       campo =registro.replace("\n", "").split(",")
#       cliente = {"id":campo [0], "nombre":campo [1], "apellido":campo [2], "telefono":campo[3], "correo":campo [4]}
#       clientes.append(cliente)
#     self.__archivo.close()
#     self.__imprimir(clientes)
#   def __imprimir(self, clientes):
#     for c in clientes:
#       print("{} {} {} {} {}".format(c['id'], c['nombre'], c['apellido'], c['telefono'], c['correo']))
# cliente = Cliente()
# cliente.leer

####################NUMPY############################
import numpy as np
arreglo = np.array([1,2,3,4])
print(type(arreglo))
print("esto es una prueba")
arreglo =np.array ([1, 2, 3, 4])
print(arreglo)


##################Pandas###########################
import pandas as pd
datos = {"a": [1, 2, 3, 4], "b": [1, 4, 9, 16]}
df1 = pd.DataFrame (data =datos)

print(df1)

df2 = pd.DataFrame(data = [[1, 2], [2, 4], [3, 9], [4,16]], columns = ["a", "b"])
print(df2)

datos = [{"a": 1, "b": 2},
{"a": 2, "b": 4},
{"a": 3, "b": 9},
{"a": 4, "b": 16}]
df3 = pd.DataFrame(data = datos)
print(df3)



##################