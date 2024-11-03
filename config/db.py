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





