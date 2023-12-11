# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Employee:
    def __init__(self, name: str, surname: str, salary: float):
        """
                Создание и подготовка к работе объекта "Сотрудник"

                :param name: Имя сотрудника
                :param surname: Фамилия сотрудника
                :param salary: Зарплата сотрудника

                Примеры:
                >>> employee = Employee("Иван", "Иванов", 20000)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Значение должно быть типа str")
        self.name = name
        if not isinstance(surname, str):
            raise TypeError("Значение должно быть типа str")
        self.surname = surname
        if not isinstance(salary, (int, float)):
            raise TypeError("Значение должно быть типа int или float")
        if salary < 0:
            raise ValueError("Значение не может быть отрицательным")
        self.salary = salary

    def display_employee(self) -> None:
        """
                Функция выводит данные о сотруднике

                :return: None

                Примеры:
                >>> employee = Employee("Иван", "Иванов", 20000)
                >>> employee.display_employee()
        """
        ...

    def change_salary(self, new_salary: int) -> None:
        """
                Изменение зарплаты сотрудника.

                :param new_salary: Новая зарплата сотрудника
                :raise ValueError: Если значение не типа int или float,
                то возвращается ошибка.
                :raise ValueError: Если значение отрицательное,
                то возвращается ошибка.

                :return: None

                Примеры:
                >>> employee = Employee("Иван", "Иванов", 20000)
                >>> employee.change_salary(25000)
        """
        ...


class Cat:
    def __init__(self, name: str, age: float, color: str):
        """
                Создание и подготовка к работе объекта "Кот"

                :param name: Имя кота
                :param age: Возраст кота
                :param color: Цвет кота

                Примеры:
                >>> cat = Cat("Лютик", 5, "Рыжий")  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Значение должно быть типа str")
        self.name = name
        if not isinstance(age, (int, float)):
            raise TypeError("Значение должно быть типа int или float")
        if age < 0:
            raise ValueError("Значение не может быть отрицательным")
        self.salary = age
        if not isinstance(color, str):
            raise TypeError("Значение должно быть типа str")
        self.color = color

    def display_cat(self) -> None:
        """
                Функция выводит данные о коте

                :return: None

                Примеры:
                >>> cat = Cat("Лютик", 5, "Рыжий")
                >>> cat.display_cat()
        """
        ...

    def pet_cat(self) -> None:
        """
                Поглаживание кота.

                :return: None

                Примеры:
                >>> cat = Cat("Лютик", 5, "Рыжий")
                >>> cat.pet_cat()
        """
        ...

    def feed_cat(self) -> None:
        """
                Кормление кота.

                :return: None

                Примеры:
                >>> cat = Cat("Лютик", 5, "Рыжий")
                >>> cat.feed_cat()
        """
        ...

class Knife:
    def __init__(self, length: float, sharpening: bool):
        """
                Создание и подготовка к работе объекта "Нож"

                :param length: Длина ножа в см
                :param sharpening: Заточка ножа

                Примеры:
                >>> knife = Knife(13, True)  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Значение должно быть типа int или float")
        if length < 0:
            raise ValueError("Значение не может быть отрицательным")
        self.length = length
        if not isinstance(sharpening, bool):
            raise TypeError("Значение должно быть типа bool")
        self.sharpening = sharpening

    def cut_vegetable(self, vegetable: str) -> None:
        """
                Нарезание овоща.

                :param vegetable: Овощ, который будет нарезаться
                :raise ValueError: Если значение не типа str,
                то возвращается ошибка.
                :return: None

                Примеры:
                >>> knife = Knife(13, True)
                >>> knife.cut_vegetable('Помидор')
        """
        ...

    def sharpen_knife(self) -> None:
        """
                Заточка ножа.

                :return: None

                Примеры:
                >>> knife = Knife(13, True)
                >>> knife.sharpen_knife()
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
