tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def mark_completed(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

def view_todo_list():
    print("\nTo-Do List:")
    for index, task in enumerate(tasks, start=1):
        status = "Complete" if task["completed"] else "Incomplete"
        print(f"{index}. {task['task']} - {status}")

def main():
    print("Welcome to the To-Do List App! ✨")

    while True:
        print("\n1. Add a new task\n2. Mark a task as completed\n3. View the to-do list\n0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
            print("Task added successfully!")

        elif choice == '2':
            view_todo_list()
            task_index = int(input("Enter the index of the task to mark as completed: "))
            mark_completed(task_index - 1)

        elif choice == '3':
            view_todo_list()

        elif choice == '0':
            print("Exiting the To-Do List App. Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
