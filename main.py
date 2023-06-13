import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QDesktopWidget, QLabel, QMainWindow, QApplication, QFormLayout, \
    QLineEdit, QPushButton, QMessageBox, QCheckBox, QWidget

from ayudas import Ayudas
from pantalla2 import Pantalla2
from usuarios import Usuarios


class InicioSesion(QMainWindow):
    # Hacer el método constructor de la ventana
    def __init__(self):
        # Para que se inicie la ventana
        super().__init__()
        # Poner título
        self.setWindowTitle("Inicio sesión")
        self.setWindowIcon(QtGui.QIcon('imagenes/icono.png'))
        # Establecer el ancho y el alto
        self.ancho = 1400
        self.alto = 600
        # Líneas para encontrar el ancho y alto del monitor.
        """user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        ancho, alto = user32.GetSystemMetrics(0)-5, user32.GetSystemMetrics(1)-55"""
        self.resize(self.ancho, self.alto)
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Establecemos el fondo principal
        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap('imagenes/Fondo3.png')
        self.fondo.setPixmap(self.imagenFondo)

        # Establecer el modo para escalar la imagen (Permite que la imagen se acople al alto y ancho que la contiene)
        self.fondo.setScaledContents(True)

        # El tamaño de la imagen se adapta al tamaño de su contenedor
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())
        self.setCentralWidget(self.fondo)
        self.formulario = QFormLayout()

        # Escribimos el título
        self.lblTitulo = QLabel()
        self.lblTitulo.setText("Inicio de sesión")
        self.lblTitulo.setFont(QFont("Andale Mono", 40))
        self.lblTitulo.setAlignment(Qt.AlignLeft)
        self.lblTitulo.setStyleSheet("color:Black; padding: 50px; border-radius: 10px; margin-bottom: 50px;")

        # Label y texto del usuario
        self.lblUsuario = QLabel()
        self.lblUsuario.setText("Usuario")
        self.lblUsuario.setFont(QFont("Andale Mono", 12))
        self.lblUsuario.setStyleSheet("color:black; margin-bottom: 50px;")
        self.txtUsuario = QLineEdit()
        self.txtUsuario.setPlaceholderText("Ingrese su nombre de usuario")

        self.txtUsuario.setFixedWidth(200)

        # Label y texto de la contraseña
        self.lblContrasena = QLabel()
        self.lblContrasena.setText("Contraseña")
        self.lblContrasena.setFont(QFont("Andale Mono", 12))
        self.lblContrasena.setStyleSheet("color:black; border-radius: 10px;")
        self.txtContrasena = QLineEdit()
        self.txtContrasena.setEchoMode(QLineEdit.Password)
        self.txtContrasena.setPlaceholderText("Ingrese su contraseña")
        self.txtContrasena.setFixedWidth(200)

        self.lblEspacio = QLabel()
        self.lblEspacio.setText("")


        self.spacer = QWidget()
        self.spacer.setFixedHeight(20)  # Establecer la altura del espacio en blanco

        # Casilla ver clave
        self.checkBox = QCheckBox("Mostrar contraseña")
        self.checkBox.setStyleSheet("margin-bottom: 50px;")
        self.negrita = QFont()
        self.negrita.setBold(True)
        self.checkBox.setFont(self.negrita)


        def onStateChanged(state):
            if state == Qt.Checked:
                self.txtContrasena.setEchoMode(QLineEdit.Normal)
            else:
                self.txtContrasena.setEchoMode(QLineEdit.Password)

        # Conectar la señal de cambio de estado de la casilla de validación a la función onStateChanged
        self.checkBox.stateChanged.connect(onStateChanged)

        # Botón enviar
        self.btnEnviar = QPushButton("Iniciar sesión")
        self.btnEnviar.setFixedWidth(200)
        self.btnEnviar.setFont(QFont("Andale Mono", 14))
        self.btnEnviar.setStyleSheet("color:black;")
        self.btnEnviar.clicked.connect(self.iniciarSesion)

        # Botón salir
        self.btnSalir = QPushButton("Salir")
        self.btnSalir.setFixedWidth(200)
        self.btnSalir.setFont(QFont("Andale Mono", 14))
        self.btnSalir.setStyleSheet("color:black;")
        self.btnSalir.clicked.connect(self.salir)

        self.formulario.addRow(self.lblTitulo)
        self.formulario.addRow(self.lblUsuario, self.txtUsuario)
        self.formulario.addRow(self.lblContrasena, self.txtContrasena)
        self.formulario.addRow(self.lblEspacio, self.checkBox)
        self.formulario.addRow(self.btnEnviar, self.btnSalir)

        # Siempre poner de último
        # Establecer que la ventana va a tener una distribución de formulario

        self.fondo.setLayout(self.formulario)

    def iniciarSesion(self):
        self.mensaje = QMessageBox()
        if self.txtUsuario.text() == "" and self.txtContrasena.text() == "":
            self.mensaje.setIcon(QMessageBox.Warning)
            self.mensaje.setWindowTitle("Datos incorrectos")
            self.mensaje.setInformativeText('Por favor diligenciar todos los campos')
            self.txtUsuario.setText("")
            self.txtContrasena.setText("")
            self.mensaje.exec_()
        else:

            self.file = open('Archivos/datos.txt', 'rb')
            usuarios = []
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                lista = linea.split(";")
                # paramos el bucle si ya no encuentra más registros en el archivo
                if linea == '':
                    break
                u = Usuarios(lista[0],
                             lista[1],
                             lista[2],
                             lista[3],
                             lista[4],
                             lista[5],
                             lista[6],
                             lista[7])
                # Agregar los datos a la lista
                usuarios.append(u)
                # cerramos ael archivo txt
            self.file.close()
            existeDocumento = False
            existeClave = False
            for u in usuarios:
                if u.documento == self.txtUsuario.text():
                    existeDocumento = True
                    if u.clave == self.txtContrasena.text():
                        existeClave = True
                        Ayudas.usuario = u.nombreCompleto
                        Ayudas.rol = u.rol
                        self.pantalla2 = Pantalla2(self)
                        # Mostrar la ventana nueva
                        self.txtUsuario.setText("")
                        self.txtContrasena.setText("")
                        self.hide()
                        self.pantalla2.show()
                        break
                    break

            if not existeDocumento:
                self.mensaje.setIcon(QMessageBox.Warning)
                self.mensaje.setWindowTitle("Datos incorrectos")
                self.mensaje.setInformativeText('El usuario ingresado no se encuentra registrado')
                self.txtUsuario.setText("")
                self.txtContrasena.setText("")
                self.mensaje.exec_()

            elif not existeClave:
                self.mensaje.setIcon(QMessageBox.Warning)
                self.mensaje.setWindowTitle("Datos incorrectos")
                self.mensaje.setInformativeText('La contraseña ingresada es incorrecta')
                self.txtContrasena.setText("")
                self.mensaje.exec_()

            self.checkBox.setChecked(False)
    def salir(self):
        self.close()


if __name__ == '__main__':

    # Creamos una aplicación pyqt5
    app = QApplication(sys.argv)

    # Creamos un objeto tipo ventana1
    ventana1 = InicioSesion()
    # Indicamos que se vea la ventana
    ventana1.show()

    # Indicamos que la ventana se deje cerrar
    sys.exit(app.exec_())

