import PySimpleGUI as sg

import functions
import time
import os

if not os.path.exists("todos.txt"):
    with open ("todos.txt","w") as file:
        pass
sg.theme("Black")
label_1 = sg.Text("Type a todo")
clock = sg.Text(" ", key="clock")
Input_Box = sg.InputText(tooltip="Enter a Todo", key="todo")
add_button = sg.Button("Add", size=10)
edit_button = sg.Button("Edit", size=10)
complete_button = sg.Button("Complete", size=10)
exit_button = sg.Button("Exit", size=10)
list_box = sg.Listbox(values=functions.get_todo(), key="todos", enable_events=True, size=(45, 10))
window = sg.Window("My Todo",
                   layout=[[clock],
                           [label_1],
                           [Input_Box, add_button],
                           [list_box, edit_button],
                           [complete_button],
                           [exit_button]],
                   font=('Helvetica', 10))
while True:
    event, value = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%d %b %Y  Time - %H:%M:%S"))
    match event:
        case 'Add':
            todos = functions.get_todo()
            todo = value['todo']
            todo = todo + "\n"
            todos.append(todo)
            functions.to_write(todos)
            window["todos"].update(values=todos)
        case 'Edit':
            try:
                todos = functions.get_todo()
                todo_edit = value['todos'][0]
                new_todo = value['todo']
                idx = todos.index(todo_edit)
                todos[idx] = new_todo
                functions.to_write(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please Select Something ", font=("Helvetica", 10))
        case 'todos':
            window["todo"].update(value=value['todos'][0])
        case 'Complete':
            try:
                todos = functions.get_todo()
                complete_todo = value['todos'][0]
                todos.remove(complete_todo)
                functions.to_write(todos)
                window["todos"].update(values=todos)
                window["todo"].update(values="")
            except IndexError:
                sg.popup("Please Select Something ", font=("Helvetica", 10))
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()