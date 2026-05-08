# API de Reservas - ITM

Microservicio web desarrollado con **FastAPI** y **Pydantic** para la 
gestión de reservas de salas académicas. Proyecto desarrollado para 
la asignatura Aplicaciones y Servicios Web - Tecnología en Desarrollo 
de Software.

---

## Estructura del proyecto

```
SERVI/
├── app/
│   ├── main.py
│   ├── db.py
│   ├── models/
│   │   └── laboratorios.py
│   └── schemas/
│       └── laboratorios.py
├── datos_prueba.json
├── .gitignore
└── requirements.txt
```

---

## Instalación

```bash
# 1. Clonar el repositorio
git clone <https://github.com/1803790/reservas_microservicio.git>
cd SERVI

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 4. Instalar dependencias
pip install -r requirements.txt
```

---

## Ejecución

```bash
uvicorn app.main:app --reload
```

La API estará disponible en: http://127.0.0.1:8000

Documentación automática: http://127.0.0.1:8000/docs

---

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/` | Mensaje de bienvenida |
| POST | `/reservas` | Registrar una nueva reserva |
| GET | `/reservas` | Consultar todas las reservas |
| GET | `/reservas/{id_reserva}` | Consultar una reserva por ID |

---

## Ejemplos de uso

### POST `/reservas` — Crear una reserva

**Body (JSON):**
```json
{
  "id_reserva": 1,
  "id_sala": 10,
  "id_usuario": 201,
  "fecha": "2026-05-10",
  "hora_inicio": "08:00",
  "hora_fin": "10:00",
  "personas": 25,
  "estado": "pendiente"
}
```

**Respuesta exitosa (201):**
```json
{
  "id_reserva": 1,
  "id_sala": 10,
  "id_usuario": 201,
  "fecha": "2026-05-10",
  "hora_inicio": "08:00",
  "hora_fin": "10:00",
  "personas": 25,
  "estado": "pendiente"
}
```

---

### GET `/reservas` — Consultar todas las reservas

**Respuesta exitosa (200):**
```json
[
  {
    "id_reserva": 1,
    "id_sala": 10,
    "id_usuario": 201,
    "fecha": "2026-05-10",
    "hora_inicio": "08:00",
    "hora_fin": "10:00",
    "personas": 25,
    "estado": "pendiente"
  }
]
```

---

### GET `/reservas/{id_reserva}` — Consultar una reserva por ID

**Ejemplo:** `GET /reservas/1`

**Respuesta exitosa (200):**
```json
{
  "id_reserva": 1,
  "id_sala": 10,
  "id_usuario": 201,
  "fecha": "2026-05-10",
  "hora_inicio": "08:00",
  "hora_fin": "10:00",
  "personas": 25,
  "estado": "pendiente"
}
```

**Respuesta error (404):**
```json
{
  "detail": "Reserva no encontrada"
}
```

---

## Errores de validación comunes

| Error | Causa |
|-------|-------|
| `422` | Formato de fecha incorrecto, personas fuera de rango, estado no permitido |
| `400` | ID de reserva duplicado |
| `422` | hora_fin menor o igual a hora_inicio |

---

## Integrantes

| Nombre | Aporte |
|--------|--------|
| Santiago Orrego Castaño | Modelos de datos con Pydantic,Implementación endpoints POST y GET |
| Juan José Zapata villada|Datos de prueba y documentación  |
