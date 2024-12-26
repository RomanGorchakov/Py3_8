#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog, messagebox


def open_file():
    filename = entry.get()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text.delete(1.0, tk.END)  # Очистить текстовое поле
            content = file.read()
            text.insert(tk.END, content)  # Вставить содержимое файла в текстовое поле
    except FileNotFoundError:
        messagebox.showerror("Ошибка", f"Файл '{filename}' не найден.")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))


def save_file():
    filename = entry.get()
    content = text.get(1.0, tk.END)  # Получить содержимое текстового поля
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content.strip())  # Сохранить содержимое в файл
        messagebox.showinfo("Информация", f"Файл '{filename}' успешно сохранен.")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Текстовый редактор")

    entry = tk.Entry(root, width=40)
    entry.pack(pady=10)

    text = tk.Text(root, wrap='word', width=50, height=15)
    text.pack(pady=10)

    open_button = tk.Button(root, text="Открыть", command=open_file)
    open_button.pack(side=tk.LEFT, padx=10, pady=10)

    save_button = tk.Button(root, text="Сохранить", command=save_file)
    save_button.pack(side=tk.RIGHT, padx=10, pady=10)

    root.mainloop()