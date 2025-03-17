# app/main.py
from fastapi import FastAPI
from app.routes import sensor_routes, websocket

app = FastAPI()

# Đăng ký router
app.include_router(sensor_routes.router, prefix="/api")
app.include_router(websocket.router)