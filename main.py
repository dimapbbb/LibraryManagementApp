from src.library import Library


def main():
    library = Library()
    print(library.commands)
    while True:
        command = input('Введите номер команды: ')
        if command == '1':
            library.new_book()
        elif command == '0':
            return
        else:
            print('Такой команды не существует, введите корректную команду')


if __name__ == "__main__":
    main()
