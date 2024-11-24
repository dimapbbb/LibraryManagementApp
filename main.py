from src.library import Library


def main():
    library = Library()
    print(library.commands)
    while True:
        command = input('Введите номер команды: ')
        if command == '1':
            library.add_book()
        elif command == '2':
            library.view_all_books()
        elif command == '3':
            library.delete_book()
        elif command == '4':
            library.change_status()
        elif command == '5':
            library.search_book()
        elif command == '0':
            return
        else:
            print('Такой команды не существует, введите корректную команду')
            print(library.commands)


if __name__ == "__main__":
    main()
