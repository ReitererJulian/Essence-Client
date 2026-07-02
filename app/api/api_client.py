import os

from app.core.config import REST_BASE_URL
import requests
import time
import json

def check_status(status_code: int) -> None:
    if status_code == 200:
        print("Status: OK | Code: 200")
    else:
        print(f"Status: Error | Code: {status_code}")

def ping() -> None:
    url = REST_BASE_URL + "status"
    request = requests.get(url)
    check_status(request.status_code)

def get_raw():
    url = REST_BASE_URL + "cache/50c6e2d8-7259-4da2-adce-74fc7edfc14b-raw.json"
    request = requests.get(url)
    return request.json()

def save_raw() -> None:
    data = get_raw()
    current_time = time.strftime("%Y-%m-%d %H-%M-%S")
    file_name = f"cache/raw-{current_time}.json"

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def single_measurement():
    url = REST_BASE_URL + "measurement.start.single.measurement"
    request = requests.post(url)
    check_status(request.status_code)

def wipe_cache():
    files = os.listdir("cache")
    if not files:
        print("No files to wipe")
        return

    for file in files:
        os.remove(os.path.join("cache", file))

    print("Cache wiped successfully")