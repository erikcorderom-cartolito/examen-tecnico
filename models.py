class Empleado:
    def __init__(self, id: int, nombre: str, edad: int, username: str, departamento: str, activo: bool = True):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.username = username
        self.departamento = departamento
        self.activo = activo
