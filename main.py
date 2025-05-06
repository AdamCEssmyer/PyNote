import os
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