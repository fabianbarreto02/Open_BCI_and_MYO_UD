import sys
sys.path.append('C:/Python37/Lib/site-packages')
from IPython.display import clear_output
import csv
import os
import wx
#----MATPLOTLIB-----------------------
from wx.adv import Animation, AnimationCtrl
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.backends.backend_wx import _load_bitmap
from matplotlib.figure import Figure
#----PYQT5----------------------------
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import random

from pyOpenBCI import OpenBCICyton
import threading
import time
import numpy as np
from scipy import signal
from pyOpenBCI import OpenBCICyton
#---------------------------------Declaracion de variables------------------------------
t=0
fs=250                                # frecuencia de muestreo
fila= 0                               #Fila de el dato actual obtenido del OpenBCI
pg.setConfigOption('background','w')  # Fondo blanco
SCALE_FACTOR = (4500000)/24/(2**23-1) # Factor de escala de cada canal
colors = 'rgbycmwr'                   # Colores graficas
data = [[0,0,0,0,0,0,0,0]] #Vector a actualizar de los canales del OpenBCI
#----------------------------------DISEÑO DE FILTROS------------------------------------
#NOTCH A 60Hz
notch_freq_Hz = np.array([float(60)]) 
for freq_Hz in np.nditer(notch_freq_Hz):
    bp_stop_Hz = freq_Hz + 3.0 * np.array([-1, 1])
    n_b, n_a = signal.butter(3, bp_stop_Hz / (fs / 2.0), 'bandstop')
#PASABANDA DE 7-13Hz
bp_Hz = np.array([7, 13])
bp_b, bp_a = signal.butter(2, bp_Hz / (fs / 2.0), btype='bandpass')
# LLAMAR signal.lfilter(b,a,datos) para aplicar la funcion de transferencia del filtro a un arreglo

#-----------------------GUI-----------------------------------
app = QtGui.QApplication([])
win = pg.GraphicsWindow(title='Python OpenBCI GUI')
ts_plots = [win.addPlot(row=i, col=0, colspan=2, title='Channel %d' % i, labels={'left': 'uV'}) for i in range(1,9)]
#-----------------------MATPLOTLIB----------------------------

#------------------------DEFINICION DE FUNCIONES----------------------------------------------
def save_data(sample): # Funcion de callback
    global data
    global fila
    data.append([i*SCALE_FACTOR for i in sample.channels_data])
    Guardar_Datos(data)
    fila += 1
#---------------------------------------ALMACENAMIENTO Y GUARDADO-----------------------
def Crear_carpeta():# Creacion de carpeta para almacenar archivos
    global carpeta 
    global j
    Archivo = True
    j = 1
    Tipo = "Parpadeos"
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
def Guardar_Datos(datos):
    global fila
   
    with open(os.path.join(carpeta, "datos %d.csv"% j), 'a') as fp: # Guardar datos en el archivo csv        
        for i in range(0,8):
            fp.write(str(datos[fila][i])+";")
        fp.write("\n")
#--------------------------------------ACTUALIZACION DE GRAFICAS-------------------------        
def updater():
    global data, colors,n_a,n_b,bp_a,bp_b
    t_data = np.array(data[-1250:]).T #transpose data
    nf_data = [[],[],[],[],[],[],[],[]]
    bp_nf_data = [[],[],[],[],[],[],[],[]]
    for i in range(8):
        nf_data[i] = signal.lfilter(n_b,n_a, t_data[i])
        bp_nf_data[i]= signal.lfilter(bp_b,bp_a, nf_data[i])
    # Plot a time series of the raw data
    for j in range(8):
        ts_plots[j].clear()
        ts_plots[j].plot(pen=colors[j]).setData(t_data[j])
#----------------------------HILO STARTBOARD-------------------------------
def start_board():
    board = OpenBCICyton(port='COM8', daisy=False)
    
    board.start_stream(save_data)
#MAIN ----------------------------------------------------------------------------------
Crear_carpeta()
if __name__ == '__main__':
    
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        x = threading.Thread(target=start_board)
        x.daemon = True
        x.start()

        timer = QtCore.QTimer()
        timer.timeout.connect(updater)
        timer.start(0)
        

        QtGui.QApplication.instance().exec_()