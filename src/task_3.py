#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Необходимо написать программу по следующему описанию:
Размеры многострочного текстового поля определяются значениями, введенными
в однострочные текстовые поля. Изменение размера происходит при нажатии
мышью на кнопку, а также при нажатии клавиши Enter. Цвет фона экземпляра
Text светлосерый (lightgrey), когда поле не в фокусе, и белый, когда имеет фокус.
"""

import tkinter as tk


class DynamicTextFieldApp:
    """
    Класс приложения для управления размерами и фокусом многострочного текстового поля.
    """

    def __init__(self, root):
        """
        Инициализирует главное окно и создает виджеты приложения.

        :param root: Главное окно Tkinter.
        """

        self.root = root
        self.root.title("Управление текстовым полем")

        self.initialize_widgets()

    def initialize_widgets(self):
        """
        Инициализирует и размещает виджеты в главном окне приложения.
        """

        # Поле для ввода ширины текстового поля
        self.width_input = tk.Entry(self.root, width=5)
        self.width_input.insert(0, "30")  # Устанавливаем значение по умолчанию
        self.width_input.grid(row=0, column=0, padx=5, pady=5)

        # Поле для ввода высоты текстового поля
        self.height_input = tk.Entry(self.root, width=5)
        self.height_input.insert(0, "10")  # Устанавливаем значение по умолчанию
        self.height_input.grid(row=1, column=0, padx=5, pady=5)

        # Кнопка для изменения размеров текстового поля
        self.update_button = tk.Button(self.root, text="Изменить", command=self.update_text_field)
        self.update_button.grid(row=0, column=1, rowspan=2, padx=5, pady=5)

        # Многострочное текстовое поле
        self.text_field = tk.Text(self.root, width=30, height=10, bg="lightgrey")
        self.text_field.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Привязка событий изменения фокуса
        self.text_field.bind("<FocusIn>", self.set_focus_background)
        self.text_field.bind("<FocusOut>", self.remove_focus_background)

        # Привязка клавиши Enter для изменения размеров
        self.width_input.bind("<Return>", self.update_text_field)
        self.height_input.bind("<Return>", self.update_text_field)

    def update_text_field(self, event=None):
        """
        Изменяет размеры текстового поля на основе введенных данных.

        :param event: Событие, связанное с нажатием клавиши Enter.
        """

        try:
            new_width = int(self.width_input.get())
            new_height = int(self.height_input.get())
            self.text_field.config(width=new_width, height=new_height)
        except ValueError:
            # Игнорируем ошибки, если введены некорректные данные
            pass

    def set_focus_background(self, event):
        """
        Устанавливает белый цвет фона для текстового поля при получении фокуса.

        :param event: Событие получения фокуса.
        """

        self.text_field.config(bg="white")

    def remove_focus_background(self, event):
        """
        Устанавливает светло-серый цвет фона для текстового поля при потере фокуса.

        :param event: Событие потери фокуса.
        """

        self.text_field.config(bg="lightgrey")


if __name__ == "__main__":
    root = tk.Tk()
    app = DynamicTextFieldApp(root)
    root.mainloop()
