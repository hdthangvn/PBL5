import asyncio
import websockets
import random
import logging
from websockets.exceptions import ConnectionClosed

# Thiết lập logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def connect_and_send():
    uri = "ws://10.10.59.182:8080/ws"
    
    while True:  # Vòng lặp vô hạn để duy trì kết nối
        try:
            async with websockets.connect(uri, ping_interval=30, ping_timeout=300) as websocket:
                logger.info("Connected to WebSocket server")
                
                while True:  # Vòng lặp gửi dữ liệu
                    try:
                        # Tạo dữ liệu giả lập
                        temperature = random.uniform(20.0, 30.0)
                        air_pressure = random.uniform(1000.0, 1020.0)
                        air_humidity = random.uniform(30.0, 70.0)
                        rainfall = random.uniform(0.0, 100.0)
                        soil_humidity = random.uniform(20.0, 50.0)
                        water_level = random.uniform(0.0, 10.0)

                        # Định dạng dữ liệu
                        data = f"{temperature:.2f};{air_pressure:.2f};{air_humidity:.2f};{rainfall:.2f};{soil_humidity:.2f};{water_level:.2f}"
                        
                        # Gửi dữ liệu
                        await websocket.send(data)
                        logger.info(f"Sent: {data}")

                        # Đợi 5 giây trước khi gửi mẫu tiếp theo
                        await asyncio.sleep(5)

                    except ConnectionClosed:
                        logger.warning("Connection closed, attempting to reconnect...")
                        break
                    except Exception as e:
                        logger.error(f"Error during data sending: {e}")
                        break

        except Exception as e:
            logger.error(f"Connection error: {e}")
            logger.info("Retrying connection in 5 seconds...")
            await asyncio.sleep(5)

async def main():
    while True:
        try:
            await connect_and_send()
        except Exception as e:
            logger.error(f"Main loop error: {e}")
            await asyncio.sleep(5)

if __name__ == "__main__":
    logger.info("Starting ESP8266 simulator...")
    asyncio.run(main())
