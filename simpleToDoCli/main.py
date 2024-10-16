todos = []
user_input = ""

while user_input != "exit":
    user_input = input("What do you want to do? 1-Add 2-Show 3-Edit 4-Exit ").strip()
    match user_input:
        case "1":
            task = ""
            while task != "done":
                task = input("what is your task? type done to return ").strip()
                if task != "done":
                    todos.append(task)
        case "2" :
            print("Showing the tasks: ")
            for i in range(0, len(todos)):
                print(f'number {i+1} task is {todos[i]}\n')
        case "3" :
            todo_number = input("enter the number of the task you want to edit: type canel to return ")
            if todo_number != "cancel":
                existing_todo = todos[int(todo_number)-1]
                print(f'Your current number {todo_number} is {existing_todo} how do you want to change it? type cancel to return: ')
                updated_todo = input().strip()
                if updated_todo != "cancel":
                    todos[int(todo_number)-1] = updated_todo
                    print("done")
        case "4" :
            print("Exiting....")
            exit()