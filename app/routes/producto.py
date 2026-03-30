from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.producto import Producto
from ..schemas.producto import ProductoCreate, ProductoResponse

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.post("/", response_model=ProductoResponse)
def crear_producto(item: ProductoCreate, db: Session = Depends(get_db)):
    try:
        nuevo_producto = Producto(
            nombre=item.nombre,
            descripcion=item.descripcion,
            precio=item.precio,
            stock=item.stock
        )
        
        db.add(nuevo_producto)
        db.commit()
        db.refresh(nuevo_producto)
        return nuevo_producto

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Error al crear producto"
        )