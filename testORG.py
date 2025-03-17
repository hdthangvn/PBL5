from influxdb_client import InfluxDBClient
import os

token = "WBw6sQ9y9vTJR-HjIwAXMCjEuJIPOI2mCVwS9gRB-XpY7WDNmMYSPzrH7p3Lk2A4QR3D9oiEiWIc99zmsyXI3w=="
url = "http://localhost:8086"

client = InfluxDBClient(url=url, token=token)
orgs = client.organizations_api().find_organizations()
for o in orgs:
    print(o.name)