class Order:
    def __init__(self, name,  coordinates, item_list, n_ordered, n_products):
        self.name = name
        self.coordinates = coordinates
        self.n_ordered = n_ordered
        self.items_list1 = item_list
        self.n_products = n_products
        self.items_list = self.normal_items()
        self.active = not (item_list == [0 for i in range(n_products)])


    def normal_items(self):
        available_items = [0 for i in range(self.n_products)]
        for i in self.items_list1:
            available_items[i] += 1

        return available_items
