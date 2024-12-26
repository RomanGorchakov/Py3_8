#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


def on_button_click(color_name, color_code):
    color_entry.delete(0, tk.END)  # Очистить текстовое поле
    color_entry.insert(0, color_code)  # Вставить код цвета
    color_label.config(text=color_name)  # Изменить текст метки


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

    for color_name, color_code in rainbow_colors.items():
        button = tk.Button(root, text=color_name, bg=color_code, 
command=lambda name=color_name, code=color_code: on_button_click(name, code))
        button.pack(fill=tk.X, padx=20, pady=5)

    root.mainloop()