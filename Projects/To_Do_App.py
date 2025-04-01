def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            status = "[Done]" if task["done"] else "[Pending]"
            print(f"{index}. {task['name']} {status}")


def add_task(tasks):
    task_name = input("Enter task name: ")
    tasks.append({"name": task_name, "done": False})
    print("Task added successfully!")


def mark_as_done(tasks):
    show_tasks(tasks)
    try:
        task_index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_index = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Task '{removed_task['name']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = []
    while True:
        print("\nTo-Do List Menu:")
        print("1) Show tasks")
        print("2) Add task")
        print("3) Mark as done")
        print("4) Delete task")
        print("5) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_as_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
