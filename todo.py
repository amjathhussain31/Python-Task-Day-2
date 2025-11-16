todo_list = []

def show_menu():
    print("\n------ TO-DO LIST ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("------------------------")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        todo_list.append(task)
        print("Task added!")

    elif choice == "2":
        if not todo_list:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        if not todo_list:
            print("No tasks to delete!")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")

            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(todo_list):
                    removed = todo_list.pop(task_num - 1)
                    print(f"Deleted: {removed}")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid input, try again!")
