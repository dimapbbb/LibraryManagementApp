from datetime import datetime


def validate_year(year):
    """ Проверка введеного года """
    if year.isdigit():
        if int(year) > datetime.now().year:
            print(ValueError("Год издания не может быть из будущего"))
        else:
            return year
    else:
        print(ValueError("Год издания должен состоять из цифр"))


def validate_book_id(book_id):
    """ Проверка введенного id книги """
    if book_id.isdigit():
        return int(book_id)
    else:
        print(ValueError("id должен состоять из цифр"))


