import sys
import os
import time
import json

# Allow imports from project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from messaging.message_queue import get_from_queue

# Determine project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Storage location
STORAGE_DIR = os.path.join(BASE_DIR, "stored_data")


def store_data(data):
    os.makedirs(STORAGE_DIR, exist_ok=True)

    file_path = os.path.join(STORAGE_DIR, "telemetry.json")

    with open(file_path, "a") as f:
        f.write(json.dumps(data) + "\n")

    print("Telemetry stored for user access")


while True:
    telemetry = get_from_queue()

    if telemetry:
        store_data(telemetry)

    time.sleep(1)
