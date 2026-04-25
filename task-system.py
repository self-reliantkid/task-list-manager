from utils import get_current_date, clear_screen, gen_id


date = get_current_date()


def empty_list(tasks_list):
    tasks_list[date] = {}
    return tasks_list



def add_task(task, priority, tasks_list):

    ids = list(tasks_list[date].keys())
    last_id = max(ids) if ids else "000"

    task_id = int(last_id) + 1
    task_id = gen_id(task_id)

    task_details = [task, priority, "uncomplete", date, task_id]

    tasks_list[date][task_id] = task_details

    return tasks_list



def view_tasks(tasks_list):
    print(f"Tasks for today, {date}")

    for task in tasks_list[date]:
        print(f"\nTask ID: {tasks_list[date][task][-1]}")
        print(f"Task: {tasks_list[date][task][0]}")
        print(f"Priority: {tasks_list[date][task][1]}")
        print(f"Status: {tasks_list[date][task][2]}")