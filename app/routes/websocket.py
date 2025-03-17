from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import app.services.sensor_service as sensor_service
import asyncio

router = APIRouter()

class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        print("Client connected via WebSocket")

    async def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
            print("Client disconnected")

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except:
                await self.disconnect(connection)

manager = ConnectionManager()

async def keep_connection_alive(websocket: WebSocket):
    try:
        while True:
            await asyncio.sleep(20)  # Gửi ping mỗi 20 giây
            await websocket.send_text("ping")
    except Exception as e:
        print(f"Heartbeat error: {e}")

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    
    # Tạo task cho heartbeat
    heartbeat_task = asyncio.create_task(keep_connection_alive(websocket))
    
    try:
        while True:
            try:
                message = await websocket.receive_text()
                if message == "ping":
                    continue  # Bỏ qua tin nhắn ping
                    
                print(f"Received: {message}")
                
                parts = message.split(";")
                temperature = float(parts[0].strip())
                air_pressure = float(parts[1].strip())
                air_humidity = float(parts[2].strip())
                rainfall = float(parts[3].strip())
                soil_humidity = float(parts[4].strip())
                water_level = float(parts[5].strip())

                # Lưu vào database
                sensor_service.process_sensor_data(
                    rainfall, soil_humidity, air_humidity, 
                    air_pressure, temperature, water_level
                )
                
                # Gửi dữ liệu cho tất cả clients
                await manager.broadcast(message)
                
            except (ValueError, IndexError) as e:
                print(f"Invalid data format: {e}")
                continue
                
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
    except Exception as e:
        print(f"Error: {e}")
        await manager.disconnect(websocket)
    finally:
        heartbeat_task.cancel()  # Hủy task heartbeat khi kết thúc