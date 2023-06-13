import datetime
import locale

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QVBoxLayout, QLabel, QPushButton, \
    QScrollArea, QTableWidget, QAction, QToolBar, QHBoxLayout, QFormLayout, QLineEdit, QTableWidgetItem, QMessageBox, \
    QDialogButtonBox, QDialog

from ayudas import Ayudas
from usuarios import Productos, Usuarios


class Compras(QMainWindow):

    def __init__(self, anterior):
        super(Compras, self).__init__(anterior)
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

        # Diferencial
        self.vertical = QVBoxLayout()
        self.titulo1 = QLabel()
        self.titulo1.setText("Registrar los productos")
        # Para centrar el letrero
        self.titulo1.setAlignment(Qt.AlignCenter)
        self.titulo1.setStyleSheet('background-color:#434343; color:#F7F7F7; padding: 30px; border-radius: 15px;')
        self.titulo1.setFont(QFont("Andale Mono", 12))
        # para poner el letrero arriba
        self.vertical.addWidget(self.titulo1)
        self.fondo.setLayout(self.vertical)

        # CONSTRUIR EL MENÚ TOOL BAR
        self.toolbar = QToolBar('Main toolbar')
        self.toolbar.setIconSize(QSize(40, 40))
        self.addToolBar(self.toolbar)

        # Eliminar
        self.delete = QAction(QIcon('imagenes/delete.png'), '&Eliminar', self)
        self.delete.triggered.connect(self.accionDelete)
        self.toolbar.addAction(self.delete)

        # Agregar
        self.add = QAction(QIcon('imagenes/add.png'), '&Add', self)
        self.add.triggered.connect(self.accionAdd)
        self.toolbar.addAction(self.add)

        # Editar
        self.edit = QAction(QIcon('imagenes/edit.png'), '&Nuevo Cliente', self)
        self.edit.triggered.connect(self.accionEdit)
        self.toolbar.addAction(self.edit)
        # FIN TOOLBAR
        # FIN TOOLBAR

        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet("background-color:transparent;")
        self.scrollArea.setWidgetResizable(True)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(6)
        # Definimos el ancho de las columnas
        self.tabla.setColumnWidth(0, 180)
        self.tabla.setColumnWidth(1, 300)
        self.tabla.setColumnWidth(2, 600)
        self.tabla.setColumnWidth(3, 300)
        self.tabla.setColumnWidth(4, 200)
        self.tabla.setColumnWidth(5, 300)
        self.tabla.setHorizontalHeaderLabels(["Código",
                                              "Producto",
                                              "Descripción",
                                              "Precio unitario",
                                              "Cantidad",
                                              "Total"])
        self.scrollArea.setWidget(self.tabla)
        self.vertical.addWidget(self.scrollArea)
        self.horizontal = QHBoxLayout()
        self.formulario = QFormLayout()
        self.lblCodigo = QLabel("Código")
        self.lblCodigo.setFont(QFont("Andale Mono", 15))
        self.txtCodigo = QLineEdit()
        self.txtCodigo.setFixedWidth(300)
        self.formulario.addRow(self.lblCodigo, self.txtCodigo)

        self.lblCantidad = QLabel("Cantidad")
        self.lblCantidad.setFont(QFont("Andale Mono", 15))
        self.txtCantidad = QLineEdit()
        self.txtCantidad.setFixedWidth(300)
        self.formulario.addRow(self.lblCantidad, self.txtCantidad)



        # Hacemos un botón para regresar a la ventana1
        self.botonRegresar = QPushButton(self)
        # Establecemos el ancho del botón
        self.botonRegresar.setIcon(QIcon('imagenes/Imagen4.png'))
        self.botonRegresar.setFixedWidth(180)
        self.botonRegresar.setIconSize(QSize(180, 180))
        self.botonRegresar.setStyleSheet('background-color:transparent;')
        self.vertical.addWidget(self.botonRegresar)
        self.botonRegresar.clicked.connect(self.accionBotonRegresar)
        self.horizontal.addWidget(self.botonRegresar)
        self.horizontal.addSpacing(600)

        self.btnAgregar = QPushButton("Agregar")
        self.btnAgregar.setStyleSheet('background-color:#1D9A08;')
        self.btnAgregar.setFixedWidth(150)
        self.btnAgregar.clicked.connect(self.accionBtnAgregar)

        self.btnTotal = QPushButton("Total")
        self.btnTotal.setStyleSheet('background-color:#1D9A08;')
        self.btnTotal.setFixedWidth(300)
        self.btnTotal.clicked.connect(self.accionBtnTotal)
        self.formulario.addRow(self.btnAgregar, self.btnTotal)



        self.horizontal.addLayout(self.formulario)
        self.vertical.addLayout(self.horizontal)


        # Hacemos el método para volver

    def accionBotonRegresar(self):
        # Ocultamos la ventana actual
        self.hide()
        # Mostramos la ventana anterior
        self.ventanaMenu.show()
    def accionDelete(self):
        # Creamos una ventana de diálogo
        if Ayudas.rol == "Cajero":
            self.dialogo = QDialog(self)
            self.dialogo.setWindowTitle("Se requiere clave administrador")
            self.dialogo.setGeometry(300, 300, 200, 100)
            self.layout = QVBoxLayout()
            self.boton1 = QPushButton("Enviar")
            self.boton1.setStyleSheet('background-color:#1D9A08;')
            self.boton1.setFixedWidth(300)
            self.txtClave = QLineEdit()
            self.txtClave.setFixedWidth(300)
            self.txtClave.setEchoMode(QLineEdit.Password)
            self.layout.addWidget(self.txtClave)
            self.layout.addWidget(QLabel("Ingrese por favor una clave de administrador\no supervisor "))

            self.boton1.clicked.connect(self.accion_boton1)
            self.layout.addWidget(self.boton1)
            self.dialogo.setLayout(self.layout)

            # Mostrar el cuadro de diálogo y bloquear la ejecución
            self.dialogo.exec_()

        else:
            self.tabla.removeRow(self.tabla.currentRow())

    def accionAdd(self):
        self.ultimaFila = self.tabla.rowCount()
        self.tabla.insertRow(self.ultimaFila)

    def accionEdit(self):
        locale.setlocale(locale.LC_ALL, 'es_MX.UTF-8')
        total = 0

        for row in range(self.tabla.rowCount()):
            item = self.tabla.item(row, 5)
            if item is not None and item.text():
                total += float(item.text())
        self.vrPago = (locale.currency(total, grouping=True))

        self.dialogo2 = QDialog(self)
        self.dialogo2.setWindowTitle("Finalizar compra")
        self.dialogo2.setGeometry(300, 300, 200, 100)
        self.layout = QVBoxLayout()
        self.boton2 = QPushButton("No")
        self.boton2.setStyleSheet('background-color:#1D9A08;')
        self.boton2.setFixedWidth(150)
        self.boton3 = QPushButton("Sí")
        self.boton3.setStyleSheet('background-color:#1D9A08;')
        self.boton3.setFixedWidth(150)
        self.layout.addWidget(QLabel(f"El valor total de los productos registrados es:\n"
                                     f"{self.vrPago} ¿Desea finalizar?"))

        self.boton2.clicked.connect(self.accion_boton2)
        self.boton3.clicked.connect(self.accion_boton3)
        self.layout.addWidget(self.boton2)
        self.layout.addWidget(self.boton3)
        self.dialogo2.setLayout(self.layout)

        self.dialogo2.exec_()

    def accionBtnAgregar(self):
        self.ultimaFila = self.tabla.rowCount()
        self.tabla.insertRow(self.ultimaFila)
        self.file = open('Archivos/productos.txt', 'rb')
        usuarios = []
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            lista = linea.split(";")
            # paramos el bucle si ya no encuentra más registros en el archivo
            if linea == '':
                break
            u = Productos(lista[0],
                         lista[1],
                         lista[2],
                         lista[3],
                         lista[4])

            # Agregar los datos a la lista
            usuarios.append(u)
            # cerramos ael archivo txt
        self.file.close()
        existeCodigo = False
        self.total = 0
        for u in usuarios:
            if u.codigo == self.txtCodigo.text():
                existeCodigo = True
                self.tabla.setItem(self.ultimaFila, 0, QTableWidgetItem(u.codigo))
                self.tabla.item(self.ultimaFila, 0).setFlags(Qt.ItemIsEnabled)
                self.tabla.setItem(self.ultimaFila, 1, QTableWidgetItem(u.producto))
                self.tabla.item(self.ultimaFila, 1).setFlags(Qt.ItemIsEnabled)
                self.tabla.setItem(self.ultimaFila, 2, QTableWidgetItem(u.descripcion))
                self.tabla.item(self.ultimaFila, 2).setFlags(Qt.ItemIsEnabled)
                self.tabla.setItem(self.ultimaFila, 3, QTableWidgetItem(u.precio))
                self.tabla.item(self.ultimaFila, 3).setFlags(Qt.ItemIsEnabled)
                self.tabla.setItem(self.ultimaFila, 4, QTableWidgetItem(self.txtCantidad.text()))
                self.tabla.item(self.ultimaFila, 4).setFlags(Qt.ItemIsEnabled)
                self.total = int(self.txtCantidad.text())*int(u.precio)
                self.tabla.setItem(self.ultimaFila, 5, QTableWidgetItem(str(self.total)))
                self.tabla.item(self.ultimaFila, 5).setFlags(Qt.ItemIsEnabled)
                self.txtCodigo.setText("")
                self.txtCantidad.setText("")

                break
        if not existeCodigo:
            self.dialogo2 = QDialog(self)
            self.dialogo2.setWindowTitle("Error")
            self.dialogo2.setGeometry(300, 300, 200, 100)
            self.layout = QVBoxLayout()
            self.boton2 = QPushButton("Aceptar")
            self.boton2.setStyleSheet('background-color:#1D9A08;')
            self.boton2.setFixedWidth(300)
            self.layout.addWidget(QLabel(f"El código buscado ({self.txtCodigo.text()}), no se encuentra registrado\n"
                                         f"confírmalo e intenta de nuevo"))
            self.txtCodigo.setText("")

            self.boton2.clicked.connect(self.accion_boton2)
            self.layout.addWidget(self.boton2)
            self.dialogo2.setLayout(self.layout)

            # Mostrar el cuadro de diálogo y bloquear la ejecución
            self.dialogo2.exec_()
    def accionBtnTotal(self):

        locale.setlocale(locale.LC_ALL, 'es_MX.UTF-8')
        self.pago = 0

        for row in range(self.tabla.rowCount()):
            item = self.tabla.item(row, 5)
            if item is not None and item.text():
                self.pago += float(item.text())
        self.vrPago = (locale.currency(self.pago, grouping=True))
        self.titulo1.setText(f"Registrar los productos, hasta ahora el total de la compra es: {self.vrPago}")

    def accion_boton1(self):
        clave = self.txtClave.text()
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
        self.existeClave = False
        for u in usuarios:
            if u.clave == clave:
                self.existeClave = True
                # print(u.nombreCompleto)
                if u.rol == "Cajero":
                    self.dialogo2 = QDialog(self)
                    self.dialogo2.setWindowTitle("Se requiere clave administrador")
                    self.dialogo2.setGeometry(300, 300, 200, 100)
                    self.layout = QVBoxLayout()
                    self.boton2 = QPushButton("Aceptar")
                    self.boton2.setStyleSheet('background-color:#1D9A08;')
                    self.boton2.setFixedWidth(300)
                    self.layout.addWidget(QLabel(f"La clave del usuario {u.nombreCompleto} con rol {u.rol} no tiene\n"
                                                 f"permisos para la acción que intenta realizar"))

                    self.boton2.clicked.connect(self.accion_boton2)
                    self.layout.addWidget(self.boton2)
                    self.dialogo2.setLayout(self.layout)

                    # Mostrar el cuadro de diálogo y bloquear la ejecución
                    self.dialogo.close()
                    self.dialogo2.exec_()

                else:
                    self.tabla.removeRow(self.tabla.currentRow())
                    self.dialogo.close()


        if not self.existeClave:
            self.dialogo2 = QDialog(self)
            self.dialogo2.setWindowTitle("Se requiere clave administrador")
            self.dialogo2.setGeometry(300, 300, 200, 100)
            self.layout = QVBoxLayout()
            self.boton2 = QPushButton("Aceptar")
            self.boton2.setStyleSheet('background-color:#1D9A08;')
            self.boton2.setFixedWidth(300)
            self.layout.addWidget(QLabel("La clave ingresada no pertenece\n"
                                         "a ninguno de los usuarios registrados"))

            self.boton2.clicked.connect(self.accion_boton2)
            self.layout.addWidget(self.boton2)
            self.dialogo2.setLayout(self.layout)

            # Mostrar el cuadro de diálogo y bloquear la ejecución
            self.dialogo.close()
            self.dialogo2.exec_()

    def accion_boton2(self):
        self.dialogo2.close()

    def accion_boton3(self):
        self.dialogo2.close()
        self.tabla.setRowCount(0)
        self.fechaHoy = datetime.date.today()
        with open('Archivos/proveedores.txt', 'a') as archivo:
            archivo.write(f"{self.fechaHoy};{self.pago}")
            archivo.write("\n")
