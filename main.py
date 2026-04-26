import time
import sys
from utils import clear_screen, delay
from task_system import empty_list, add_task, view_tasks, mark_complete, change_priority, delete_task


tasks_database = empty_list({})


def main_menu():
    while True:
        clear_screen()
        print("Task List Manager")
        print(" 1. Add task")
        print(" 2. View tasks")
        print(" 3. Manage tasks")
        print(" 4. Exit")

        try:
            user_choice = int(input("\nYour choice: "))

            if user_choice not in range(1, 5):
                clear_screen()
                print("Option not in menu. Try again!")
            else:
                if user_choice == 1:
                    add_task_menu(tasks_database)
                elif user_choice == 2:
                    view_tasks_menu()
                elif user_choice == 3:
                    manage_tasks_menu()
                elif user_choice == 4:
                    exit()
        except ValueError:
            clear_screen()
            print("Invalid input! Try again!")



def add_task_menu(data):
    clear_screen()
    task = input("Enter task: ")
    priority = input("Enter priority (low/medium/high): ")
    data = add_task(task, priority, data)

    clear_screen()
    print("Task successfully added!")
    time.sleep(0.8)



def view_tasks_menu():
    clear_screen()
    view_tasks(tasks_database)
    time.sleep(0.8)



def manage_tasks_menu():
    while True:
        clear_screen()
        print("Manage Tasks")
        print(" 1. Modify task")
        print(" 2. Delete task")
        print(" 3. Clear tasks")
        print(" 4. Return to main menu")
        print(" 5. Exit")

        try:
            user_choice = int(input("\nYour choice: "))

            if user_choice not in range(1, 6):
                clear_screen()
                print("Option not in menu. Try again!")
            else:
                if user_choice == 1:
                    modify_task_menu()
                elif user_choice == 2:
                    delete_task_menu(tasks_database)
                elif user_choice == 3:
                    clear_tasks_menu(tasks_database)
                elif user_choice == 4:
                    main_menu()
                elif user_choice == 5:
                    exit()
        except ValueError:
            clear_screen()
            print("Invalid input! Try again!")



def modify_task_menu():
    while True:
        clear_screen()

        print("Modify Task")
        print(" 1. Change task priority")
        print(" 2. Mark task as completed")
        print(" 3. Return to manage tasks menu")
        print(" 4. Return to main menu")
        print(" 5. Exit")

        try:
            user_choice = int(input("\nYour choice: "))

            if user_choice not in range(1, 6):
                clear_screen()
                print("Option not in menu. Try again!")
            else:
                if user_choice == 1:
                    change_priority_menu(tasks_database)
                elif user_choice == 2:
                    mark_complete_menu(tasks_database)
                elif user_choice == 3:
                    manage_tasks_menu()
                elif user_choice == 4:
                    main_menu()
                elif user_choice == 5:
                    exit()
        except ValueError:
            clear_screen()
            print("Invalid input! Try again!")



def change_priority_menu(data):
    clear_screen()
    id = input("Enter task ID: ")
    priority = input("Enter priority (low/medium/high): ")
    data = change_priority(id, priority, data)



def mark_complete_menu(data):
    clear_screen()
    id = input("Enter task ID: ")
    data = mark_complete(id, data)



def delete_task_menu(data):
    clear_screen()
    id = input("Enter task ID: ")
    data = delete_task(id, data)

    # clear_screen()
    # print("Task successfully deleted!")
    # time.sleep(0.8)



def clear_tasks_menu(data):
    data = empty_list({})

    clear_screen()
    print("All tasks successfully cleared!")
    time.sleep(0.8)



def exit():
    clear_screen(1.25)
    print("Quitting program", end="")
    delay()
    clear_screen()
    sys.exit("Program exit successful")

    

if __name__ == "__main__":
    main_menu()