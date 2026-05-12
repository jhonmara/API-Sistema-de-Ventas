import time
from sqlalchemy.exc import OperationalError
from fastapi import FastAPI
from app.database import engine, Base
import app.models.producto
import app.models.usuario
from app.routes import producto as rutas_producto
from app.routes import usuario

from app.utils.handlers import validation_exception_handler, http_exception_handler
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI(title="Sistema de Ventas")

app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)


retries = 5
while retries > 0:
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Conectado a MySQL y tablas verificadas/creadas con éxito.")
        break  
    except OperationalError as e:
        retries -= 1
        print(f"⏳ Esperando a que MySQL esté 100% listo... Reintentando en 3 segundos. (Intentos restantes: {retries})")
        if retries == 0:
            print("❌ Error crítico: No se pudo conectar a la base de datos.")
            raise e  
        time.sleep(3)


app.include_router(usuario.router)
app.include_router(rutas_producto.router)

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la API"}