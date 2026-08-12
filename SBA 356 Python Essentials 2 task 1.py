class Task:
    def __init__(self, title, due_date=None, completed=False):
        self.title = title
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        status = "X" if self.completed else "-"
        return f"[{status}] {self.title} (due {self.due_date})"


# Test code
task1 = Task("Submit assignment", "2025-03-10")

print(task1)

task2 = Task("Submit assignment", "2025-03-10", True)

print(task2)