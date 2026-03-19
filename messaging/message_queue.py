import json
import os
import time

QUEUE_DIR = "message_bus"

os.makedirs(QUEUE_DIR, exist_ok=True)

def send_to_queue(data):
    filename = f"{QUEUE_DIR}/{int(time.time()*1000)}.json"

    with open(filename, "w") as f:
        json.dump(data, f)

    print("Telemetry added to queue")

def get_from_queue():
    files = os.listdir(QUEUE_DIR)

    if not files:
        return None

    file_path = os.path.join(QUEUE_DIR, files[0])

    with open(file_path, "r") as f:
        data = json.load(f)

    os.remove(file_path)

    return data
