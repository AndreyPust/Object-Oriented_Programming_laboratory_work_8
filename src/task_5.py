#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Необходимо по примеру кода создать программу анимации перемещения
круга, который движется плавно в ту сторону, в которую пользователь
кликает левой кнопкой мыши.
"""

from tkinter import Canvas, Tk


class BallMover:
    """
    Класс, управляющий перемещением круга на холсте.
    """

    def __init__(self, canvas, ball):
        """
        Инициализирует объект BallMover.

        :param canvas: Экземпляр холста.
        :param ball: Круг.
        """

        self.canvas = canvas
        self.ball = ball
        self.target_x = None  # Целевая координата X
        self.target_y = None  # Целевая координата Y

    def move_to_target(self):
        """
        Перемещает круг в сторону установленной цели.
        Если цель не достигнута, продолжает двигаться с задержкой.
        """

        if self.target_x is not None and self.target_y is not None:
            # Получаем текущие координаты круга
            x1, y1, x2, y2 = self.canvas.coords(self.ball)
            ball_center_x = (x1 + x2) / 2
            ball_center_y = (y1 + y2) / 2

            # Вычисляем смещение
            dx = 1 if ball_center_x < self.target_x else -1 if ball_center_x > self.target_x else 0
            dy = 1 if ball_center_y < self.target_y else -1 if ball_center_y > self.target_y else 0

            # Двигаем круг, если он не достиг цели
            if dx != 0 or dy != 0:
                self.canvas.move(self.ball, dx, dy)
                self.canvas.after(10, self.move_to_target)

    def set_target(self, event):
        """
        Устанавливает новую цель для движения круга.

        :param event: Событие мыши, содержащее координаты клика.
        """

        self.target_x = event.x
        self.target_y = event.y
        self.move_to_target()


def main():
    """
    Главная функция программы. Создаёт окно с холстом и запускает анимацию.
    """

    root = Tk()
    root.title("Ball Movement")

    # Создаём холст
    canvas = Canvas(root, width=300, height=200, bg="white")
    canvas.pack()

    # Создаём круг
    ball = canvas.create_oval(50, 20, 70, 40, fill="orange")

    # Создаём объект BallMover
    ball_mover = BallMover(canvas, ball)

    # Привязываем обработчик клика мыши
    canvas.bind("<Button-1>", ball_mover.set_target)

    root.mainloop()


if __name__ == "__main__":
    main()
