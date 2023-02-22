import os
from os import path
from random import seed
import random
from random import randint
import string
import re
# seed random number generator
seed(1)
# generate random numbers between 0-1
def generar_numero_random():
    for _ in range(10):
        value = randint(0,9)
        return value
    
def modificar_contenido_archivo(archivo):
    with open(archivo,'r') as x:
        nuevo_contenido = ""
        for linea in x:
            nueva_linea = ""
            for caracter in linea:
                if re.match(r"[a-zA-Z]",caracter):
                    nueva_linea = nueva_linea + str(generar_numero_random())
                elif re.match(r"[0-9]",caracter):
                    nueva_linea = nueva_linea + random.choice(string.ascii_letters).upper()
            nuevo_contenido = nuevo_contenido + nueva_linea + '\n'        
    return nuevo_contenido
    

#Ruta de la carpeta
ruta_original = "C:/Users/gamit/Desktop/Trabajos-Seminario-Operativos/archivos practica"
ruta_copia = "C:/Users/gamit/Desktop/Trabajos-Seminario-Operativos/copias"


def recorrer_carperta(ruta,ruta_copia):
    os.chdir(ruta)
    ruta_madre = os.getcwd()
    subruta = ruta.split("/")
    subruta = subruta[-1]
    ruta_copia_actual = ruta_copia + "/" + subruta
    for archivo in os.listdir():
        if os.path.isdir(archivo):
            recorrer_carperta(os.getcwd()+"/"+archivo, ruta_copia_actual )
            os.chdir(ruta_madre)         
        elif os.path.isfile(archivo):
            copia=modificar_contenido_archivo(archivo)
            ruta_archivo_actual = os.getcwd()
            os.chdir(ruta_copia_actual)
            
            with open(os.path.basename(archivo),"w") as archivo_copia:
                archivo_copia.write(copia)
            os.chdir(ruta_archivo_actual) 
    os.chdir(ruta_madre)

os.chdir(ruta_original)
recorrer_carperta(ruta_original,ruta_copia)

# for archivo in os.listdir():
#     if os.path.isdir(archivo):
#         carpeta_madre = os.getcwd()
#         subcarpeta = carpeta_madre + "/"+archivo
#         os.chdir(subcarpeta)
#         print(os.getcwd())
#         print(carpeta_madre)
#     else:
#         copia=modificar_contenido_archivo(archivo)
#         print(os.getcwd())
#         os.chdir(ruta_copia)
#         with open(os.path.basename(archivo),"w") as archivo_copia:
#             archivo_copia.write(copia)
#         os.chdir(ruta_original)
    
        

