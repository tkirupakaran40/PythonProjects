from sqlalchemy import Table, Column, String, Float, create_engine

#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Vehicle(Base):
    __tablename__ = 'vehicles'

    vin = Column(String(255), primary_key=True)
    vehicle_brand = Column(String(255))
    vehicle_model = Column(String(255))
    vehicle_colour = Column(String(255))
    vehicle_price = Column(Float)
    vehicle_registered_country = Column(String(255))
    vehicle_registered_number = Column(String(255))
    vehicle_owner_firstName = Column(String(255))
    vehicle_owner_lastName = Column(String(255))
    vehicle_owner_phoneNumber = Column(String(255))
    
    




