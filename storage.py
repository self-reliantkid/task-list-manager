import json
from task_system import date


def save_records(info):
    with open("tasks.json", "w") as file:
        json.dump(info, file)



def load_records():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file) or {date: {}}
    except FileNotFoundError:
        return {date: {}}
    except json.JSONDecodeError:
        return {date: {}}
