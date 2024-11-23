from datetime import datetime


class Book:
    def __init__(self, title:str, author:str, year:str):
        self.book_id = 0
        self.title = title.title()
        self.author = author.title()
        self.year = year
        self.status = "в наличии"

    def books_list(self):
        pass

    @classmethod
    def create(cls, **kwargs):
        if cls.validate_year(kwargs.get('year')):
            return cls(**kwargs)

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    @staticmethod
    def validate_year(year:str):
        if year.isdigit():
            if int(year) > datetime.now().year:
                return
            else:
                return True
        else:
            return