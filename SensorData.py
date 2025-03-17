from pydantic import BaseModel

class SensorData(BaseModel):
    rainfall: float  # Đo lượng mưa
    soil_humidity: float  # Độ ẩm đất
    air_humidity: float  # Độ ẩm không khí
    air_pressure: float  # Áp suất không khí
    temperature: float  # Nhiệt độ
    water_level: float  # Mực nước

    def __repr__(self):
        return (
            f"water_level={self.water_level})"
            f"SensorData(rainfall={self.rainfall}, soil_humidity={self.soil_humidity}, "
            f"air_humidity={self.air_humidity}, air_pressure={self.air_pressure}, "
            # f"humidity={self.humidity}, water_level={self.water_level})"
        )

    def to_dict(self):
        return {
            'rainfall': self.rainfall,
            'humidity': self.humidity,
            'air_humidity': self.air_humidity,
            'air_pressure': self.air_pressure,
            'temperature': self.temperature,
            'water_level': self.water_level
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            rainfall=data['rainfall'],
            humidity=data['humidity'],
            air_humidity=data['air_humidity'],
            air_pressure=data['air_pressure'],
            temperature=data['temperature'],
            water_level=data['water_level']
        )
