#fucntional programming
#going to implement this in a to-do list
import json, os
print("Welcome!")
#lets load json files
def jsonFileloadOrCreation():
    pyDir = os.path.dirname(os.path.abspath(__file__))
    JStodoList = os.path.join(pyDir, "TodoList.json")
    if not os.path.exists(JStodoList):
        # if there isn't one, make a fresh one
        with open(JStodoList, "w") as creation:
            json.dump({}, creation)
        print(f"{JStodoList} has been made")
    else:
        print("loading to-do lists")
    return JStodoList

def clearterminal(): os.system('cls' if os.name == 'nt' else 'clear')

def mainMenu():
    #cleat terminal for menu
    clearterminal()
    #writing them like this so i can check if each one can be done
    #also a lot easier to read
    print("1. View to-do's")
    print("2. Add to-do")
    print("3. Toggle completion")
    print("4. Delete To-do")
    print("5 (or nothing). exit program")

    MenuSelect = int(input())

    clearterminal()
    match MenuSelect:
        case 1:
            ViewTodo()
        case 2:
            AddTodo()
        case 3:
            ToggleCompletion()
        case 4:
            DeleteTodo()
        case 5:
            exit
        case _:
            print("please input a valid expression")
            mainMenu()


def ViewTodo():
    dataLoad = jsonFileloadOrCreation()
    with open(dataLoad, "r") as y:
        TodoList = json.load(y)
    
    print("your To-do list: ")
    for taskNum, Todo in TodoList.items():
        completion = "[x]" if Todo["completed"] else "[ ]"
        print(f"{taskNum}: {Todo['task']} {completion}")

    input("press any key to exit")

    mainMenu()

def AddTodo():
    dataLoad = jsonFileloadOrCreation()
    with open(dataLoad, "r") as y:
        TodoList = json.load(y)
    #pull the json file and add a value to the task list
    #firstly find how many "tasks" there are
    numTasks = 0
    if isinstance(TodoList, dict): #sees if array has objects
        numTasks = len(TodoList)
    else:
        numTasks = 0

    Newtask = str(input("what task would you like to add?: "))
    NewTaskNumber = f"task {numTasks + 1}"
    TodoList[NewTaskNumber] = {"task" : Newtask, "completed" : False}
    
    with open(dataLoad, "w") as JSON:
        json.dump(TodoList, JSON)
    print("task added")
    input()
    mainMenu()
 

def ToggleCompletion():
    #need to create file firstly
    #but list out all the to-do's with a [x] to show that the are completed
    print("read comments")
    input()
    mainMenu()

def DeleteTodo():
    dataLoad = jsonFileloadOrCreation()
    with open(dataLoad, "r") as y:
        TodoList = json.load(y)
    #show what tasks to remove
    print(TodoList)
    numTasks = 0
    if isinstance(TodoList, dict): #sees if array has objects
        numTasks = len(TodoList)
    else:
        numTasks = 0

    taskRemoveNum = str(input("what task would you like to remove?: "))
    del TodoList[f"task {taskRemoveNum}"]

    with open(dataLoad, "w") as JSON:
        json.dump(TodoList, JSON)
    print("task removed")
    input()
    mainMenu()

#main running program
mainMenu()




    

