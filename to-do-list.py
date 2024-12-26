
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