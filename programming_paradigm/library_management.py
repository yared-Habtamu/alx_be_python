class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.__is_checked_out=True

        def is_checked(self):
            return self.__is_checked_out

class Library:
    def __init__(self):
        self.__books=[]
    book=Book()
    def add_book(self,book):
        self.__books.append(self.book.title)
        self.__books.append(self.book.author)

    def check_out_book(self,title):
        if self.book.title in self.__books:
            return self.book.is_checked()
        return not self.book.is_checked()
