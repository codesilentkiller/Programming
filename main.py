from book import Book
from library import Library

# Create instances of books
book1 = Book("The Alchemist", "Paulo Coelho", "9780061122415", 5, 10)
book2 = Book("1984", "George Orwell", "9780451524935", 2, 5)
book3 = Book("The Alchemist", "Paulo Coelho", "9780061123456", 3, 7)  # Same title, different ISBN

# Create a library
library = Library("City Library")

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Borrow a book
library.borrow_book("9780061122415")

# Return a book
library.return_book("9780451524935")

# Search for books by title
library.find_books_by_title("The Alchemist")

# List all available books
available_books = library.list_available_books()
for book in available_books:
    print(book)

# Print library details
print(library)
