from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    username: str
    password: str

class UsuarioResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True