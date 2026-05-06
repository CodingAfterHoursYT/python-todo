import os
from task import Task
from file import load_tasks, save_tasks

# Clear the screen - used whenever we "refresh"
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Prompt the user for a new task to add to an existing list
def add_task(tasks):
    clear_screen()
    print("Please enter a new item:")
    newItem = input()
    tasks.append(Task(newItem))
    save_tasks(tasks)

# Mark a task as completed - this does not delete the task
def complete_task(tasks, num):
    tasks[num].completed = True
    save_tasks(tasks)

# Delete any tasks which have been marked as completed
def clear_tasks(tasks):
    filteredTasks = [task for task in tasks if not task.completed]
    save_tasks(filteredTasks)
    return filteredTasks

# Print out the list of tasks
def print_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "✔️ " if task.completed == True else "❌"
        print(str(i + 1) + ". " + status + " " + task.description)

def main():
    # Initialise our list of tasks and message
    tasks = load_tasks()
    message = ""
    running = True

    # Continue around the UI loop until told otherwise (q option)
    while running:

        # User interface printing
        clear_screen()
        if message: 
            print(message)
            print("")
            message = ""
        print("ToDo:")
        print("")
        if tasks:
            print_tasks(tasks)
            print("")
        print("Select a number to complete an item, press A to add a new item, press R to remove completed items or press Q to quit.")
        print("")

        # Get input
        option = input()

        # Handle input
        if option == 'Q' or option == 'q':
            running = False

        elif option == 'A' or option == 'a':
            add_task(tasks)
            
        elif option == 'R' or option == 'r':
            tasks = clear_tasks(tasks)

        else:
            try:
                num = int(option)
                if num < 1 or num > len(tasks):
                    message = "Invalid input"
                else:
                    complete_task(tasks, num - 1)
            except:
                message = "Invalid input"

if __name__ == "__main__":
    main()