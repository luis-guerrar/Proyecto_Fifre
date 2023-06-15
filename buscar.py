import locale

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, \
    QFormLayout, QLineEdit, QDialog
from ayudas import Ayudas
from usuarios import Productos


class Buscar(QMainWindow):

    def __init__(self, anterior):
        super(Buscar, self).__init__(anterior)
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
        self.titulo1.setText("Consultar precios de los productos")
        # Para centrar el letrero
        self.titulo1.setAlignment(Qt.AlignCenter)
        self.titulo1.setStyleSheet('background-color:#434343; color:#F7F7F7; padding: 30px; '
                                   'border-radius: 15px; margin-bottom: 50px;')
        self.titulo1.setFont(QFont("Andale Mono", 20))
        self.titulo1.setFixedSize(1880, 200)
        # para poner el letrero arriba
        self.vertical.addWidget(self.titulo1)
        self.fondo.setLayout(self.vertical)
        # Construir la tabla de consulta de precios
        self.horizontal = QHBoxLayout()
        self.formulario = QFormLayout()

        self.lblCodigo = QLabel("Código")
        self.lblCodigo.setFont(QFont("Andale Mono", 15))
        self.font = QFont()
        self.font.setPointSize(14)
        self.txtCodigo = QLineEdit()
        self.txtCodigo.setFixedWidth(300)
        self.txtCodigo.setFont(self.font)
        self.formulario.addRow(self.lblCodigo, self.txtCodigo)
        self.lblEspacio = QLabel("")
        self.formulario.addRow(self.lblEspacio)

        self.lblNombre = QLabel("Nombre")
        self.lblNombre.setFont(QFont("Andale Mono", 15))
        self.txtNombre = QLineEdit()
        self.txtNombre.setFixedWidth(300)
        self.txtNombre.setFont(self.font)
        self.txtNombre.setReadOnly(True)
        self.formulario.addRow(self.lblNombre, self.txtNombre)
        self.lblEspacio = QLabel("")
        self.formulario.addRow(self.lblEspacio)

        self.lblPrecio = QLabel("Precio por Unidad")
        self.lblPrecio.setFont(QFont("Andale Mono", 15))
        self.formulario.addRow(self.lblPrecio)
        self.lblPrecio.setStyleSheet('background-color:#1BBC9B; color:#F7F7F7; padding: 30px; border-radius: 15px;')
        self.lblPrecio.setFixedSize(400, 100)

        self.titulo2 = QLabel()
        self.titulo2.setText(f"«La gastronomía es el arte de usar los alimentos para crear "
                             f"felicidad». Theodore Zeldin\n\n"
                             "En este segmento encontraras la descripción de los productos")
        # Para centrar el letrero
        self.titulo2.setAlignment(Qt.AlignCenter)
        self.titulo2.setStyleSheet('background-color:#ECF0F1; color:#000000; padding: 30px; border-radius: 15px;')
        self.titulo2.setFont(QFont("Andale Mono", 12))

        self.horizontal.addLayout(self.formulario)
        self.horizontal.addSpacing(20)
        self.horizontal.addWidget(self.titulo2)
        self.vertical.addLayout(self.horizontal)

        self.btnBuscar = QPushButton(self)
        # Establecemos el ancho del botón
        self.btnBuscar.setIcon(QIcon('imagenes/buscar2.png'))
        self.btnBuscar.setFixedWidth(180)
        self.btnBuscar.setIconSize(QSize(180, 180))
        self.btnBuscar.setStyleSheet('background-color:transparent;')
        self.horizontal.addWidget(self.btnBuscar)
        self.btnBuscar.clicked.connect(self.accionbtnBuscar)

        # Hacemos un botón para regresar a la ventana1
        self.botonRegresar = QPushButton(self)
        # Establecemos el ancho del botón
        self.botonRegresar.setIcon(QIcon('imagenes/Imagen4.png'))
        self.botonRegresar.setFixedWidth(180)
        self.botonRegresar.setIconSize(QSize(180, 180))
        self.botonRegresar.setStyleSheet('background-color:transparent;')
        self.vertical.addWidget(self.botonRegresar)
        self.botonRegresar.clicked.connect(self.accionBotonRegresar)

        # Hacemos el método para volver

    def accionBotonRegresar(self):
        # Ocultamos la ventana actual
        self.hide()
        # Mostramos la ventana anterior
        self.ventanaMenu.show()
    def accionbtnBuscar(self):
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
                          lista[9])

            # Agregar los datos a la lista
            usuarios.append(u)
            # cerramos ael archivo txt
        self.file.close()
        existeCodigo = False
        for u in usuarios:
            if u.codigo == self.txtCodigo.text():
                existeCodigo = True
                locale.setlocale(locale.LC_ALL, 'es_MX.UTF-8')
                self.pago = (locale.currency(float(u.precio), grouping=True))
                self.txtNombre.setText(u.producto)
                self.lblPrecio.setText(f"{self.pago}")
                self.titulo2.setText(f"«La gastronomía es el arte de usar los alimentos para crear "
                                     f"felicidad». Theodore Zeldin\n\n"
                                     f"Para este producto tenemos la siguiente descripción: {u.descripcion}")

        if not existeCodigo:
            self.dialogo2 = QDialog(self)
            self.dialogo2.setWindowTitle("Error")
            self.dialogo2.setGeometry(300, 300, 200, 100)
            self.layout = QVBoxLayout()
            self.boton2 = QPushButton("Aceptar")
            self.boton2.setStyleSheet('background-color:#1D9A08;')
            self.boton2.setFixedWidth(300)
            self.layout.addWidget(
                QLabel(f"El código buscado ({self.txtCodigo.text()}), no se encuentra registrado\n"
                       f"confírmalo e intenta de nuevo"))
            self.txtCodigo.setText("")

            self.boton2.clicked.connect(self.accion_boton2)
            self.layout.addWidget(self.boton2)
            self.dialogo2.setLayout(self.layout)

            # Mostrar el cuadro de diálogo y bloquear la ejecución
            self.dialogo2.exec_()

    def accion_boton2(self):
        self.dialogo2.close()