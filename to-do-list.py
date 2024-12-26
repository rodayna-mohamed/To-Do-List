
tasks = [] 
def add_task(task): 
    tasks.append(task) 
    print(f"Task added: {task}")

def view_tasks(): 
    if not tasks: 
        print("Your to-do list is empty.") 
    else: 
        print("Your tasks:") 
    for i, task in enumerate(tasks, start=1): 
        print(f"{i}. {task}") 

def mark_task_complete(index): 
    if 0 <= index < len(tasks): 
        completed_task = tasks.pop(index) 
        print(f"Task completed: {completed_task}") 
    else: 
        print("Invalid task number.") 

def delete_task(index): 
    if 0 <= index < len(tasks): 
        deleted_task = tasks.pop(index) 
        print(f"Task deleted: {deleted_task}") 
    else: 
        print("Invalid task number.")
        

def main(): 
    while True: 
        print("\nOptions:") 
        print("1. Add Task") 
        print("2. View Tasks") 
        print("3. Mark Task Complete") 
        print("4. Delete Task") 
        print("5. Exit") 
        choice = input("Choose an option: ").strip() 
        if choice == "1": 
            task = input("Enter a new task: ") 
            add_task(task) 
        elif choice == "2": 
            view_tasks() 
        elif choice == "3": 
            index = int(input("Enter the task number to mark as complete: ")) - 1 
            mark_task_complete(index) 
        elif choice == "4": 
            index = int(input("Enter the task number to delete: ")) - 1 
            delete_task(index)
        elif choice == "5": 
            print("Goodbye!") 
            break 
        else: 
            print("Invalid choice. Please try again.") 
            
if __name__ == "__main__": 
    main()