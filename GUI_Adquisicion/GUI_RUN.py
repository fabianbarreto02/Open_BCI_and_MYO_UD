import wx
from GUI_adquisicion_funcional import FrameMain

if __name__ == '__main__':
    app = wx.App()
    ventana = FrameMain(None)
    ventana.Show()
    app.MainLoop()

