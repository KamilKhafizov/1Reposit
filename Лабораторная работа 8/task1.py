from typing import Union


class Vehicle:
    """Базовый класс для транспортных средств."""
    def __init__(self, brand: str, model: str, year: int):
        self._brand = brand
        self._model = model
        self._year = year

    @property
    def brand(self) -> str:
        """Марка транспортного средства."""
        return self._brand

    @property
    def model(self) -> str:
        """Модель транспортного средства."""
        return self._model

    @property
    def year(self) -> int:
        """Год выпуска транспортного средства."""
        return self._year

    def start_engine(self) -> str:
        """Метод для запуска двигателя."""
        return f"The engine of {self.brand} {self.model} is started."

    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.year})"


class Car(Vehicle):
    """Дочерний класс для легкового автомобиля."""
    def __init__(self, brand: str, model: str, year: int, num_doors: int):
        super().__init__(brand, model, year)
        self._num_doors = num_doors

    @property
    def num_doors(self) -> int:
        """Количество дверей у автомобиля."""
        return self._num_doors

    def drive(self, distance: float) -> str:
        """Метод для езды на автомобиле."""
        return f"{self.brand} {self.model} is driving for {distance} km."


class Truck(Vehicle):
    """Дочерний класс для грузового автомобиля."""
    def __init__(self, brand: str, model: str, year: int, cargo_capacity: Union[int, float]):
        super().__init__(brand, model, year)
        self._cargo_capacity = cargo_capacity

    @property
    def cargo_capacity(self) -> Union[int, float]:
        """Грузоподъемность грузового автомобиля."""
        return self._cargo_capacity

    def load_cargo(self, weight: Union[int, float]) -> str:
        """Метод для загрузки груза на грузовик."""
        return f"{weight} kg of cargo loaded onto {self.brand} {self.model}."

    def __str__(self) -> str:
        return f"{super().__str__()} with cargo capacity: {self.cargo_capacity} tons"


if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2022, 4)
    print(car.start_engine())
    print(car.drive(50))
    print(f"Details: {car}")

    truck = Truck("Volvo", "FH16", 2021, 30.5)
    print(truck.start_engine())
    print(truck.load_cargo(1500))
    print(f"Details: {truck}")
