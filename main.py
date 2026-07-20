import time
program_running = True
tasks =[]
while program_running:
    print("""===== TASK MANAGER =====

    1. Add Task

    2. View Tasks

    3. Delete Task

    4. Exit""")
    time.sleep(0.2)
    selection = input("Choose an option: ")
    if selection == "1":
        print("You have selected -Add Task-")
        task_added = input ("New Task: ")
        tasks.append (task_added)
        print("Your Tasks list has been updated!")
    elif selection == "2":
        print("You have selected -View Tasks-")
        print(str(tasks))
    elif selection == "3":
        print("You have selected -Delete Task-")
        task_removed = input ("Remove a task: ")
        tasks.remove (task_removed)
        print("Your Tasks list has been updated!")
    elif selection == "4":
        print ("You have selected -Exit-")
        program_running = False
    else:
        print("Please choose a correct option: 1,2,3 or 4")