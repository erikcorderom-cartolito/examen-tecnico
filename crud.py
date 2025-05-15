from data import empleados
from schemas import DEPARTAMENTOS_VALIDOS

def get_empleados(activo: bool | None = None):
    if activo is None:
        return empleados
    return [emp for emp in empleados if emp["activo"] == activo]

def delete_empleado(id: int):
    empleado = next((emp for emp in empleados if emp["id"] == id), None)
    if not empleado:
        return None
    empleado["activo"] = False
    return empleado
