#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from tkinter import Tk

from src.task_1 import ProductTransferApp


class TestProductTransferApp(unittest.TestCase):
    """
    Набор юнит-тестов для проверки функциональности приложения ProductTransferApp.
    """

    def setUp(self):
        """
        Создает экземпляр главного окна Tkinter и приложения
        ProductTransferApp перед каждым тестом.
        """

        self.root = Tk()
        self.app = ProductTransferApp(self.root)
        self.root.update()

    def tearDown(self):
        """
        Закрывает главное окно Tkinter после каждого теста.
        """

        self.root.destroy()

    def test_initial_product_list(self):
        """
        Проверяет, что изначальный список продуктов содержит ожидаемые элементы.
        """

        expected_products = [
            "Гвозди",
            "Шурупы",
            "Краска",
            "Кисти",
            "Молоток",
            "Отвёртка",
            "Цемент",
            "Линейка",
            "Пила",
            "Перчатки",
        ]
        actual_products = [self.app.product_list.get(i) for i in range(self.app.product_list.size())]
        self.assertEqual(expected_products, actual_products)

    def test_add_to_cart(self):
        """
        Проверяет, что выделенные товары корректно перемещаются из списка продуктов в корзину.
        """

        self.app.product_list.select_set(0)  # Выбираем "Гвозди"
        self.app.add_to_cart()

        # Проверяем, что "Гвозди" переместились в корзину и исчезли из списка продуктов
        self.assertEqual(self.app.cart_list.get(0), "Гвозди")
        self.assertEqual(self.app.product_list.size(), 9)  # Количество элементов уменьшилось

    def test_remove_from_cart(self):
        """
        Проверяет, что выделенные товары корректно возвращаются из корзины в список продуктов.
        """

        # Добавляем элемент в корзину
        self.app.product_list.select_set(0)  # Выбираем "Гвозди"
        self.app.add_to_cart()

        # Удаляем его из корзины
        self.app.cart_list.select_set(0)  # Выбираем "Гвозди" в корзине
        self.app.remove_from_cart()

        # Проверяем, что "Гвозди" вернулись в список продуктов и исчезли из корзины
        self.assertEqual(self.app.product_list.size(), 10)  # Количество элементов восстановилось
        self.assertEqual(self.app.product_list.get(self.app.product_list.size() - 1), "Гвозди")
        self.assertEqual(self.app.cart_list.size(), 0)  # Корзина пуста


if __name__ == "__main__":
    unittest.main()
