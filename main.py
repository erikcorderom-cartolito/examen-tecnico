from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional

from schemas import EmpleadoBase
from crud import get_empleados, delete_empleado

app = FastAPI()

@app.get("/empleados", response_model=List[EmpleadoBase])
def listar_empleados(activo: Optional[bool] = Query(None)):
    return get_empleados(activo)

@app.delete("/empleados/{id}", response_model=EmpleadoBase)
def eliminar_empleado(id: int):
    empleado = delete_empleado(id)
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado
