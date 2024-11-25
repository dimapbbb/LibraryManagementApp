from src.library import Library
from src.validators import validate_book_id, validate_year


def main():
    library = Library()
    print(library.commands)

    while True:
        command = input('Введите номер команды: ')

        if command == '1':
            title = input('Название: ')
            author = input('Автор: ')
            year = input('Год издания: ')
            if validate_year(year):
                new_book = library.add_book(title, author, year)
                print(new_book, "Успешно добавлено")

        elif command == '2':
            for book in library.view_all_books():
                print(book)

        elif command == '3':
            book_id = input("Введите id книги: ")
            if validate_book_id(book_id):
                if library.delete_book(int(book_id)):
                    print("Удалено")
                else:
                    print("Не найдено")

        elif command == '4':
            book_id = input("Введите id книги: ")
            if validate_book_id(book_id):
                new_status = library.change_status(int(book_id))
                print(new_status)

        elif command == '5':
            keywords = input("Введите ключевые слова через пробел: ").split()
            result = library.search_book(keywords)
            if result:
                for book in result:
                    print(book)
            else:
                print("Нет результатов")

        elif command == '0':
            return

        else:
            print('Такой команды не существует, введите корректную команду')
            print(library.commands)


if __name__ == "__main__":
    main()
