# Initiate the task list
tasks = {}
# Welcome message to user
print("Welcome to the task manager")
print("Add, Update, Delete, View")
# Asks the user which action to do
user_response = input("What would you like to do?\n")
# View-only action has one step
if user_response.lower() == "view":
  print(tasks)
  quit()
# Else, proceeds with asking the task name 
task_name = input("What is the name of the task?\n")
# Checking if task exist or does not exist, in the next 3 lines below
if user_response.lower() == "add" and task_name in tasks:
  print("Task already exists")
  quit()

if user_response.lower() == "update" and task_name not in tasks:
  print("Task does not exist")
  quit()

if user_response.lower() == "delete" and task_name not in tasks:
  print("Task does not exist")
  quit()
# Else, proceeds with asking the task description
task_description = input("What is the description of the task?\n")

# Task assessing
def task_assesor(user_response, task_name, task_description):
  user_response_desensitized = user_response.lower()
  if user_response_desensitized == "add":
      tasks[task_name] = task_description
      quit()
  elif user_response_desensitized == "update":
      tasks[task_name] = task_description
      quit()
  elif user_response_desensitized == "delete":
      del tasks[task_name]
      quit()
# But if the user decides to delete, update, or add, they go through a condition
if user_response.lower() == "delete" and task_name in tasks:
  task_assesor(user_response, task_name, task_description)
  quit()

if user_response.lower() == "update" and task_name in tasks:
  task_assesor(user_response, task_name, task_description)
  quit()

if user_response.lower() == "add" and task_name not in tasks:
  task_assesor(user_response, task_name, task_description)
  quit()
