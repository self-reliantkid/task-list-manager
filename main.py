import time
import sys
from utils import clear_screen, delay
from task_system import empty_list, add_task, view_tasks


tasks_database = empty_list({})


def main_menu():
    while True:
        clear_screen()
        print("Task List Manager")
        print(" 1. Add task")
        print(" 2. View tasks")
        print(" 3. Exit")

        try:
            user_choice = int(input("\nYour choice: "))

            if user_choice not in range(1, 4):
                clear_screen()
                print("Option not in menu. Try again!")
            else:
                if user_choice == 1:
                    add_task_menu(tasks_database)
                elif user_choice == 2:
                    view_tasks_menu()
                elif user_choice == 3:
                    exit()
        except ValueError:
            clear_screen()
            print("Invalid input! Try again!")



def add_task_menu(data):
    clear_screen()
    task = input("Enter task: ")
    priority = input("Enter priority(low/medium/high): ")
    data = add_task(task, priority, data)



def view_tasks_menu():
    clear_screen()
    view_tasks(tasks_database)
    input("\nPRESS ENTER TO CONTINUE...")



def exit():
    clear_screen(1.25)
    print("Quitting program", end="")
    delay()
    clear_screen()
    sys.exit("Program exit successful")

    

if __name__ == "__main__":
    main_menu()