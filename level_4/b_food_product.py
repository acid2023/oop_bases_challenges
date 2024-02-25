"""
У нас есть класс Product, который подходит для многих продуктов, но не для еды.
В пищевом продукте нам нужно хранить еще срок годности, который будет влиять и на другие методы

Задания:
    1. Переопределите частично метод __init__ у FoodProduct так, чтобы там хранилось еще свойство expiration_date.
       Используйте super() для этого.
    2. Переопределите у FoodProduct полностью метод get_full_info, чтобы он возвращал еще и информацию о сроке годности
    3. Переопределите частично метод is_available у FoodProduct, чтобы там учитывался еще и срок годности. Если он
       меньше чем текущая дата - то is_available должен возвращать False. Используйте super() для этого.
    3. Создайте экземпляры каждого из двух классов и вызовите у них все доступные методы
"""
from datetime import datetime


class Product:
    def __init__(self, title, quantity):
        self.title = title
        self.quantity = quantity

    def get_full_info(self):
        return f'Product {self.title}, {self.quantity} in stock.'

    def is_available(self):
        return self.quantity > 0


class FoodProduct(Product):
    def __init__(self, title, quantity, expiration_date):
        if type(expiration_date) is datetime:
            expiration_date = expiration_date.date()
        elif type(expiration_date) is str:
            self.expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d').date()
        else:
            raise TypeError
        super().__init__(title, quantity)

    def get_full_info(self):
        return f'Product {self.title}, {self.quantity} in stock, expriration date - {self.expiration_date}.'

    def is_available(self):
        if self.expiration_date <= datetime.now().date():
            return False
        else:
            return super().is_available()


if __name__ == '__main__':
    table = Product('table', 15)
    print(f'{table.get_full_info()} available - {table.is_available()}')

    apple = FoodProduct('apple', 100, '2024-01-01')
    print(f'{apple.get_full_info()} available - {apple.is_available()}')
    
    orange = FoodProduct('orange', 10, '2025-01-01')
    print(f'{orange.get_full_info()} available - {orange.is_available()}')
