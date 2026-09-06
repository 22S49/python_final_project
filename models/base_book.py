class Book:

    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__status = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def display_info(self):
        return f'도서명: {self.__title}\n작가명: {self.__author}\nISBN: {self.__isbn}\n대여상태: {'대여가능' if self.__status else '대여불가'}'