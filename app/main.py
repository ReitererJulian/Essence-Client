from core import cache
from models.sensor import Sensor
import time

def show_menu():
    print("\n=========================")
    print("      ESSENCE CLIENT      ")
    print("=========================")
    print("1. Ping sensor (status)")
    print("2. Single Measurement and save raw data")
    print("3. Wipe Cache")
    print("4. Exit")

def main():
    sensor_fc = Sensor("ESF00000000fc2f4839", "8700", name="fc2f4839")
    sensor_56 = Sensor("SES00000000567f49fa", "8700", name="567f49fa")

    sensor_fc_file_link = f"{sensor_fc.rest_base_url}cache/50c6e2d8-7259-4da2-adce-74fc7edfc14b-raw.json"
    sensor_56_file_link = ""

    while True:
        show_menu()
        user_input = input("Choose an option: ")

        if user_input == "1":
            print("Pinging sensors...")
            print("-------------------")
            print("Sensor: " + sensor_fc.name)
            sensor_fc.ping()
            print("-------------------")
            print("Sensor: " + sensor_56.name)
            sensor_56.ping()
            print("-------------------")
        elif user_input == "2":
            print("Starting single measurement...")
            sensor_fc.single_measurement()
            sensor_56.single_measurement()
            time.sleep(1)
            cache.save_raw(sensor_fc.get_raw(sensor_fc_file_link), sensor_fc.name)
            cache.save_raw(sensor_56.get_raw(sensor_56_file_link), sensor_56.name)
            print("-------------------")
        elif user_input == "3":
            print("Wiping cache...")
            cache.wipe_cache()
            print("-------------------")
        elif user_input == "4":
            break

if __name__ == "__main__":
    main()