import time
program_running = True
add_task_running = False
add_multiple_tasks_running = False
remove_task_running = False
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
        add_task_running =True
        while add_task_running:
            add_task_option_selection = input ("Choose an option: ")
            if add_task_option_selection == "1":
                task_added = input ("New Task: ")
                tasks.append (task_added)
                add_task_running = False
                print("Task "+""" " """+task_added+""" " """+" added")
            elif add_task_option_selection == "2":
                add_multiple_tasks_running = True
                print("""Write "back" if you want to exit this mode\n""")
                while add_multiple_tasks_running:
                    task_added = input ("New Task: ")
                    if task_added == "back":
                        add_multiple_tasks_running = False
                        add_task_running = False
                    else:
                        tasks.append (task_added)
                        print ("Task "+""" " """+task_added+""" " """+" added")
            elif add_task_option_selection == "3":
                add_task_running = False
            else:
                print("Please choose a correct option: 1,2 or 3")
    elif selection == "2":
        print("You have selected -View Tasks-")
        print("YOUR TASKS:")
        print ("-------------------------")
        if not tasks:
            print("Your tasks list is empty.")
        else:
            indexed_tasks = list(enumerate(tasks, start=1))
            for numero, tarea in indexed_tasks:
                print (str(numero) + ".",tarea)
        print ("--------------------------")
    elif selection == "3":
        remove_task_running = True
        while remove_task_running:
            print("You have selected -Delete Task-")
            task_removed = input ("Enter the number of the task to be removed: ")
            print("YOUR TASKS:")
            print ("-------------------------")
            print (str(numero) + ".",tarea)
            print ("--------------------------")
        if task_removed != numero:
            print("Please Choose a correct option.")
        elif task_removed == numero:
            tasks.remove (numero)
            print("Your Tasks list has been updated!")            
    elif selection == "4":
        print ("You have selected -Exit-")
        program_running = False
    else:
        print("Please choose a correct option: 1,2,3 or 4")