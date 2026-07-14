import glob
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
        if entry == ".gitkeep":
            continue

        path = os.path.join(folder, entry)

        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

    print("Cache wiped successfully")

def list_files(sensor_name: str) -> list[str]:
    folder = f"cache/{sensor_name}"
    files = glob.glob(f"{folder}/*.json")
    files.sort(key=os.path.getmtime, reverse=True)
    return files

def get_latest_file(sensor_name: str):
    files = list_files(sensor_name)
    return files[0] if files else None