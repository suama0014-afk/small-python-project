def add_task(tasks:dict, title:str, status="pending") -> bool:
    """add a new task to the dictionary"""
    task = {"title":title,"status":status}
    if tasks:
        task_id = max(tasks.keys()) + 1
    else:
        task_id = 1
    tasks[task_id] = task
    return True

def delete_task(tasks:dict,task_id:int) -> bool:
    """delete task from dictionary"""
    if task_id in tasks:
        tasks.pop(task_id)
        return True
    else:
        print(f"No task with ID:{task_id}")
        return False
def update_task_status(tasks:dict,task_id:int, new_status:str) -> bool:
    """update status of task"""
    if task_id in tasks:
        tasks[task_id]['status'] = new_status
        return True
    else:
        print(f"No task with ID:{task_id}")
        return False
def display_tasks(tasks:dict) -> None:
    if not tasks:
        print("No tasks!")
        return 
    for key,value in tasks.items():
        print(f"ID:{key} title:{value['title']} status:{value['status']}")

def main():
    tasks = {}
    while True:
        print("--- Task Tracker ---")
        print("1. Add task\n" \
              "2. display tasks\n" \
              "3. update task\n" \
              "4. delete task\n" \
              "5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            title = input("Enter task name: ").strip()
            add_task(tasks,title)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            try:
                task_id = int(input("Enter task id: ").strip())
            except ValueError:
                print("you should Enter integer number")
            else:
                new_status = input("Enter the new status: ").strip()
                update_task_status(tasks,task_id,new_status)
        elif choice == "4":
            try:
                task_id = int(input("Enter task id: ").strip())
            except ValueError:
                print("you should enter integer number")
            else:
                delete_task(tasks, task_id)
        elif choice == "5":
            break
if __name__ == "__main__":
    main()