class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"



class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"
    def pages(self) -> int:
        return self._pages


    def pages(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self) -> str:
        return f"Бумажная {super().__str__()}. Количество страниц: {self.pages}"



class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        self.name = name
        self.author = author
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration


    def duration(self) -> float:
        return self._duration


    def duration(self, value: float) -> None:
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Длительность должна быть положительным числом.")
        self._duration = value

    def __str__(self) -> str:
        return f"Аудиокнига {super().__str__()}. Продолжительность: {self.duration} часов"


if __name__ == "__main__":
    # Пример использования:
    paper_book = PaperBook("Война и мир", "Лев Толстой", 1225)
    print(paper_book)

    audio_book = AudioBook("1984", "Джордж Оруэлл", 9.5)
    print(audio_book)