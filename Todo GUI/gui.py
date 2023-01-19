import PySimpleGUI as sg

import functions


label_1 = sg.Text("Type a todo")
Input_Box = sg.InputText(tooltip="Enter a Todo", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
list_box = sg.Listbox(values=functions.get_todo(), key="todos", enable_events=True, size=(45, 10))
window = sg.Window("My Todo",
                   layout=[[label_1], [Input_Box, add_button], [list_box, edit_button], [complete_button],[exit_button]],
                   font=('Helvetica', 10))
while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case 'Add':
            todos = functions.get_todo()
            todo = value['todo']
            todo = todo + "\n"
            todos.append(todo)
            functions.to_write(todos)
            window["todos"].update(values=todos)
        case 'Edit':
            todos = functions.get_todo()
            todo_edit = value['todos'][0]
            new_todo = value['todo']
            idx = todos.index(todo_edit)
            todos[idx] = new_todo+"\n"
            functions.to_write(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window["todo"].update(value=value['todos'][0])
        case 'Complete':
            todos = functions.get_todo()
            complete_todo = value['todos'][0]
            todos.remove(complete_todo)
            functions.to_write(todos)
            window["todos"].update(values=todos)

        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()
