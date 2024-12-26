#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


def show_phone():
    # Получаем значение выбранной радиокнопки
    selected_name = radio_var.get()
    
    # Устанавливаем номер телефона в зависимости от выбранного имени
    if selected_name == "Вася":
        phone_label.config(text="+7 910 123 45 67")
    elif selected_name == "Петя":
        phone_label.config(text="+4 908 765 43 21")
    elif selected_name == "Маша":
        phone_label.config(text="+7 912 345 67 89")
    else:
        phone_label.config(text="")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Телефонный справочник")

    radio_var = tk.StringVar(value="")

    button_width = 15
    button_height = 2

    radio_1 = tk.Radiobutton(root, text="Вася", variable=radio_var,
                             value="Вася", indicatoron=0, command=show_phone,
                             width=button_width, height=button_height)
    radio_2 = tk.Radiobutton(root, text="Петя", variable=radio_var,
                             value="Петя", indicatoron=0, command=show_phone,
                             width=button_width, height=button_height)
    radio_3 = tk.Radiobutton(root, text="Маша", variable=radio_var,
                             value="Маша", indicatoron=0, command=show_phone,
                             width=button_width, height=button_height)

    radio_1.grid(row=0, column=0, padx=10, pady=5, sticky='w')
    radio_2.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    radio_3.grid(row=2, column=0, padx=10, pady=5, sticky='w')

    phone_label = tk.Label(root, text="", font=("Arial", 14))
    phone_label.grid(row=0, column=1, rowspan=3, padx=20, pady=20, sticky='e')

    root.mainloop()