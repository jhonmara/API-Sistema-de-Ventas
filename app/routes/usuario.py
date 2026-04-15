from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioResponse
from passlib.context import CryptContext
from app.auth.auth import crear_token
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/", response_model=UsuarioResponse, status_code=201)
def crear_usuario(item: UsuarioCreate, db: Session = Depends(get_db)):
    
    usuario_existente = db.query(Usuario).filter(Usuario.username == item.username).first()

    if usuario_existente:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    password_encriptado = pwd_context.hash(item.password)

    nuevo_usuario = Usuario(
        username=item.username,
        password=password_encriptado
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario

@router.post("/login", status_code=200)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(Usuario).filter(Usuario.username == form_data.username).first()

    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=401,
            detail="Credenciales incorrectas"
        )
    token = crear_token({"sub": user.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }