from pydantic import BaseModel

class MarcaBase(BaseModel):
    descripcion: str

class MarcaCreate(MarcaBase):
    pass

class Marca(MarcaBase):
    id: int
    class Config:
        orm_mode = True

class ModeloBase(BaseModel):
    descripcion: str
    marca_id: int

class ModeloCreate(ModeloBase):
    pass

class Modelo(ModeloBase):
    id: int
    class Config:
        orm_mode = True

class AutoBase(BaseModel):
    color: str
    anio: int
    estado: str
    modelo_id: int

class AutoCreate(AutoBase):
    pass

class Auto(AutoBase):
    id: int
    class Config:
        orm_mode = True
