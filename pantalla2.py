from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QFormLayout, QLineEdit, QPushButton, QMessageBox, \
    QToolBar, QAction, QWidget, QGridLayout
from ayudas import Ayudas
from compras import Compras
from buscar import Buscar
from proveedores import Proveedores
from cerrarCaja import CerrarCaja
from informes import Informes
from administrar import Administrar

class Pantalla2(QMainWindow):
    def __init__(self, anterior):
        super(Pantalla2, self).__init__(anterior)
        # Poner título
        rol = Ayudas.rol
        usuario = Ayudas.usuario
        self.ventanaAnterior = anterior
        self.setWindowTitle(f"Fifre | {usuario}")
        self.setWindowIcon(QtGui.QIcon('imagenes/icono.png'))
        self.mensaje = QMessageBox()
        self.mensaje.setIcon(QMessageBox.Information)
        self.mensaje.setWindowTitle(f"Hola {usuario}")
        self.mensaje.setInformativeText("¡Inicio de sesión correcto!")
        self.mensaje.exec_()
        # Establecer el ancho y el alto
        self.ancho = Ayudas.ancho
        self.alto = Ayudas.alto
        self.resize(self.ancho, self.alto)
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)
        # Establecemos el fondo principal
        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap('imagenes/Fondo5.png')
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)

        # El tamaño de la imagen se adapta al tamaño de su contenedor
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())
        self.setCentralWidget(self.fondo)
        self.barraHerramientas = QToolBar("Barra de herramientas")
        # Establecemos el tamaño de los íconos de las opciones
        self.barraHerramientas.setIconSize(QSize(150, 150))

        # Agregamos la barra de herramientas
        self.addToolBar(self.barraHerramientas)
        self.compras = QAction(QIcon("imagenes/Compras.png"), "Registro de los productos | Facturas", self)
        self.proveedores = QAction(QIcon("imagenes/Proveedores.png"), "Ingreso de mercancía | Proveedores", self)
        '''self.cerrarCaja = QAction(QIcon("imagenes/Cerrar.png"), "Cierre de caja | Validar ventas y recepción "
                                                                "de productos", self)'''
        self.buscar = QAction(QIcon("imagenes/Buscar.png"), "Consultar el valor de los productos | Buscar", self)
        self.informes = QAction(QIcon("imagenes/perfil.png"), "Mi perfil", self)
        self.salir = QAction(QIcon("imagenes/Salir.png"), "Cerrar sesión | Salir", self)
        self.administrar = QAction(QIcon("imagenes/Administrar.png"), "Crear y modificar usuarios | Administrar", self)

        if (rol == "Administrador"):
            self.barraHerramientas.addAction(self.compras)
            self.barraHerramientas.addAction(self.buscar)
            self.barraHerramientas.addAction(self.proveedores)
            '''self.barraHerramientas.addAction(self.cerrarCaja)'''
            self.barraHerramientas.addAction(self.informes)
            self.barraHerramientas.addAction(self.administrar)
            self.barraHerramientas.addAction(self.salir)

        elif (rol == "Supervisor"):
            self.barraHerramientas.addAction(self.compras)
            self.barraHerramientas.addAction(self.buscar)
            self.barraHerramientas.addAction(self.proveedores)
            self.barraHerramientas.addAction(self.informes)
            '''self.barraHerramientas.addAction(self.cerrarCaja)'''
            self.barraHerramientas.addAction(self.salir)

        else:
            self.barraHerramientas.addAction(self.compras)
            self.barraHerramientas.addAction(self.buscar)
            self.barraHerramientas.addAction(self.informes)
            self.barraHerramientas.addAction(self.salir)

        # Activamos la barra de herramientas
        self.barraHerramientas.actionTriggered[QAction].connect(self.accionBarraHerramientas)

    def accionBarraHerramientas(self, opcion):
        # Ocultamos la ventana actual
        self.hide()
        # Validamos la opción que se pulsó
        if opcion.text() == "Cerrar sesión | Salir":
            self.hide()
            # Mostramos ventana anterior
            self.ventanaAnterior.show()

        elif opcion.text() == "Registro de los productos | Facturas":
            # Creamos una nueva ventana
            self.compras = Compras(self)
            self.hide()
            # Mostrar la ventana nueva
            self.compras.show()

        elif opcion.text() == "Consultar el valor de los productos | Buscar":
            # Creamos una nueva ventana
            self.buscar = Buscar(self)
            self.hide()
            # Mostrar la ventana nueva
            self.buscar.show()

        elif opcion.text() == "Ingreso de mercancía | Proveedores":
            # Creamos una nueva ventana
            self.proveedores = Proveedores(self)
            self.hide()
            # Mostrar la ventana nueva
            self.proveedores.show()

        elif opcion.text() == "Cierre de caja | Validar ventas y recepción de productos":
            # Creamos una nueva ventana
            self.cerrarCaja = CerrarCaja(self)
            self.hide()
            # Mostrar la ventana nueva
            self.cerrarCaja.show()

        elif opcion.text() == "Mi perfil":
            # Creamos una nueva ventana
            self.informes = Informes(self)
            self.hide()
            # Mostrar la ventana nueva
            self.informes.show()

        elif opcion.text() == "Crear y modificar usuarios | Administrar":
            # Creamos una nueva ventana
            self.administrar = Administrar(self)
            self.hide()
            # Mostrar la ventana nueva
            self.administrar.show()


