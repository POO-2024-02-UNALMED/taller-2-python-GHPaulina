class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco":
            # Luego de verificar que esté entre los permitidos
            # El atributo color del objeto tendrá el valor de color 
            self.color = color


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo


class Auto:
    # Atributo de clase
    cantidadCreados = 0

    # Inicializador, atributos de instancia
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos  # Lista de objetos Asiento
        self.marca = marca
        self.motor = motor  # Objeto de la clase Motor
        self.registro = registro

    def cantidadAsientos(self):
        cantidad = 0
        # Recorremos la lista de asientos
        for elemento in self.asientos:
            # Verificamos que el elemento no sea None y sea de tipo Asiento
            if isinstance(elemento, Asiento):
                cantidad += 1
        return cantidad

    def verificarIntegridad(self):
        # Verificamos que el registro del motor coincida con el registro del auto
        if self.registro == self.motor.registro:
            # Comprobamos que todos los asientos sean válidos y tengan el mismo registro que el auto
            for asiento in self.asientos:
                # Si el asiento no es None, verificamos su registro
                if asiento is not None and asiento.registro != self.registro:
                    return "Las piezas no son originales"
            return "Auto original"
        return "Las piezas no son originales"
