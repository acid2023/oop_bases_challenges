"""
У нас есть класс банковского аккаунта со свойствами: полное имя владельца и баланс, но не реализован
метод, который увеличивает баланс.

Задания:
    1. Допишите логику в метод increase_balance, который должен увеличивать баланс банковского счета на значение income.
    2. Создайте экземпляр класса банковского счета и распечатайте баланс.
    3. Увеличьте баланс счета у экземпляра класса с помощью метода increase_balance и снова распечатайте текущий баланс.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float| int) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float |int) -> None:
        if (type(income) is float) or (type(income) is int):
            if income < 0:
                raise ValueError('income should be non-negative')
            self.balance += income
        else:
            raise TypeError('incorrect type')


if __name__ == '__main__':
    vasya_account = BankAccount('Vasya', 100)
    print(vasya_account.balance)
    try:
        vasya_account.increase_balance(150)
        print(vasya_account.balance)
    except Exception as e:
        print(e)

    try:
        vasya_account.increase_balance(-150)
        print(vasya_account.balance)
    except Exception as e:
        print(e)

