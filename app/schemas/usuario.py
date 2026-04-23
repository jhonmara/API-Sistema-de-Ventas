from pydantic import BaseModel, Field, validator

class UsuarioCreate(BaseModel):
    username: str = Field(..., min_length=3)
    password: str
    @validator('username')
    def username_must_not_have_spaces(cls, v):
        return v.strip()

class UsuarioResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True