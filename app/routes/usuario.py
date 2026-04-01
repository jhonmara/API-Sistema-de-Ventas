from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioResponse

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioResponse)
def crear_usuario(item: UsuarioCreate, db: Session = Depends(get_db)):
    
    usuario_existente = db.query(Usuario).filter(Usuario.username == item.username).first()

    if usuario_existente:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    nuevo_usuario = Usuario(
        username=item.username,
        password=item.password
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario