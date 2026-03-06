import random
import time
import json
from datetime import datetime

def generate_sensor_data():
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "temperature": round(random.uniform(70, 120), 2),
        "pressure": round(random.uniform(10, 30), 2),
        "vibration": round(random.uniform(0, 5), 2)
    }

    return data

while True:
    telemetry = generate_sensor_data()
    print(json.dumps(telemetry))
    time.sleep(2)
