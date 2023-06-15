from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QLabel, QPushButton, QFormLayout, \
    QLineEdit, QHBoxLayout, QMessageBox, QDialog
from ayudas import Ayudas
from usuarios import Usuarios


class Informes(QMainWindow):

    def __init__(self, anterior):
        super(Informes, self).__init__(anterior)
        self.ventanaMenu = anterior
        # Poner título
        rol = Ayudas.rol
        usuario = Ayudas.usuario
        self.setWindowTitle(f"Fifre | {usuario}")
        self.setWindowIcon(QtGui.QIcon('imagenes/icono.png'))
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




        self.vertical = QVBoxLayout()

        # Layout horizontal
        self.horizontal = QHBoxLayout()
        # Le ponemos las márgenes
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # ---------- Layout izquierdo -----------

        # Creamos el layout del lado izquierdo
        self.ladoIzquierdo = QFormLayout()

        # ---------------- TODO EL CÓDIGO DEL LAGO IZQUIERDO INICIA EN ESTA SECCIÓN ---------------------#

        # ETIQUETAS Y LINEAS DE TEXTO
        # -----Documento
        self.lblDocumento = QLabel("Documento")
        self.lblDocumento.setFont(QFont("Andale Mono", 15))
        self.lblDocumento.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font = QFont()
        self.font.setPointSize(14)
        self.txtDocumento = QLineEdit()
        self.txtDocumento.setFixedWidth(300)
        self.txtDocumento.setFont(self.font)
        self.txtDocumento.setText(Ayudas.documento)
        self.txtDocumento.setReadOnly(True)
        self.ladoIzquierdo.addRow(self.lblDocumento, self.txtDocumento)

        # -----Nombre
        self.lblNombre = QLabel("Nombres")
        self.lblNombre.setFont(QFont("Andale Mono", 15))
        self.lblNombre.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font.setPointSize(14)
        self.txtNombre = QLineEdit()
        self.txtNombre.setFixedWidth(300)
        self.txtNombre.setFont(self.font)
        self.txtNombre.setText(Ayudas.usuario)
        self.txtNombre.setPlaceholderText("Nombre usuario")
        self.ladoIzquierdo.addRow(self.lblNombre, self.txtNombre)

        # -----Apellidos
        self.lblApellidos = QLabel("Apellidos")
        self.lblApellidos.setFont(QFont("Andale Mono", 15))
        self.lblApellidos.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font.setPointSize(14)
        self.txtApellidos = QLineEdit()
        self.txtApellidos.setFixedWidth(300)
        self.txtApellidos.setFont(self.font)
        self.txtApellidos.setText(Ayudas.apellido)
        self.txtApellidos.setPlaceholderText("Apellidos usuario")
        self.ladoIzquierdo.addRow(self.lblApellidos, self.txtApellidos)

        # -----Rol
        self.lblRol = QLabel("Rol")
        self.lblRol.setFont(QFont("Andale Mono", 15))
        self.lblRol.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font.setPointSize(14)
        self.txtRol = QLineEdit()
        self.txtRol.setFixedWidth(300)
        self.txtRol.setFont(self.font)
        self.txtRol.setText(Ayudas.rol)
        self.txtRol.setReadOnly(True)
        self.ladoIzquierdo.addRow(self.lblRol, self.txtRol)

        # ---------- Layout derecho -----------

        # Creamos el layout del lado izquierdo
        self.ladoDerecho = QFormLayout()

        # ---------------- TODO EL CÓDIGO DEL LADO DERECHO INICIA EN ESTA SECCIÓN ---------------------#

        # ETIQUETAS Y LINEAS DE TEXTO
        # -----Celular
        self.lblClave = QLabel("Clave")
        self.lblClave.setFont(QFont("Andale Mono", 15))
        self.lblClave.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font = QFont()
        self.font.setPointSize(14)
        self.txtClave = QLineEdit()
        self.txtClave.setFixedWidth(300)
        self.txtClave.setFont(self.font)
        self.txtClave.setPlaceholderText("Ingresar la clave")
        self.txtClave.setEchoMode(QLineEdit.Password)
        self.ladoDerecho.addRow(self.lblClave, self.txtClave)

        # -----Celular
        self.lblCel = QLabel("Celular")
        self.lblCel.setFont(QFont("Andale Mono", 15))
        self.lblCel.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font = QFont()
        self.font.setPointSize(14)
        self.txtCel = QLineEdit()
        self.txtCel.setFixedWidth(300)
        self.txtCel.setFont(self.font)
        self.txtCel.setText(Ayudas.celular)
        self.txtCel.setPlaceholderText("Número celular usuario")
        self.ladoDerecho.addRow(self.lblCel, self.txtCel)

        # -----Correo
        self.lblCorreo = QLabel("Correo")
        self.lblCorreo.setFont(QFont("Andale Mono", 15))
        self.lblCorreo.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font.setPointSize(14)
        self.txtCorreo = QLineEdit()
        self.txtCorreo.setFixedWidth(300)
        self.txtCorreo.setFont(self.font)
        self.txtCorreo.setText(Ayudas.correo)
        self.txtCorreo.setPlaceholderText("Correo usuario")
        self.ladoDerecho.addRow(self.lblCorreo, self.txtCorreo)

        # -----Dirección
        self.lblDir = QLabel("Dirección")
        self.lblDir.setFont(QFont("Andale Mono", 15))
        self.lblDir.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font.setPointSize(14)
        self.txtDir = QLineEdit()
        self.txtDir.setFixedWidth(300)
        self.txtDir.setFont(self.font)
        self.txtDir.setText(Ayudas.dirreccion)
        self.txtDir.setPlaceholderText("Dirección usuario")
        self.ladoDerecho.addRow(self.lblDir, self.txtDir)

        # Título
        self.letreroP = QLabel()
        self.letreroP.setText(f"¡Hola {Ayudas.usuario}! En esta sección podrás ver y modificar tu perfil \U0001F600")
        self.letreroP.setFont(QFont("Andale Mono", 20))
        self.letreroP.setStyleSheet('background-color:#434343; color:#F7F7F7; padding: 30px; '
                                    'border-radius: 15px;')
        self.letreroP.setAlignment(Qt.AlignCenter)

        # ------Botón registrar
        self.btnActualizar = QPushButton("Actualizar")
        self.btnActualizar.setFixedWidth(300)
        self.btnActualizar.setIconSize(QSize(180, 180))
        self.btnActualizar.setStyleSheet("background-color: #1BBC9B;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")
        self.btnActualizar.clicked.connect(self.accionBtnActualizar)

        # Agregamos el letrero en la línea siguiente:
        self.vertical.addWidget(self.letreroP)
        self.vertical.addStretch()
        self.horizontal.addLayout(self.ladoIzquierdo)
        self.horizontal.addLayout(self.ladoDerecho)
        self.horizontal.addWidget(self.btnActualizar)
        self.vertical.addLayout(self.horizontal)


        # --------- TODO EL CÓDIGO ENCIMA BOTÓN REGRESAR ----------------
        # Hacemos un botón para regresar a la ventana1
        self.botonRegresar = QPushButton(self)
        # Establecemos el ancho del botón
        self.botonRegresar.setIcon(QIcon('imagenes/Imagen4.png'))
        self.botonRegresar.setFixedWidth(180)
        self.botonRegresar.setIconSize(QSize(180, 180))
        self.botonRegresar.setStyleSheet('background-color:transparent;')
        self.vertical.addWidget(self.botonRegresar)
        self.botonRegresar.clicked.connect(self.accionBotonRegresar)

        # ------------ PONER AL FINAL -----------------

        self.fondo.setLayout(self.vertical)
        # Hacemos el método para volver

    def accionBotonRegresar(self):
        # Ocultamos la ventana actual
        self.hide()
        # Mostramos la ventana anterior
        self.ventanaMenu.show()

    def accionBtnActualizar(self):
        if (self.txtDocumento.text() == ''
                or self.txtClave.text() == ''
                or self.txtNombre.text() == ''
                or self.txtApellidos.text() == ''
                or self.txtRol.text() == ''
                or self.txtCel.text() == ''
                or self.txtCorreo.text() == ''
                or self.txtDir.text() == ''):
            return QMessageBox.warning(self, 'Cuidado', 'Para modificar debe diligenciar todos los campos')
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
                             lista[7], )

                # Agregar los datos a la lista
                usuarios.append(u)
                # cerramos ael archivo txt
            self.file.close()
            self.boton = QMessageBox.question(
                self,
                'Confirmación',
                'Esta seguro que desea editar este usuario',
                QMessageBox.StandardButton.Yes |
                QMessageBox.StandardButton.No)
            if self.boton == QMessageBox.StandardButton.Yes:
                self.dialogo = QDialog(self)
                self.dialogo.setWindowTitle("Se requiere clave administrador")
                self.dialogo.setGeometry(900, 500, 200, 100)
                self.layout = QVBoxLayout()
                self.boton1 = QPushButton("Enviar")
                self.boton1.setStyleSheet('background-color:#1D9A08;')
                self.boton1.setFixedWidth(300)
                self.txtClave2 = QLineEdit()
                self.txtClave2.setFixedWidth(300)
                self.txtClave2.setEchoMode(QLineEdit.Password)
                self.layout.addWidget(self.txtClave2)
                self.lblMensaje = QLabel("Confirme la clave ingresada")
                self.lblMensaje.setFont(QFont("Andale Mono", 12))
                self.layout.addWidget(self.lblMensaje)

                self.boton1.clicked.connect(self.accion_boton1)
                self.layout.addWidget(self.boton1)
                self.dialogo.setLayout(self.layout)
                self.dialogo.exec_()

                if self.txtClave2.text() != self.txtClave.text():
                    return QMessageBox.warning(self, 'Cuidado', 'Las claves no coinciden')
                else:
                    for u in usuarios:
                        if u.documento == self.txtDocumento.text():
                            existeCodigo = True
                            u.clave = self.txtClave.text()
                            u.nombreCompleto = self.txtNombre.text()
                            u.apellidos = self.txtApellidos.text()
                            u.telefono = self.txtCel.text()
                            u.correo = self.txtCorreo.text()
                            u.direccion = self.txtDir.text()
                            break

                    # Ingresar los datos con el registro editado
                    if existeCodigo:
                        self.file = open('Archivos/datos.txt', 'wb')
                        for u in usuarios:
                            self.file.write(bytes(u.documento + ";"
                                                  + u.clave + ";"
                                                  + u.rol + ";"
                                                  + u.nombreCompleto + ";"
                                                  + u.apellidos + ";"
                                                  + u.correo + ";"
                                                  + u.direccion + ";"
                                                  + u.telefono, encoding='UTF-8'))
                        self.file.close()
                        return QMessageBox.question(
                            self,
                            'Confirmación',
                            'El usuarios se editó correctamente',
                            QMessageBox.StandardButton.Ok)




    def accion_boton1(self):
        self.dialogo.close()
