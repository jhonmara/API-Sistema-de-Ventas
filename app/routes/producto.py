from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.producto import Producto
from ..schemas.producto import ProductoCreate, ProductoResponse
from typing import List
from app.auth.auth import obtener_usuario_actual

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.post("/", response_model=ProductoResponse, status_code=201)
def crear_producto(item: ProductoCreate, db: Session = Depends(get_db), usuario: str = Depends(obtener_usuario_actual)):
    try:
        existente = db.query(Producto).filter(Producto.nombre == item.nombre).first()
        if existente:
            raise HTTPException(status_code=400, detail="El producto ya existe")

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

    except HTTPException:
        raise

    except Exception as e:
        db.rollback()
        print(f"ERROR DE SISTEMA: {str(e)}")
        raise HTTPException(
           status_code=500,
           detail="Error interno del servidor"
        )
    
@router.get("/", response_model=List[ProductoResponse], status_code=200)
def obtener_productos(db: Session = Depends(get_db), usuario_actual: str = Depends(obtener_usuario_actual)):
    productos = db.query(Producto).all()
    return productos

@router.get("/{id}", response_model=ProductoResponse, status_code=200)
def obtener_producto(id: int, db: Session = Depends(get_db), user: str = Depends(obtener_usuario_actual)):
    producto = db.query(Producto).filter(Producto.id == id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.put("/{id}", response_model=ProductoResponse, status_code=200)
def actualizar_producto(
    id: int,
    item: ProductoCreate,
    db: Session = Depends(get_db),
    usuario: str = Depends(obtener_usuario_actual)
):
    try:
        producto = db.query(Producto).filter(Producto.id == id).first()

        if not producto:
            raise HTTPException(
                status_code=404,
                detail="Producto no encontrado"
            )

        producto_existente = (
            db.query(Producto)
            .filter(
                Producto.nombre == item.nombre,
                Producto.id != id
            )
            .first()
        )

        if producto_existente:
            raise HTTPException(
                status_code=400,
                detail="Ya existe otro producto con ese nombre"
            )

        producto.nombre = item.nombre
        producto.descripcion = item.descripcion
        producto.precio = item.precio
        producto.stock = item.stock

        db.commit()
        db.refresh(producto)

        return producto

    except HTTPException:
        raise

    except Exception as e:
        db.rollback()
        print(f"ERROR DE SISTEMA: {str(e)}")

        raise HTTPException(
            status_code=500,
            detail="Error interno del servidor"
        )


@router.delete("/{id}", status_code=204)
def eliminar_producto(
    id: int,
    db: Session = Depends(get_db),
    user: str = Depends(obtener_usuario_actual)
):
    try:
        producto = db.query(Producto).filter(Producto.id == id).first()

        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

        db.delete(producto)
        db.commit()

        return 

    except HTTPException:
        raise

    except Exception as e:
        db.rollback()
        print(f"ERROR INTERNO: {str(e)}")

        raise HTTPException(
            status_code=500,
            detail="Error interno del servidor"
        )


    
