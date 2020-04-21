import os
def Crear_carpetaEEG():
        global carpetaEEG 
        global j
        global fila
        fila = 0
        Archivo = True
        j = 1
        Tipo = "Prueba"
        carpetaEEG = f"Base_Datos_{Tipo}" #Creacion de carpetas para guarda archivos si no existe
        if not os.path.exists(carpetaEEG):
            os.makedirs("pruena/" + carpetaEEG)
Crear_carpetaEEG()