class Book:
    def __init__(self, title, author, ISBN, total_copies, available_copies):
        self.__title = title
        self.__author = author
        self.__ISBN = ISBN
        self.__total_copies = total_copies
        self.__available_copies = available_copies

    def get_book_info(self):
        print(f'Title of the book : {self.__title}')
        print(f'Author of the book : {self.__author}')
        print(f'ISBN of the book : {self.__ISBN}')
        print(f'Total Copies : {self.__total_copies}')
        print(f'Available Copies : {self.__available_copies}')

    def borrow_book(self):
        if self.__available_copies > 0:
            self.__available_copies -= 1
            print(f'{self.__title} was borrowed.')
            return f'Available Books : {self.__available_copies}'
        else:
            return f'{self.__title} is not available'

    def return_book(self):
        self.__available_copies += 1
        print(f'{self.__title} has been returned.')
        return f'Available Books : {self.__available_copies}'

    def set_title(self, new_value):
        if isinstance(new_value, str):
            self.__title = new_value
        else:
            print('You are only allowed to enter a string value.')

    def get_title(self):
        return self.__title

    def set_author(self, new_value):
        if isinstance(new_value, str):
            self.__author = new_value
        else:
            print('You are only allowed to enter a string value.')

    def get_author(self):
        return self.__author

    def set_ISBN(self, new_value):
        if isinstance(new_value, int):
            self.__ISBN = new_value
        else:
            print('You are only allowed to enter an integer value.')

    def get_ISBN(self):
        return self.__ISBN

    def set_total_copies(self, new_value):
        if isinstance(new_value, int):
            self.__total_copies = new_value
        else:
            print('You are only allowed to enter an integer value.')

    def get_total_copies(self):
        return self.__total_copies

    def set_available_copies(self, new_value):
        if isinstance(new_value, int):
            self.__available_copies = new_value
        else:
            print('You are only allowed to enter an integer value.')

    def get_available_copies(self):
        return self.__available_copies

