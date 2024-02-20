"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float |int) -> None:
        if (type(income) is float) or (type(income) is int):
            if income < 0:
                raise ValueError('income cannot be negative')
            self.balance += income
        else:
            raise TypeError('incorrect type of argument income')
        
    def decrease_balance(self, outcome: float | int) -> None:
        if (type(outcome) is float) or (type(outcome) is int):
            if outcome < 0:
                raise ValueError('outcome cannot be negative')
            if self.balance - outcome >= 0:
                self.balance -= outcome
            else:
                raise ValueError('outcome cannot be greater than balance')
        else:
            raise TypeError('incorrect type of argument outcome')

if __name__ == '__main__':
    vasya_account = BankAccount('Vasya', 100)
    print(vasya_account.balance)
    try:
        vasya_account.decrease_balance(-50)
    except Exception as e:
        print(e)
    print(vasya_account.balance)
    try:
        vasya_account.decrease_balance(150)
        print(vasya_account.balance)
    except Exception as e:
        print(e)
