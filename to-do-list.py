
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