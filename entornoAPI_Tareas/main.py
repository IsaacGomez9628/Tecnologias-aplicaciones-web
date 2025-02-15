from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title='API de tareas',
    description = 'Isaac Gomez',
    version = '1.0.1'
)

Tareas = [
    {
        "id": 1,
        "titulo": "Estudiar para el examen",
        "descripcion": "Repasar los apuntes de TAI ",
        "vencimiento": '14-02-24',
        "Estado": 'completada',
    },
    {
        "id": 2,
        "titulo": "Hacer un entorno virtual de tareas",
        "descripcion": "Hacer los commits para el repositorio",
        "vencimiento": "15-02-24",
        "Estado": "pendiente",
    },

]

@app.get('/tareas', tags=['Lista de tareas'])
def ConsultarTareas():
    return {"Usuarios Registrados ": Tareas}

