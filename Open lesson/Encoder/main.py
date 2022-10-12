import tkinter as tk
from tkinter import ttk
from itertools import cycle
import functions as f

# Параметры экрана
window = tk.Tk()
window.title('DEncoder')
#window.iconbitmap(default='etsyicon.ico')
window.resizable(width=False, height=False)

frame_choices = tk.Frame(width=680, height=45)
frame_input_output = tk.Frame(width=580, height=205)
frame_copyright = tk.Frame(width=580, height=45)

frame_choices.grid()
frame_input_output.grid()
frame_copyright.grid()

# Набор данных для выбора
languages = ['Русский', 'Английский', 'оба']
ciphers = ['Цезаря', 'Рельсовый', 'Виженера']
actions = ['Зашифровать', 'Расшифровать']

# Алфавит
sumb = ',. !"№;%:?*()_-#@$+=0123456789'
ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
en = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Функция очистки
def clear():
    l_text_input.delete(0, tk.END)
    l_key_input.delete(0, tk.END)
    l_output.delete(0, tk.END)

def start():
    message = l_text_input.get()
    key = l_key_input.get()
    method = l_choice_method.get()
    lang = l_choice_lang.get()
    action = l_choice_action.get()

    if lang == 'Английский':
        b = 82
        alp = sumb + en
    elif lang == 'Русский':
        b = 96
        alp = sumb + ru
    elif lang == 'оба':
        b = 148
        alp = sumb + en + ru

    if method == 'Цезаря':
        if action == 'Зашифровать':
            key = int(key)
            output = str(f.encode_caesar(message, key, alp))
            l_output.delete(0, tk.END)
            l_output.insert(0, output)
        elif action == 'Расшифровать':
            key = int(key)
            output = str(f.decode_caesar(message, key, alp))
            l_output.delete(0, tk.END)
            l_output.insert(0, output)
    elif method == 'Виженера':
        if action == 'Зашифровать':
            output = str(f.encode_vijn(message, key, alp, b))
            l_output.delete(0, tk.END)
            l_output.insert(0, output)
        elif action == 'Расшифровать':
            output = str(f.decode_vijn(message, key, alp, b))
            l_output.delete(0, tk.END)
            l_output.insert(0, output)
    elif method == 'Рельсовый':
        if action == 'Зашифровать':
            key = int(key)
            output = str(f.encode_rail_fence(message, key))
            l_output.delete(0, tk.END)
            l_output.insert(0, output)
        elif action == 'Расшифровать':
            key = int(key)
            output = str(f.decode_rail_fence(message, key))
            l_output.delete(0, tk.END)
            l_output.insert(0, output)


l_choice_method = ttk.Combobox(frame_choices, values=ciphers)
l_choice_lang = ttk.Combobox(frame_choices, values=languages)
l_choice_action = ttk.Combobox(frame_choices, values=actions)

l_text_input = ttk.Entry(frame_input_output, width=65)
l_key_input = ttk.Entry(frame_input_output, width=65)
l_output = ttk.Entry(frame_input_output, width=65)
l_start = ttk.Button(frame_input_output, text="Старт", command=start)
l_clear = ttk.Button(frame_input_output, text="clear", command=clear)
l_text = tk.Label(frame_input_output, text="Текст")
l_text_key = tk.Label(frame_input_output, text="Ключ")
l_text_output = tk.Label(frame_input_output, text="Результат")

l_copyright = tk.Label(frame_copyright, text="© Klubkov Daniil ISP-320p")

l_choice_method.grid(row=0, column=0, sticky='w', padx=10, pady=10)
l_choice_lang.grid(row=0, column=1, sticky='w', padx=10, pady=10)
l_choice_action.grid(row=0, column=2, sticky='w', padx=10, pady=10)

l_text_input.grid(row=1, column=0, padx=15, pady=5)
l_key_input.grid(row=3, column=0, padx=15, pady=5)
l_start.grid(row=0, column=1, padx=10, pady=5)
l_clear.grid(row=1, column=1, padx=10, pady=5)
l_text.grid(row=0, column=0)
l_text_key.grid(row=2, column=0)
l_text_output.grid(row=4, column=0)
l_output.grid(padx=10, pady=10)

l_copyright.grid()

window.mainloop()
