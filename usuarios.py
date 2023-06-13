class Usuarios:
    def __init__(self, documento, clave, rol, nombreCompleto, apellidos, correo, direccion, telefono):
        self.documento = documento
        self.nombreCompleto = nombreCompleto
        self.apellidos = apellidos
        self.clave = clave
        self.rol = rol
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono


    def __str__(self):
        return f"Nombre: {self.nombreCompleto} Documento: {self.documento}"

class Productos:
    def __init__(self, codigo, producto, descripcion, precio, recetas):
        self.codigo = codigo
        self.producto = producto
        self.descripcion = descripcion
        self.precio = precio
        self.recetas = recetas


    def __str__(self):
        return f"Nombre: {self.codigo} Documento: {self.producto}"

