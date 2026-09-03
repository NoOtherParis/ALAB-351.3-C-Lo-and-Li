from todolist import add_task, complete_task, delete_task, list_tasks


tasks = []

while True:

    print("\n(A) Add a new task")
    print("(C) Mark a task as completed")
    print("(D) Delete a task")
    print("(L) List all tasks")
    print("(Q) Quit")

    choice = input("Choose an option: ").upper()

    if choice == "A":
        title = input("Enter task title: ")
        due_date = input("Enter due date (YYYY-MM-DD), or press Enter for none: ")

        if due_date == "":
            due_date = None

        add_task(tasks, title, due_date)

    elif choice == "C":
        try:
            index = int(input("Enter the task index to complete: "))
            complete_task(tasks, index)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "D":
        try:
            index = int(input("Enter the task index to delete: "))
            delete_task(tasks, index)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "L":
        list_tasks(tasks)

    elif choice == "Q":
        save_choice = input("Would you like to save your task list? (Y/N): ").upper()

        if save_choice == "Y":
            with open("tasks.txt", "w") as file:
                for task in tasks:
                    file.write(str(task) + "\n")

            print("Task list saved to tasks.txt.")

        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select A, C, D, L, or Q.")