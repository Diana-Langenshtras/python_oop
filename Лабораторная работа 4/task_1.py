class Car:
    def __init__(self, model: str, color: str, price: int):
        """
                Создание и подготовка к работе объекта "Автомобиль"

                :param model: Модель автомобиля
                :param color: Цвет автомобиля
                :param price: Цена автомобиля

                Примеры:
                >>> car = Car("BMW", "Черный", 4000000)  # инициализация экземпляра класса
        """
        self.model = model
        self.color = color
        self.price = price

    def __str__(self):
        """
                Метод определяет поведение функции str(), вызванной для экземпляра класса.

                :return: str

                Примеры:
                >>> car = Car("BMW", "Черный", 4000000)
                >>> print(str(car))
        """
        return f"Автомобиль {self.model}. Цвет {self.color}. Цена {self.price}"

    def __repr__(self):
        """
                Метод определяет поведение функции repr(), вызванной для экземпляра класса.

                :return: str

                Примеры:
                >>> car = Car("BMW", "Черный", 4000000)
                >>> print(repr(car))
        """
        return f"{self.__class__.__name__}(model={self.model!r}, color={self.color!r}, price={self.price!r})"

    def weigh(self, weight: float) -> bool:
        """
                Метод проверяет вес автомобиля и сравнивает с максимально допустимым значением.

                :return: bool

                Примеры:
                >>> car = Car("BMW", "Черный", 4000000)
                >>> car.weigh(1000)
        """
        ...

    def add_fuel(self) -> None:
        """
                Метод пополняет топливо в автомобиле.

                :return: None

                Примеры:
                >>> car = Car("BMW", "Черный", 4000000)
                >>> car.add_fuel()
        """
        ...


class PassengerCar(Car):
    """
            Создание и подготовка к работе объекта "Легковой автомобиль".

            Конструктор базового класса унаследован.

            Примеры:
            >>> passenger_car = PassengerCar("BMW", "Черный", 4000000)  # инициализация экземпляра класса
    """
    def __str__(self):
        """
                Метод определяет поведение функции str(), вызванной для экземпляра класса.

                Метод базового класса перегружен, так как идет уточнение, что объект класса - легковой автомобиль.

                :return: str

                Примеры:
                >>> passenger_car = PassengerCar("BMW", "Черный", 4000000)
                >>> print(str(passenger_car))
        """
        return f"Легковой автомобиль {self.model}. Цвет {self.color}. Цена {self.price}"


class TruckCar(Car):
    """
            Создание и подготовка к работе объекта "Грузовой автомобиль"

            Конструктор базового класса расширен

            :param cargo_weight: Вес груза автомобиля

            Примеры:
            >>> truck_car = TruckCar("BMW", "Черный", 4000000, 100)  # инициализация экземпляра класса
    """
    def __init__(self, model: str, color: str, price: int, cargo_weight: float):
        super().__init__(model, color, price)
        self.cargo_weight = cargo_weight

    def __str__(self):
        """
                Метод определяет поведение функции str(), вызванной для экземпляра класса.

                Метод базового класса перегружен, так как идет уточнение, что объект класса - грузовой автомобиль,
                и указывается информация про вес груза.

                :return: str

                Примеры:
                >>> truck_car = TruckCar("BMW", "Черный", 4000000, 100)
                >>> print(str(truck_car))
        """
        return f"Грузовой автомобиль {self.model}. Цвет {self.color}. Цена {self.price}. Вес груза {self.cargo_weight}"

    def __repr__(self):
        """
                Метод определяет поведение функции repr(), вызванной для экземпляра класса.

                Метод базового класса перегружен,
                так как в объекте класса TruckCar при инициализации необходимо еще указать вес груза cargo_weight.

                :return: str

                Примеры:
                >>> truck_car = TruckCar("BMW", "Черный", 4000000, 100)
                >>> print(repr(truck_car))
        """
        return f"{self.__class__.__name__}(model={self.model!r}, color={self.color!r}, price={self.price!r}, cargo_weight={self.cargo_weight!r})"

    def weigh(self, weight: float) -> bool:
        """
                Метод проверяет вес автомобиля и сравнивает с максимально допустимым значением.

                Метод необходимо перегрузить,
                так как для грузового автомобиля максимально допустимое значение будет другим.

                :return: bool

                Примеры:
                >>> truck_car = TruckCar("BMW", "Черный", 4000000, 100)
                >>> truck_car.weigh(8000)
        """
        ...


if __name__ == "__main__":
    # Write your solution here
    pass
