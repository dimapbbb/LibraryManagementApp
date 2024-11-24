from src.validators import validate_book_id, validate_year
from src.fileworker import JsonWorkerMixin


class Library(JsonWorkerMixin):
    """
    Класс для работы с библиотекой
    """

    def add_book(self):
        """ Добавление книги в библиотеку """
        title = input('Название: ')
        author = input('Автор: ')
        year = input('Год издания: ')
        year = validate_year(year)
        if year:
            library = self.read_file()
            new_book = {
                "book_id": self.get_unique_id(library),
                "title": title,
                "author": author,
                "year": year,
                "status": "в наличии"
            }
            library.append(new_book)
            self.write_file(library)
            print("Успешно")


    def search_book(self):
        """ Поиск книг по ключевым словам """
        keywords = input("Введите ключевые слова через пробел: ").split()
        library = self.read_file()
        result = 0
        for book in library:
            for keyword in keywords:
                if keyword.lower() in map(lambda x:x.lower(), " ".join([book['title'], book['author'], book['year']]).split()):
                    print(book)
                    result += 1
                    break
        if not result:
            print(ValueError('Не найдено'))

    def delete_book(self):
        """ Удаление книги из библиотеки """
        book_id = input("Введите id книги: ")
        book_id = validate_book_id(book_id)
        if book_id:
            library = self.read_file()
            for book in library:
                if book_id == book.get('book_id'):
                    library.remove(book)
                    self.write_file(library)
                    print('Удалено')
                    break
            else:
                print(ValueError("Не найдено"))

    def change_status(self):
        """ Изменение статуса книги """
        book_id = input("Введите id книги: ")
        book_id = validate_book_id(book_id)
        if book_id:
            library = self.read_file()
            for book in library:
                if book_id == book.get('book_id'):
                    if book['status'] == 'выдана':
                        book['status'] = 'в наличии'
                        print('в наличии')
                    else:
                        book['status'] = 'выдана'
                        print('выдана')
                    self.write_file(library)
                    break
            else:
                print(ValueError("Не найдено"))

    def view_all_books(self):
        """ Просмотр всех книг из библиотеки """
        library = self.read_file()
        for book in library:
            print(book)

    @property
    def commands(self):
        """ Список команд для работы с библиотекой """
        commands_list = (f"1  -->  Добавить книгу в библиотеку\n"
                         f"2  -->  Просмотр списка всех книг\n"
                         f"3  -->  Удалить книгу из библиотеки\n"
                         f"4  -->  Изменить статус книги\n"
                         f"5  -->  Поиск по ключевым словам\n"
                         f"0  -->  Завершить работу")

        return commands_list

    @staticmethod
    def get_unique_id(library):
        """ Получение уникального id при создании книги """
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