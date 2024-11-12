class Asiento:
    # El inicializador crea los atributos para cada asiento
    def __init__(self, color, precio, registro):
        self.color = color  # Color del asiento
        self.precio = precio  # Precio del asiento
        self.registro = registro  # Registro único del asiento

    # Método para cambiar el color del asiento
    def cambiarColor(self, color):
        # Solo colores válidos
        colores_validos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in colores_validos:
            self.color = color  # Cambia el color si es válido

class Motor:
    # El inicializador crea los atributos para el motor
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros  # Número de cilindros del motor
        self.tipo = tipo  # Tipo de motor (eléctrico o gasolina)
        self.registro = registro  # Registro único del motor

    # Cambiar el registro del motor
    def cambiarRegistro(self, registro):
        self.registro = registro

    # Asignar el tipo de motor
    def asignarTipo(self, tipo):
        # Solo se permiten tipos "eléctrico" o "gasolina"
        if tipo in ["electrico", "gasolina"]:
            self.tipo = tipo

class Auto:
    # Atributo de clase para contar cuántos autos han sido creados
    cantidadCreados = 0

    # Inicializador para el auto, creando los atributos del auto
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo  # Modelo del auto
        self.precio = precio  # Precio del auto
        self.asientos = asientos  # Lista de asientos en el auto
        self.marca = marca  # Marca del auto
        self.motor = motor  # Motor del auto (objeto de la clase Motor)
        self.registro = registro  # Registro único del auto

    # Método para contar la cantidad de asientos en el auto
    def cantidadAsientos(self):
        cantidad = 0
        # Contamos los asientos que son objetos de la clase Asiento
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                cantidad += 1
        return cantidad

    # Método para verificar si las piezas del auto son originales
    def verificarIntegridad(self):
        # Verificamos que el registro del motor coincida con el registro del auto
        if self.registro == self.motor.registro:
            # Comprobamos que todos los asientos tengan el mismo registro que el auto
            for asiento in self.asientos:
                if asiento.registro != self.registro:
                    return "Las piezas no son originales"
            return "Auto original"
        return "Las piezas no son originales"
