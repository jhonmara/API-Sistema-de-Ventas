from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.producto import Producto
from ..schemas.producto import ProductoCreate, ProductoResponse
from typing import List
from app.auth.auth import verificar_token

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.post("/", response_model=ProductoResponse)
def crear_producto(item: ProductoCreate, db: Session = Depends(get_db), user: dict = Depends(verificar_token)):
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
    
@router.get("/", response_model=List[ProductoResponse])
def obtener_productos(db: Session = Depends(get_db)):
    productos = db.query(Producto).all()
    return productos

@router.get("/{id}", response_model=ProductoResponse)
def obtener_producto(id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.put("/{id}", response_model=ProductoResponse)
def actualizar_producto(
    id: int,
    item: ProductoCreate,
    db: Session = Depends(get_db),
    user: dict = Depends(verificar_token)
):

    producto = db.query(Producto).filter(Producto.id == id).first()

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    producto.nombre = item.nombre
    producto.descripcion = item.descripcion
    producto.precio = item.precio
    producto.stock = item.stock

    db.commit()
    db.refresh(producto)

    return producto


@router.delete("/{id}", response_model=ProductoResponse)
def eliminar_producto(
    id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(verificar_token)
):
    producto = db.query(Producto).filter(Producto.id == id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(producto)
    db.commit()
    return producto


    
