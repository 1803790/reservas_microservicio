from pydantic import BaseModel, Field
from typing import Literal
from datetime import date, time


class Reserva(BaseModel):
    id_reserva: int = Field(..., gt=0, description="ID único de la reserva")
    id_sala: int = Field(..., gt=0, description="ID de la sala a reservar")
    id_usuario: int = Field(..., gt=0, description="ID del usuario que reserva")
    fecha: date = Field(..., description="Fecha de la reserva (YYYY-MM-DD)")
    hora_inicio: time = Field(..., description="Hora de inicio (HH:MM)")
    hora_fin: time = Field(..., description="Hora de fin (HH:MM)")
    personas: int = Field(..., gt=0, le=100, description="Número de personas (1-100)")
    estado: Literal["pendiente", "confirmada", "cancelada"] = Field(
        default="pendiente",
        description="Estado de la reserva"
    )