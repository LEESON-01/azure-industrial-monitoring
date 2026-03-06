import random
import time

def generate_sensor_data():
    temperature = random.uniform(70, 120)
    pressure = random.uniform(10, 30)
    vibration = random.uniform(0, 5)

    data = {
        "temperature": round(temperature, 2),
        "pressure": round(pressure, 2),
        "vibration": round(vibration, 2)
    }

    return data

while True:
    sensor_data = generate_sensor_data()
    print("Sensor Telemetry:", sensor_data)
    time.sleep(2)
