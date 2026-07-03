import time
import json
import os

def save_raw(data, sensor_name: str) -> None:
    current_time = time.strftime("%Y-%m-%d %H-%M-%S")
    folder = f"cache/{sensor_name}"

    if not os.path.exists(folder):
        os.makedirs(folder)

    file_name = f"{folder}/raw-{current_time}.json"

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def wipe_cache(folder: str = "cache") -> None:
    files = os.listdir(folder)
    if not files:
        print("No files to wipe")
        return
    for file in files:
        os.remove(os.path.join(folder, file))
    print("Cache wiped successfully")