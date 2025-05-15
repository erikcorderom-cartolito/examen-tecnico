from pydantic import BaseModel, Field
from typing import Optional

DEPARTAMENTOS_VALIDOS = {"TI", "RRHH", "Ventas", "Produccion"}

class EmpleadoBase(BaseModel):
    nombre: str
    edad: int
    departamento: str
    username: str

    class Config:
        schema_extra = {
            "example": {
                "nombre": "Pedro",
                "edad": 28,
                "departamento": "TI",
                "username": "pedro.peligro"
            }
        }

class EmpleadoCreate(EmpleadoBase):
    pass