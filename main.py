import keyboard
import pyperclip

def f():
    data = pyperclip.paste()
    print(data)


keyboard.add_hotkey("1+esc", f)
