#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Необходимо написать программу, состоящую из двух списков Listbox.
# В первом будет, например, перечень товаров, заданный программно.
# Второй изначально пуст, пусть это будет перечень покупок. При клике
# на одну кнопку товар должен переходить из одного списка в другой.
# При клике на вторую кнопку – возвращаться (человек передумал покупать).
# Предусмотрите возможность множественного выбора элементов списка и их перемещения.

import tkinter as tk
from tkinter import MULTIPLE, Button, Listbox


class ProductTransferApp:
    """
    Приложение для управления перечнем товаров.
    Позволяет перемещать товары из списка товаров в корзину и обратно.
    """

    def __init__(self, root):
        """
        Инициализирует главное окно приложения и виджеты.

        :param root: Главное окно tkinter.
        """

        self.root = root
        self.root.title("Перечень товаров")

        self.create_widgets()
        self.populate_product_list()

    def create_widgets(self):
        """
        Создает виджеты приложения: списки и кнопки управления.
        """

        # Список товаров
        self.product_list = Listbox(self.root, selectmode=MULTIPLE, width=30, height=15)
        self.product_list.grid(row=0, column=0, padx=10, pady=10)

        # Кнопки управления
        self.add_button = Button(self.root, text=">>>", command=self.add_to_cart)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.remove_button = Button(self.root, text="<<<", command=self.remove_from_cart)
        self.remove_button.grid(row=1, column=1, padx=5, pady=5)

        # Список покупок
        self.cart_list = Listbox(self.root, selectmode=MULTIPLE, width=30, height=15)
        self.cart_list.grid(row=0, column=2, padx=10, pady=10)

    def populate_product_list(self):
        """
        Заполняет список товаров предустановленными значениями.
        """

        products = [
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
        for product in products:
            self.product_list.insert(tk.END, product)

    def add_to_cart(self):
        """
        Перемещает выделенные товары из списка товаров в корзину.
        """

        selected_items = self.product_list.curselection()
        for index in reversed(selected_items):  # Перебор в обратном порядке для корректного удаления
            item = self.product_list.get(index)
            self.cart_list.insert(tk.END, item)
            self.product_list.delete(index)

    def remove_from_cart(self):
        """
        Перемещает выделенные товары из корзины обратно в список товаров.
        """

        selected_items = self.cart_list.curselection()
        for index in reversed(selected_items):  # Перебор в обратном порядке для корректного удаления
            item = self.cart_list.get(index)
            self.product_list.insert(tk.END, item)
            self.cart_list.delete(index)


if __name__ == "__main__":
    root = tk.Tk()
    app = ProductTransferApp(root)
    root.mainloop()
