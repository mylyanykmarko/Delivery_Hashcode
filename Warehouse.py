import numpy as np


class Warehouse:
    def __init__(self, index, n_items, items_list, coordinates):
        self.index = index
        self.n_items = n_items
        self.items_list = items_list
        self.coordinates = coordinates

    def is_empty(self):
        return self.items_list == [0 for i in range(self.n_items)]

