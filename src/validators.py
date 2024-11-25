from datetime import datetime


def validate_year(year:str):
    """ Проверка введеного года """
    if year.isdigit():
        if int(year) > datetime.now().year:
            print(ValueError("Год издания не может быть из будущего"))
        else:
            return True
    else:
        print(ValueError("Год издания должен состоять из цифр"))


def validate_book_id(book_id:str):
    """ Проверка введенного id книги """
    if book_id.isdigit():
        return True
    else:
        print(ValueError("id должен состоять из цифр"))


