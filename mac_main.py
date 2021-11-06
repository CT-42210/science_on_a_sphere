import PySimpleGUI as sg
import serial

sg.theme('Dark Grey 13')

# this is the port for my mac, to find yours go to terminal and type:
#       screen /dev/tty.usb
# then click the tab key, it should autofill the port assuming the mbed is connected
# good luck, i dont know how i did this either
ser = serial.Serial('/dev/tty.usbmodem11202',9600)

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


def button5():
    layout1 = [
        [sg.Text('Drag the sliders to make a custom color of blue and red.', auto_size_text=True)],
        [sg.Text('Red', auto_size_text=True),
         sg.Slider(range=(0, 15), orientation='h', size=(20,10), default_value=7, key='-RED_SLIDER-'),
         sg.Button('How It Works')],
        [sg.Text('Blue', auto_size_text=True),
         sg.Slider(range=(0, 15), orientation='h', size=(20,10), default_value=7, key='-BLUE_SLIDER-'),
         sg.Button('Binary Legend')],
        [sg.Button('Set Custom Colors'), sg.Button('Back')]
        ]


    window1 = sg.Window('Settings', layout1, keep_on_top=True, finalize=True)


    def setcustomcolors(red_brightness,blue_brightness):

        def number_fixer(input):
            if input == 0.0:
                return 0
            elif input == 1.0:
                return 1
            elif input == 2.0:
                return 2
            elif input == 3.0:
                return 3
            elif input == 4.0:
                return 4
            elif input == 5.0:
                return 5
            elif input == 6.0:
                return 6
            elif input == 7.0:
                return 7
            elif input == 8.0:
                return 8
            elif input == 9.0:
                return 9
            elif input == 10.0:
                return 10
            elif input == 11.0:
                return 11
            elif input == 12.0:
                return 12
            elif input == 13.0:
                return 13
            elif input == 14.0:
                return 14
            elif input == 15.0:
                return 15

        red_brightness_fixed = number_fixer(red_brightness)
        blue_brightness_fixed = number_fixer(blue_brightness)

        custom_color_value = f"{red_brightness_fixed},{blue_brightness_fixed}\n"

        print(custom_color_value)
        encoded = str.encode(custom_color_value)
        ser.write(encoded)

    while True:
        event, value = window1.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            if event == 'Set Custom Colors':
                setcustomcolors(value['-RED_SLIDER-'], value['-BLUE_SLIDER-'])
            elif event != 'Set Custom Colors':
                if event in ('Quit', 'Back', 'None', sg.WIN_CLOSED):
                    window1.close()
                elif event not in ('Quit', 'Back', 'None', sg.WIN_CLOSED):
                    if event in dispatch_dictionary:
                        func_to_call = dispatch_dictionary[event]
                        func_to_call()
                    else:
                        print('Event {} not in dispatch dictionary'.format(event))


def button6():
    layout2 = [[sg.Text("The MBED has 8 LED lights. 4 Red, 4 Blue. The ball changes colors from the lights shining onto "
                       "it.\nThe MBED decides what lights to light up based on binary. For example:\n1 in binary is 1. "
                       "That means only the first light will light up.\n15, in binary, is 1111. That means all the "
                       "lights will light up.\nThe MBED reads the binary through text sent over USB, which will look "
                       "like:\n[##,##] (replace the # with the value, right is red and left is blue.)\nThis is why "
                       "there are 2 sliders for custom colors. To find a key, click the 'Binary Legend' button\njust "
                       "below this one.\nHave fun, hope i made sense :) \n -Nick", auto_size_text=True)],
               [sg.Button('OK')]]

    window2 = sg.Window('How It Works', layout2, keep_on_top=True, finalize=True)

    while True:
        event, value = window2.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            if event == 'OK':
                window2.close()
            elif event != 'Set Custom Colors':
                if event in ('Quit', 'Back', 'None', sg.WIN_CLOSED):
                    window2.close()
                elif event not in ('Quit', 'Back', 'None', sg.WIN_CLOSED):
                    if event in dispatch_dictionary:
                        func_to_call = dispatch_dictionary[event]
                        func_to_call()
                    else:
                        print('Event {} not in dispatch dictionary'.format(event))


def button7():
    layout3 = [
        [sg.Text("'NUMBER' - {REAL BINARY} - [LIGHT ORDER]")],
        [sg.Text(r"'0' - {0} - [0000]", auto_size_text=True)],
        [sg.Text(r"'1' - {1} - [1000]", auto_size_text=True)],
        [sg.Text(r"'2' - {10} - [0100]", auto_size_text=True)],
        [sg.Text(r"'3' - {11} - [1100]", auto_size_text=True)],
        [sg.Text(r"'4' - {100} - [0010]", auto_size_text=True)],
        [sg.Text(r"'5' - {101} - [1010]", auto_size_text=True)],
        [sg.Text(r"'6' - {110} - [0110]", auto_size_text=True)],
        [sg.Text(r"'7' - {111} - [1110]", auto_size_text=True)],
        [sg.Text(r"'8' - {1000} - [0001]", auto_size_text=True)],
        [sg.Text(r"'9' - {1001} - [1001]", auto_size_text=True)],
        [sg.Text(r"'10' - {1010} - [0101]", auto_size_text=True)],
        [sg.Text(r"'11' - {1011} - [1101]", auto_size_text=True)],
        [sg.Text(r"'12' - {1100} - [0011]", auto_size_text=True)],
        [sg.Text(r"'13' - {1101} - [1001]", auto_size_text=True)],
        [sg.Text(r"'14' - {1110} - [0111]", auto_size_text=True)],
        [sg.Text(r"'15' - {1111} - [1111]", auto_size_text=True)],
        [sg.Button('OK')]]

    window3 = sg.Window('Binary Legend', layout3, keep_on_top=True, finalize=True)

    while True:
        event, value = window3.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            if event == 'OK':
                window3.close()
            elif event != 'Set Custom Colors':
                if event in ('Quit', 'Back', 'None', sg.WIN_CLOSED):
                    window3.close()
                elif event not in ('Quit', 'Back', 'None', sg.WIN_CLOSED):
                    if event in dispatch_dictionary:
                        func_to_call = dispatch_dictionary[event]
                        func_to_call()
                    else:
                        print('Event {} not in dispatch dictionary'.format(event))


dispatch_dictionary = {
    'Purple':button1,
    'Blue':button2,
    'Red':button3,
    'Off':button4,
    'Custom Colors':button5,
    'How It Works':button6,
    'Binary Legend':button7,
}

layout = [[sg.Text('Click a button', auto_size_text=True)],
          [sg.Button('Purple'), sg.Button('Blue'), sg.Button('Red'), sg.Button('Off')],
          [sg.Button('Custom Colors'), sg.Quit()]]

window = sg.Window('science on a sphere', layout, size=(200,100))


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


def main():
    while True:
        event, value = window.read()
        if event in ('Quit', 'Back', 'None', sg.WIN_CLOSED):
            break
        if event in dispatch_dictionary:
            func_to_call = dispatch_dictionary[event]
            func_to_call()
        else:
            print('Event {} not in dispatch dictionary'.format(event))


main()
