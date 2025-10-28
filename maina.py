from librarya import Library
from booka import Book
book1 = Book("The Alchemist", "Paulo Coelho", "9780061123456", 3, 7)  # Same title, different ISBN

print(book1.get_title())




library1 = Library('sl')

print(library1.add_books(book1))