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

Base.metadata.create_all(bind=engine)

app.include_router(usuario.router)
app.include_router(rutas_producto.router)

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la API"}