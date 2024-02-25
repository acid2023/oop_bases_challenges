"""
У нас есть класс для работы с группами студентов, и нам хотелось бы иметь возможность суммировать все оценки от двух групп.
Но сейчас мы почему-то не можем этого делать и получаем ошибку, нужно разобраться почему и дописать код класса.

Задания:
    1. Запустите текущий код и убедитесь, что он падает с ошибкой
    2. Допишите класс StudentGroup таким образом, чтобы при суммировании двух его инстансов мы получали сумму всех
       оценок двух инстансов.
    3. Запустите текущий код и убедитесь, что теперь мы получаем число в выводе, вместо ошибки.
"""


class StudentGroup:
    def __init__(self, group_number: int, grades: list[int]):
        self.group_number = group_number
        self.grades = grades
    
    def __str__(self) -> str:
        return str(sum([x for x in self.grades]))
    
    def __add__(self, other):
        if isinstance(other, StudentGroup):
            return StudentGroup(self.group_number + other.group_number, [x for x in self.grades] + [y for y in other.grades])
        else:
            raise TypeError("Unsupported operand type for +")


if __name__ == '__main__':
    first_group = StudentGroup(group_number=1, grades=[1, 4, 6, 3])
    second_group = StudentGroup(group_number=2, grades=[6, 3, 7, 3, 2])
    print(first_group)
    print(second_group)
    print(first_group + second_group)
