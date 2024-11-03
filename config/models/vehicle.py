from sqlalchemy import Table, Column, String
from config.db import meta

vehicles = Table(
    'vehicles', meta,
    Column('vin', String(255), primary_key=True),
    Column('vehicle_brand', String(255)),
    Column('vehicle_model', String(255)),
    Column('vehicle_colour', String(255)),
    Column('vehicle_price', String(255)),
    Column('vehicle_registered_country', String(255)),
    Column('vehicle_registered_number', String(255)),
    Column('vehicle_owner_firstName', String(255)),
    Column('vehicle_owner_lastName', String(255)),
    Column('vehicle_owner_phoneNumber', String(255))

)








