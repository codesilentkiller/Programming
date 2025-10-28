from booka import Book

_ = Book # temporary placeholder
class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_books(self, book):
        self.books[book.get_ISBN()] = book
        print(f'{book.get_title()} with {book.get_ISBN()} by {book.get_author()} was added to library.')

    def delete_book(self, ISBN):
        if ISBN in self.books:
            del self.books[ISBN]
        else:
            print('The book is not in our Library.')

    def find_book_by_title(self):
        return [book.get_book_info() for book in self.books.values() if book.title == book.title]

    def list_available_copies(self):
        return [book.get_book_info() for book in self.books.values() if book.available_copies > 0]

    def borrow_book(self, ISBN):
        if ISBN in self.books:
            return self.books[ISBN].borrow_book()
        else:
            print('The book is not available.')

    def return_book(self, ISBN):
        if ISBN in self.books:
            return self.books[ISBN].return_book()
        else:
            print('The book is not available.')

