import csv
import os
import random
x = 5


j = 1
Archivo = True
Tipo = "Parpadeos"
datos = [0]*8
x = 0

def Guardar_Datos():
    for i in range(8):
        datos[i] = random.randint(0, 1000)  
    with open(os.path.join(carpeta, "datos %d.csv"% j), 'a') as fp: # Guardar datos en el archivo csv        
        [fp.write(str(datos[i])+";")for i in range(0,8)]
        fp.write("\n")
    return datos


carpeta = f"Base_Datos_{Tipo}" #Creacion de carpetas para guarda archivos si no existe
if not os.path.exists(carpeta):
    os.mkdir(carpeta)

while(Archivo == True):# Se crea un archivo csv en caso de que no exista
    if os.path.isfile(carpeta + "/datos %d.csv"% j):
        print('El archivo existe.')
        j+=1
    else:
        with open(os.path.join(carpeta, "datos %d.csv"% j), 'w') as fp:
            [fp.write('CH%d ;'%i)for i in range(1,9)]
            fp.write("\n")
            print("Archivo Creado")
            Archivo = False

while(True):
    numAle = Guardar_Datos()
    print(numAle)
    
