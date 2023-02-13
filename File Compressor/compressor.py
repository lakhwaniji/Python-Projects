import PySimpleGUI as sg
import zipfunctions
label1 = sg.Text("Select Files To Compress")
input_1 = sg.Input()
choose_button1 = sg.FilesBrowse("Browse", key="files")
label2 = sg.Text("Select Destination Folder")
input_2 = sg.Input()
choose_button2 = sg.FolderBrowse("Browse", key="folder")
choose_button3 = sg.Button("Compress")
output = sg.Text("", text_color="Green", key="output")
window = sg.Window("File Compressor",
                   layout=[[label1, input_1, choose_button1],
                           [label2, input_2, choose_button2],
                           [choose_button3],
                           [output]])
while True:
    event, values = window.read()
    if sg.WIN_CLOSED:
        break
    filepaths = values['files'].split(";")
    folderpath = values['folder']
    zipfunctions.make_archive(filepaths, folderpath)
    window["output"].update(value="Compression Completed")
window.close()
