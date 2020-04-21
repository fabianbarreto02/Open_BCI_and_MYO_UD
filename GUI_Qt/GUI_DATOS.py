# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_DATOS_PACIENTE.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5.QtWidgets import  QMessageBox

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Datos_Paciente(object):
    def setupUi(self, Datos_Paciente):
        Datos_Paciente.setObjectName("Datos_Paciente")
        Datos_Paciente.resize(881, 723)
        self.centralwidget = QtWidgets.QWidget(Datos_Paciente)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 0, 221, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 751, 71))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 180, 261, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(480, 180, 151, 31))
        self.textEdit.setStyleSheet("font: 14pt \".SF NS Text\";")
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 280, 131, 16))
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(480, 280, 151, 31))
        self.textEdit_2.setStyleSheet("font: 14pt \".SF NS Text\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 330, 161, 16))
        self.label_5.setObjectName("label_5")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(480, 330, 151, 31))
        self.textEdit_3.setStyleSheet("font: 14pt \".SF NS Text\";")
        self.textEdit_3.setObjectName("textEdit_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(480, 220, 151, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 230, 141, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 370, 371, 91))
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(480, 400, 151, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(100, 500, 361, 61))
        self.label_8.setObjectName("label_8")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(490, 510, 51, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.clicked.connect(self.crear_paciente)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(550, 510, 51, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(520, 630, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 630, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close_application)
        Datos_Paciente.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Datos_Paciente)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 881, 22))
        self.menubar.setObjectName("menubar")
        Datos_Paciente.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Datos_Paciente)
        self.statusbar.setObjectName("statusbar")
        Datos_Paciente.setStatusBar(self.statusbar)

        self.retranslateUi(Datos_Paciente)
        QtCore.QMetaObject.connectSlotsByName(Datos_Paciente)

    def retranslateUi(self, Datos_Paciente):
        _translate = QtCore.QCoreApplication.translate
        Datos_Paciente.setWindowTitle(_translate("Datos_Paciente", "MainWindow"))
        self.label.setText(_translate("Datos_Paciente", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Datos del Paciente</span></p></body></html>"))
        self.label_2.setText(_translate("Datos_Paciente", "<html><head/><body><p align=\"justify\"><span style=\" font-size:18pt;\">Acontinuación debe ingresar una información básica que es relevanta para el estudio de las</span></p><p align=\"justify\"><span style=\" font-size:18pt;\">señales, por favor ingrese la siguiente informacion:</span></p></body></html>"))
        self.label_3.setText(_translate("Datos_Paciente", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Numero de identificación del estudio:</span></p></body></html>"))
        self.label_4.setText(_translate("Datos_Paciente", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Edad del paciente:</span></p></body></html>"))
        self.label_5.setText(_translate("Datos_Paciente", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Peso (Kg) del paciente:</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Datos_Paciente", "Femenino"))
        self.comboBox.setItemText(1, _translate("Datos_Paciente", "Masculino"))
        self.comboBox.setItemText(2, _translate("Datos_Paciente", "Prefiero no decir"))
        self.label_6.setText(_translate("Datos_Paciente", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Genero del paciente:</span></p></body></html>"))
        self.label_7.setText(_translate("Datos_Paciente", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Presenta alguna condición de </span></p><p><span style=\" font-size:14pt; font-weight:600;\">discapacidad motora o perdida de miembro superior :</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("Datos_Paciente", "Si"))
        self.comboBox_2.setItemText(1, _translate("Datos_Paciente", "No"))
        self.label_8.setText(_translate("Datos_Paciente", "<html><head/><body><p align=\"justify\"><span style=\" font-weight:600;\">Autoriza al equipo de investigador exponer sus datos </span></p><p align=\"justify\"><span style=\" font-weight:600;\">consignados con anterioridada la comunidad cientifica: </span></p><p align=\"justify\"><span style=\" font-weight:600;\"><br/></span></p></body></html>"))
        self.radioButton.setText(_translate("Datos_Paciente", "Si"))
        self.radioButton_2.setText(_translate("Datos_Paciente", "No"))
        self.pushButton.setText(_translate("Datos_Paciente", "SIGUIENTE"))
        self.pushButton_2.setText(_translate("Datos_Paciente", "CANCELAR"))
    
    def close_application(self):
        sys.exit()

    def crear_paciente(self):
        if not (self.textEdit_3.toPlainText() and self.textEdit.toPlainText() and self.textEdit_2.toPlainText())  :
            print("El QLineEdit esta vacio")
            msg = QMessageBox()
            msg.setWindowTitle("Control")
            msg.setText("Atención!")
            msg.setIcon(QMessageBox.Warning)
            msg.setInformativeText("Por favor ingrese todos los campos!")
            msg.exec()
            self.radioButton.setAutoExclusive(False)
            self.radioButton.setChecked(False)
        else:
            global carpetaPaciente 
            print(self.comboBox.currentText())
            carpetaPaciente = f"Paciente_ID_{self.textEdit.toPlainText()}" #Creacion de carpetas para guarda archivos si no existe
            if not os.path.exists(carpetaPaciente):
                os.mkdir(carpetaPaciente)
                with open(os.path.join(carpetaPaciente, "datos_paciente.txt"), 'w') as fp:
                    fp.write("Numero de identificación del estudio: %s" %self.textEdit.toPlainText())
                    fp.write("\n")
                    fp.write("Genero del paciente: %s" %self.comboBox.currentText())
                    fp.write("\n")
                    fp.write("Edad del paciente: %s" %self.textEdit_2.toPlainText())
                    fp.write("\n")
                    fp.write("Peso (Kg) del paciente: %s" %self.textEdit_3.toPlainText())
                    fp.write("\n")
                    fp.write("Paciente con condicion de discapacidad: %s" %self.comboBox_2.currentText())

            self.pushButton.setEnabled(True)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Datos_Paciente = QtWidgets.QMainWindow()
    ui = Ui_Datos_Paciente()
    ui.setupUi(Datos_Paciente)
    Datos_Paciente.show()
    sys.exit(app.exec_())
