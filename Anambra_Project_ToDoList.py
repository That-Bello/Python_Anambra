#
# Python Boot Camp Week 3
#
# THE PROJECT.
#
# Simple To-Do List:
# Create a to-do list application where users can add, remove,
# and view tasks. Use functions to handle different operations.


def todo_prog():
    tasks = []
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Complete Task")
        print("4. Exit")

        menu_choice = input("Enter Menu Choice: ")

        if menu_choice == '1':
            num_tasks = int(input("How many tasks do you want to add: "))
            for i in range(num_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif menu_choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif menu_choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task completed!")
            else:
                print("Invalid task number.")

        elif menu_choice == '4':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    todo_prog()

