from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app import models, schemas

async def create_marca(db: AsyncSession, marca: schemas.MarcaCreate):
    db_marca = models.Marca(**marca.dict())
    db.add(db_marca)
    await db.commit()
    await db.refresh(db_marca)
    return db_marca

async def create_modelo(db: AsyncSession, modelo: schemas.ModeloCreate):
    db_modelo = models.Modelo(**modelo.dict())
    db.add(db_modelo)
    await db.commit()
    await db.refresh(db_modelo)
    return db_modelo

async def create_auto(db: AsyncSession, auto: schemas.AutoCreate):
    db_auto = models.Auto(**auto.dict())
    db.add(db_auto)
    await db.commit()
    await db.refresh(db_auto)
    return db_auto

async def get_autos(db: AsyncSession):
    result = await db.execute(select(models.Auto))
    return result.scalars().all()
