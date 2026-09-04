import os
import csv
from datetime import datetime, date
from task import Task

TASK_FILE = "tasks.csv"
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
        
def load_tasks(filename=TASK_FILE):
    task_list = []

    if not os.path.exists(filename):
        return task_list

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                due_date = None

                if row["due_date"]:
                    due_date = datetime.strptime(
                        row["due_date"], "%Y-%m-%d"
                    ).date()

                completed = row["completed"].lower() == "true"

                task = Task(
                    row["title"],
                    due_date,
                    completed
                )

                task_list.append(task)

    except (OSError, KeyError, ValueError) as error:
        print(f"Could not load tasks: {error}")

    return task_list

def save_tasks(task_list, filename=TASK_FILE):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["title", "due_date", "completed"]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            for task in task_list:
                writer.writerow({
                    "title": task.title,
                    "due_date": (
                        task.due_date.isoformat()
                        if task.due_date
                        else ""
                    ),
                    "completed": task.completed
                })

        print("Tasks saved successfully.")

    except OSError as error:
        print(f"Could not save tasks: {error}")



