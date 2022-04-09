import keyboard
import pyperclip
import os
import win10toast

tost = win10toast.ToastNotifier()
all_data = []


def f():
    data = pyperclip.paste()
    all_data.append(data)
    tost.show_toast(f'F{len(all_data)}', f'добавлено: {data}', duration=4)
    keyboard.add_abbreviation(f'F{len(all_data)}', f'{all_data[len(all_data) - 1]}')
    return 0


while True:
    if keyboard.is_pressed('shift+space'):
        f()
    
