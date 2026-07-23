import time
program_running = True
option1_running = False
option3_running = False
option1_1_running = False
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
        print("""===== ADD TASK =====

    1. Add one task

    2. Add multiple tasks

    3. Back""")
        option1_running =True
        while option1_running:
            selection_option1 = input ("Choose an option: ")
            if selection_option1 == "1":
                task_added = input ("New Task: ")
                tasks.append (task_added)
                print("Your Tasks list has been updated!")
            elif selection_option1 == "2":
                option1_1_running = True
                print("Write ""back"" if you want to exit this mode\n")
                while option1_1_running:
                    task_added = input ("New Task: ")
                    tasks.append (task_added)
                    print ("Task "+task_added+" added")
                    if task_added == "back":
                        tasks.remove("back")
                        option1_1_running = False
            elif selection_option1 == "3":
                option1_running = False
            else:
                print("Please choose a correct option: 1,2 or 3")
    elif selection == "2":
        print("You have selected -View Tasks-")
        print("YOUR TASKS:")
        print ("-------------------------")
        if not tasks:
            print("Your tasks list is empty.")
        else:
            indice = list(enumerate(tasks, start=1))
            for numero, tarea in indice:
                print (str(numero) + ".",tarea)
        print ("--------------------------")
    elif selection == "3":
        print("You have selected -Delete Task-")
        task_removed = input ("Enter the name of the task to remove: ")
        if task_removed in tasks:
            tasks.remove (task_removed)
            print("Your Tasks list has been updated!")
        else:
            print("That task is not in your list.")
    elif selection == "4":
        print ("You have selected -Exit-")
        program_running = False
    else:
        print("Please choose a correct option: 1,2,3 or 4")