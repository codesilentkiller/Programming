# library.py
from book import Book

_ = Book  # temporary placeholder to handle the import


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self, book):
        if book.get_isbn() not in self.books:
            self.books[book.get_isbn()] = book
            print(f"Added book: {book.get_title()} to the library.")
        else:
            print(f"Book with ISBN {book.get_isbn()} already exists in the library.")

    def remove_book(self, isbn):
        if isbn in self.books:
            removed_book = self.books.pop(isbn)
            print(f"Removed book: {removed_book.get_title()} from the library.")
        else:
            print(f"No book with ISBN {isbn} found.")

    def find_books_by_title(self, title):
        found_books = [book for book in self.books.values() if book.get_title().lower() == title.lower()]
        if found_books:
            for book in found_books:
                print(book)  # Will use the __str__() method of the Book class
        else:
            print(f"No books found with the title '{title}'")
        return found_books

    def list_available_books(self):
        available_books = [book for book in self.books.values() if book.get_available_copies() > 0]
        return available_books  # Always return a list, even if empty

    def borrow_book(self, isbn):
        if isbn in self.books:
            self.books[isbn].borrow_book()
        else:
            print(f"No book with ISBN {isbn} found.")

    def return_book(self, isbn):
        if isbn in self.books:
            self.books[isbn].return_book()
        else:
            print(f"No book with ISBN {isbn} found.")

    def __str__(self):
        # Create a string representation of the library
        book_list = "\n".join(str(book) for book in self.books.values())  # Use __str__() of Book
        return f"Library Name: {self.name}\nBooks in Collection:\n{book_list if book_list else 'No books available.'}"
