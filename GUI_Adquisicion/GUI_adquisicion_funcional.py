# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Sep 12 2010)
# http://www.wxformbuilder.org/
##
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
from wx.adv import Animation, AnimationCtrl
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from matplotlib import pyplot as plt
from collections import deque
from threading import Lock, Thread
import wx.lib.agw.aui as aui
import wx.lib.mixins.inspection as wit
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.backends.backend_wx import _load_bitmap
from matplotlib.figure import Figure
from scipy import signal
import time
import wx.gizmos as gizmos
from tkinter import *
import sys
import matplotlib.animation as manim
import threading

# Librerias MYO
import subprocess
import os
from MYO_conexion import *
from time import clock

import myo

# Librerias UltraCortex
from pyOpenBCI import OpenBCICyton

###########################################################################
# Class FrameMain
###########################################################################


class FrameMain (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Proyecto Investigación LASER",
                          pos=wx.DefaultPosition, size=wx.Size(1400, 700), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        BoxMain = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        Sizer_titulo = wx.BoxSizer(wx.VERTICAL)

        self.m_Bienvenido = wx.StaticText(
            self, wx.ID_ANY, u"Bienvenidos al proyecto de investigación Modelo híbrido de control  con señales  mioeléctrica y encefalográfica para la identificación de gestos en miembro superior\n", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_Bienvenido.Wrap(800)
        self.m_Bienvenido.SetFont(
            wx.Font(36, 70, 90, 90, False, wx.EmptyString))
        self.m_Bienvenido.SetForegroundColour(wx.Colour(53, 55, 254))

        Sizer_titulo.Add(self.m_Bienvenido, 0, wx.ALL, 5)

        Sizer_imagen = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bitmap1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(
            u"/Users/macfabian/Documents/Desarrollo Tesis/GUI_Adquisicion/bienvenido.png", wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.Size(-1, -1), 0)
        Sizer_imagen.Add(self.m_bitmap1, 0, wx.ALIGN_CENTER |
                         wx.ALIGN_BOTTOM, 5)

        Sizer_titulo.Add(Sizer_imagen, 10, wx.ALIGN_CENTER, 5)

        Sizer_botones = wx.BoxSizer(wx.HORIZONTAL)

        Sizer_botones.SetMinSize(wx.Size(300, 50))
        self.button_iniciar = wx.Button(
            self, wx.ID_ANY, u"Iniciar", wx.DefaultPosition, wx.Size(150, -1), 0)
        self.button_iniciar.SetFont(
            wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        self.button_iniciar.SetForegroundColour(wx.Colour(17, 0, 254))
        self.button_iniciar.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        Sizer_botones.Add(self.button_iniciar, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        self.button_salir = wx.Button(
            self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.Size(150, -1), 0)
        self.button_salir.SetFont(
            wx.Font(18, 70, 90, 90, False, wx.EmptyString))

        Sizer_botones.Add(self.button_salir, 0, wx.ALIGN_CENTER_VERTICAL, 50)

        Sizer_titulo.Add(Sizer_botones, 0, wx.ALIGN_CENTER |
                         wx.ALIGN_CENTER_HORIZONTAL, 0)

        BoxMain.Add(Sizer_titulo, 50, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER, 0)

        self.SetSizer(BoxMain)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.button_iniciar.Bind(wx.EVT_BUTTON, self.OnClickIniciar)
        self.button_salir.Bind(wx.EVT_BUTTON, self.OnClickSalir)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnClickSalir(self, event):
        self.Close()
    # Virtual event handlers, overide them in your derived class

    def OnClickIniciar(self, event):
        self.Close()
        app1 = wx.App()
        ventanaExplicacion = FrameObjetivos(None)
        ventanaExplicacion.Show()
        app1.MainLoop()


###########################################################################
# Class FrameObjetivos
###########################################################################


class FrameObjetivos (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Objetivos de la investigación",
                          pos=wx.DefaultPosition, size=wx.Size(1400, 700), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(
            self, wx.ID_ANY, u"Objetivo General", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(
            wx.Font(34, 70, 90, 90, False, wx.EmptyString))

        bSizer4.Add(self.m_staticText2, 0, wx.ALIGN_CENTER_HORIZONTAL, 10)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(
            self, wx.ID_ANY, u"Diseñar un modelo híbrido que relacione las  señales  mioeléctrica y   las señales encefalográficas para la   identificación de gestos  comunes realizados por  un  miembro superior. ", wx.DefaultPosition, wx.Size(800, 160), 0)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(
            wx.Font(26, 70, 90, 90, False, wx.EmptyString))

        bSizer7.Add(self.m_staticText3, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALIGN_CENTER_HORIZONTAL |
                    wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT | wx.ALIGN_TOP | wx.ALL | wx.BOTTOM | wx.LEFT | wx.RIGHT | wx.TOP, 0)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText4 = wx.StaticText(
            self, wx.ID_ANY, u"Objetivos Especificos", wx.DefaultPosition, wx.Size(-1, 50), 0)
        self.m_staticText4.Wrap(-1)
        self.m_staticText4.SetFont(
            wx.Font(34, 70, 90, 90, False, wx.EmptyString))

        bSizer9.Add(self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"- Establecer los gestos que serán razón de estudio en el desarrollo del proyecto. \n -Identificar, caracterizar, procesar y analizar las características principales de las  señales mioeléctricas junto a las señales encefalográficas obtenidas en el estudio.  \n - Definir  un modelo conceptual que incluya las señales bioeléctricas relacionadas del miembro  superior.   \n - Realizar un cuadro comparativo donde se compare la efectividad  del modelo relacional ( señales mioeléctricas y  encefalográficas) obtenidos  de los gestos estudiados contra un modelo  ya establecido  de gestos obtenidos con señales mioeléctricas. ", wx.Point(-1, -1), wx.Size(1300, 300), 0)
        self.m_staticText5.Wrap(-1)
        self.m_staticText5.SetFont(
            wx.Font(22, 70, 90, 90, False, wx.EmptyString))

        bSizer10.Add(self.m_staticText5, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALIGN_CENTER_VERTICAL |
                     wx.ALIGN_TOP | wx.ALL | wx.BOTTOM | wx.FIXED_MINSIZE | wx.LEFT | wx.RIGHT | 0)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer8.SetMinSize(wx.Size(300, 80))
        self.button_siguiente = wx.Button(
            self, wx.ID_ANY, u"Siguiente", wx.DefaultPosition, wx.Size(150, -1), 0)
        self.button_siguiente.SetFont(
            wx.Font(18, 70, 90, 90, False, wx.EmptyString))

        bSizer8.Add(self.button_siguiente, 0, wx.ALL, 5)

        self.button_salir = wx.Button(
            self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.Size(150, -1), 0)
        self.button_salir.SetFont(
            wx.Font(18, 70, 90, 90, False, wx.EmptyString))

        bSizer8.Add(self.button_salir, 0, wx.ALL, 5)

        bSizer10.Add(bSizer8, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 50)

        bSizer9.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer7.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer4.Add(bSizer7, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.button_siguiente.Bind(wx.EVT_BUTTON, self.OnClickConcentimiento)
        self.button_salir.Bind(wx.EVT_BUTTON, self.OnClickSalir)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnClickConcentimiento(self, event):
        self.Close()
        app2 = wx.App()
        ventanaConsentimiento = FrameConsentimiento(None)
        ventanaConsentimiento.Show()
        app2.MainLoop()

    def OnClickSalir(self, event):
        self.Close()


###########################################################################
# Class FrameConsentimiento
###########################################################################


class FrameConsentimiento (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Consentimiento de la investigación",
                          pos=wx.DefaultPosition, size=wx.Size(1400, 700), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(
            self, wx.ID_ANY, u"Consentimiento informado", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(
            wx.Font(34, 70, 90, 90, False, wx.EmptyString))

        bSizer4.Add(self.m_staticText2, 0, wx.ALIGN_CENTER_HORIZONTAL, 10)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"Para continuar con el desarrollo del experimento es necesario  que usted, como participante lea cuidadosamente el consentimiento  informado previamente entregado por el equipo investigador, si tiene alguna duda o no entiende alguna palabra del consentiento por favor no dude en realizar todas las preguntas pertinente al equipo investigador.", wx.DefaultPosition, wx.Size(720, 270), 0)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(
            wx.Font(26, 70, 90, 90, False, wx.EmptyString))

        bSizer7.Add(self.m_staticText3, 0, wx.ALIGN_BOTTOM |
                    wx.ALIGN_CENTER_HORIZONTAL, 0)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(
            self, wx.ID_ANY, u"¿ Ha leido y comprendido en su totalidad el consentimiento informado dado con  anterioridad ? ", wx.DefaultPosition, wx.Size(400, 150), 0)
        self.m_staticText5.Wrap(-1)
        self.m_staticText5.SetFont(
            wx.Font(24, 70, 90, 90, False, wx.EmptyString))

        bSizer10.Add(self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer8.SetMinSize(wx.Size(300, 50))
        self.button_siguiente = wx.Button(
            self, wx.ID_ANY, u"Siguiente", wx.DefaultPosition, wx.Size(150, -1), 0)
        self.button_siguiente.SetFont(
            wx.Font(18, 70, 90, 90, False, wx.EmptyString))

        bSizer8.Add(self.button_siguiente, 0, wx.ALL, 5)

        self.button_salir = wx.Button(
            self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.Size(150, -1), 0)
        self.button_salir.SetFont(
            wx.Font(18, 70, 90, 90, False, wx.EmptyString))

        bSizer8.Add(self.button_salir, 0, wx.ALL, 5)

        bSizer10.Add(bSizer8, 2, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 50)

        bSizer9.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer7.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer4.Add(bSizer7, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.button_siguiente.Bind(wx.EVT_BUTTON, self.OnClickConcentimiento)
        self.button_salir.Bind(wx.EVT_BUTTON, self.OnClickSalir)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnClickConcentimiento(self, event):
        self.Close()
        app3 = wx.App()
        ventanaCalibracion = FrameCalibracion(None)
        ventanaCalibracion.Show()
        app3.MainLoop()

    def OnClickSalir(self, event):
        self.Close()

    ###########################################################################
# Class FrameCalibracion

###########################################################################


class FrameCalibracion(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Calibración de herramientas",
                          pos=wx.DefaultPosition, size=wx.Size(1400, 700), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(
            self, wx.ID_ANY, u"Calibración de herramientas", wx.DefaultPosition, wx.Size(-1, 80), 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(
            wx.Font(34, 70, 90, 90, False, wx.EmptyString))

        bSizer4.Add(self.m_staticText2, 0, wx.ALIGN_CENTER_HORIZONTAL, 10)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(
            self, wx.ID_ANY, u"En esta etapa del proceso el equipo investigador procedera a realizar la calibración de la herramienta  UltraCortex (casco) y la herramienta MYO (brazalete).", wx.DefaultPosition, wx.Size(700, 280), 0)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(
            wx.Font(26, 70, 90, 90, False, wx.EmptyString))

        bSizer7.Add(self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(
            self, wx.ID_ANY, u"¿ Las herramientas ya han sido  calibradas en su totalidad  por el equipo de investigación? ", wx.DefaultPosition, wx.Size(400, 100), 0)
        self.m_staticText5.Wrap(-1)
        self.m_staticText5.SetFont(
            wx.Font(24, 70, 90, 90, False, wx.EmptyString))

        bSizer10.Add(self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer8.SetMinSize(wx.Size(300, 50))
        self.button_siguiente = wx.Button(
            self, wx.ID_ANY, u"Siguiente", wx.DefaultPosition, wx.Size(150, -1), 0)
        self.button_siguiente.SetFont(
            wx.Font(18, 70, 90, 90, False, wx.EmptyString))

        bSizer8.Add(self.button_siguiente, 0, wx.ALL, 5)

        self.button_salir = wx.Button(
            self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.Size(150, -1), 0)
        self.button_salir.SetFont(
            wx.Font(18, 70, 90, 90, False, wx.EmptyString))

        bSizer8.Add(self.button_salir, 0, wx.ALL, 5)

        bSizer10.Add(bSizer8, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 170)

        bSizer9.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer7.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer4.Add(bSizer7, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.button_siguiente.Bind(wx.EVT_BUTTON, self.OnClickCInstruccion)
        self.button_salir.Bind(wx.EVT_BUTTON, self.OnClickSalir)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnClickCInstruccion(self, event):
        self.Close()
        app4 = wx.App()
        ventanaInstruccion = FrameInstrucion(None)
        ventanaInstruccion.Show()
        app4.MainLoop()

    def OnClickSalir(self, event):
        self.Close()


###########################################################################
# Class FrameInstrucion
###########################################################################

class FrameInstrucion (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Instruciones del proyecto",
                          pos=wx.DefaultPosition, size=wx.Size(1400, 700), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(
            self, wx.ID_ANY, u"Instrucciones de toma de señales", wx.DefaultPosition, wx.Size(-1, 60), 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(
            wx.Font(34, 70, 90, 90, False, wx.EmptyString))

        bSizer4.Add(self.m_staticText2, 0, wx.ALIGN_CENTER_HORIZONTAL, 10)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"A continuación usted tendra que realizar una serie de gestos con o sin ayuda de elementos que le seran brindados por el equipo de investigación, por favor lea  con atención y realice el gesto lo mas parecido posible  a las imagenes de refencia, tendra que realizar los  los gestos las veces definidas y el tiempo que se  le indique el equipo de investigación.", wx.DefaultPosition, wx.Size(700, 280), 0)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(
            wx.Font(26, 70, 90, 90, False, wx.EmptyString))

        bSizer7.Add(self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(
            self, wx.ID_ANY, u"¿ Esta de acuerdo con seguir las instruciones definidas por el equipo de investigación? ", wx.DefaultPosition, wx.Size(400, 120), 0)
        self.m_staticText5.Wrap(-1)
        self.m_staticText5.SetFont(
            wx.Font(24, 70, 90, 90, False, wx.EmptyString))

        bSizer10.Add(self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer8.SetMinSize(wx.Size(300, 50))
        self.button_siguiente = wx.Button(
            self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.Size(150, -1), 0)
        self.button_siguiente.SetFont(
            wx.Font(18, 70, 90, 90, False, wx.EmptyString))

        bSizer8.Add(self.button_siguiente, 0, wx.ALL, 5)

        self.button_salir = wx.Button(
            self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.Size(150, -1), 0)
        self.button_salir.SetFont(
            wx.Font(18, 70, 90, 90, False, wx.EmptyString))

        bSizer8.Add(self.button_salir, 0, wx.ALL, 5)

        bSizer10.Add(bSizer8, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 170)

        bSizer9.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer7.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer4.Add(bSizer7, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.button_siguiente.Bind(wx.EVT_BUTTON, self.OnClickConcentimiento)
        self.button_salir.Bind(wx.EVT_BUTTON, self.OnClickSalir)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnClickConcentimiento(self, event):
        self.Close()
        app5 = wx.App()
        ventanaGesto1 = FrameGesto1(None)
        ventanaGesto1.Show()
        app5.MainLoop()

    def OnClickSalir(self, event):
        self.Close()


###########################################################################
# Class FrameGesto1
###########################################################################
global s
s = 0
global m
m = 0
global t
t = 0
global i
i = 0
global c
c = 0
SCALE_FACTOR = (4500000)/24/(2**23-1) #From the pyOpenBCI repo
data_eeg = [[0,0,0,0,0,0,0,0]]
bp_Hz = np.array([7, 13])
bp_b, bp_a = signal.butter(2, bp_Hz / (250 / 2.0), btype='bandpass')


class FrameGesto1 (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Captura de señales para el gesto 1",
                          pos=wx.DefaultPosition, size=wx.Size(1400, 1000), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)
        self.panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.panel.SetSizer(sizer)
        self.m_staticText2 = wx.StaticText(
            self, wx.ID_ANY, u"Captura de señales para el primer gesto \n", wx.DefaultPosition, wx.Size(700, -1), 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(
            wx.Font(34, 70, 90, 90, False, wx.EmptyString))

        bSizer4.Add(self.m_staticText2, 0, wx.ALIGN_CENTER_HORIZONTAL, 10)

        bSizer49 = wx.BoxSizer(wx.VERTICAL)

        bSizer50 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer50.SetMinSize(wx.Size(700, 50))
        self.m_staticText30 = wx.StaticText(
            self, wx.ID_ANY, u"Para iniciar el experimento por favor observe \n ", wx.DefaultPosition, wx.Size(1000, -1), 0)
        self.m_staticText30.Wrap(-1)
        self.m_staticText30.SetFont(
            wx.Font(17, 70, 90, 90, False, wx.EmptyString))

        bSizer50.Add(self.m_staticText30, 0, wx.ALL, 5)

        bSizer52 = wx.BoxSizer(wx.VERTICAL)

        bSizer52.SetMinSize(wx.Size(90, -1))
        self.m_button32 = wx.Button(
            self, wx.ID_ANY, u"Inicio", wx.Point(-1, -1), wx.Size(150, -1), 0)
        self.m_button32.SetFont(wx.Font(25, 70, 90, 90, False, wx.EmptyString))

        bSizer52.Add(self.m_button32, 0, wx.TOP, 10)

        bSizer50.Add(bSizer52, 1, 0, 5)

        self.m_animCtrl1 = AnimationCtrl(self, pos=(
            40, 40), size=(14, 14), name="AnimationCtrl")
        self.m_animCtrl1.LoadFile(
            r"C:\Users\crist\OneDrive\Escritorio\Universidad\LASER\Tesis\Open_BCI_and_MYO_UD\GUI_Adquisicion/manos.gif")
        self.m_animCtrl1.Play()
        self.m_animCtrl1.SetMinSize(wx.Size(200, -1))

        bSizer50.Add(self.m_animCtrl1, 0, wx.ALIGN_CENTER, 5)

        bSizer49.Add(bSizer50, 1, 0, 5)

        bSizer51 = wx.BoxSizer(wx.VERTICAL)
        bSizer57 = wx.BoxSizer(wx.HORIZONTAL)

        # grafica EMG
        self.figureEMG = plt.figure(figsize=(1, 6), dpi=60)
        self.axes = [self.figureEMG.add_subplot(
            '81' + str(i)) for i in range(1, 9)]    
        self.n = 512
        [(ax.set_ylim(ymin=-200, ymax=200) )for ax in self.axes]
        global graphs
        self.graphs = [ax.plot(np.arange(self.n), np.zeros(self.n))[
                               0] for ax in self.axes]
        plt.ion()
        self.canvEMG = FigureCanvas(self, wx.ID_ANY, self.figureEMG)
        bSizer57.Add(self.canvEMG, 1, wx.TOP | wx.LEFT | wx.EXPAND)

        # grafica EEG
        self.figureEEG = plt.figure(figsize=(1, 6), dpi=60)
        self.axesEEG = [self.figureEEG.add_subplot(
            '81' + str(i)) for i in range(1, 9)]
        [(ax.set_ylim([-150000,150000])) for ax in self.axesEEG]
        self.m = 100
        self.graphsEEG = [ax.plot(np.arange(self.m), np.zeros(self.m))[
                               0] for ax in self.axesEEG]
        plt.ion()
        self.canvasEEG = FigureCanvas(self, -1, self.figureEEG)
        bSizer57.Add(self.canvasEEG, 1, wx.TOP | wx.LEFT | wx.EXPAND)

        bSizer51.Add(bSizer57, 1, wx.EXPAND, 5)

        bSizer49.Add(bSizer51, 1, wx.EXPAND, 5)

        bSizer53 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText31 = wx.StaticText(
            self, wx.ID_ANY, u"Señal EMG", wx.DefaultPosition, wx.Size(700, 30), 0)
        self.m_staticText31.Wrap(-1)
        self.m_staticText31.SetFont(
            wx.Font(18, 70, 90, 90, False, wx.EmptyString))

        bSizer53.Add(self.m_staticText31, 0, wx.LEFT, 5)

        self.m_staticText32 = wx.StaticText(
            self, wx.ID_ANY, u"Señal EEG", wx.DefaultPosition, wx.Size(-1, 30), 0)
        self.m_staticText32.Wrap(-1)
        self.m_staticText32.SetFont(
            wx.Font(18, 70, 90, 90, False, wx.EmptyString))

        bSizer53.Add(self.m_staticText32, 0, 0, 5)

        bSizer49.Add(bSizer53, 1, 0, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText33 = wx.StaticText(
            self, wx.ID_ANY, u"Tiempo:", wx.DefaultPosition, wx.Size(550, -1), 0)
        self.m_staticText33.Wrap(-1)
        self.m_staticText33.SetFont(
            wx.Font(18, 70, 90, 90, False, wx.EmptyString))
        bSizer8.Add(self.m_staticText33, 0, wx.ALL, 5)
        pos = wx.DefaultPosition
        size = wx.Size(1, 11)
        style = gizmos.LED_ALIGN_CENTER
        self.led = gizmos.LEDNumberCtrl(self, -1, pos, size, style)
        self.led.SetBackgroundColour("white")
        self.led.SetForegroundColour("black")
        bSizerTimmer = wx.BoxSizer(wx.VERTICAL)
        bSizerTimmer.Add(self.led, 1, wx.TOP | wx.LEFT | wx.EXPAND)
        bSizer49.Add(bSizerTimmer, 1, wx.EXPAND, 5)

        self.button_siguiente = wx.Button(
            self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.Size(150, -1), 0)
        self.button_siguiente.SetFont(
            wx.Font(18, 70, 90, 90, False, wx.EmptyString))

        bSizer8.Add(self.button_siguiente, 0, wx.ALL, 5)

        self.button_salir = wx.Button(
            self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.Size(150, -1), 0)
        self.button_salir.SetFont(
            wx.Font(18, 70, 90, 90, False, wx.EmptyString))

        bSizer8.Add(self.button_salir, 0, wx.ALL, 5)

        bSizer49.Add(bSizer8, 0, wx.TOP, 1)

        bSizer4.Add(bSizer49, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button32.Bind(wx.EVT_BUTTON, self.OnClickInicio)
        self.button_siguiente.Bind(wx.EVT_BUTTON, self.OnClickConcentimiento)
        self.button_salir.Bind(wx.EVT_BUTTON, self.OnClickSalir)
        # Arrancar conexion myo
        self.conexionMYO()
        def hiloMYOConexion(arg):
            hiloConexionMYO = threading.currentThread()
            while getattr(hiloConexionMYO, "do_run", True):
                    print("working on %s" % arg)
                    self.mainMYO()
            print("Stopping as you wish.")
        self.hiloConexionMYO = threading.Thread(target=hiloMYOConexion,args=("PLOT_EMG_MYO",))
        self.hiloConexionMYO.setDaemon(True)
        self.hiloConexionMYO.start()
        # Arranca conexion UltraCortex
        self.datosEEG = []
        self.start_board()
        def hiloPlotUltracortex(arg):
            hiloPlotUltracortex = threading.currentThread()
            while getattr(hiloPlotUltracortex, "do_run", True):
                    print("working on %s" % arg)
                    time.sleep(3)
                    self.mainplotUltracortex()
            print("Stopping as you wish.")
        self.hiloPlotUltracortex = threading.Thread(target=hiloPlotUltracortex,args=("PLOT_EEG_ULTRACORTEX",))
        self.hiloPlotUltracortex.setDaemon(True)
        self.hiloPlotUltracortex.start()
       
    def __del__(self):
        pass


# Virtual event handlers, overide them in your derived class
    def OnClickInicio(self, event):
        self.GetSegundos(None)

    def OnClickConcentimiento(self, event):
        event.Skip()

    def OnClickSalir(self, event):
        self.Close()
        sys.exit()

    

    def GetSegundos(self, e):
        global segundos
        self.board.stop_stream()
        self.stopconexioUltracortexPlot = True
        self.hiloPlotUltracortex.do_run = False
        self.hiloPlotUltracortex.join()
        self.stopconexion= True
        self.hiloConexionMYO.do_run = False
        self.hiloConexionMYO.join()
        dlg = wx.TextEntryDialog(self.panel, 'Ingrese los segundos a grabar el gesto:',"Captura del gesto","", 
                style=wx.OK)
        dlg.ShowModal()
        segundos = int(dlg.GetValue()) 
        
        def hiloRunTimmer(arg):
            hiloRunTimmer = threading.currentThread()
            while getattr(hiloRunTimmer, "do_run", True):
                    print("working on %s" % arg)
                    self.led.SetValue("00:00")
                    self.OnTimer(None, e=segundos)
            print("Stopping as you wish.")
        self.hiloRunTimmer = threading.Thread(target=hiloRunTimmer,args=("RUN_Timmer",))
        self.hiloRunTimmer.setDaemon(True)
        self.hiloRunTimmer.start()


        def hiloMYOSaved(arg):
            hiloMYOSaved = threading.currentThread()
            while getattr(hiloMYOSaved, "do_run", True):
                    print("working on %s" % arg)
                    self.mainSavedMYO()
            print("Stopping as you wish.")
        self.hiloMYOSaved = threading.Thread(target=hiloMYOSaved,args=("Saved_EMG_MYO",))
        self.hiloMYOSaved.setDaemon(True)
        self.hiloMYOSaved.start()

        def hiloUltracortesConexion(arg):
            hiloUltracortesConexion = threading.currentThread()
            while getattr(hiloUltracortesConexion, "do_run", True):
                    print("working on %s" % arg)
                    self.mainULTRACORTEX()
            print("Stopping as you wish.")
        self.hiloUltracortesConexion = threading.Thread(target=hiloUltracortesConexion,args=("SAVE_EEG_ULTRACORTEX",))
        self.hiloUltracortesConexion.setDaemon(True)
        self.hiloUltracortesConexion.start()

  

        dlg.Destroy()

    def OnTimer(self, event, e):
        print("OnTimmer Inicia")
        global i
        global c
        c = e
        if(i < c):
            i += 1   
            time.sleep(1)
            self.TimerGo(None)
            
            
        else:
            print("Termino Timer")
            self.board.stop_stream()
            self.stopconexioUltracortex = True
            self.hiloUltracortesConexion.do_run = False
            self.hiloUltracortesConexion.join()
            self.hiloRunTimmer.do_run = False
            self.stopsaved= True
            self.hiloMYOSaved.do_run = False
            self.hiloMYOSaved.join()
            
          
                 

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
        self.led.SetValue(t)
        self.OnTimer(None, c)

    def conexionMYO(self):
        print("Realizando Conexión MYO")
        myo.init()
        self.hub = myo.Hub()
        self.listener = EmgCollector(512)
        self.stopconexion = False
        self.stopsaved = False
        print("Conexión MYO Establecida")
        self.Crear_carpetaMYO()
        

    def mainMYO(self):
        global data_total
        data_total = []
        with self.hub.run_in_background(self.listener.on_event):
            while True:
                self.plotMYO()
                time.sleep(0.1)
                if (self.stopconexion == True):
                    break
    
    def mainSavedMYO(self):
        global fila
        fila = 0
        with self.hub.run_in_background(self.listener.on_event):
            while True:
                self.SaveMYO()
                time.sleep(2.56)
                if (self.stopsaved == True):
                    break
    
    def plotMYO(self):
        global graphs
        emg_data = self.listener.get_emg_data()
        emg_data = np.array([x[1] for x in emg_data]).T
        for g, data in zip(self.graphs, emg_data):
            if len(data) < self.n:
                data = np.concatenate([np.zeros(self.n - len(data)), data])
            g.set_ydata(data)
        #plt.draw()
    
    def SaveMYO(self):
        global fila
        global data_total
        numMuestras = 512
        emg_data = self.listener.get_emg_data()
        emg_data = [x[1] for x in emg_data]
        with open(os.path.join(carpetaEMG, "datos %d.csv"% j), 'a') as fp: # Guardar datos en el archivo csv
            for h in range(0,512):
                for i in range(0,8):
                    fp.write(str(emg_data[h][i])+";")
                fp.write("\n")
    ###########################################################################
    # Ultracortex
    def start_board(self):
        global fila
        fila=0
        self.board = OpenBCICyton(port='COM8', daisy=False)
        self.stopconexioUltracortex= False
        self.stopconexioUltracortexPlot= False
        self.Crear_carpetaEEG()
        
    
    def mainULTRACORTEX(self):
        while (self.stopconexioUltracortex == False):
            self.board.start_stream(self.save_data)
            
        print("entro if")
        self.board.stop_stream()
    

    def mainplotUltracortex(self):
        while (self.stopconexioUltracortexPlot==False):
            time.sleep(0.1)
            self.board.start_stream(self.plot_eeg)
        print("entro if")
        self.board.stop_stream()
    
    def plot_eeg(self, sample):
        global datosEEG,bp_a,bp_b
        global graphsEEG
        self.datosEEG.append([i*(SCALE_FACTOR) for i in sample.channels_data])
        datosEEGplot = np.array(self.datosEEG).T
        # for o in range (8):
        #    datosEEGplot[o] = signal.lfilter(bp_b, bp_a, datosEEGplot[o]) 
        for g, data in zip(self.graphsEEG, datosEEGplot):
            if len(data) < self.m: 
                data = np.concatenate([np.zeros(self.m - len(data)), data])              
            else:
                data = np.array(data[(len(data)-self.m):])
            # dy = (max(data) - min(data))*0.7
            # [(ax.set_ylim([min(data)-dy, max(data)+dy])) for ax in self.axesEEG]
            g.set_ydata(data)
        #plt.draw()>:V
        self.board.stop_stream()


    def save_data(self, sample):
        global fila
        global datosEEG,bp_a,bp_b
        self.datosEEG.append([i*(SCALE_FACTOR) for i in sample.channels_data])
        datosEEGplot = np.array(self.datosEEG).T
        with open(os.path.join(carpetaEEG, "datos %d.csv"% j), 'a') as fp: # Guardar datos en el archivo csv        
            for i in range(0,8):
                fp.write(str(self.datosEEG[fila][i])+";")
            fp.write("\n")
            fila+= 1

            
    
    def Crear_carpetaEEG(self):
        global carpetaEEG 
        global j
        global fila
        fila = 0
        Archivo = True
        j = 1
        Tipo = "PruebaUltracortex"
        carpetaEEG = f"Base_Datos_{Tipo}" #Creacion de carpetas para guarda archivos si no existe
        if not os.path.exists(carpetaEEG):
            os.mkdir(carpetaEEG)

        while(Archivo == True):# Se crea un archivo csv en caso de que no exista
            if os.path.isfile(carpetaEEG + "/datos %d.csv"% j):
                print('El archivo existe.')
                j+=1
            else:
                with open(os.path.join(carpetaEEG, "datos %d.csv"% j), 'w') as fp:
                    [fp.write('CH%d ;'%i)for i in range(1,9)]
                    fp.write("\n")
                    print("Archivo Creado")
                    Archivo = False
    
    def Crear_carpetaMYO(self):
        global carpetaEMG 
        global j
        global fila
        fila = 0
        Archivo = True
        j = 1
        Tipo = "PruebaMYO"
        carpetaEMG = f"Base_Datos_{Tipo}" #Creacion de carpetas para guarda archivos si no existe
        if not os.path.exists(carpetaEMG):
            os.mkdir(carpetaEMG)

        while(Archivo == True):# Se crea un archivo csv en caso de que no exista
            if os.path.isfile(carpetaEMG + "/datos %d.csv"% j):
                print('El archivo existe.')
                j+=1
            else:
                with open(os.path.join(carpetaEMG, "datos %d.csv"% j), 'w') as fp:
                    [fp.write('CH%d ;'%i)for i in range(1,9)]
                    fp.write("\n")
                    print("Archivo Creado")
                    Archivo = False
    
                                    

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

