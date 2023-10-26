import datetime
tasks = {}


def add_task(name, deadline):
    tasks[name] = deadline



def display_tasks():
    if not tasks:
        print("No tasks to display.")
        return

    sorted_tasks = sorted(tasks.items(), key=lambda x: x[1])
    for task, deadline in sorted_tasks:
        remaining_time = deadline - datetime.datetime.now()
        print(f"Task: {task}, Deadline: {deadline}, Time Remaining: {remaining_time}")

def time_until_next_task():
    if not tasks:
        print("No tasks to display.")
        return

    next_task, next_deadline = min(tasks.items(), key=lambda x: x[1])
    remaining_time = next_deadline - datetime.datetime.now()
    print(f"Time until next task '{next_task}': {remaining_time}")

def mark_task_completed(name):
    if name in tasks:
        del tasks[name]
        print(f"Task '{name}' is complete.")
    else:
        print(f"Task '{name}' not found.")


# Main program loop
while True:
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Time Until Next Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        name = input("Enter task name: ")
        deadline_str = input("Enter task deadline (YYYY-MM-DD HH:MM): ")
        try:
            deadline = datetime.datetime.strptime(deadline_str, '%Y-%m-%d %H:%M')
            add_task(name, deadline)
            print("Task added successfully.")
        except ValueError:
            print("Invalid datetime format. Use 'YYYY-MM-DD HH:MM'.")

    elif choice == '2':
        display_tasks()

    elif choice == '3':
        time_until_next_task()

    elif choice == '4':
        name = input("Enter task name to mark as complete: ")
        mark_task_completed(name)

    elif choice == '5':
        break

    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5).")

print("Goodbye")









