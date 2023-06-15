from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea, QTableWidget, \
    QTableWidgetItem, QHBoxLayout, QFormLayout, QLineEdit, QMessageBox, QToolBar, QAction, QComboBox
from ayudas import Ayudas
from usuarios import Usuarios, Productos


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

        # Layout
        self.vertical = QVBoxLayout()
        # CONSTRUIR EL MENÚ TOOL BAR
        self.toolbar = QToolBar('Main toolbar')
        self.toolbar.setIconSize(QSize(80, 80))
        self.toolbar.setFloatable(False)
        self.addToolBar(self.toolbar)

        # Borrar Campos
        self.delete = QAction(QIcon('imagenes/limpiar.png'), '&Eliminar', self)
        self.delete.triggered.connect(self.limpiar)
        self.toolbar.addAction(self.delete)

        # Regenerar Clave
        self.regenerarC = QAction(QIcon('imagenes/regenerar.png'), '&Regenerar Clave', self)
        self.regenerarC.triggered.connect(self.regenerar)
        self.toolbar.addAction(self.regenerarC)

        # Layout horizontal
        self.horizontal = QHBoxLayout()
        # Le ponemos las márgenes
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # ---------- Layout izquierdo -----------

        # Creamos el layout del lado izquierdo
        self.ladoIzquierdo = QFormLayout()

        # ---------------- TODO EL CÓDIGO DEL LAGO IZQUIERDO INICIA EN ESTA SECCIÓN ---------------------#

        # ETIQUETAS Y LINEAS DE TEXTO
        # -----Código
        self.lblDocumento = QLabel("Documento")
        self.lblDocumento.setFont(QFont("Andale Mono", 15))
        self.lblDocumento.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font = QFont()
        self.font.setPointSize(14)
        self.txtDocumento = QLineEdit()
        self.txtDocumento.setFixedWidth(300)
        self.txtDocumento.setFont(self.font)
        self.txtDocumento.setPlaceholderText("Número documento")
        self.ladoIzquierdo.addRow(self.lblDocumento, self.txtDocumento)

        # -----Nombre
        self.lblNombre = QLabel("Nombres")
        self.lblNombre.setFont(QFont("Andale Mono", 15))
        self.lblNombre.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font.setPointSize(14)
        self.txtNombre = QLineEdit()
        self.txtNombre.setFixedWidth(300)
        self.txtNombre.setFont(self.font)
        self.txtNombre.setPlaceholderText("Nombre usuario")
        self.ladoIzquierdo.addRow(self.lblNombre, self.txtNombre)

        # -----Precio
        self.lblApellidos = QLabel("Apellidos")
        self.lblApellidos.setFont(QFont("Andale Mono", 15))
        self.lblApellidos.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font.setPointSize(14)
        self.txtApellidos = QLineEdit()
        self.txtApellidos.setFixedWidth(300)
        self.txtApellidos.setFont(self.font)
        self.txtApellidos.setPlaceholderText("Apellidos usuario")
        self.ladoIzquierdo.addRow(self.lblApellidos, self.txtApellidos)

        # -----Rol
        self.lblRol = QLabel("Rol usuario")
        self.setFont(QFont("Andale Mono", 15))
        self.lblRol.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font.setPointSize(14)
        self.lblRol.setFont(self.font)
        self.txtRol = QComboBox(self)
        self.txtRol.setFixedWidth(300)
        self.txtRol.setFont(self.font)
        self.txtRol.addItem("Cajero")
        self.txtRol.addItem("Supervisor")
        self.txtRol.addItem("Administrador")
        self.ladoIzquierdo.addRow(self.lblRol, self.txtRol)

        # ---------- Layout derecho -----------

        # Creamos el layout del lado izquierdo
        self.ladoDerecho = QFormLayout()

        # ---------------- TODO EL CÓDIGO DEL LADO DERECHO INICIA EN ESTA SECCIÓN ---------------------#

        # ETIQUETAS Y LINEAS DE TEXTO
        # -----Celular
        self.lblCel = QLabel("Celular")
        self.lblCel.setFont(QFont("Andale Mono", 15))
        self.lblCel.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font = QFont()
        self.font.setPointSize(14)
        self.txtCel = QLineEdit()
        self.txtCel.setFixedWidth(300)
        self.txtCel.setFont(self.font)
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
        self.txtDir.setPlaceholderText("Dirección usuario")
        self.ladoDerecho.addRow(self.lblDir, self.txtDir)

        # Título
        self.letreroP = QLabel()
        self.letreroP.setText("Consulta y registro de usuarios")
        self.letreroP.setFont(QFont("Andale Mono", 20))
        self.letreroP.setStyleSheet('background-color:#434343; color:#F7F7F7; padding: 30px; '
                                    'border-radius: 15px;')
        self.letreroP.setAlignment(Qt.AlignCenter)

        # ------Botón registrar
        self.btnRegistrar = QPushButton("Registrar")
        self.btnRegistrar.setFixedWidth(300)
        self.btnRegistrar.setIconSize(QSize(180, 180))
        self.btnRegistrar.setStyleSheet("background-color: #1BBC9B;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")
        self.btnRegistrar.clicked.connect(self.accionBtnRegistrar)

        # ------Botón consultar
        self.btnCosultar = QPushButton("Consultar")
        self.btnCosultar.setFixedWidth(180)
        self.btnCosultar.setIconSize(QSize(180, 180))
        self.btnCosultar.setStyleSheet("background-color: #1BBC9B;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 40px;")
        self.btnCosultar.clicked.connect(self.accionBtnCosultar)
        self.ladoIzquierdo.addRow(self.btnCosultar, self.btnRegistrar)

        # ------Botón editar
        self.btnEditar = QPushButton("Editar")
        self.btnEditar.setFixedWidth(300)
        self.btnEditar.setIconSize(QSize(180, 180))
        self.btnEditar.setStyleSheet("background-color: #1BBC9B;"
                                     "color: #FFFFFF;"
                                     "padding: 10px;"
                                     "margin-top: 40px;")
        self.btnEditar.clicked.connect(self.accionBtnEditar)

        # ------Botón eliminar
        self.btnEliminar = QPushButton("Eliminar")
        self.btnEliminar.setFixedWidth(180)
        self.btnEliminar.setIconSize(QSize(180, 180))
        self.btnEliminar.setStyleSheet("background-color: #1BBC9B;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 40px;")
        self.btnEliminar.clicked.connect(self.accionBtnEliminar)
        self.ladoDerecho.addRow(self.btnEliminar, self.btnEditar)



        # Agregamos el letrero en la línea siguiente:
        self.vertical.addWidget(self.letreroP)
        self.vertical.addStretch()
        self.horizontal.addLayout(self.ladoIzquierdo)
        self.horizontal.addLayout(self.ladoDerecho)
        self.vertical.addLayout(self.horizontal)

        # --------- TODO EL CÓDIGO ENCIMA BOTÓN REGRESAR ----------------
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

    def accionBtnRegistrar(self):
        if (self.txtDocumento.text() == ''
                or self.txtNombre.text() == ''
                or self.txtApellidos.text() == ''
                or self.txtRol.currentText() == ''
                or self.txtCel.text() == ''
                or self.txtCorreo.text() == ''
                or self.txtDir.text() == ''):

            return QMessageBox.warning(self, 'Cuidado',
                                       f"Por favor diligenciar\ntodos los campos")
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
                              lista[7],)

                # Agregar los datos a la lista
                usuarios.append(u)
                # cerramos ael archivo txt
            self.file.close()
            existeCodigo = False
            self.total = 0
            for u in usuarios:
                if u.documento == self.txtDocumento.text():
                    existeCodigo = True
                    self.txtDocumento.setText(u.documento)
                    self.txtNombre.setText(u.nombreCompleto)
                    self.txtApellidos.setText(u.apellidos)
                    self.txtRol.setCurrentText(u.rol)
                    self.txtCel.setText(u.telefono)
                    self.txtCorreo.setText(u.correo)
                    self.txtDir.setText(u.direccion)
                    return QMessageBox.warning(self, 'Cuidado',
                                               "El usuario que intenta registrar\n"
                                               "ya existe, a continuación se\n"
                                               "cargarán los datos registrados")

            if not existeCodigo:
                self.file = open('Archivos/datos.txt', 'ab')
                self.file.write(bytes(
                    self.txtDocumento.text() + ";"
                    + "123456" + ";"
                    + self.txtRol.currentText() + ";"
                    + self.txtNombre.text() + ";"
                    + self.txtApellidos.text() + ";"
                    + self.txtCorreo.text() + ";"
                    + self.txtDir.text() + ";"
                    + self.txtCel.text() + "\n", encoding='UTF-8'))
                self.file.close()
                self.limpiar()
                return QMessageBox.information(self, 'Cuidado',
                                               "El usuario se registró correctamente")

    def accionBtnCosultar(self):
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
        existeCodigo = False
        self.total = 0
        for u in usuarios:
            if u.documento == self.txtDocumento.text():
                existeCodigo = True
                self.txtDocumento.setText(u.documento)
                self.txtDocumento.setReadOnly(True)
                self.txtNombre.setText(u.nombreCompleto)
                self.txtApellidos.setText(u.apellidos)
                self.txtRol.setCurrentText(u.rol)
                self.txtCel.setText(u.telefono)
                self.txtCorreo.setText(u.correo)
                self.txtDir.setText(u.direccion)
        if not existeCodigo:
            self.limpiar()
            return QMessageBox.warning(self, 'Cuidado', 'El usuario que intenta buscar\n nose encuentra registrado')

    def accionBtnEditar(self):
        if (self.txtDocumento.text() == ''
                or self.txtNombre.text() == ''
                or self.txtApellidos.text() == ''
                or self.txtRol.currentText() == ''
                or self.txtCel.text() == ''
                or self.txtCorreo.text() == ''
                or self.txtDir.text() == ''):
            return QMessageBox.warning(self, 'Cuidado', 'Para realizar la edición '
                                                        'todos los\ncampos deben estar diligenciados')
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
            existeCodigo = False
            if self.boton == QMessageBox.StandardButton.Yes:
                for u in usuarios:
                    if u.documento == self.txtDocumento.text():
                        existeCodigo = True
                        u.nombreCompleto = self.txtNombre.text()
                        u.apellidos = self.txtApellidos.text()
                        u.rol = self.txtRol.currentText()
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
                    self.limpiar()
                    self.txtDocumento.setReadOnly(False)
                    return QMessageBox.question(
                                self,
                                'Confirmación',
                                'El usuarios se editó correctamente',
                                QMessageBox.StandardButton.Ok)
                else:
                    self.limpiar()
                    self.txtCodigo.setReadOnly(False)
                    self.txtNombre.setReadOnly(False)
                    return QMessageBox.warning(
                        self,
                        'Confirmación',
                        'El usuario que intenta editar no se encuentra registrado',
                        QMessageBox.StandardButton.Ok)

    def accionBtnEliminar(self):
        if (self.txtDocumento.text() == ''
                or self.txtNombre.text() == ''
                or self.txtApellidos.text() == ''
                or self.txtRol.currentText() == ''
                or self.txtCel.text() == ''
                or self.txtCorreo.text() == ''
                or self.txtDir.text() == ''):
            return QMessageBox.warning(self, 'Cuidado', 'Por favor seleccionar un documento válido\n'
                                                        ' se recomienda primero buscar con el código')
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
                'Esta seguro que desea eliminar este usuario',
                QMessageBox.StandardButton.Yes |
                QMessageBox.StandardButton.No)
            existeCodigo = False
            if self.boton == QMessageBox.StandardButton.Yes:
                for u in usuarios:
                    if u.documento == self.txtDocumento.text():
                        existeCodigo = True
                        usuarios.remove(u)
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
                    self.limpiar()
                    self.txtDocumento.setReadOnly(False)
                    return QMessageBox.question(
                        self,
                        'Confirmación',
                        'El usuario se editó correctamente',
                        QMessageBox.StandardButton.Ok)
                else:
                    self.limpiar()
                    self.txtCodigo.setReadOnly(False)
                    self.txtNombre.setReadOnly(False)
                    return QMessageBox.warning(
                        self,
                        'Confirmación',
                        'El usuario que intenta editar no se encuentra registrado',
                        QMessageBox.StandardButton.Ok)

    def limpiar(self):
        self.txtDocumento.setText('')
        self.txtNombre.setText('')
        self.txtApellidos.setText('')
        self.txtRol.setCurrentIndex(0)
        self.txtCel.setText('')
        self.txtCorreo.setText('')
        self.txtDir.setText('')
        self.txtDocumento.setReadOnly(False)

    def regenerar(self):
        self.accionBtnCosultar()
        if self.txtDocumento.text() == '':
            return QMessageBox.warning(self, 'Cuidado', 'Para realizar la regeneración '
                                                        'debe\ndiligenciar el documento')
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
                '¿Esta seguro que desea regenerar la clave?',
                QMessageBox.StandardButton.Yes |
                QMessageBox.StandardButton.No)
            existeCodigo = False
            if self.boton == QMessageBox.StandardButton.Yes:
                for u in usuarios:
                    if u.documento == self.txtDocumento.text():
                        existeCodigo = True
                        u.clave = "123456"
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
                    self.limpiar()
                    self.txtDocumento.setReadOnly(False)
                    return QMessageBox.question(
                        self,
                        'Confirmación',
                        'Se regeneró la clave correctamente',
                        QMessageBox.StandardButton.Ok)
                else:
                    self.limpiar()
                    self.txtCodigo.setReadOnly(False)
                    self.txtNombre.setReadOnly(False)
                    return QMessageBox.warning(
                        self,
                        'Confirmación',
                        'No se encuentra registrado ningún usuario con el documento proporcionado',
                        QMessageBox.StandardButton.Ok)
