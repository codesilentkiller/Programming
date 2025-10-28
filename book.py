# Creating the Book Class
class Book:

    def __init__(self, title, author, isbn, available_copies, total_copies):  # Initialize the object's attributes
        self._title = None
        self._author = None
        self._isbn = None
        self._available_copies = None
        self._total_copies = None

        # Use setters to initialize
        self.set_title(title)
        self.set_author(author)
        self.set_isbn(isbn)
        self.set_available_copies(available_copies)
        self.set_total_copies(total_copies)

    # Getters and Setters for Title
    def get_title(self):
        return self._title

    def set_title(self, title):
        if isinstance(title, str) and title:  # Validating that title is a non-empty string
            self._title = title
        else:
            print("Invalid Title")

    # Getters and Setters for Author
    def get_author(self):
        return self._author

    def set_author(self, author):
        if isinstance(author, str) and author:  # Validating that author is a non-empty string
            self._author = author
        else:
            print("Invalid Author")

    # Getter and Setter for ISBN
    def get_isbn(self):
        return self._isbn

    def set_isbn(self, isbn):
        if self.validate_isbn(isbn):  # Calling validate_isbn method
            self._isbn = isbn
        else:
            print("Invalid ISBN. It must be a 13-digit number.")

    # Getters and Setters for Available Copies
    def get_available_copies(self):
        return self._available_copies

    def set_available_copies(self, available_copies):
        if isinstance(available_copies, int) and available_copies >= 0:
            self._available_copies = available_copies
        else:
            print("Invalid number of available copies")

    # Getters and Setters for Total Copies
    def get_total_copies(self):
        return self._total_copies

    def set_total_copies(self, total_copies):
        if isinstance(total_copies, int) and total_copies > 0:
            self._total_copies = total_copies
        else:
            print("Invalid number of total copies")

    # Validation method for ISBN
    @staticmethod
    def validate_isbn(isbn):  # Static because it has no need to access instance or class level data
        return len(isbn) == 13 and isbn.isdigit()


    # Method to return information about the book
    def get_book_info(self):  # Return details about the book
        return f"Title: {self.get_title()} \nAuthor: {self.get_author()} \nIsbn: {self.get_isbn()} \nAvailable: {self.get_available_copies()} / {self.get_total_copies()}"

    # Borrow a book (decrease available copies)
    def borrow_book(self):
        if self.get_available_copies() > 0:
            self.set_available_copies(self.get_available_copies() - 1)
            print(f"{self.get_title()} book has been borrowed, remaining copies: {self.get_available_copies()}")
        else:
            print(f"No available copies")

    # Return a book (increase available copies)
    def return_book(self):
        if self.get_available_copies() < self.get_total_copies():
            self.set_available_copies(self.get_available_copies() + 1)
            print(f"{self.get_title()} has been returned, thank you")
        else:
            print("All copies are already returned")

    # String representation of the object
    def __str__(self):
        return f"{self.get_title()} {self.get_author()} {self.get_isbn()} {self.get_available_copies()} {self.get_total_copies()}"

