import PySimpleGUI as sg

sg.theme('Dark Grey 13')

def button1():
    print('Button 1')

def button2():
    print('Button 2')

def button3():
    print("button 3")

dispatch_dictionary = {
    '1':button1,
    '2':button2,
    '3':button3
}

layout = [[sg.Text('Click a button', auto_size_text=True)],
          [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Quit()]]

window = sg.Window('>:)', layout)

while True:
    event, value = window.read()
    if event in ('Quit', sg.WIN_CLOSED):
        break
    if event in dispatch_dictionary:
        func_to_call = dispatch_dictionary[event]
        func_to_call()
    else:
        print('Event {} not in dispatch dictionary'.format(event))

window.close()
