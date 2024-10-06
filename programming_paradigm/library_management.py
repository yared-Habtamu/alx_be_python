class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self._is_checked_out=False #available

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out=False
            return True #returned
        return False
    
    def check_book_out(self): #Available kehone return True now it's gonna be given to u
        if not self._is_checked_out:
            self._is_checked_out=True #assume tekeraye
            return True
        return False
    def available(self):
        return not self._is_checked_out
        
#Not available=Book is checked out
class Library:
    book=Book(self.title,self.author)
    def __init__(self):
        self._books=[]
    def add_book(self,book):
        self._books.append((book.title,book.author))

    def check_out_book(self,book):
        if book[0] in self._books:
            self._books.pop(book)
            return self.book.is_checked()
        return not self.book.is_checked()
    
    def return_book(self,title):
        self._books.append(self.book)

    def list_available_books(self,_books):
        for any_book in self._books:
            print(self._books(book.title))

