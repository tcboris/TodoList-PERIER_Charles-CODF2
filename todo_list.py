import os

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a task to the todo list."""
        self.tasks.append({"task": task, "completed": False})
        print(f"Task added: {task}")

    def delete_task(self, task_number):
        """Delete a task by its number."""
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task deleted: {removed_task['task']}")
        else:
            print("Invalid task number.")

    def complete_task(self, task_number):
        """Mark a task as completed by its number."""
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task completed: {self.tasks[task_number - 1]['task']}")
        else:
            print("Invalid task number.")

    def show_tasks(self):
        """Display all tasks in the todo list."""
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("\nTodo List:")
            for i, task in enumerate(self.tasks, 1):
                status = "✓" if task["completed"] else "✗"
                print(f"{i}. {task['task']} [{status}]")
        print()


def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    todo_list = TodoList()

    while True:
        clear_console()  # Clear the screen before showing the menu
        print("Todo List Application")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. Show Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "3":
            task_number = int(input("Enter task number to complete: "))
            todo_list.complete_task(task_number)
        elif choice == "4":
            todo_list.show_tasks()
            input("Press Enter to return to the menu...")  # Pause before clearing
        elif choice == "5":
            print("Exiting Todo List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        print()


if __name__ == "__main__":
    main()
