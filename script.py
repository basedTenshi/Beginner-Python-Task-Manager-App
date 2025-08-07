tasks = {}
def taskAdd():
    print("You are now adding a task, please enter the task name and description")
    taskName = input("Please enter the task name: ")
    taskDescription = input("Please enter the task's description: ")
    if taskName == "" or taskDescription == "":
        print("Please enter a name and description")
    elif taskName in tasks.keys():
        print("Task already exists")
    else:
        tasks[taskName] = taskDescription

def taskView():
    print("You are now viewing your tasks")
    print(tasks)

def taskDelete():
    print("You are now deleting a task, please enter the task name")
    taskName = input("Please enter the task name: ")
    if taskName == "":
        print("Please enter a name")
    elif taskName not in tasks.keys():
        print("Task does not exists")
    else:
        del tasks[taskName]

actionList = {"add": taskAdd, "view": taskView, "delete": taskDelete}

print("Welcome to the task manager")
print("Add, Delete, View")
taskAction = input("What would you like to do?")

def task_input_checker(response):
   userResponse = response.lower()
   for action in actionList.keys():
       if action == userResponse:
           return actionList[action]()






