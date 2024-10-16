todos = []
user_input = ""

while user_input != "exit":
    user_input = input("What do you want to do? 1-Add 2-Show 3-Exit ")
    match user_input:
        case "1":
            task = ""
            while task != "done":
                task = input("what is your task? type done to return ")
                if task != "done":
                    todos.append(task)
        case "2" :
            print(todos)
        case "3" :
            print("Exiting....")
            exit()