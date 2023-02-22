import time
import modules
import os

if not os.path.exists("todos.txt"):
    with open ("todos.txt","w"):
        pass
def get_todo():
    with open('todos.txt', 'r') as locally:
        local_todos = locally.readlines()
    return local_todos


def to_write(local_todo):
    with open('todos.txt', 'w') as writer:
        writer.writelines(local_todo)
    return "Success"


def get_today():
    print("Today's details are ", time.strftime("%d %b %Y  Time - %H:%M:%S"))


get_today()


modules.info()


while True:
    user_action = input("Type add, show, edit,complete, or exit")
    user_action = user_action.strip()
    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"
        todos = get_todo()
        todos.append(todo)
        to_write(todos)
    elif user_action.startswith('show'):
        todos = get_todo()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            idx = int(user_action[5:])
            todos = get_todo()
            todos[idx - 1] = input("Enter the updated task") + "\n"
            to_write(todos)
        except ValueError:
            print("Code is Invalid")
            continue
    elif user_action.startswith('complete'):
        try:
            idx = int(user_action[9:])
            todos = get_todo()
            removed = todos.pop(idx - 1)
            print(f"Successfully removed the todo {removed}")
            to_write(todos)
        except IndexError:
            print("There is no task at this number")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is Not Valid")
