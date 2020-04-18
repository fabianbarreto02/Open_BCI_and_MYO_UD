import sys
sys.path.append('C:/Python37/Lib/site-packages')
from IPython.display import clear_output
from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QMessageBox
from PyQt5.QtGui import QMovie
import pyqtgraph as pg
import random
from pyOpenBCI import OpenBCICyton
import threading
import time
import numpy as np
from scipy import signal
from pyqtgraph import PlotWidget

# Librerias Myo
import myo
from collections import deque
from threading import Lock, Thread

##########################################################
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, GraphicsLayoutWidget
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')
data = [[0,0,0,0,0,0,0,0]]
SCALE_FACTOR = (4500000)/24/(2**23-1) #From the pyOpenBCI repo
colors = 'rgbycmwr'
i = 0
s = 0
m = 0
t = 0


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1339, 721)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Plot primeros 8 canales EEG
        self.graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(180, 10, 371, 651))
        self.graphicsView.setObjectName("graphicsView")
        self.ts_plots = [self.graphicsView.addPlot(row=i, col=0, colspan=2, title='Channel %d' % i, labels={'left': 'uV'}) for i in range(1,9)]

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 630, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.close_application)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 530, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.inittimer)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 60, 141, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 230, 111, 61))
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(4)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.display("0:00")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 140, 81, 41))
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 140, 71, 31))
        self.textEdit.setObjectName("textEdit")

        self.graphicsView_2 = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(570, 10, 371, 651))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.ts_plots_2 = [self.graphicsView_2.addPlot(row=i, col=0, colspan=2, title='Channel %d' % i, labels={'left': 'uV'}) for i in range(9,17)]

        self.graphicsView_3 = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(950, 10, 371, 651))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.ts_plots_emg = [self.graphicsView_3.addPlot(row=i, col=0, colspan=2, title='Channel %d' % i, labels={'left': 'mV'}) for i in range(1,9)]


        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 580, 131, 41))
        self.pushButton_4.setObjectName("pushButton_4")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 660, 101, 41))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(690, 660, 101, 41))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1080, 660, 101, 41))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 360, 131, 151))
        self.label_5.setObjectName("label_5")
        self.movie = QMovie('manos.gif')
        self.label_5.setMovie(self.movie)
        self.movie.start()

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 290, 81, 41))
        self.label_6.setObjectName("label_6")

        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Primer Gesto"))
        self.pushButton.setText(_translate("MainWindow", "SALIR"))
        self.pushButton_2.setText(_translate("MainWindow", "INICIO"))
        self.pushButton_3.setText(_translate("MainWindow", "ACTUALIZAR"))
        self.label.setText(_translate("MainWindow", "SEGUNDOS"))
        self.pushButton_4.setText(_translate("MainWindow", "SIGUIENTE"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">EEG 8 Canales</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">EEG 8 Canales</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">EMG 8 Canales</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Timer</span></p></body></html>"))
