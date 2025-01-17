#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from tkinter import Tk

from src.task_3 import DynamicTextFieldApp


class TestDynamicTextFieldApp(unittest.TestCase):
    """
    Набор юнит-тестов для проверки функциональности программы задания 9.
    """

    def setUp(self):
        """
        Создает корневое окно и экземпляр приложения перед каждым тестом.
        """

        self.root = Tk()
        self.app = DynamicTextFieldApp(self.root)
        self.root.update()  # Обновляем окно для корректной работы тестов

    def tearDown(self):
        """
        Закрывает главное окно Tkinter после каждого теста.
        """

        self.root.destroy()

    def test_initial_sizes(self):
        """
        Проверяет начальные размеры текстового поля.
        """

        width = int(self.app.text_field["width"])
        height = int(self.app.text_field["height"])
        self.assertEqual(width, 30)  # Начальная ширина
        self.assertEqual(height, 10)  # Начальная высота

    def test_update_text_field(self):
        """
        Проверяет изменение размеров текстового поля.
        """

        # Устанавливаем новые значения в поля ввода
        self.app.width_input.delete(0, "end")
        self.app.width_input.insert(0, "31")
        self.app.height_input.delete(0, "end")
        self.app.height_input.insert(0, "15")

        # Вызываем метод изменения размеров
        self.app.update_text_field()

        # Проверяем, что размеры текстового поля изменились
        width = int(self.app.text_field["width"])
        height = int(self.app.text_field["height"])
        self.assertEqual(width, 31)
        self.assertEqual(height, 15)

    def test_invalid_input_handling(self):
        """
        Проверяет поведение приложения при некорректном вводе размеров.
        """

        # Устанавливаем некорректные значения в поля ввода
        self.app.width_input.delete(0, "end")
        self.app.width_input.insert(0, "invalid")
        self.app.height_input.delete(0, "end")
        self.app.height_input.insert(0, "invalid")

        # Вызываем метод изменения размеров
        self.app.update_text_field()

        # Проверяем, что размеры текстового поля остались прежними
        width = int(self.app.text_field["width"])
        height = int(self.app.text_field["height"])
        self.assertEqual(width, 30)  # Начальная ширина
        self.assertEqual(height, 10)  # Начальная высота


if __name__ == "__main__":
    unittest.main()
