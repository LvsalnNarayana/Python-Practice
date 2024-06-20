from texttable import Texttable

t = Texttable()
tasks = list(
    (
        {"description": "Task 1", "status": "Incomplete"},
        {"description": "Task 2", "status": "Incomplete"},
    )
)


def action_performer(option):
    if option == 1:
        task_input = input("Enter your task description here :\t")
        tasks.append(dict(description=task_input, status="Incomplete"))
    elif option == 2:
        delete_task_input = input("Enter your task id to delete :\t")
        if int(delete_task_input) <= len(tasks):
            tasks.pop(int(delete_task_input) - 1)
        else:
            print("Task not exist")
    elif option == 3:
        update_taskid_input = input("Enter your task number to upadte :\t")
        if int(update_taskid_input) <= len(tasks):
            update_task_info = input("Enter your updated task info :\t")
            tasks[int(update_taskid_input) - 1]["description"] = update_task_info
        else:
            print("Task not exist")
    elif option == 4:
        update_taskid_input = input("Enter your task number to upadte :\t")
        if int(update_taskid_input) <= len(tasks):
            tasks[int(update_taskid_input) - 1]["status"] = "Completed"
        else:
            print("Task not exist")


while True:
    t = Texttable()
    t.add_row(["Id", "Description", "Status"])
    for i, task in enumerate(tasks, start=1):
        t.add_row([i, task["description"], task["status"]])
    print(t.draw())

    print("=====================================================")
    print("Choose an Option")
    print("1) Create New task")
    print("2) Delete a task")
    print("3) Update a task")
    print("4) Mark task as complete")
    option_input = input("Enter your option here :\t")
    if option_input.isdigit() and int(option_input) in (1, 2, 3, 4):
        action_performer(int(option_input))
    else:
        print("Enter correct option")
