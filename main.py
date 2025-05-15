from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional

from schemas import EmpleadoOut, EmpleadoCreate, EmpleadoUpdate
from crud import create_empleado, get_empleados, delete_empleado, update_empleado, get_empleado_by_id

app = FastAPI()

@app.get("/empleados", response_model=List[EmpleadoOut])
def listar_empleados(activo: Optional[bool] = Query(None)):
    return get_empleados(activo)

@app.delete("/empleados/{id}", response_model=EmpleadoOut)
def eliminar_empleado(id: int):
    empleado = delete_empleado(id)
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado
