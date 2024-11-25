def print_(book:dict):
    """ Перевод в удобочитаемый формат """
    print(f"{book["book_id"]}: {book["title"]} | {book["author"]}; {book["year"]} ({book["status"]})")