# Evaluación Técnica - Departamento de Desarrollo Cartolito

**Versión:** 1.0

## Descripción
Este proyecto es una evaluación técnica diseñada por el departamento de desarrollo de Cartolito. El objetivo principal es implementar una API RESTful utilizando FastAPI que permita realizar operaciones CRUD (Create, Read, Update, Delete) sobre una entidad de empleados.

## Objetivo de la Entrevista Técnica
El candidato debe demostrar habilidades para:
- Implementar endpoints para obtener empleados por ID (`get_by_id`), crear (`create`) y actualizar (`update`) empleados.
- Aplicar ejercicios de lógica en los procesos de creación y actualización de empleados.

## Ejercicios de Lógica
Durante la entrevista, se solicita que el candidato resuelva los siguientes ejercicios de lógica:

### 1. Lógica al Crear un Empleado
- **Validación de Username Único:** Al crear un empleado, se debe verificar que el `username` no exista previamente en la base de datos. Si ya existe, se debe rechazar la creación.
- **Asignación Automática de Departamento:** Si el empleado tiene menos de 25 años y no se especifica el departamento, asignar automáticamente el departamento "Produccion".

### 2. Lógica al Actualizar un Empleado
- **Cambio de Departamento Restringido:** Si se intenta cambiar el departamento de un empleado que tiene más de 10 años de antigüedad (simulado por un campo `antiguedad`), rechazar el cambio y devolver un mensaje de error.
- **Actualización de Username:** Si se actualiza el `username`, validar que el nuevo username también sea único.

## Endpoints Principales
- `GET /empleados/{id}`: Obtener empleado por ID.
- `POST /empleados`: Crear un nuevo empleado (con lógica de validación y asignación automática).
- `PUT /empleados/{id}`: Actualizar un empleado (con lógica de restricción y validación).

## Requisitos
- Python 3.10+
- FastAPI
- Uvicorn

## Ejecución
1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta el servidor:
   ```bash
   uvicorn main:app --reload
   ```

## Notas
- Este proyecto es solo para fines de evaluación técnica y no debe usarse en producción.
- Los datos se almacenan en memoria o en archivos locales para simplificar la lógica.

---
Departamento de Desarrollo - Cartolito
