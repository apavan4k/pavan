tasks = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added.")

def view_tasks():
    if not tasks:
        print("No tasks to show.")
        return
    for index, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{index}. {task['task']} [{status}]")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        deleted = tasks.pop(task_num - 1)
        print(f"Deleted: {deleted['task']}")
    except (IndexError, ValueError):
        print("Invalid task number!")

def mark_task_done():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as done: "))
        tasks[task_num - 1]["done"] = True
        print(f"Marked task {task_num} as done.")
    except (IndexError, ValueError):
        print("Invalid task number!")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        mark_task_done()
    elif choice == '5':
        print("Exiting To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose between 1 and 5.")
