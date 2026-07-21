import json
import os
from models.sensor import Sensor

def load_sensors(path: str = "config/sensors.json") -> list[Sensor]:
    if not os.path.exists(path):
        print("Config file not found")

    with open(path, "r") as file:
        configs = json.load(file)

    sensors = []

    for cfg in configs:
        sensor = Sensor(
            host=cfg["host"],
            rest_port=cfg["rest_port"],
            opcua_port=cfg["opcua_port"],
            name=cfg["name"],
        )
        sensors.append(sensor)
    return sensors