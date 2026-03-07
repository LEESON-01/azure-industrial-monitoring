import queue

telemetry_queue = queue.Queue()

def send_to_queue(data):
    telemetry_queue.put(data)
    print("Telemetry added to queue")

def get_from_queue():
    if not telemetry_queue.empty():
        data = telemetry_queue.get()
        return data
    return None
