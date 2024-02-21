"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знаем о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""


class Product:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_info(self):
        return f'Product {self.title} with price {self.price}'


class PrintLoggerMixin:
    def log(self, message):
        print(message)

class PremiumProduct(Product, PrintLoggerMixin):
    def __init__(self, title: str, price: float):
        self.log('premium product created')
        super().__init__(title, price)

    def increase_price(self):
        self.price *= 1.2
        self.log('price increased')

    def get_info(self):
        base_info = super().get_info()
        self.log('info requested')
        return f'{base_info} (Premium)'


class DiscountedProduct(Product, PrintLoggerMixin):
    def __init__(self, title: str, price: float):
        self.log('discounted product created')
        super().__init__(title, price)

    def decrease_price(self):
        self.price /= 1.2
        self.log('price decreased')

    def get_info(self):
        base_info = super().get_info()
        self.log('info requested')
        return f'{base_info} (Discounted)'


if __name__ == '__main__':
    bad_potato = DiscountedProduct('potato', 10)
    bad_potato.decrease_price()
    print(bad_potato.get_info())

    great_potato = PremiumProduct('potato', 100)
    great_potato.increase_price()
    print(great_potato.get_info())
