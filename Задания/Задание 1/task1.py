#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        label_result.config(text=str(result))
    except ValueError:
        label_result.config(text="ошибка")
    except ZeroDivisionError:
        label_result.config(text="ошибка")

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Калькулятор")

    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=0)

    entry2 = tk.Entry(root)
    entry2.grid(row=1, column=0)

    button_add = tk.Button(root, text="+", command=lambda: calculate('+'))
    button_add.grid(row=0, column=1)

    button_subtract = tk.Button(root, text="-", command=lambda: calculate('-'))
    button_subtract.grid(row=1, column=1)

    button_multiply = tk.Button(root, text="*", command=lambda: calculate('*'))
    button_multiply.grid(row=0, column=2)

    button_divide = tk.Button(root, text="/", command=lambda: calculate('/'))
    button_divide.grid(row=1, column=2)

    label_result = tk.Label(root, text="")
    label_result.grid(row=2, column=0, columnspan=3)

    root.mainloop()