##############################################################################################################################
    def save_data_EEG(self, sample):
        global data
        data.append([i*SCALE_FACTOR for i in sample.channels_data])
    
    def updater_EEG(self):
        global data, plots, colors
        t_data = np.array(data[-1250:]).T #transpose data
        # Plot a time series EEG of the raw data
        for j in range(8):
            self.ts_plots[j].clear()
            # self.ts_plots[j].plot(t_data[j])
            self.ts_plots[j].plot(pen=colors[j]).setData(t_data[j])
    
    # Metodo Arranque MYO
    def conexionMYO(self):
        print("Realizando Conexión MYO")
        myo.init()
        self.hub = myo.Hub()
        self.listener = EmgCollector(512)
        self.stopconexion = False
        self.stopsaved = False
        print("Conexión MYO Establecida")
        #self.Crear_carpetaMYO()
    
    def updater_EMG(self):
        global colors
        emg_data = self.listener.get_emg_data()
        #emg_data = np.array([x[1] for x in emg_data]).T
        emg_data = np.array([2 , 3 , 4 , 5 ,6 ,7,8,9], dtype=np.int64)
        #print(emg_data)
        for j in range(8):
            #print(emg_data[j])
            self.ts_plots_emg[j].clear()
        #     # self.ts_plots[j].plot(t_data[j])
            #self.ts_plots_emg[j].plot(pen=colors[j]).setData(emg_data[j])
    
    def close_application(self):
        sys.exit()

    def inittimer(self):
        print(self.textEdit.toPlainText())
        if not self.textEdit.toPlainText():
            print("El QLineEdit esta vacio")
            msg = QMessageBox()
            msg.setWindowTitle("Control")
            msg.setText("Atención!")
            msg.setIcon(QMessageBox.Warning)
            msg.setInformativeText("Por favor ingrese los segundos!")
            msg.exec()
        else:
            def hiloRunTimmer(arg):
                hiloRunTimmer = threading.currentThread()
                while getattr(hiloRunTimmer, "do_run", True):
                        print("working on %s" % arg)
                        self.OnTimer(None, e=self.textEdit.toPlainText())
                print("Stopping as you wish.")
            self.hiloRunTimmer = threading.Thread(target=hiloRunTimmer,args=("RUN_Timmer",))
            self.hiloRunTimmer.setDaemon(True)
            self.hiloRunTimmer.start()

    
    def OnTimer(self, event, e):
        global i
        global c
        c = e
        if(i < int(c)):
            i += 1   
            time.sleep(1)
            self.TimerGo(None)
            
            
        else:
            print("Termino Timer")
            # self.board.stop_stream()
            # self.stopconexioUltracortex = True
            # self.hiloUltracortesConexion.do_run = False
            # self.hiloUltracortesConexion.join()
            self.hiloRunTimmer.do_run = False
            # self.stopsaved= True
            # self.hiloMYOSaved.do_run = False
            # self.hiloMYOSaved.join()
    
    def TimerGo(self, event):
        global s
        global m
        global t
        global c
        s = int(s)
        m = int(m)
        if(s < 59):
            s += 1
        elif(s == 59):
            s = 0
            if(m < 59):
                m += 1
            elif(m == 59):
                m = 0
        if (int(s) < 10):
            s = str(0) + str(s)
        if(int(s) > 9):
            s = str(s)
        t = str(m) + ":" + str(s)
        self.lcdNumber.display(t)
        self.OnTimer(None, c)
        



# Metodo Arranque Ultracortex
def start_board_Ultracortex():
    board = OpenBCICyton( "COM8", daisy= False)
    board.start_stream(ui.save_data_EEG)




# Clase para conexion Myo
class EmgCollector(myo.DeviceListener):
  """
  Collects EMG data in a queue with *n* maximum number of elements.
  """

  def __init__(self, n):
    self.n = n
    self.lock = Lock()
    self.emg_data_queue = deque(maxlen=n)

  def get_emg_data(self):
    with self.lock:
      return list(self.emg_data_queue)

  # myo.DeviceListener

  def on_connected(self, event):
    event.device.stream_emg(True)

  def on_emg(self, event):
    with self.lock:
      self.emg_data_queue.append((event.timestamp, event.emg))






if __name__ == "__main__":
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'): ## verificar q python no se este corriendo en modo interactivo y tenga instalado pyqt5
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        ui.conexionMYO()
        hilo_conexion_ultracortes = threading.Thread(target=start_board_Ultracortex) 
        hilo_conexion_ultracortes.daemon = True
        #hilo_conexion_ultracortes.start()
        timerEEG = QtCore.QTimer()
        timerEEG.timeout.connect(ui.updater_EEG)
        timerEEG.start(0)
        timerEMG = QtCore.QTimer()
        timerEMG.timeout.connect(ui.updater_EMG)
        timerEMG.start(0)
        sys.exit(app.exec_())
