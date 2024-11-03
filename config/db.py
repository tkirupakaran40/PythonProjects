'''
from sqlalchemy import create_engine, MetaData, Select

DATABASE_USERNAME = "root"
DATABASE_PASSWORD = "root1234"  # Replace with your actual password
DATABASE_HOST = "localhost"
DATABASE_PORT = "3306"
DATABASE_NAME = "vehicle_details"

# Create the engine with username and password
engine = create_engine(f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}")
#engine = create_engine("mysql+pymysql://root:root1234@localhost:3306/vehicle_details")
#engine = create_engine("mysql+pymysql://root:root1234@localhost:3306/vehicle_details")

meta = MetaData()
conn = engine.connect()
'''


####################

from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from .models import vehicle  # Import your Base from models.py

DATABASE_URL = "mysql+asyncmy://root:root1234@localhost/vehicle_details"

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create async session
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


