import doctest

class Computer:
    def __init__(self, brand: str, model: str, processor_speed: float):
        """
        Создание и подготовка к работе объекта "Компьютер"

        :param brand: Бренд компьютера.
        :param model: Модель компьютера.
        :param processor_speed: Скорость процессора компьютера в ГГц.

        Примеры:
        >>> computer = Computer("Dell", "Inspiron", 2.5)  # инициализация экземпляра класса
        """
        if not isinstance(processor_speed, (int, float)):
            raise TypeError("Скорость процессора должна быть типа int или float")
        if processor_speed <= 0:
            raise ValueError("Скорость процессора должна быть положительным числом")
        self.brand = brand
        self.model = model
        self.processor_speed = processor_speed

    def power_on(self):
        """Включает компьютер."""
        ...

    def run_application(self, application_name: str) -> None:
        """Запускает указанное приложение.

        :param application_name: Название приложения для запуска.

        :return: None

        Пример:
        >>> computer = Computer("Dell", "Inspiron", 2.5)
        >>> computer.run_application("Web Browser")
        """
        ...


class City:
    def __init__(self, name: str, population: int, country: str):
        """
        Создание и подготовка к работе объекта "Город"

        :param name: Название города.
        :param population: Население города.
        :param country: Страна, в которой находится город.
        """
        self.name = name
        self.population = population
        self.country = country

    def calculate_density(self) -> float:
        """Вычисляет плотность населения города.

        :return: Плотность населения города.

        Пример:
        >>> city = City("Paris", 2243833, "France")
        >>> city.calculate_density()
        """
        ...

    def is_capital(self) -> bool:
        """Проверяет, является ли город столицей.

        :return: True, если город - столица, False в противном случае.

        Пример:
        >>> city = City("Paris", 2243833, "France")
        >>> city.is_capital()
        """
        ...


class Song:
    def __init__(self, title: str, artist: str, duration: float):
        """
        Создание и подготовка к работе объекта "Песня"

        :param title: Название песни.
        :param artist: Исполнитель песни.
        :param duration: Длительность песни в минутах.
        """
        self.title = title
        self.artist = artist
        self.duration = duration

    def play(self) -> None:
        """Воспроизводит песню."""
        ...

    def get_info(self) -> str:
        """Возвращает информацию о песне.

        :return: Информация о песне.

        Пример:
        >>> song = Song("Bohemian Rhapsody", "Queen", 6.0)
        >>> song.get_info()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации



