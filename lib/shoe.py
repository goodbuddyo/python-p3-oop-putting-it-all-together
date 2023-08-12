#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand="Adidas", size=9):
        self.brand = brand
        self.size = size

    def get_size(self):
        print("Retrieving size.")
        return self._size

    def set_size(self, size):
        if (type(size) in (int, float)) and (0 <= size <= 1200):
            print(f"Setting size to { size }.")
            self._size = size

        else:
            print("size must be an integer")

    size = property(get_size, set_size,)

    def cobble(self):
        print("Your shoe is as good as new!")

        def get_condition(self):
            print("Retrieving condition value.")
            return self._condition

        def set_condition(self, condition):
            if condition == "New":
                print("New!")
                self._condition = condition
            else:
                print("Sorry, no condition info")
                self._condition = condition
                return self.condition

        condition = property(get_condition, set_condition)


guido = Shoe()
guido.cobble = True
guido.condition = "New"
guido.cobble
guido.condition
