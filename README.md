


<a href="https://laserud.co/"><img src="https://github.com/fabianbarreto02/Open_BCI_and_MYO_UD/blob/master/GUI_Qt/LOGOLASER.jpg" title="Laser" alt="Laser"></a>



# Proyecto de investigación Open BCI y MYO Armband 

Repositorio de proyecto de investigación del grupo de investigación LASER Universidad Distrital Francisco Jose de Caldas, donde se estudia las señales EMG y EEG para la caracterización de gestos del miembro superior capturadas con herramienta UltrCortex OPENBCI y MYO Arbmand

> Herramientas utilizadas en el proyecto

Para el desarrollo del proyecto de investigación se utilizaron las herramientas de captura de señales bioelécticas EMG y EEG, las herramientas MYO Armband(EMG) y el UltraCortex(EEG), para mas información revisar la siguiente documentación:
- [MYO ArmBand](https://support.getmyo.com/hc/en-us)
- [UltraCortex OpenBCI](https://openbci.com/)

> Screenshot Datos paciente

![Recordit GIF](https://github.com/fabianbarreto02/Open_BCI_and_MYO_UD/blob/master/Data_Readme/Front_datos.jpeg)

> Screenshot Captura señal paciente

![Recordit GIF](https://github.com/fabianbarreto02/Open_BCI_and_MYO_UD/blob/master/Data_Readme/Front_captura.jpeg)

## Tabla de contenido


- [Installation](#installation)
- [Contributing](#contributing)
- [Team](#team)
- [Support](#support)
- [License](#license)



---

## Installation

### Pre-requirements

Para poder corre el FrontEnd de captura de las señales EMG y EEG su equipo debe contar con los siguientes requerimientos:

- [Python 3](https://www.python.org/download/releases/3.0/)

Dependencias adicionales(se sugiere usar el gestor de paquete PIP):

- [MYO -Python](https://pypi.org/project/myo-python/) 
- [Open BCI](https://pypi.org/project/openbci/)
- [Pyqtgraph](https://pypi.org/project/pyqtgraph/)
- [Plotly](https://pypi.org/project/plotly/)
- [Plotly express](https://pypi.org/project/plotly-express/)
- [Play sound](https://pypi.org/project/playsound/)


### Clone

- Clone este repositorio en su máquina local usando `https://github.com/fabianbarreto02/Open_BCI_and_MYO_UD.git`


<p align="center"><img src="https://github.com/fabianbarreto02/Open_BCI_and_MYO_UD/blob/master/Data_Readme/Clone.gif" title="Clone del Repositorio" alt="Clone del Repositorio"></p>


### Setup

#### Configuración de herramienta (Myo Armband y UltraCortex)


> Variables de entorno MYO

> Para el correcto funcionamiento de la herramienta MYO se debe descargar el SDK del dispositivo y crear dos variable de entorno, una varible de usuario y una variable del sistema en los sistemas operativos windows, observar el siguiente gif para mayor infomación:

<p align="center"><img src="https://github.com/fabianbarreto02/Open_BCI_and_MYO_UD/blob/master/Data_Readme/Variable_myo.gif" title="Variables MYO" alt="Variables MYO"></p>


> Puerto UltraCortex

> Para el correcto funcionamiento de la herramienta UltraCortex se debe configurar el puerto del dispositivo en los sistemas operativos windows, observar el siguiente gif para mayor infomación:

<p align="center"><img src="https://github.com/fabianbarreto02/Open_BCI_and_MYO_UD/blob/master/Data_Readme/Puerto_ultracortex.gif" title="Puerto UltraCortex" alt="Puerto UltraCortex"></p>

> Iniciar MYO Connect

> Finalmente se debe iniciar el aplicativo Myo Connect para que la libreria adquiera los datos EMG por medio del SDK, observar el siguiente gif para mayor infomación:

<p align="center"><img src="https://github.com/fabianbarreto02/Open_BCI_and_MYO_UD/blob/master/Data_Readme/Myo_conect.gif" title="MYO Connect" alt="MYO Connect"></p>

### Correr  el aplicativo

> Para correr el aplicativo con python 3 debe ingresar al directorio **../../Open_BCI_and_MYO_UD/GUI_Qt** y ejecutar el script **GUI_QT.py**, observar el siguiente gif para mayor infomación:

<p align="center"><img src="https://github.com/fabianbarreto02/Open_BCI_and_MYO_UD/blob/master/Data_Readme/Arranque_frame.gif" title="Correr  el aplicativo" alt="Correr  el aplicativo"></p>


### Prueba de escritorio del aplicativo

> Se realiza una prueba de escritorio del proyecto para mostrar el resultado final del aplicativo, observar el siguiente gif para mayor infomación:

<p align="center"><img src="https://github.com/fabianbarreto02/Open_BCI_and_MYO_UD/blob/master/Data_Readme/Funcionamiento_frame.gif" title="Prueba de escritorio del aplicativo" alt="Prueba de escritorio del aplicativo"></p>



---



## Contributing


### Step 1

- **Opción 1**
    - 🍴 Realizar un Folk de este repo!

- **Opción 2**
    - 👯 Clone este repositorio en su maquina local usando:  `https://github.com/fabianbarreto02/Open_BCI_and_MYO_UD.git`


---

## Team

<center>

| <a href="https://github.com/fabianbarreto02" target="_blank">**Fabian Barreto**</a> | <a href="https://github.com/cperdomo" target="_blank">**Cesar Perdomo**</a> | <a href="https://github.com/CristianDavidSanchez" target="_blank">**Cristian Sanchez**</a> | <a href="https://github.com/NRDaza" target="_blank">**Nicolas Daza**</a> |
| :---: |:---:| :---:| :---:|
| [![Fabian](https://avatars3.githubusercontent.com/u/43799065?s=200&u=4f2296f15ee5517409891d91a2e774b9c1a183fa&v=4)](https://github.com/fabianbarreto02)   | [![Cesar](https://avatars.githubusercontent.com/u/17862195?v=4)](https://github.com/cperdomo)    | [![Cristian](https://avatars2.githubusercontent.com/u/45292213?s=200&u=f4851b78acbb0db7c5ba203982dfe71d2f1b785e&v=4)](https://github.com/CristianDavidSanchez) | [![Nicolas](https://avatars2.githubusercontent.com/u/34488581?s=200&u=f02bdb311d05b487e40fbe8dc712024596af956a&v=4)](https://github.com/NRDaza)  |
| <a href="https://github.com/fabianbarreto02" target="_blank">`github.com/fabianbarreto02`</a>| <a href="https://github.com/cperdom" target="_blank">`github.com/cperdom`</a> | <a href="https://github.com/CristianDavidSanchez" target="_blank">`github.com/CristianDavidSanchez`</a> | <a href="https://github.com/NRDaza" target="_blank">`github.com/NRDaza`</a> |

</center>

---


## Support

¡Ponte en contacto con nosotros en uno de los siguientes canales!

- Website en <a href="https://laserud.co/#contact" target="_blank">`laserud.co`</a>


---


## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © <a href="https://laserud.co/" target="_blank">Grupo de investigación LASER Universidad Distrital Francisco Jose de Caldas</a>.