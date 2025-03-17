# app/models.py
from pydantic import BaseModel

class SensorData(BaseModel):
    rainfall: float       # Đo lượng mưa
    soil_humidity: float  # Độ ẩm đất
    air_humidity: float   # Độ ẩm không khí
    air_pressure: float   # Áp suất không khí
    temperature: float    # Nhiệt độ
    water_level: float    # Mực nước