"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""

class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float):
        self.balance += amount

    def decrease_balance(self, amount: float):
        self.balance -= amount


class CreditAccount(BankAccount):
    def is_eligible_for_credit(self):
        return self.balance > 1000


if __name__ == '__main__':
    ivanov_account = BankAccount('Ivanov', 100)
    print(ivanov_account.balance)
    ivanov_account.increase_balance(150)
    print(ivanov_account.balance)
    ivanov_account.decrease_balance(50)
    print(ivanov_account.balance)

    vasya_account = CreditAccount('Vasya', 100)
    print(vasya_account.balance)
    vasya_account.increase_balance(1500)
    print(vasya_account.balance)
    print(vasya_account.is_eligible_for_credit())
    vasya_account.decrease_balance(1550)
    print(vasya_account.balance)
    print(vasya_account.is_eligible_for_credit())


