from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.database import SessionLocal
from app.schemas import schemas
from app.crud import crud

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/marcas/", response_model=schemas.Marca)
async def crear_marca(marca: schemas.MarcaCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_marca(db, marca)

@router.post("/modelos/", response_model=schemas.Modelo)
async def crear_modelo(modelo: schemas.ModeloCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_modelo(db, modelo)

@router.post("/autos/", response_model=schemas.Auto)
async def crear_auto(auto: schemas.AutoCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_auto(db, auto)

@router.get("/autos/", response_model=list[schemas.Auto])
async def listar_autos(db: AsyncSession = Depends(get_db)):
    return await crud.get_autos(db)
