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
    sensor_fc = Sensor("ESF00000000fc2f4839", "8700", "4840", name="fc2f4839")
    sensor_56 = Sensor("SES00000000567f49fa", "8700", "4840", name="567f49fa")

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
            time.sleep(5)

            sensor_fc_file_link = sensor_fc.get_link()
            sensor_56_file_link = sensor_56.get_link()

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