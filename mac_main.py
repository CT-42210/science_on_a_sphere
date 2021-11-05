import PySimpleGUI as sg
import serial

sg.theme('Dark Grey 13')

ser = serial.Serial('/dev/tty.usbmodem102',9600)

def button1():
    encoded = str.encode("15,15\n")
    ser.write(encoded)

def button2():
    encoded = str.encode("0,15\n")
    ser.write(encoded)

def button3():
    encoded = str.encode("15,0\n")
    ser.write(encoded)

def button4():
    encoded = str.encode("0,0\n")
    ser.write(encoded)

dispatch_dictionary = {
    '1':button1,
    '2':button2,
    '3':button3,
    '4':button4
}

layout = [[sg.Text('Click a button', auto_size_text=True)],
          [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'), sg.Quit()]]

window = sg.Window('>:)', layout)

def byte_machine(string):

    # string with encoding 'utf-8'
    arr = bytes(string, 'utf-8')
    arr2 = bytes(string, 'ascii')

    print(arr, '\n')

    # actual bytes in the the string
    for byte in arr:
        print(byte, end=' ')
    print("\n")
    for byte in arr2:
        print(byte, end=' ')

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
