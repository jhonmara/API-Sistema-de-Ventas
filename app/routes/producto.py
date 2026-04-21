from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.producto import Producto
from ..schemas.producto import ProductoCreate, ProductoResponse
from typing import List
from app.auth.auth import verificar_token

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.post("/", response_model=ProductoResponse, status_code=201)
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
        

        try:
            db.refresh(nuevo_producto)
        except Exception as refresh_error:
            print(f"Error en el refresh: {refresh_error}")
            
        return nuevo_producto

    except Exception as e:
        db.rollback()
        print(f"ERROR DE SISTEMA: {str(e)}")
        raise HTTPException(
           status_code=500,
           detail="Error interno del servidor"
        )
    
@router.get("/", response_model=List[ProductoResponse], status_code=200)
def obtener_productos(db: Session = Depends(get_db), user: dict = Depends(verificar_token)):
    productos = db.query(Producto).all()
    return productos

@router.get("/{id}", response_model=ProductoResponse, status_code=200)
def obtener_producto(id: int, db: Session = Depends(get_db), user: dict = Depends(verificar_token)):
    producto = db.query(Producto).filter(Producto.id == id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.put("/{id}", response_model=ProductoResponse, status_code=200)
def actualizar_producto(
    id: int,
    item: ProductoCreate,
    db: Session = Depends(get_db),
    user: dict = Depends(verificar_token)
):
    try:
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

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Error al actualizar producto: {str(e)}"
        )


@router.delete("/{id}", response_model=ProductoResponse, status_code=200)
def eliminar_producto(
    id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(verificar_token)
):
    try:
        producto = db.query(Producto).filter(Producto.id == id).first()

        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

        db.delete(producto)
        db.commit()

        return producto

    except Exception as e:
        db.rollback()
        print(f"ERROR INTERNO: {str(e)}")  

    raise HTTPException(
        status_code=500,
        detail="Error interno del servidor"
    )


    
