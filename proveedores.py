from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, \
    QFormLayout, QHBoxLayout, QTextEdit, QMessageBox
from ayudas import Ayudas
from usuarios import Productos


class Proveedores(QMainWindow):

    def __init__(self, anterior):
        super(Proveedores, self).__init__(anterior)
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
        self.vertical.addStretch()

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
        self.lblCodigo = QLabel("Código")
        self.lblCodigo.setFont(QFont("Andale Mono", 15))
        self.lblCodigo.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font = QFont()
        self.font.setPointSize(14)
        self.txtCodigo = QLineEdit()
        self.txtCodigo.setFixedWidth(300)
        self.txtCodigo.setFont(self.font)
        self.txtCodigo.setPlaceholderText("Código Producto")
        self.ladoIzquierdo.addRow(self.lblCodigo, self.txtCodigo)

        # -----Nombre
        self.lblNombre = QLabel("Nombre")
        self.lblNombre.setFont(QFont("Andale Mono", 15))
        self.lblNombre.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font.setPointSize(14)
        self.txtNombre = QLineEdit()
        self.txtNombre.setFixedWidth(300)
        self.txtNombre.setFont(self.font)
        self.txtNombre.setPlaceholderText("Nombre Producto")
        self.ladoIzquierdo.addRow(self.lblNombre, self.txtNombre)

        # -----Precio
        self.lblPrecio = QLabel("Precio")
        self.lblPrecio.setFont(QFont("Andale Mono", 15))
        self.lblPrecio.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font.setPointSize(14)
        self.txtPrecio = QLineEdit()
        self.txtPrecio.setFixedWidth(300)
        self.txtPrecio.setFont(self.font)
        self.txtPrecio.setPlaceholderText("Precio por unidad")
        self.ladoIzquierdo.addRow(self.lblPrecio, self.txtPrecio)

        # -----Descripción
        self.lblDesc = QLabel("Descripción")
        self.lblDesc.setFont(QFont("Andale Mono", 15))
        self.lblDesc.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font.setPointSize(10)
        self.txtDesc = QTextEdit()
        self.txtDesc.setFixedWidth(300)
        self.txtDesc.setFixedHeight(130)
        self.txtDesc.setFont(self.font)
        self.txtDesc.setPlaceholderText("Ingrese una descripción mas detallada del producto")
        self.ladoIzquierdo.addRow(self.lblDesc, self.txtDesc)

        # ---------- Layout derecho -----------

        # Creamos el layout del lado izquierdo
        self.ladoDerecho = QFormLayout()

        # ---------------- TODO EL CÓDIGO DEL LADO DERECHO INICIA EN ESTA SECCIÓN ---------------------#

        # ETIQUETAS Y LINEAS DE TEXTO
        # -----Nombre
        self.lblNombreP = QLabel("Nombre")
        self.lblNombreP.setFont(QFont("Andale Mono", 15))
        self.lblNombreP.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font = QFont()
        self.font.setPointSize(14)
        self.txtNombreP = QLineEdit()
        self.txtNombreP.setFixedWidth(300)
        self.txtNombreP.setFont(self.font)
        self.txtNombreP.setPlaceholderText("Nombre del proveedor")
        self.ladoDerecho.addRow(self.lblNombreP, self.txtNombreP)

        # -----Nit
        self.lblNit = QLabel("Nit")
        self.lblNit.setFont(QFont("Andale Mono", 15))
        self.lblNit.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font.setPointSize(14)
        self.txtNit = QLineEdit()
        self.txtNit.setFixedWidth(300)
        self.txtNit.setFont(self.font)
        self.txtNit.setPlaceholderText("Nit proveedor")
        self.ladoDerecho.addRow(self.lblNit, self.txtNit)

        # -----Teléfono
        self.lblTel = QLabel("Teléfono")
        self.lblTel.setFont(QFont("Andale Mono", 15))
        self.lblTel.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font.setPointSize(14)
        self.txtTel = QLineEdit()
        self.txtTel.setFixedWidth(300)
        self.txtTel.setFont(self.font)
        self.txtTel.setPlaceholderText("Teléfono proveedor")
        self.ladoDerecho.addRow(self.lblTel, self.txtTel)

        # -----Celular
        self.lblCel = QLabel("Celular")
        self.lblCel.setFont(QFont("Andale Mono", 15))
        self.lblCel.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font.setPointSize(14)
        self.txtCel = QLineEdit()
        self.txtCel.setFixedWidth(300)
        self.txtCel.setFont(self.font)
        self.txtCel.setPlaceholderText("Celular proveedor")
        self.ladoDerecho.addRow(self.lblCel, self.txtCel)

        # -----Monto mínimo
        self.lblMonto = QLabel("Monto")
        self.lblMonto.setFont(QFont("Andale Mono", 15))
        self.lblMonto.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font.setPointSize(14)
        self.txtMonto = QLineEdit()
        self.txtMonto.setFixedWidth(300)
        self.txtMonto.setFont(self.font)
        self.txtMonto.setPlaceholderText("Monto mínimo de pedido")
        self.ladoDerecho.addRow(self.lblMonto, self.txtMonto)

        # -----Día entrega
        self.lblFecha = QLabel("Fecha")
        self.lblFecha.setFont(QFont("Andale Mono", 15))
        self.lblFecha.setStyleSheet("color:black; margin-bottom: 30px;")
        self.font.setPointSize(14)
        self.txtFecha = QLineEdit()
        self.txtFecha.setFixedWidth(300)
        self.txtFecha.setFont(self.font)
        self.txtFecha.setPlaceholderText("Fecha de entrega")
        self.ladoDerecho.addRow(self.lblFecha, self.txtFecha)

        # Título
        self.letreroP = QLabel()
        self.letreroP.setText("Ingreso detalle de productos y proveedores")
        self.letreroP.setFont(QFont("Andale Mono", 20))
        self.letreroP.setStyleSheet('background-color:#434343; color:#F7F7F7; padding: 30px; '
                                    'border-radius: 15px;')
        self.letreroP.setAlignment(Qt.AlignCenter)

        # Subtítulo
        self.letreroP2 = QLabel()
        self.letreroP2.setText("Por favor diligenciar todos los campos")
        self.letreroP2.setFont(QFont("Andale Mono", 12))
        self.letreroP2.setStyleSheet('background-color:transparent; color:black; padding: 30px; '
                                    'border-radius: 15px;')
        self.letreroP2.setAlignment(Qt.AlignCenter)

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

        self.btnLimpiar = QPushButton(self)
        # Establecemos el ancho del botón
        self.btnLimpiar.setIcon(QIcon('imagenes/limpiar.png'))
        self.btnLimpiar.setFixedWidth(80)
        self.btnLimpiar.setIconSize(QSize(80, 80))
        self.btnLimpiar.setStyleSheet('background-color:transparent;')
        self.btnLimpiar.clicked.connect(self.limpiar)


        # Agregamos el letrero en la línea siguiente:
        self.vertical.addWidget(self.letreroP)
        self.vertical.addWidget(self.letreroP2)
        self.horizontal.addLayout(self.ladoIzquierdo)
        self.horizontal.addLayout(self.ladoDerecho)
        self.horizontal.addWidget(self.btnLimpiar)
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
        # Hacemos el método para volver

        # ------------ PONER AL FINAL -----------------

        self.fondo.setLayout(self.vertical)
        # Hacemos el método para volver

    def accionBotonRegresar(self):
        # Ocultamos la ventana actual
        self.hide()
        # Mostramos la ventana anterior
        self.ventanaMenu.show()

    def accionBtnRegistrar(self):
        if (self.txtCodigo.text() == ''
                or self.txtNombre.text() == ''
                or self.txtPrecio.text() == ''
                or self.txtDesc.toPlainText() == ''
                or self.txtNombreP.text() == ''
                or self.txtNit.text() == ''
                or self.txtTel.text() == ''
                or self.txtCel.text() == ''
                or self.txtMonto.text() == ''
                or self.txtFecha.text() == ''):

            return QMessageBox.warning(self, 'Cuidado',
                                       "Por favor diligenciar\ntodos los campos")
        else:
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
                              lista[4],
                              lista[5],
                              lista[6],
                              lista[7],
                              lista[8],
                              lista[9], )

                # Agregar los datos a la lista
                usuarios.append(u)
                # cerramos ael archivo txt
            self.file.close()
            existeCodigo = False
            self.total = 0
            for u in usuarios:
                if u.codigo == self.txtCodigo.text():
                    existeCodigo = True
                    self.txtCodigo.setText(u.codigo)
                    self.txtNombre.setText(u.producto)
                    self.txtDesc.setText(u.descripcion)
                    self.txtPrecio.setText(u.precio)
                    self.txtNombreP.setText(u.nombreP)
                    self.txtNit.setText(u.nit)
                    self.txtTel.setText(u.tel)
                    self.txtCel.setText(u.cel)
                    self.txtMonto.setText(u.monto)
                    self.txtFecha.setText(u.fecha)
                    return QMessageBox.warning(self, 'Cuidado',
                                               "El producto que intenta registrar\n"
                                               "ya existe, a continuación se\n"
                                               "cargarán los datos registrados")

            if not existeCodigo:
                self.file = open('Archivos/productos.txt', 'ab')
                self.file.write(bytes(
                    self.txtCodigo.text() + ";"
                    + self.txtNombre.text() + ";"
                    + self.txtDesc.toPlainText() + ";"
                    + self.txtPrecio.text() + ";"
                    + self.txtNombreP.text() + ";"
                    + self.txtNit.text() + ";"
                    + self.txtTel.text() + ";"
                    + self.txtCel.text() + ";"
                    + self.txtMonto.text() + ";"
                    + self.txtFecha.text() + "\n", encoding='UTF-8'))
                self.file.close()
                self.limpiar()
                return QMessageBox.information(self, 'Cuidado',
                                               "El registro se ingresó correctamente")

    def accionBtnCosultar(self):
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
                          lista[4],
                          lista[5],
                          lista[6],
                          lista[7],
                          lista[8],
                          lista[9], )

            # Agregar los datos a la lista
            usuarios.append(u)
            # cerramos ael archivo txt
        self.file.close()
        existeCodigo = False
        self.total = 0
        for u in usuarios:
            if u.codigo == self.txtCodigo.text():
                existeCodigo = True
                self.txtCodigo.setText(u.codigo)
                self.txtCodigo.setReadOnly(True)
                self.txtNombre.setText(u.producto)
                self.txtNombre.setReadOnly(True)
                self.txtDesc.setText(u.descripcion)
                self.txtPrecio.setText(u.precio)
                self.txtNombreP.setText(u.nombreP)
                self.txtNit.setText(u.nit)
                self.txtTel.setText(u.tel)
                self.txtCel.setText(u.cel)
                self.txtMonto.setText(u.monto)
                self.txtFecha.setText(u.fecha)
        if not existeCodigo:
            self.limpiar()
            return QMessageBox.warning(self, 'Cuidado', 'El producto que intenta buscar\n nose encuentra registrado')

    def accionBtnEditar(self):
        if (self.txtCodigo.text() == ''
                or self.txtNombre.text() == ''
                or self.txtPrecio.text() == ''
                or self.txtDesc.toPlainText() == ''
                or self.txtNombreP.text() == ''
                or self.txtNit.text() == ''
                or self.txtTel.text() == ''
                or self.txtCel.text() == ''
                or self.txtMonto.text() == ''
                or self.txtFecha.text() == ''):
            return QMessageBox.warning(self, 'Cuidado', 'Para realizar la edición '
                                                        'todos los\ncampos deben estar diligenciados')
        else:
            self.file = open('Archivos/productos.txt', 'rb')
            self.usuarios = []
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
                              lista[4],
                              lista[5],
                              lista[6],
                              lista[7],
                              lista[8],
                              lista[9], )

                # Agregar los datos a la lista
                self.usuarios.append(u)
                # cerramos ael archivo txt
            self.file.close()
            self.boton = QMessageBox.question(
                self,
                'Confirmación',
                'Esta seguro que desea editar este registro',
                QMessageBox.StandardButton.Yes |
                QMessageBox.StandardButton.No)
            existeCodigo = False
            if self.boton == QMessageBox.StandardButton.Yes:
                for u in self.usuarios:
                    if u.codigo == self.txtCodigo.text():
                        existeCodigo = True
                        u.descripcion = self.txtDesc.toPlainText()
                        u.precio = self.txtPrecio.text()
                        u.nombreP = self.txtNombreP.text()
                        u.nit = self.txtNit.text()
                        u.tel = self.txtTel.text()
                        u.cel = self.txtCel.text()
                        u.monto = self.txtMonto.text()
                        u.fecha = self.txtFecha.text()
                        break



                # Ingresar los datos con el registro editado
                if existeCodigo:
                    self.file = open('Archivos/productos.txt', 'wb')
                    for u in self.usuarios:
                        self.file.write(bytes(u.codigo + ";"
                                              + u.producto + ";"
                                              + u.descripcion + ";"
                                              + u.precio + ";"
                                              + u.nombreP + ";"
                                              + u.nit + ";"
                                              + u.tel + ";"
                                              + u.cel + ";"
                                              + u.monto + ";"
                                              + u.fecha, encoding='UTF-8'))
                    self.file.close()
                    self.limpiar()
                    self.txtCodigo.setReadOnly(False)
                    self.txtNombre.setReadOnly(False)
                    return QMessageBox.question(
                                self,
                                'Confirmación',
                                'Los datos del registro se han editado correctamente',
                                QMessageBox.StandardButton.Ok)
                else:
                    self.limpiar()
                    self.txtCodigo.setReadOnly(False)
                    self.txtNombre.setReadOnly(False)
                    return QMessageBox.warning(
                        self,
                        'Confirmación',
                        'El código que intenta editar no se encuentra registrado',
                        QMessageBox.StandardButton.Ok)




    def accionBtnEliminar(self):
        if (self.txtCodigo.text() == ''
                or self.txtNombre.text() == ''
                or self.txtPrecio.text() == ''
                or self.txtDesc.toPlainText() == ''
                or self.txtNombreP.text() == ''
                or self.txtNit.text() == ''
                or self.txtTel.text() == ''
                or self.txtCel.text() == ''
                or self.txtMonto.text() == ''
                or self.txtFecha.text() == ''):
            self.limpiar()
            return QMessageBox.warning(self, 'Cuidado', 'Por favor seleccionar un documento válido\n'
                                                        ' se recomienda primero buscar con el código')
        else:
            self.file = open('Archivos/productos.txt', 'rb')
            self.usuarios = []
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
                              lista[4],
                              lista[5],
                              lista[6],
                              lista[7],
                              lista[8],
                              lista[9], )

                # Agregar los datos a la lista
                self.usuarios.append(u)
                # cerramos ael archivo txt
            self.file.close()
            self.boton = QMessageBox.question(
                self,
                'Confirmación',
                'Esta seguro que desea eliminar este registro',
                QMessageBox.StandardButton.Yes |
                QMessageBox.StandardButton.No)
            existeCodigo = False
            if self.boton == QMessageBox.StandardButton.Yes:
                for u in self.usuarios:
                    if u.codigo == self.txtCodigo.text():
                        existeCodigo = True
                        self.usuarios.remove(u)
                        break

                # Ingresar los datos con el registro editado
                if existeCodigo:
                    self.file = open('Archivos/productos.txt', 'wb')
                    for u in self.usuarios:
                        self.file.write(bytes(u.codigo + ";"
                                              + u.producto + ";"
                                              + u.descripcion + ";"
                                              + u.precio + ";"
                                              + u.nombreP + ";"
                                              + u.nit + ";"
                                              + u.tel + ";"
                                              + u.cel + ";"
                                              + u.monto + ";"
                                              + u.fecha, encoding='UTF-8'))
                    self.file.close()
                    self.file = open('Archivos/productos.txt', 'rb')
                    while self.file:
                        linea = self.file.readline().decode('UTF-8')
                        print(linea)
                        if linea == '':
                            break
                    self.file.close()
                    self.limpiar()
                    self.txtCodigo.setReadOnly(False)
                    self.txtNombre.setReadOnly(False)
                    return QMessageBox.question(
                        self,
                        'Confirmación',
                        'EL registro se eliminó correctamente',
                        QMessageBox.StandardButton.Ok)
                else:
                    self.limpiar()
                    self.txtCodigo.setReadOnly(False)
                    self.txtNombre.setReadOnly(False)
                    return QMessageBox.warning(
                        self,
                        'Confirmación',
                        'El código que intenta eliminar no se encuentra registrado',
                        QMessageBox.StandardButton.Ok)

    def limpiar(self):
        self.txtCodigo.setText('')
        self.txtNombre.setText('')
        self.txtPrecio.setText('')
        self.txtDesc.setText('')
        self.txtNombreP.setText('')
        self.txtNit.setText('')
        self.txtTel.setText('')
        self.txtCel.setText('')
        self.txtMonto.setText('')
        self.txtFecha.setText('')