from datetime import datetime, date
from task import Task


def add_task(task_list, title, due_date=None):
    if due_date:
        try:
            due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")
            return

    task = Task(title, due_date)
    task_list.append(task)


def complete_task(task_list, index):
    try:
        task_list[index].completed = True
    except IndexError:
        print("Invalid task index.")


def delete_task(task_list, index):
    try:
        del task_list[index]
    except IndexError:
        print("Invalid task index.")


def list_tasks(task_list):
    today = date.today()

    for index, task in enumerate(task_list):
        status = "X" if task.completed else "-"

        if task.due_date is None:
            due = "No due date"
        else:
            due = str(task.due_date)

            if task.due_date < today and not task.completed:
                due += " - OVERDUE"

        print(index, f"[{status}] {task.title} - Due: {due}")


# Test code
tasks = []

add_task(tasks, "Submit assignment", "2026-08-20")
add_task(tasks, "Study Python", "2026-08-10")
add_task(tasks, "Buy groceries")

print("Initial Tasks:")
list_tasks(tasks)

print("\nCompleting Task 1:")
complete_task(tasks, 1)
list_tasks(tasks)

print("\nDeleting Task 2:")
delete_task(tasks, 2)
list_tasks(tasks)