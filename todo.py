def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour task list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task['completed'] else "✗"
            print(f"{i}. [{status}] {task['task']}")

def add_task(tasks):
    task_name = input("Enter the task: ")
    tasks.append({"task": task_name, "completed": False})
    print(f"Task '{task_name}' added.")

def mark_task_completed(tasks):
    task_number = int(input("Enter the task number to mark as completed: "))
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    task_number = int(input("Enter the task number to delete: "))
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' deleted.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
