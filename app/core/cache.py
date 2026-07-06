import time
import json
import os
import shutil

def save_raw(data, sensor_name: str) -> None:
    current_time = time.strftime("%Y-%m-%d %H-%M-%S")
    folder = f"cache/{sensor_name}"

    if not os.path.exists(folder):
        os.makedirs(folder)

    file_name = f"{folder}/raw-{current_time}.json"

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def wipe_cache(folder: str = "cache") -> None:
    entries = os.listdir(folder)
    for entry in entries:
        path = os.path.join(folder, entry)
        shutil.rmtree(path)
    print("Cache wiped successfully")