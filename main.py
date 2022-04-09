import keyboard
import pyperclip

all_data = []

def f():
    data = pyperclip.paste()
    all_data.append(data)
    print(f'добавлено: {data}')
    keyboard.add_abbreviation(f'F{len(all_data)}', f'{all_data[len(all_data) -1]}')
    
keyboard.add_hotkey("1+esc", f)
    
