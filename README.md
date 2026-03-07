# Azure Industrial Telemetry Monitoring Pipeline

## Overview

This project simulates an industrial telemetry monitoring pipeline similar to what might be used in a manufacturing or industrial environment. Sensor data is generated, placed into a message queue, processed, and stored for later analysis.

The project demonstrates how telemetry data flows through a simple processing architecture.

---

## Architecture

Sensor Simulator
      │
      ▼
Message Queue
      │
      ▼
Telemetry Processor
      │
      ▼
Stored Telemetry Data (JSON)

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
