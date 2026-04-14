from pydantic import BaseModel, Field
from typing import Optional

class ProductoCreate(BaseModel):
    nombre: str = Field(..., min_length=3)
    descripcion: Optional[str] = None
    precio: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)

class ProductoResponse(ProductoCreate):
    id: int

    class Config:
        from_attributes = True