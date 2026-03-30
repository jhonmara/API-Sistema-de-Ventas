from fastapi import FastAPI
from app.database import engine, Base
from app.routes import producto as rutas_producto

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Ventas")

app.include_router(rutas_producto.router)

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la API"}