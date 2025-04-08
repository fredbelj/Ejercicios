# Ejercicio Pandas

import pandas as pd
import os
clear = lambda: os.system('clear')
clear()
archivo_data = pd.read_csv("../../IA_ETB/Titanic-Dataset.csv")
print(archivo_data)
print(archivo_data.head(2))
