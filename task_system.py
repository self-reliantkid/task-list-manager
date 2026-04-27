import time
from utils import get_current_date, gen_id,  clear_screen


date = get_current_date()


def empty_list(tasks_list):
    tasks_list[date] = {}
    return tasks_list



def add_task(task, priority, tasks_list):

    ids = list(tasks_list[date].keys())
    last_id = max(ids) if ids else "000"

    task_id = int(last_id) + 1
    task_id = gen_id(task_id)

    task_details = [task, priority, "uncompleted", date, task_id]

    tasks_list[date][task_id] = task_details

    return tasks_list



def view_tasks(tasks_list):
    print(f"Tasks for today, {date}")

    if not tasks_list[date]:
        print("No available tasks to display!")
        time.sleep(0.5)

    else:    
        for task in tasks_list[date]:
            print(f"\nTask ID: {tasks_list[date][task][-1]}")
            print(f"Task: {tasks_list[date][task][0]}")
            print(f"Priority: {tasks_list[date][task][1]}")
            print(f"Status: {tasks_list[date][task][2]}")

        input("\nPRESS ENTER TO CONTINUE...")


def mark_complete(id, tasks_list):
    if id not in tasks_list[date]:
        print("Task ID not found!")
    else:
        clear_screen()
        print("Task marked complete!")
        time.sleep(0.8)

        tasks_list[date][id][2] = "completed"
        return tasks_list



def change_priority(id, priority, tasks_list):
    if id not in tasks_list[date]:
        print("Task ID not found!")
    else:
        clear_screen()
        print("Task priority updated!")
        time.sleep(0.8)

        tasks_list[date][id][1] = priority
        return tasks_list



def delete_task(id, tasks_list):
    if id not in tasks_list[date]:
        print("Task ID not found!")
    else:
        clear_screen()
        print("Task successfully deleted!")
        time.sleep(0.8)

        tasks_list[date].pop(id, None)
        return tasks_list
    


def clear_tasks(tasks_list):
    clear_screen()
    print("All tasks successfully cleared!")
    time.sleep(0.8)

    tasks_list[date].clear()
    return tasks_list