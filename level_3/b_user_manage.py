"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self, users_list: list[str] = []) -> None:
        self.usernames = users_list

    def add_user(self, username: str) -> None:
        self.usernames.append(username)

    def get_users(self) -> list[str]:
        return self.usernames

class AdminManager(UserManager):
    def ban_username(self, username: str) -> None:
        print(f'Banning user {username}')
        if username in self.usernames:
            print('Успешно!')
            self.usernames.remove(username)
        else:
            print("Такого пользователя не существует.")

class SuperAdminManager(AdminManager):
    def ban_all_users(self) -> None:
        print('Banning all users...')
        self.usernames.clear()



if __name__ == '__main__':
    anna = UserManager()
    anna.add_user('Anna')
    anna.add_user('Vasya')
    users_list = anna.get_users()
    print(f"Anna's users -{users_list}")

    kolya = AdminManager(users_list=users_list)
    print(f"Kolya's users - {kolya.get_users()}")
    kolya.ban_username('Vasya')
    kolya.ban_username('Petya')
    kolya.add_user('Sasha')
    users_list = kolya.get_users()
    print(f"Kolya's users - {users_list}")

    tolya = SuperAdminManager(users_list=users_list)
    print(f"Tolya's users - {tolya.get_users()}")
    tolya.ban_username('Petya')
    tolya.ban_username('Sasha')
    tolya.add_user('Misha')
    print(tolya.get_users())
    tolya.ban_all_users()
    print(tolya.get_users())

