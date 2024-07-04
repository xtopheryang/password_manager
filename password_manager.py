import random
import string
import json
import os

PASSWORD_FILE = "service_passwords.txt"


def load_passwords():
    if not os.path.exists(PASSWORD_FILE):
        return {}
    with open(PASSWORD_FILE, "r") as file:
        return json.load(file)


def save_passwords(passwords):
    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file)


def generate_password(length=12):
    """Generate a Random Password (Alphanumeric + symbols)"""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def password_length():
    length_input = input("Enter password length (press Enter to use default length of 12): ")
    if length_input == "":
        length = 12
    elif length_input.isdigit() and int(length_input) > 0:
        length = int(length_input)
    else:
        print(f"Invalid Length. Please Try Again!")
        length = password_length()
    return length

def get_password(service):
    """Retrieve a password for existing service, otherwise generate a one."""
    passwords = load_passwords()
    if service in passwords:
        return passwords[service]
    else:
        print(f"Service '{service}' not found. The system will generate a password.")
        length = password_length()
        new_password = generate_password(length)
        passwords[service] = new_password
        save_passwords(passwords)
        return new_password


def get_services():
    passwords = load_passwords()
    return list(passwords.keys())

def main_menu():
    os.system('cls')
    print("PASSWORD MANAGER")
    print("1. Retrieve a Service Password")
    print("2. Display all Services")
    print("3. Exit")
    return input("Enter your choice: ")

def back_to_main():
    input("Press Enter to go back to Main Menu...")
    password_manager()

def password_manager():
    choice = main_menu()
    match choice:
        case "1":
            os.system('cls')
            service = input("Enter the service name: ")
            password = get_password(service)
            print(f"Password for '{service}': {password}")
            back_to_main()
        case "2":
            os.system('cls')
            services = get_services()
            if services:
                print("Services:")
                for service in services:
                    print(f" - {service}")
            else:
                print("No services stored.")
            back_to_main()

        case "3":
            print("Exiting Password Manager, Thank you.")
        case _:
            os.system('cls')
            input("Invalid Input, Press Enter to go back to Main Menu...")
            back_to_main()

password_manager()
