#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Необходимо написать программу, которая рисует дом,
 солнце и траву циклом на холсте.
"""

import tkinter as tk


def create_landscape(canvas, canvas_width, canvas_height):
    """
    Рисует на холсте небо, дом, солнце и траву.

    :param canvas: Холст.
    :param canvas_width: Ширина холста.
    :param canvas_height: Высота холста.
    """

    # Небо
    canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill="white", outline="")

    # Крыша
    canvas.create_polygon(
        canvas_width // 2 - 70,
        canvas_height // 2,  # Левая точка крыши
        canvas_width // 2 + 70,
        canvas_height // 2,  # Правая точка крыши
        canvas_width // 2,
        canvas_height // 2 - 100,  # Верхняя точка крыши
        fill="lightblue",
        outline="",
    )

    # Каркас
    canvas.create_rectangle(
        canvas_width // 2 - 50,
        canvas_height // 2,
        canvas_width // 2 + 50,
        canvas_height // 2 + 100,
        fill="lightblue",
        outline="",
    )

    # Солнце
    canvas.create_oval(canvas_width - 100, 50, canvas_width - 50, 100, fill="orange", outline="")

    # Трава
    for position_x in range(0, canvas_width, 15):
        canvas.create_arc(
            position_x,
            canvas_height - 80,
            position_x + 30,
            canvas_height - 20,
            start=120,
            extent=60,
            style=tk.ARC,
            outline="green",
            width=2,
        )


if __name__ == "__main__":
    """
    Основная функция программы.
    Настраивает окно и вызывает функцию для рисования.
    """

    # Настройка окна
    root = tk.Tk()
    root.title("Сцена с домом и травой")

    # Размеры холста
    canvas_width, canvas_height = 400, 300
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    # Рисуем сцену
    create_landscape(canvas, canvas_width, canvas_height)

    # Запуск основного цикла Tkinter
    root.mainloop()
