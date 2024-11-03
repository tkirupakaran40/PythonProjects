from fastapi import APIRouter
from config.db import conn
from config.models.index import vehicles
from config.schemas.index import vehicleSchema
import logging
import os
from sqlalchemy import create_engine, Table, MetaData, select

vehicle = APIRouter()

log_file_path = os.path.join(os.path.dirname(__file__), 'app.log')

logging.basicConfig(
    filename=log_file_path,         # Absolute path to the log file
    filemode='a',                   # Append mode ('w' for overwrite)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    level=logging.INFO              # Log level
)


@vehicle.get("/getVehicle")
async def fetch_data():
    result = conn.execute(vehicles.select()).fetchall
    #result = conn.execute(select(vehicles)).fetchall
    logging.info("This is a debug message.")
    return result  # Converting each row to a dictionary
    
     


@vehicle.get("/{vin}")
async def fetch_by_Vin(vin:str):
    logging.INFO(vin)
    result = conn.execute(vehicles.select().where(vehicles.c.vin==vin)).fetchall
    logging.INFO("This is a debug message. VIN")
    logging.INFO(result)
    return result

@vehicle.post("/InsertVehicleData")
async def write_data(vehicle:vehicleSchema):
    conn.execute(vehicles.insert().values(
        vin=vehicle.vin,
        vehicle_brand=vehicle.vehicle_brand,
        vehicle_model=vehicle.vehicle_model,
        vehicle_colour=vehicle.vehicle_colour,
        vehicle_price=vehicle.vehicle_price,
        vehicle_registered_country=vehicle.vehicle_registered_country,
        vehicle_registered_number=vehicle.vehicle_registered_number,
        vehicle_owner_firstName=vehicle.vehicle_owner_firstName,
        vehicle_owner_lastName=vehicle.vehicle_owner_lastName,
        vehicle_owner_phoneNumber=vehicle.vehicle_owner_phoneNumber

    ))
    return conn.execute(vehicles.select()).fetchall

@vehicle.put("/{vin}")
async def update_data(vin:str, vehicle: vehicleSchema):
    conn.execute(vehicles.update().values(
        vin=vehicle.vin,
        vehicle_brand=vehicle.vehicle_brand,
        vehicle_model=vehicle.vehicle_model,
        vehicle_colour=vehicle.vehicle_colour,
        vehicle_price=vehicle.vehicle_price,
        vehicle_registered_country=vehicle.vehicle_registered_country,
        vehicle_registered_number=vehicle.vehicle_registered_number,
        vehicle_owner_firstName=vehicle.vehicle_owner_firstName,
        vehicle_owner_lastName=vehicle.vehicle_owner_lastName,
        vehicle_owner_phoneNumber=vehicle.vehicle_owner_phoneNumber

    ).where(vehicles.c.vin == vin))
    return conn.execute(vehicles.select()).fetchall

@vehicle.delete("/deleteVehicle")
async def delete_data(vin:str):
    conn.execute(vehicles.delete().where(vehicles.c.vin == vin))
    return conn.execute(vehicles.select()).fetchall


