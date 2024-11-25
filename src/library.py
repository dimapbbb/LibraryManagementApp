from src.fileworker import JsonWorkerMixin


class Library(JsonWorkerMixin):
    """
    Класс для работы с библиотекой
    """

    def add_book(self, title:str, author:str, year:str):
        """ Добавление книги в библиотеку """
        library = self.read_file()
        new_book = {
            "book_id": self.get_unique_id(library),
            "title": title.strip(),
            "author": author.strip(),
            "year": year.strip(),
            "status": "в наличии"
        }
        library.append(new_book)
        self.write_file(library)

        return new_book

    def search_book(self, keywords:list):
        """ Поиск книг по ключевым словам """
        library = self.read_file()
        result = []
        for book in library:
            word_list = self.get_word_list(book)
            for keyword in keywords:
                if keyword.lower() in word_list:
                    result.append(book)
                    break
        return result

    def delete_book(self, book_id:int):
        """ Удаление книги из библиотеки """
        library = self.read_file()
        for book in library:
            if book_id == book.get('book_id'):
                library.remove(book)
                self.write_file(library)
                return True

    def change_status(self, book_id:int):
        """ Изменение статуса книги """
        library = self.read_file()
        for book in library:
            if book_id == book.get('book_id'):
                if book['status'] == 'выдана':
                    book['status'] = 'в наличии'
                    new_status = 'в наличии'
                else:
                    book['status'] = 'выдана'
                    new_status = 'выдана'
                self.write_file(library)
                break
        else:
            new_status = "Не найдено"
        return new_status

    def view_all_books(self):
        """ Просмотр всех книг из библиотеки """
        library = self.read_file()
        return library

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
    def get_unique_id(library:list):
        """ Получение уникального id при добавлении книги """
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

    @staticmethod
    def get_word_list(book:dict):
        """ Слова из названия, автора и года издания возвращаются в одном списке """
        # Все в одну строку
        string = " ".join([book['title'], book['author'], book['year']])
        clear_string = ""

        # Все что не буква или цифра заменить на пробел
        for letter in string:
            if letter.isdigit() or letter.isalpha():
                clear_string += letter
            else:
                clear_string += " "

        # Собрать в список и сделать все буквы маленькими
        word_list = list(map(lambda x: x.lower(), clear_string.split()))

        return word_list