#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from tkinter import Tk

from src.task_2 import TextInputListApp


class TestTextInputListApp(unittest.TestCase):
    """
    Набор юнит-тестов для проверки функциональности приложения TextInputListApp.
    """

    def setUp(self):
        """
        Создает экземпляр главного окна Tkinter и приложения TextInputListApp перед каждым тестом.
        """

        self.root = Tk()
        self.app = TextInputListApp(self.root)
        self.root.update()  # Обновляем окно для корректной работы тестов

    def tearDown(self):
        """
        Закрывает главное окно Tkinter после каждого теста.
        """

        self.root.destroy()

    def test_add_text_to_list(self):
        """
        Проверяет, что текст из текстового поля добавляется в список.
        """

        self.app.entry_field.insert(0, "Тестовая строка")  # Устанавливаем текст в поле ввода

        self.app.add_text_to_list()  # Вызываем добавление текста в список

        # Проверяем, что текст добавлен в список и поле ввода очищено
        self.assertEqual(self.app.list_box.size(), 1)
        self.assertEqual(self.app.list_box.get(0), "Тестовая строка")
        self.assertEqual(self.app.entry_field.get(), "")

    def test_add_empty_text(self):
        """
        Проверяет, что пустая строка не добавляется в список.
        """

        self.app.entry_field.delete(0, "end")  # Очищаем поле ввода

        self.app.add_text_to_list()  # Пытаемся добавить пустую строку

        # Проверяем, что список остался пустым
        self.assertEqual(self.app.list_box.size(), 0)

    def test_copy_text_to_entry(self):
        """
        Проверяет, что текст из списка копируется в текстовое поле.
        """

        self.app.list_box.insert(0, "Тестовая строка")  # Добавляем элемент в список
        self.app.list_box.select_set(0)  # Выбираем добавленный элемент

        self.app.copy_text_to_entry()  # Копируем текст в поле ввода

        # Проверяем, что текст копировался в поле ввода
        self.assertEqual(self.app.entry_field.get(), "Тестовая строка")

    def test_copy_without_selection(self):
        """
        Проверяет, что ничего не происходит при попытке копирования без выделения.
        """
        self.app.copy_text_to_entry()  # Пытаемся копировать при отсутствии выделения

        # Проверяем, что поле ввода осталось пустым
        self.assertEqual(self.app.entry_field.get(), "")


if __name__ == "__main__":
    unittest.main()
