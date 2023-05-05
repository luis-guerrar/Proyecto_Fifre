from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QLabel, QPushButton
from ayudas import Ayudas

class Administrar(QMainWindow):

    def __init__(self, anterior):
        super(Administrar, self).__init__(anterior)
        self.ventanaMenu = anterior
        # Poner título
        rol = Ayudas.rol
        usuario = Ayudas.usuario
        self.setWindowTitle(f"Fifre | {usuario}")
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
        self.imagenFondo = QPixmap('imagenes/Fondo4.png')
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        # El tamaño de la imagen se adapta al tamaño de su contenedor
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())
        self.setCentralWidget(self.fondo)

        # Diferencial
        self.vertical = QVBoxLayout()
        self.titulo1 = QLabel()
        self.titulo1.setText("En esta pantalla el administrador podrá agregar borrar y editar los perfiles de usuario")
        # Para centrar el letrero
        self.titulo1.setAlignment(Qt.AlignCenter)
        self.titulo1.setStyleSheet('background-color:#434343; color:#F7F7F7; padding: 30px;')
        self.titulo1.setFont(QFont("Andale Mono", 12))
        # para poner el letrero arriba
        self.vertical.addWidget(self.titulo1)
        self.fondo.setLayout(self.vertical)

        self.vertical.addStretch()

        # Hacemos un botón para regresar a la ventana1
        self.botonRegresar = QPushButton("Regresar")
        # Establecemos el ancho del botón
        self.botonRegresar.setFixedWidth(150)
        self.botonRegresar.setFont(QFont("Andale Mono", 12))
        # Le ponemos al botón color de: fondo, texto y márgenes
        self.botonRegresar.setStyleSheet('background-color:#434343; color:#F7F7F7; padding: 20px;')
        self.vertical.addWidget(self.botonRegresar)
        self.botonRegresar.clicked.connect(self.accionBotonRegresar)

        # Hacemos el método para volver

    def accionBotonRegresar(self):
        # Ocultamos la ventana actual
        self.hide()
        # Mostramos la ventana anterior
        self.ventanaMenu.show()