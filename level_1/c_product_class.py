"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(self, product_name: str, product_description: str, product_price: float, product_weight: float) -> None:
        self.name = product_name
        self.description = product_description
        self.price = product_price
        self.weight = product_weight



if __name__ == '__main__':
    apple = Product('apple', 'red apple', 1.5, 0.5)
    print(f'Информация о продукте: {apple.name}, {apple.description}, {apple.price}, {apple.weight}')
