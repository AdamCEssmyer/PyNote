import os
import database

def main_menu():
    global clear_needed
    if clear_needed:
        def clear_screen():
            os.system('cls' if os.name == 'nt' else 'clear')
        clear_needed = False
    else:
        clear_screen()
    print("Welcome to the main menu")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Exit")
    choice = input("Enter your choice: ")

    import random
    import string

    def random_CIN(length: int) -> str:
        result_CIN = ''.join(random.choices(string.digits, k=length));
        return result_CIN;

        def create_console():
            print("Input new debtor database\n")

            while True:
                cin = random_CIN(8)
                if not is_duplicate_cin(cin):
                    break;

    def is_duplicate_cin(cin_to_check):
        try:
            with open(database.DB_CUSTOMERS, 'r') as file:
                for line in file:
                    cin = line.strip().split(",")[0]
                    if cin == cin_to_check:
                        print("Duplicate CIN found. Please try again.")
                        return True
            return False
        except FileNotFoundError:
            return False
        except Exception as e:
            print(f"An error occurred while checking for duplicate CIN: {e}")
            return True


                            

    
    
    
    
    
    