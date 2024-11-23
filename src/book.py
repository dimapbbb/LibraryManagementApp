class Book:
    def __init__(self, title, author, year):
        self.book_id = self.get_id
        self.title = title
        self.author = author
        self.year = year
        self.status = True

    def get_id(self):
        """ Create unique id fo book """
        pass

