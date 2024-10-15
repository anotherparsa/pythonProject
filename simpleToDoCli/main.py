todos = []
user_input = ""
while user_input != "exit":
    user_input  = input("what is your task? type exit to exit the app: ")
    todos.append(user_input)
    print(user_input)

print("All Todos")
print(todos)