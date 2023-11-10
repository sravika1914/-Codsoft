 # Define an empty list to store tasks
tasks = []
# Define an empty list to store tasks
tasks = []

# Function to add a task to the to-do list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' has been added to the to-do list.")

# Function to display the to-do list
def display_tasks():
    if not tasks:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to remove a task from the to-do list
def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' has been removed from the to-do list.")
    else:
        print("Invalid task index.")

# Main loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Display tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '2':
        display_tasks()
    elif choice == '3':
        display_tasks()
        task_index = int(input("Enter the index of the task to remove: "))
        remove_task(task_index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")