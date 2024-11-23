from datetime import datetime


class Book:
    def __init__(self, title:str, author:str, year:str, book_id=0, status="в наличии"):
        self.book_id = book_id
        self.title = title.title()
        self.author = author.title()
        self.year = year
        self.status = status

    def __str__(self):
        return f"{self.book_id}: {self.author} - {self.title}. {self.year} ({self.status})"

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