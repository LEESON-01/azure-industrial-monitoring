# Industrial Telemetry Processing Pipeline

## 🌍 Real-World Use Case

This project models a cloud-based industrial telemetry system similar to those used in manufacturing plants, power stations, and industrial environments.

It simulates how sensor data (temperature, pressure, vibration) is:

* Generated from industrial equipment
* Ingested through a messaging layer
* Processed for monitoring and analysis

This type of architecture is commonly used in:

* Predictive maintenance systems
* Real-time equipment monitoring
* Industrial IoT (IIoT) platforms

My background in industrial operations directly influenced the design of this system.


---

## 🏗️ Architecture

```id="yrrd9r"
Sensor Simulator
     ↓
Message Queue (Decoupling Layer)
     ↓
Telemetry Processor (Python Service)
     ↓
Stored Telemetry Data (JSON / Future DB)
```
---

## ☁️ Cloud Architecture Extension

This system is designed to be extended into a full cloud-native solution:

* Message Queue → Azure Service Bus
* Processing Service → Azure Functions or Container Apps
* Storage → Azure Blob Storage / Cosmos DB
* Monitoring → Azure Monitor & Log Analytics

This demonstrates how traditional industrial systems can be modernized using cloud technologies.



---

## 🧠 Engineering Decisions

* Used a **message queue pattern** to decouple data ingestion from processing
* Simulated real-world telemetry patterns based on industrial systems
* Designed system to be **event-driven**, improving scalability and fault tolerance
* Structured code to allow easy transition to cloud-native services

This reflects real-world system design used in distributed and industrial cloud platforms.

---

## 🏭 Industrial Context

With 13+ years in industrial operations, I designed this system based on real plant conditions:

* Continuous data generation from equipment
* Need for reliable and fault-tolerant processing
* Importance of monitoring critical parameters (temperature, pressure, vibration)

This project bridges the gap between industrial systems and modern cloud engineering.

---

## Components

### Sensor Simulator
Generates simulated industrial telemetry data including:

- Temperature
- Pressure
- Vibration
- Timestamp

The simulator produces telemetry events at regular intervals.

Location:
app/sensor_simulator.py

---

### Message Queue
Acts as the communication layer between the telemetry generator and the processing service.

Location:
messaging/message_queue.py

---

### Telemetry Processor
Consumes telemetry messages from the queue and stores them for later use.

Location:
processor/telemetry_processor.py

---

### Storage
Telemetry data is stored locally in JSON format.

Location:
stored_data/telemetry.json

---

## Infrastructure

Infrastructure resources can be provisioned using Terraform (Infrastructure as Code).

Location:
infrastructure/terraform/main.tf

---

## Technologies Used

- Python
- Message Queue Architecture
- Docker
- Terraform (Infrastructure as Code)
- JSON Data Storage

---

## Running the Project

Run the telemetry simulator:

python3 -m app.sensor_simulator

Run the telemetry processor:

python3 -m processor.telemetry_processor

---

## Example Telemetry Data

{
 "timestamp": "2026-03-07T10:11:26.780453",
 "temperature": 89.79,
 "pressure": 26.85,
 "vibration": 3.57
}

---

## Purpose

This project demonstrates the flow of telemetry data through a simple monitoring pipeline and illustrates concepts used in cloud-based monitoring systems.
