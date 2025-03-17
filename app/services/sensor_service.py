# app/services/sensor_service.py
import app.database as database
from app.SensorData import SensorData

def process_sensor_data(rainfall, soil_humidity, air_humidity, air_pressure, temperature, water_level):
    sensor_data = SensorData(
        rainfall=rainfall,
        soil_humidity=soil_humidity,
        air_humidity=air_humidity,
        air_pressure=air_pressure,
        temperature=temperature,
        water_level=water_level
    )
    return database.save_sensor_data(sensor_data)
