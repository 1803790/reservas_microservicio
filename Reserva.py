from pydantic import BaseModel
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Reserva(BaseModel):
    id_reserva: int
    id_sala: int
    id_usuario: int
    fecha: str
    hora_inicio: str
    hora_fin: str
    personas: int
    estado: str

reservas = []

class Reserva(BaseModel):
    id_reserva: int
    id_sala: int
    id_usuario: int
    fecha: str
    hora_inicio: str
    hora_fin: str
    personas: int
    estado: str

    @app.post("/reservas")
def crear_reserva(reserva: Reserva):
    reservas.append(reserva)
    return {"mensaje": "Reserva creada correctamente"}

    @app.get("/reservas")
def listar_reservas():
    return reservas
    