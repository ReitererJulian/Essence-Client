from core import cache
from core.config import load_sensors
from models.sensor import Sensor
from core.plot import *
import time

def show_menu():
    print("\n=========================")
    print("      ESSENCE CLIENT      ")
    print("=========================")
    print("1. Ping sensor (status)")
    print("2. Single Measurement")
    print("3. Wipe Cache")
    print("4. Show Plots")
    print("5. Toggle writing JSON")
    print("6. Apply default Settings")
    print("0. Exit")
    print("=========================")

def select_files(sensor_name: str):
    files = cache.list_files(sensor_name)

    if not files:
        print("No files found for the selected sensor.")
        return None

    print(f"Select a file to plot for {sensor_name}):")
    print("0. Newest file ")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")

    choice = input("Select a file number:")

    if choice == "0":
        return files[0]
    else:
        try:
            index = int(choice) - 1
            return files[index] if 0 <= index < len(files) else None
        except ValueError:
            print("Invalid input. Please enter a number between 0 and the number of files.")
            return None

def select_sensor(sensors: list[Sensor]):
    print("Select a sensor:")
    for i, sensor in enumerate(sensors, 1):
        print(f"{i}. {sensor.name}")

def toggle_json_write(sensors: list[Sensor]):
    select_sensor(sensors)
    choice = input("Enter choice: ")

    try:
        index = int(choice) - 1
        sensor = sensors[index] if 0 <= index < len(sensors) else None
    except ValueError:
        sensor = None

    if sensor is None:
        print("Invalid input.")
        return

    current = sensor.read_opcua("Storage.Control.SaveMeasurementData")
    new_value = not current
    sensor.write_opcua("Storage.Control.SaveMeasurementData", not current)
    print(f"[{sensor.name}] SaveMeasurementData: {current} -> {new_value}")

def main():
    sensors = load_sensors()

    while True:
        show_menu()
        user_input = input("Choose an option: ")

        if user_input == "1":
            print("-------------------")
            print("Pinging sensors...")
            for sensor in sensors:
                print("-------------------")
                print("Sensor: " + sensor.name)
                sensor.ping()
            print("-------------------")

        elif user_input == "2":
            print("-------------------")
            user_input = input("Trigger all sensors? (y/n): ").lower()
            if user_input == "n":
                select_sensor(sensors)
                sensor_choice = input("Enter choice: ")
                sensor = sensors[int(sensor_choice) - 1]
                sensor.single_measurement()
                time.sleep(2)
                link = sensor.get_link()
                cache.save_raw(sensor.get_raw(link), sensor.name)
            else:
                print("Triggering all sensors...")
                for sensor in sensors:
                    sensor.single_measurement()
                time.sleep(5)

                for sensor in sensors:
                    link = sensor.get_link()
                    cache.save_raw(sensor.get_raw(link), sensor.name)
            print("-------------------")

        elif user_input == "3":
            print("Wiping cache...")
            cache.wipe_cache()
            print("-------------------")

        elif user_input == "4":
            print("-------------------")
            selected_files = {}
            for sensor in sensors:
                f = select_files(sensor.name)
                if f:
                    selected_files[sensor.name] = f
            plot_compare_sensors(selected_files)
            print("-------------------")

        elif user_input == "5":
            print("-------------------")
            toggle_json_write(sensors)
            print("-------------------")

        elif user_input == "6":
            print("-------------------")
            user_input = input("Apply default settings for all sensors? (y/n): ").lower()
            if user_input == "n":
                select_sensor(sensors)
                sensor_choice = input("Enter choice: ")
                sensor = sensors[int(sensor_choice) - 1]
                sensor.apply_default_settings()
            else:
                for sensor in sensors:
                    sensor.apply_default_settings()
            print("-------------------")

        elif user_input == "0":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()