#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

def on_button_click(color_name, color_code):
    color_entry.delete(0, tk.END)
    color_entry.insert(0, color_code)
    color_label.config(text=color_name)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Цвета радуги")

    rainbow_colors = {
        "Красный": "#FF0000",
        "Оранжевый": "#FF7F00",
        "Желтый": "#FFFF00",
        "Зеленый": "#00FF00",
        "Голубой": "#00FFFF",
        "Синий": "#0000FF",
        "Фиолетовый": "#7F00FF"
    }

    color_label = tk.Label(root, text="", font=("Arial", 16))
    color_label.pack(pady=10)

    color_entry = tk.Entry(root, font=("Arial", 16), width=20)
    color_entry.pack(pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    for color_name, color_code in rainbow_colors.items():
        button = tk.Button(button_frame, text='', bg=color_code, width=4,
        height=2, command=lambda name=color_name, code=color_code: 
        on_button_click(name, code))
        button.pack(side=tk.LEFT, padx=5)

    root.mainloop()