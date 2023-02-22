import time


def get_todos():
    with open('todos.txt', 'r') as locally:
        local_todos = locally.readlines()
        """This is the code for getting todos from the txt file"""
    return local_todos


def write_todos(local_todo):
    with open('todos.txt', 'w') as writer:
        writer.writelines(local_todo)
        """This is the code for writing todos on the txt file"""
    return "Success"


def get_today():
    """The details of the day can be obtained by this function """
    print("Today's details are ", time.strftime("%d %b %Y  Time - %H:%M:%S"))
