#!/usr/bin/env python3

class Book:

    def __init__(self, title='Enter a title', page_count=0):
        self.title = title
        self.page_count = page_count

    def get_page_count(self):
        print("Retrieving page_count.")
        return self._page_count

    def set_page_count(self, page_count):
        if (type(page_count) in (int, float)) and (0 <= page_count <= 1200):
            print(f"Setting page_count to { page_count }.")
            self._page_count = page_count

        else:
            print("page_count must be an integer")

    page_count = property(get_page_count, set_page_count,)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


guido = Book()
guido.page_count = 0
guido.page_count = False
guido.page_count = 66
guido.page_count
# booktest = Book("Titanic", 201)
