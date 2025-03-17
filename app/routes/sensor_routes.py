from fastapi import APIRouter
from app.SensorData import SensorData
from app.services.sensor_service import process_sensor_data
from app.database import get_latest_data

router = APIRouter()

@router.post("/upload-data/")
def upload_data(data: SensorData):
    return process_sensor_data(
        rainfall=data.rainfall,
        soil_humidity=data.soil_humidity,
        air_humidity=data.air_humidity,
        air_pressure=data.air_pressure,
        temperature=data.temperature,
        water_level=data.water_level
    )

@router.get("/latest-data/")
def latest_data():
    return get_latest_data()