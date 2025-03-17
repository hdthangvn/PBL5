import os
# Cấu hình kết nối đến InfluxDB
INFLUXDB_URL = "http://localhost:8086"  
INFLUXDB_TOKEN = "WBw6sQ9y9vTJR-HjIwAXMCjEuJIPOI2mCVwS9gRB-XpY7WDNmMYSPzrH7p3Lk2A4QR3D9oiEiWIc99zmsyXI3w=="  
INFLUXDB_ORG = "SAP"
INFLUXDB_BUCKET = "PBL5"

# Cấu hình truy vấn dữ liệu
QUERY_RANGE = "-1h"  # Lấy dữ liệu trong vòng 1 giờ qua
