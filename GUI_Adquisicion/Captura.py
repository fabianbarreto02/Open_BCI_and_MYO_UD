# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui_bases.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
#########################################################

import sys
sys.path.append('C:/Python37/Lib/site-packages')
from IPython.display import clear_output
from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
from PyQt5 import QtWidgets
import pyqtgraph as pg
import random
from pyOpenBCI import OpenBCICyton
import threading
import time
import numpy as np
from scipy import signal


##########################################################
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, GraphicsLayoutWidget
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')
data = [[0,0,0,0,0,0,0,0]]
SCALE_FACTOR = (4500000)/24/(2**23-1) #From the pyOpenBCI repo
colors = 'rgbycmwr'

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 699)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(180, 10, 931, 651))
        self.graphicsView.setObjectName("graphicsView")
        self.ts_plots = [self.graphicsView.addPlot(row=i, col=0, colspan=2, title='Channel %d' % i, labels={'left': 'uV'}) for i in range(1,9)]

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 500, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 390, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 60, 141, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 250, 111, 61))
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 140, 61, 41))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 140, 71, 41))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "SALIR"))
        self.pushButton_2.setText(_translate("MainWindow", "INICIO"))
        self.pushButton_3.setText(_translate("MainWindow", "ACTUALIZAR"))
        self.label.setText(_translate("MainWindow", "SEGUNDOS."))
    ################################################################################
    def save_data(self,sample):
        global data
        data.append([i*SCALE_FACTOR for i in sample.channels_data])

    def updater(self):
        global data, plots, colors
        t_data = np.array(data[-1250:]).T #transpose data
        fs = 250 #Hz
        # Plot a time series of the raw data
        for j in range(8):
            self.ts_plots[j].clear()
            # self.ts_plots[j].plot(t_data[j])
            self.ts_plots[j].plot(pen=colors[j]).setData(t_data[j])

def start_board():                              # Hilo configuracion cyton y lectura de datos
    board = OpenBCICyton( "COM8",daisy=False)   # LLamado de la clase OpenBCYCyton.
    board.start_stream(ui.save_data)              # Se llama el metodo de solicitud de datos.
    

if __name__ == "__main__":
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'): ## verificar q python no se este corriendo en modo interactivo y tenga instalado pyqt5
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        x = threading.Thread(target=start_board)# crea Hilo asignando nombre start_board
        x.daemon = True                         # declara este hilo como demonio(finaliza cuando hilo principal finalice)
        x.start()                               # inicia Hilo
        timer = QtCore.QTimer()                 # timer digital del pyqt5
        timer.timeout.connect(ui.updater)          # actualizacion grapica
        timer.start(0)                          # pendiente...
        sys.exit(app.exec_())
