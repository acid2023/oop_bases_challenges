"""
Задания:
    1. Запустите текущий код и посмотрите на вывод.
    2. Допишите класс User таким образом, чтобы при вызове print() на его инстансах появлялась информация
       об айдишнике пользователя и его емэйле, а при вызове repr() возвращалась информация о том, является ли пользователь
       админом
"""


class User:
    def __init__(self, user_id: int, email: str, is_admin: bool):
        self.user_id = user_id
        self.email = email
        self.is_admin = is_admin

    def __repr__(self) -> str:
        if self.is_admin:
            return f'User {self.user_id} is admin'
        else:
            return f'User {self.user_id} is not admin'
        
    def __str__(self) -> str:
        return f'User {self.user_id} with email {self.email}'


if __name__ == '__main__':
    user_instance = User(user_id=3, email='dev@yandex.ru', is_admin=True)
    print(user_instance)
    print(repr(user_instance))
