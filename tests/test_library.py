import unittest

from src.fileworker import JsonWorkerMixin
from src.library import Library


class TestLibrary(unittest.TestCase):
    fileworker = JsonWorkerMixin()
    test_library_data = [
        {
            "book_id": 1,
            "title": "Мастер и Маргарита",
            "author": "Михаил Булгаков",
            "year": "1928",
            "status": "в наличии"
        },
        {
            "book_id": 2,
            "title": "Анна/Каренина,",
            "author": "Лев_Толстой",
            "year": "1877!",
            "status": "выдана"
        },
        {
            "book_id": 3,
            "title": "отцы!и_дети",
            "author": "Иван Тургенев",
            "year": "1861",
            "status": "в наличии"
        }
    ]
    fileworker.write_file(test_library_data)
    test_library = Library()

    def test_get_unique_id(self):
        # Если библиотека пустая
        self.assertEqual(self.test_library.get_unique_id([]), 1)
        # Получение следующего номера
        self.assertEqual(self.test_library.get_unique_id([
            {"book_id": 1},
            {"book_id": 2},
            {"book_id": 3}
        ]), 4)
        # Получение номера, который ранее был удален
        self.assertEqual(self.test_library.get_unique_id([
            {"book_id": 1},
            {"book_id": 2},
            {"book_id": 4}
        ]), 3)
        # Проверка различных вариантов
        self.assertEqual(self.test_library.get_unique_id([
            {"book_id": 4},
            {"book_id": 3},
            {"book_id": 2}
        ]), 1)
        self.assertEqual(self.test_library.get_unique_id([
            {"book_id": 1},
            {"book_id": 4},
            {"book_id": 3}
        ]), 2)

    def test_view_all_books(self):
        # Тест на получение списка всех книг библиотеки
        self.assertEqual(len(self.test_library.view_all_books()), 3)

    def test_get_word_list(self):
        # Тест на игнрирование знаков препинания при поиске
        self.assertEqual(self.test_library.get_word_list(
            {
                "book_id": 2,
                "title": "Анна/Каренина,",
                "author": "Лев_Толстой",
                "year": "1877!",
                "status": "выдана"
            },
        ), ["анна", "каренина", "лев", "толстой", "1877"])

    def test_search_book(self):
        # Тест на отсутсвие результатов
        self.assertEqual(self.test_library.search_book(["гоголь"]), [])
        # Тест на отсутсвие дубликатов
        self.assertEqual(len(self.test_library.search_book(["толстой", "лев"])), 1)
        # тест на результат
        self.assertEqual(self.test_library.search_book(["лев"]), [self.test_library_data[1]])

    def test_change_status(self):
        # Тест на смену статуса с "в наличии" на "выдана"
        self.assertEqual(self.test_library.change_status(1), "выдана")
        # И наоборот
        self.assertEqual(self.test_library.change_status(1), "в наличии")

    def test_add_book(self):
        # Тест на создание книги
        result = {
            "book_id": 4,
            "title": "Евгений Онегин",
            "author": "Александр Сергеевич Пушкин",
            "year": "1831",
            "status": "в наличии"
        }
        self.assertEqual(self.test_library.add_book(
            "Евгений Онегин",
            "Александр Сергеевич Пушкин",
            "1831"
        ), result)

    def test_delete_book(self):
        # Тест на удаление книги
        self.assertTrue(self.test_library.delete_book(4))
        # Тест на случай отсутсвия книги в хранилище
        self.assertFalse(self.test_library.delete_book(5))
