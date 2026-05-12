from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioResponse
from app.auth.auth import crear_token
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import hash_password, verify_password

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.post("/", response_model=UsuarioResponse, status_code=201)
def crear_usuario(item: UsuarioCreate, db: Session = Depends(get_db)):
    
    usuario_existente = db.query(Usuario).filter(Usuario.username == item.username).first()

    if usuario_existente:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    nuevo_usuario = Usuario(
        username=item.username,
        password=hash_password(item.password)
    )

    db.add(nuevo_usuario)

    try:
        db.commit()
        db.refresh(nuevo_usuario)
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al guardar usuario")

    return nuevo_usuario

@router.post("/login", status_code=200)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(Usuario).filter(Usuario.username == form_data.username).first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=401,
            detail="Usuario o contraseña incorrectos"
        )
    token = crear_token({"sub": user.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }