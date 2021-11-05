import PySimpleGUI as sg
import serial

sg.theme('Dark Grey 13')

# this is the port for my mac, to find yours go to terminal and type:
#       screen /dev/tty.usb
# then click the tab key, it should autofill the port assuming the mbed is connected
# good luck, i dont know how i did this either
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
    'Purple':button1,
    'Blue':button2,
    'Red':button3,
    'Off':button4
}

layout = [[sg.Text('Click a button', auto_size_text=True)],
          [sg.Button('Purple'), sg.Button('Blue'), sg.Button('Red'), sg.Button('Off'), sg.Quit()]]

window = sg.Window('science on a sphere', layout)

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
