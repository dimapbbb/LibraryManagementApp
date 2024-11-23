from src.book import Book
from src.fileworker import JsonWorkerMixin


class Library(JsonWorkerMixin):
    def __init__(self):
        pass

    def new_book(self):
        title = input('Название: ')
        author = input('Автор: ')
        year = input('Год издания: ')

        new_book = Book.create(
            title=title,
            author=author,
            year=year
        )
        if new_book:
            self.save(new_book.__dict__)
            print(f"Успешно")
        else:
            print("Ошибка, Неверный формат года издания")

    def save(self, book:dict):
        """ Save book in library """
        library = self.read_file()
        book['book_id'] = self.get_unique_id(library)
        library.append(book)
        self.write_file(library)


    @staticmethod
    def get_unique_id(library):
        new_id = 1
        if library:
            ids_list = [book['book_id'] for book in library]
            while True:
                if new_id in ids_list:
                    new_id += 1
                    continue
                else:
                    return new_id
        else:
            return new_id

    @property
    def commands(self):
        """ Commands list """
        commands_list = (f"1  -->  Добавить книгу в библиотеку\n"
                         f"0  -->  Завершить работу")

        return commands_list