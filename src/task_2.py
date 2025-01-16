#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Необходимо написать программу по следующему описанию:
# Нажатие Enter в однострочном текстовом поле приводит
# к перемещению текста из него в список (экземпляр Listbox).
# При двойном клике ( <Double-Button-1> ) по элементу-строке
# списка, она должна копироваться в текстовое поле.

import tkinter as tk


class TextInputListApp:
    """
    Класс приложения для работы с текстовым полем и списком.
    """

    def __init__(self, root):
        """
        Инициализация главного окна и создание виджетов.

        :param root: Главное окно Tkinter.
        """

        self.root = root
        self.root.title("Текстовое поле и список")

        self.initialize_widgets()

    def initialize_widgets(self):
        """
        Создает виджеты: текстовое поле и список.
        """

        # Текстовое поле для ввода
        self.entry_field = tk.Entry(self.root, width=40)
        self.entry_field.grid(row=0, column=0, padx=10, pady=10)

        # Привязываем нажатие Enter к методу add_text_to_list
        self.entry_field.bind("<Return>", self.add_text_to_list)

        # Список для отображения текста
        self.list_box = tk.Listbox(self.root, width=40, height=15)
        self.list_box.grid(row=1, column=0, padx=10, pady=10)

        # Привязываем двойной клик к методу copy_text_to_entry
        self.list_box.bind("<Double-Button-1>", self.copy_text_to_entry)

    def add_text_to_list(self, event=None):
        """
        Добавляет текст из текстового поля в список.

        :param event: Событие, связанное с нажатием клавиши Enter.
        """

        text = self.entry_field.get().strip()
        if text:  # Проверяем, что текст не пустой
            self.list_box.insert(tk.END, text)
            self.entry_field.delete(0, tk.END)  # Очищаем текстовое поле

    def copy_text_to_entry(self, event=None):
        """
        Копирует выделенный элемент из списка в текстовое поле.

        :param event: Событие, связанное с двойным кликом.
        """

        selected_indices = self.list_box.curselection()
        if selected_indices:  # Проверяем, что есть выделенный элемент
            text = self.list_box.get(selected_indices[0])
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(0, text)


if __name__ == "__main__":
    root = tk.Tk()
    app = TextInputListApp(root)
    root.mainloop()
