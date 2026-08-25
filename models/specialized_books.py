from models.base_book import Book

class PaperBook(Book):

    def __init__(self, title, author, isbn, binding):
        super().__init__(title, author, isbn)
        self.__binding = binding

    def display_info(self):
        return f'{super().display_info()}\n제본방식: {self.__binding}(#종이책)'

class EBook(Book):

    def __init__(self, title, author, isbn, format):
        super().__init__(title, author, isbn)
        self.__format = format

    def display_info(self):
        return f'{super().display_info()}\n발행유형: {self.__format}(#전자책)'