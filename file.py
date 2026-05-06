import json 
from task import Task 

FILENAME = "todo.json"

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            data = json.load(file)
            return [Task.from_dict(item) for item in data]
    except:
        return []

