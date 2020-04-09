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
import time
import wx.gizmos as gizmos
from tkinter import *
import sys
import matplotlib.animation as manim
import threading


import subprocess
import os
from MYO_conexion import *
import signal

import myo


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
global t_eeg
t_eeg = np.arange(0.0, 3.0, 0.01)

global data_eeg
data_eeg = np.sin(10 * np.pi * t_eeg)


class FrameGesto1 (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Captura de señales para el gesto 1",
                          pos=wx.DefaultPosition, size=wx.Size(1400, 800), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

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

        bSizer50.SetMinSize(wx.Size(700, -1))
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
            40, 40), size=(24, 24), name="AnimationCtrl")
        self.m_animCtrl1.LoadFile(
            u"/Users/macfabian/Documents/Desarrollo Tesis/GUI_Adquisicion/manos.gif")
        self.m_animCtrl1.Play()
        self.m_animCtrl1.SetMinSize(wx.Size(200, -1))

        bSizer50.Add(self.m_animCtrl1, 0, wx.ALIGN_CENTER, 5)

        bSizer49.Add(bSizer50, 1, 0, 5)

        bSizer51 = wx.BoxSizer(wx.VERTICAL)
        bSizer57 = wx.BoxSizer(wx.HORIZONTAL)

        # grafica EMG
        self.figureEMG = plt.figure(figsize=(1, 7), dpi=60)
        self.axes = [self.figureEMG.add_subplot(
            '81' + str(i)) for i in range(1, 9)]
        [(ax.set_ylim([-100, 100])) for ax in self.axes]
        self.n = 512
        global graphs
        self.graphs = [ax.plot(np.arange(self.n), np.zeros(self.n))[
                               0] for ax in self.axes]
        plt.ion()
        self.canvEMG = FigureCanvas(self, wx.ID_ANY, self.figureEMG)
        # self.animator = manim.FuncAnimation(self.figureEMG,self.anim, interval=200)
        bSizer57.Add(self.canvEMG, 1, wx.TOP | wx.LEFT | wx.EXPAND)

        # grafica EEG
        self.figure = Figure(figsize=(1, 2), dpi=80)
        self.axesE = self.figure.add_subplot(811)
        self.axesE = self.figure.add_subplot(812)
        self.axesE = self.figure.add_subplot(813)
        self.axesE = self.figure.add_subplot(814)
        self.axesE = self.figure.add_subplot(815)
        self.axesE = self.figure.add_subplot(816)
        self.axesE = self.figure.add_subplot(817)
        self.axesE = self.figure.add_subplot(818)
        # self.axes.plot(t_eeg, data_eeg)
        self.canvasEEG = FigureCanvas(self, -1, self.figure)
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
        self.hiloConexionMYO.start()
        
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
        self.hiloRunTimmer.start()


        def hiloMYOSaved(arg):
            hiloMYOSaved = threading.currentThread()
            while getattr(hiloMYOSaved, "do_run", True):
                    print("working on %s" % arg)
                    self.mainSavedMYO()
            print("Stopping as you wish.")
        self.hiloMYOSaved = threading.Thread(target=hiloMYOSaved,args=("Saved_EMG_MYO",))
        self.hiloMYOSaved.start()

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
            self.hiloRunTimmer.do_run = False
            self.stopconexion= True
            self.hiloConexionMYO.do_run = False
            self.hiloConexionMYO.join()
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
        self.Crear_carpeta()
        

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
        plt.draw()
    
    def SaveMYO(self):
        global fila
        global data_total
        numMuestras = 512
        emg_data = self.listener.get_emg_data()
        print("datos saved originales")
        print(emg_data)
        emg_data = [x[1] for x in emg_data]
        print("datos saved")
        print(emg_data)
        self.Guardar_Datos(emg_data)
        # a = list()
        # a = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[11, 12, 13, 14, 15, 16, 17, 18, 19, 20],[21, 22, 23, 24, 25, 26, 27, 28, 29, 30,],[31,32,33,34,35,36,37,38,39,40],[51,52,53,54,55,56,57,58,59,60],[51,52,53,54,55,56,57,58,59,60],[61,62,63,64,65,66,67,68,69,70],[71,72,73,74,75,76,77,78,79,80]]
        # for g, data in zip(self.graphs,  emg_data):
        #     if len(data) < numMuestras:
        #         # completa vector columna con zeros para tener longitud de 512 o n
        #         data = np.concatenate([np.zeros(numMuestras - len(data)), data]) 
        #     #data_total.append(np.array(data))
        #     data_total.append(np.array(data[-10:]))
        # print("Dato: " + str(i))
        # print(data_total)
        # print("fin")
       
    
    def Guardar_Datos(self, datos):
        global fila
        numCanales = 8
        print("guarda")
        print(len(datos))
        #datos= np.array(datos)
        print(datos)
        print("array")
        # contadorcanal = 0
        # datoscanal1 =[0]
        # datoscanal2 =[0]
        # datoscanal3 =[0]
        # datoscanal4 =[0]
        # datoscanal5 =[0]
        # datoscanal6 =[0]
        # datoscanal7 =[0]
        # datoscanal8 =[0]

        # for g in range(0,len(datos),8):
        #     for h in range(0,512):
        #         datoscanal1= datoscanal1 + datos[h][g]
        #         datoscanal2= datoscanal2 + datos[h][g+1]
        #         datoscanal3= datoscanal3 + datos[h][g+2]
        #         datoscanal4= datoscanal4 + datos[h][g+3]
        #         datoscanal5= datoscanal5 + datos[h][g+4]
        #         datoscanal6= datoscanal6 + datos[h][g+5]
        #         datoscanal7= datoscanal7 + datos[h][g+6]
        #         datoscanal8= datoscanal8 + datos[h][g+7]

             
        # print("array canal1")
        # print(datoscanal1)
        # print(len(datoscanal1))
        # print("array canal2")
        # print(datoscanal2)
        # print("array canal3")
        # print(datoscanal3)
        # print("array canal4")
        # print(datoscanal4)
        # print("array canal5")
        # print(datoscanal5)
        # print("array canal6")
        # print(datoscanal6)
        # print("array canal7")
        # print(datoscanal7)
        # print("array canal8")
        # print(datoscanal8)

        with open(os.path.join(carpeta, "datos %d.csv"% j), 'a') as fp: # Guardar datos en el archivo csv
            for h in range(0,512):
                for i in range(0,8):
                    fp.write(str(datos[h][i])+";")
                fp.write("\n")
                fila += 1
                # for i in range(0,len(datoscanal1)):
                #     fp.write(str(datoscanal1[i])+";")
                #     fp.write(str(datoscanal2[i])+";")
                #     fp.write(str(datoscanal3[i])+";")
                #     fp.write(str(datoscanal4[i])+";")
                #     fp.write(str(datoscanal5[i])+";")
                #     fp.write(str(datoscanal6[i])+";")
                #     fp.write(str(datoscanal7[i])+";")
                #     fp.write(str(datoscanal8[i])+";")
                #     fp.write("\n")
            
    
    def Crear_carpeta(self):
        global carpeta 
        global j
        global fila
        fila = 0
        Archivo = True
        j = 1
        Tipo = "PruebaMYO"
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

