# Essence Client

## Description
**Essence Client** is a Python application for controlling and reading data from industrial acceleration sensors. It communicates with multiple sensors simultaneously via **REST** (for status, triggering measurements, and reading data) and **OPC UA** (for writing configuration values), stores measurement data locally, and visualizes it using **Matplotlib**.

[![Python](https://img.shields.io/badge/Language-Python%203.11-blue.svg)](https://www.python.org/)
[![OPC UA](https://img.shields.io/badge/Protocol-OPC%20UA-green.svg)](https://opcfoundation.org/about/opc-technologies/opc-ua/)
[![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-orange.svg)](https://matplotlib.org/)

## Key Features
* **Multi-Sensor Support:** Control and read from multiple sensors simultaneously, configured via a simple JSON file.
* **Dual-Protocol Communication:**
    * **REST API** for status checks, triggering measurements, and retrieving raw data.
    * **OPC UA** for writing configuration and control values (e.g. measurement intervals, data saving settings).
* **Local Caching:** Automatically stores raw measurement data as timestamped JSON files, organized per sensor.
* **Data Visualization:** Compare acceleration data (X/Y/Z axes) across multiple sensors, with optional mean-centering to highlight deviations between sensors.
* **Interactive CLI:** Simple menu-driven interface for pinging sensors, starting measurements, managing cache, and plotting results.

## Tech Stack
* **Language:** Python 3.11
* **Communication:** `requests` (REST), `opcua` (OPC UA client)
* **Visualization:** Matplotlib, NumPy
* **Configuration:** JSON-based sensor configuration

---

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Credits](#credits)

## Installation

```bash
git clone https://github.com/ReitererJulian/essence-client.git
cd essence-client
pip install -r requirements.txt
```

Copy the example sensor configuration and add your own sensors:

```bash
cp config/sensors.example.json config/sensors.json
```

Edit `config/sensors.json` with your sensor details:

```json
[
  {
    "name": "SENSOR_NAME",
    "host": "SENSOR_IP",
    "rest_port": "REST_PORT",
    "opcua_port": "OPCUA_PORT"
  }
]
```

## Usage

Run the client:

```bash
python main.py
```

You'll be presented with a menu:

```text
=========================
ESSENCE CLIENT
=========================
1. Ping sensor (status)
2. Single Measurement and save raw data
3. Wipe Cache
4. Show Plots
5. Toggle writing JSON
6. Apply default Settings
0. Exit 
=========================
```

- **Ping sensors** – checks connectivity to all configured sensors
- **Single Measurement** – triggers a measurement on all sensors and saves the raw data locally
- **Wipe Cache** – clears all locally stored measurement files
- **Show Plots** – select and compare measurement files across sensors, with optional mean-centering
- **Toggle writing JSON** – enables/disables raw data saving on a selected sensor
- **Apply default Settings** – applies the default settings specified in `config/default_settings.json`

> To take single measurements, you must first enable writing JSON on the sensors you want to measure

## Project Structure

```
app/
├── cache/              # Locally stored measurement data (per sensor)
├── config/             # Sensor configuration
├── core/                # Cache management, plotting, config loading
├── models/             # Sensor class (REST + OPC UA communication)
└── main.py             # CLI entry point
```

## Credits

**Developer:**
- [Reiterer Julian](https://github.com/ReitererJulian)