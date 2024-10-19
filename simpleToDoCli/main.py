user_input = ""
counter = 1

def write_to_the_files(task):
    with open("todos.txt", "a") as file:
        file.writelines(str(counter) + "- " + task + '\n')

def read_from_file():
    print("Showing the task: ")
    with open("todos.txt", "r") as file:
        return file.readlines()

def write_all_tasks_to_file(tasks):
    with open("todos.txt", "w") as file:
        file.writelines(tasks)

while user_input != "exit":
    user_input = input("What do you want to do? 1-Add 2-Show 3-Edit 4-Delete 5-Exit ").strip()
    match user_input:
        case "1":
                task = ""
                while task != "done":
                    task = input("What is your task? type done to return ").strip()
                    if task != "done":
                        write_to_the_files(task)
                        counter += 1

        case "2" :
            for task in read_from_file():
                task.strip()
                print(task)

        case "3" :
            todo_number = input("enter the number of the task you want to edit: type canel to return ")
            if todo_number != "cancel":
                existing_todos = read_from_file()
                print(f'Your current number {todo_number} is {existing_todos[int(todo_number) - 1]} how do you want to change it? type cancel to return: ')
                updated_todo = input().strip()
                if updated_todo != "cancel":
                    existing_todos[int(todo_number) - 1] = f"{todo_number}- " + updated_todo
                    write_all_tasks_to_file(existing_todos)
                    print("done")

        case "4" :
            todo_number = input("enter the number of the task you want to delete: type cancel to return ")
            if todo_number != "cancel":
                todos.pop(int(todo_number) - 1)
                print("Done")

        case "5" :
            print("Exiting....")
            exit()