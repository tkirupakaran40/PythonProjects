from pydantic import BaseModel

class vehicleSchema(BaseModel):
    vin: str
    vehicle_brand: str
    vehicle_model: str
    vehicle_colour: str
    vehicle_price: float
    vehicle_registered_country: str
    vehicle_registered_number: str
    vehicle_owner_firstName: str
    vehicle_owner_lastName: str
    vehicle_owner_phoneNumber: str




