import tkinter as tk
from processor import calculate
import json

li = []

#call calculate
def call_calculate():
    with open('inter.json', 'r') as file:
        data = json.load(file)

    val1 = calculate(data)
    data["result"] = val1
    data["input_value"] = 0
    with open('inter.json', 'w') as file:
            json.dump(data, file, indent=4)  

# changes beign made to json file
def save_changes(cmd_list):
    with open('inter.json', 'r') as file:
        data = json.load(file)

    if cmd_list is None:  
        data["result"] = 0
        data["operator"] = ''
        data["input_value"] = 0
       
    else:
        if cmd_list[0].isdigit():
            data["result"] = cmd_list[0]
        else:            
            data["result"] = 0

        data["operator"] = cmd_list[1]

        if cmd_list[2].isdigit():
            data["input_value"] = cmd_list[2]
        else:            
            data["input_value"] = 0

    with open('inter.json', 'w') as file:
        json.dump(data, file, indent=4)

def getter(text):
    if text == '=':
        call_calculate()
    if text == 'AC':
        save_changes(None)
        li.clear()
        return
    if len(li) < 3:
        li.append(text)
    else:
        save_changes(li)
        li.clear()


def create_button(text, row, column):
    button = tk.Button(root, text=text, command=lambda: getter(text), width=7, height=7)
    button.grid(row=row, column=column, sticky="nsew")
    return button


root = tk.Tk()
root.geometry("500x500")

elements = [["1", "4", "7", "AC"], ["2", "5", "8", "0"], ["3", "6", "9", "="], ["+", "-", "*", "/"]]

# Create buttons for each element in the grid
for i, row in enumerate(elements):
    for j, element in enumerate(row):
        create_button(element, i, j)

root.mainloop()
