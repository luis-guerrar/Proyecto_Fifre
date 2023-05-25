from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea, QTableWidget, \
    QTableWidgetItem, QHBoxLayout, QFormLayout, QLineEdit
from ayudas import Ayudas
from usuarios import Usuarios


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
        self.titulo1 = QLabel()
        self.titulo1.setText("En esta pantalla el administrador podrá agregar borrar y editar los perfiles de usuario")
        # Para centrar el letrero
        self.titulo1.setAlignment(Qt.AlignCenter)
        self.titulo1.setStyleSheet('background-color:#434343; color:#F7F7F7; padding: 30px;')
        self.titulo1.setFont(QFont("Andale Mono", 12))
        # para poner el letrero arriba
        self.vertical.addWidget(self.titulo1)

        self.vertical.addStretch()

        # -------- AGREGAR EL CRUD ------------------
        self.file = open('Archivos/datos.txt', 'rb')
        self.usuarios = []
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
            self.usuarios.append(u)
            # cerramos ael archivo txt
        self.file.close()
        self.numeroUsuarios = len(self.usuarios)
        self.contador = 0
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        # Creamos la tabla
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(7)
        # Definimos el ancho de las columnas
        self.tabla.setColumnWidth(0, 200)
        self.tabla.setColumnWidth(1, 200)
        self.tabla.setColumnWidth(2, 200)
        self.tabla.setColumnWidth(3, 200)
        self.tabla.setColumnWidth(4, 200)
        self.tabla.setColumnWidth(5, 200)
        self.tabla.setColumnWidth(6, 200)
        # Definimos los encabezados de la tabla
        self.tabla.setHorizontalHeaderLabels(["Documento", "Nombre Completo", "Apellidos",
                                              "Rol", "Correo", "Dirección", "Teléfono"])

        self.tabla.setRowCount(self.numeroUsuarios)
        for u in self.usuarios:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(u.documento))
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.nombreCompleto))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.apellidos))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.rol))
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.correo))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.direccion))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.telefono))
            # Aumentamos el contador
            self.contador += 1

            self.scrollArea.setWidget(self.tabla)
            self.vertical.addWidget(self.scrollArea)
            self.vertical.addStretch()

        # ---------- SE CONSTRUYE EL LAYOUT HORIZONTAL ---------------
        self.horizontal = QHBoxLayout()

        # -------------- Lado izquierdo ------------------------------
        self.ladoIzquierdo = QFormLayout()

        self.lblDocumento = QLabel("Documento")
        self.lblDocumento.setFont(QFont("Andale Mono", 14))
        self.lblDocumento.setStyleSheet("color:black;")
        self.txtDocumento = QLineEdit()
        self.txtDocumento.setFixedWidth(320)
        self.ladoIzquierdo.addRow(self.lblDocumento, self.txtDocumento)

        self.lblRol = QLabel("Rol")
        self.lblRol.setFont(QFont("Andale Mono", 14))
        self.lblRol.setStyleSheet("color:Black;")
        self.txtRol = QLineEdit()
        self.txtRol.setFixedWidth(320)
        self.ladoIzquierdo.addRow(self.lblRol, self.txtRol)

        self.lblNombres = QLabel("Nombres")
        self.lblNombres.setFont(QFont("Andale Mono", 14))
        self.lblNombres.setStyleSheet("color:black;")
        self.txtNombres = QLineEdit()
        self.txtNombres.setFixedWidth(320)
        self.ladoIzquierdo.addRow(self.lblNombres, self.txtNombres)

        self.lblApellidos = QLabel("Apellidos")
        self.lblApellidos.setFont(QFont("Andale Mono", 14))
        self.lblApellidos.setStyleSheet("color:black;")
        self.txtApellidos = QLineEdit()
        self.txtApellidos.setFixedWidth(320)
        self.ladoIzquierdo.addRow(self.lblApellidos, self.txtApellidos)
        self.horizontal.addLayout(self.ladoIzquierdo)

        self.lyCentro = QFormLayout()

        self.lblCorreo = QLabel("Correo")
        self.lblCorreo.setFont(QFont("Andale Mono", 14))
        self.lblCorreo.setStyleSheet("color:black;")
        self.txtCorreo = QLineEdit()
        self.txtCorreo.setFixedWidth(320)
        self.lyCentro.addRow(self.lblCorreo, self.txtCorreo)


        self.lblDireccion = QLabel("Dirección")
        self.lblDireccion.setFont(QFont("Andale Mono", 14))
        self.lblDireccion.setStyleSheet("color:black;")
        self.txtDireccion = QLineEdit()
        self.txtDireccion.setFixedWidth(320)
        self.lyCentro.addRow(self.lblDireccion, self.txtDireccion)

        self.lblTelefono = QLabel("Teléfono")
        self.lblTelefono.setFont(QFont("Andale Mono", 14))
        self.lblTelefono.setStyleSheet("color:black; margin-bottom: 45px;")
        self.txtTelefono = QLineEdit()
        self.txtTelefono.setFixedWidth(320)
        self.lyCentro.addRow(self.lblTelefono, self.txtTelefono)
        self.horizontal.addLayout(self.lyCentro)



        # -------------- Lado Derecho ------------------------------
        self.ladoDerecho = QFormLayout()

        self.lblTitulo = QLabel()
        self.lblTitulo.setText("Opciones de\n   Usuario")
        self.lblTitulo.setFont(QFont("Andale Mono", 20))
        self.lblTitulo.setAlignment(Qt.AlignLeft)
        self.lblTitulo.setStyleSheet("color:Black;")
        self.ladoDerecho.addRow(self.lblTitulo)

        self.btnAgregar = QPushButton("Agregar")
        self.btnAgregar.setFixedWidth(186)
        self.btnAgregar.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;")

        self.btnAgregar.clicked.connect(self.accionBtnAgregar)
        self.ladoDerecho.addWidget(self.btnAgregar)

        self.btnEditar = QPushButton("Editar")
        self.btnEditar.setFixedWidth(186)
        self.btnEditar.setStyleSheet("background-color: #008B45;"
                                     "color: #FFFFFF;"
                                     "padding: 10px;")

        self.btnEditar.clicked.connect(self.accionBtnEditar)
        self.ladoDerecho.addWidget(self.btnEditar)

        self.btnEliminar = QPushButton("Eliminar")
        self.btnEliminar.setFixedWidth(186)
        self.btnEliminar.setStyleSheet("background-color: #008B45;"
                                     "color: #FFFFFF;"
                                     "padding: 10px;")

        self.btnEliminar.clicked.connect(self.accionBtnEliminar)
        self.ladoDerecho.addWidget(self.btnEliminar)








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

    def accionBtnAgregar(self):
        pass

    def accionBotonRegresar(self):
        # Ocultamos la ventana actual
        self.hide()
        # Mostramos la ventana anterior
        self.ventanaMenu.show()

    def accionBtnEditar(self):
        pass

    def accionBtnEliminar(self):
        pass