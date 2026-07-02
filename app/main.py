import api.api_client as api
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
    while True:
        show_menu()
        user_input = input("Choose an option: ")

        if user_input == "1":
            print("Pinging sensor...")
            api.ping()
            print("-------------------")
        elif user_input == "2":
            print("Starting single measurement...")
            api.single_measurement()
            time.sleep(1)
            api.save_raw()
            print("-------------------")
        elif user_input == "3":
            print("Wiping cache...")
            api.wipe_cache()
            print("-------------------")
        elif user_input == "4":
            break


if __name__ == "__main__":
    main()