from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class Marca(Base):
    __tablename__ = "marcas"
    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, unique=True, index=True)

    modelos = relationship("Modelo", back_populates="marca")

class Modelo(Base):
    __tablename__ = "modelos"
    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, index=True)
    marca_id = Column(Integer, ForeignKey("marcas.id"))

    marca = relationship("Marca", back_populates="modelos")
    autos = relationship("Auto", back_populates="modelo")

class Auto(Base):
    __tablename__ = "autos"
    id = Column(Integer, primary_key=True, index=True)
    color = Column(String)
    anio = Column(Integer)
    estado = Column(String)
    modelo_id = Column(Integer, ForeignKey("modelos.id"))

    modelo = relationship("Modelo", back_populates="autos")
