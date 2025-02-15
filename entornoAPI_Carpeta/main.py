
from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title='Mi primer API',
    description = 'Isaac Gomez',
    version = '1.0.0'
)

usuarios = [
    {"id": 1, "nombre": "Isaac", "edad": 21},
    {"id": 2, "nombre": "Juan", "edad": 22},
    {"id": 3,"nombre": "Pedro", "edad": 23},
]

@app.get('/', tags=['Inicio'])
def main():
    return {'hola FastAPI' : 'Isaac'}

# endpoint Consultar todos
@app.get('/usuarios', tags=['Operaciones CRUD'])
def ConsultarTodos():
    return {"Usuarios Registrados ": usuarios}

# endpoint paea agregar usuarios
@app.post('/usuarios/', tags=['Operaciones CRUD'])
# lo que hace dict es que recibe un diccionario y lo pone como lista
def AgregarUsuario(usuarionuevo: dict):
    for usr in usuarios:
        if usr['id'] == usuarionuevo.get('id'):
            raise HTTPException(status_code=400, detail="El id ya existe")

    usuarios.append(usuarionuevo)
    return {"mensaje": "Usuario agregado correctamente"}

@app.put('/usuarios/{id}', tags=['Operaciones CRUD'])
# lo que hace dict es que recibe un diccionario y lo pone como lista
def ActualizarUsuario(id: int, usuariosNuevos: dict):
    for index, usr in enumerate (usuarios):
        if usr['id'] == id:
            usuarios[index].update(usuariosNuevos)
            return usuarios[index]
    raise HTTPException(status_code=404, detail="Usuario no encontrado") 

@app.delete('/usuarios/{id}', tags=["Operaciones CRUD"])
def EliminarUsuarios(id:int):
    for  usr in range(len(usuarios)):
        if usuarios[usr]["id"] == id:
            usuarios.pop(usr)
            return {"mensaje" : "Usuario Eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado") 

# @app.get('/promedio', tags=['Mi calificacion'])
# def promedio():
#     return(10);

# #endPoint Parametro Obligatorio
# @app.get('/usuario/{id}', tags=['Parametro Obligatorio'])
# def consultaUsuario(id:int):
#         # Consulta a la base de datos
#     return {"Se encontro el usuario":id} 

# #endPoint Parametro Opcional
# @app.get('/usuariox', tags=['Parametro Opcional'])
# def consultaUsuario2(id:Optional[int] = None):
    
#     if id is not None:
#         for usuario in usuarios:
#             if usuario['id'] == id:
#                 return {"mensaje":"Usuario encontrado","usuario":usuario}
#         return {"usuario":f"No se encontro el id : {id}"}
#     else:
#         return {"mensaje":"No se porporciono un id"}

# #endpoint con varios parametro opcionales
# @app.get("/usuarios/", tags=["3 parámetros opcionales"])
# async def consulta_usuarios(
#     usuario_id: Optional[int] = None,
#     nombre: Optional[str] = None,
#     edad: Optional[int] = None
# ):
#     resultados = []

#     for usuario in usuarios:
#         if (
#             (usuario_id is None or usuario["id"] == usuario_id) and
#             (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
#             (edad is None or usuario["edad"] == edad)
#         ):
#             resultados.append(usuario)

#     if resultados:
#         return {"usuarios_encontrados": resultados}
#     else:
#         return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}

