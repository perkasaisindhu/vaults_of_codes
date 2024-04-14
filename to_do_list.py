# Function to add a task
def add_task(todo_list, task):
    todo_list.append({"task": task, "completed": False})
    print("Task added successfully!")

# Function to delete a task
def delete_task(todo_list, index):
    if index < 0 or index >= len(todo_list):
        print("Invalid index!")
    else:
        del todo_list[index]
        print("Task deleted successfully!")

# Function to display the list of tasks
def display_tasks(todo_list):
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for i, item in enumerate(todo_list):
            print(f"{i+1}. {'[X]' if item['completed'] else '[ ]'} {item['task']}")

# Function to mark a task as complete
def mark_complete(todo_list, index):
    if index < 0 or index >= len(todo_list):
        print("Invalid index!")
    else:
        todo_list[index]['completed'] = True
        print("Task marked as complete!")

def main():
    todo_list = []

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Mark Task as Complete")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(todo_list, task)
        elif choice == '2':
            index = int(input("Enter the index of task to delete: ")) - 1
            delete_task(todo_list, index)
        elif choice == '3':
            display_tasks(todo_list)
        elif choice == '4':
            index = int(input("Enter the index of task to mark as complete: ")) - 1
            mark_complete(todo_list, index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
