from fastapi import FastAPI, HTTPException
from typing import List
from Reserva import Reserva

app = FastAPI(
    title="API de Reservas - ITM",
    description="Microservicio para gestión de reservas de salas académicas",
    version="1.0.0"
)

# Base de datos en memoria
reservas_db: List[Reserva] = []


@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la API de Reservas del ITM"}


@app.post("/reservas", response_model=Reserva, status_code=201)
def crear_reserva(reserva: Reserva):
    # Verificar id duplicado
    for r in reservas_db:
        if r.id_reserva == reserva.id_reserva:
            raise HTTPException(
                status_code=400,
                detail=f"Ya existe una reserva con el id {reserva.id_reserva}"
            )
    # Validar hora_fin mayor que hora_inicio
    if reserva.hora_fin <= reserva.hora_inicio:
        raise HTTPException(
            status_code=422,
            detail="La hora de fin debe ser mayor que la hora de inicio"
        )
    reservas_db.append(reserva)
    return reserva


@app.get("/reservas", response_model=List[Reserva])
def obtener_reservas():
    return reservas_db


@app.get("/reservas/{id_reserva}", response_model=Reserva)
def obtener_reserva(id_reserva: int):
    for r in reservas_db:
        if r.id_reserva == id_reserva:
            return r
    raise HTTPException(status_code=404, detail="Reserva no encontrada")