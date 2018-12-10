import numpy as np
from Order import Order
#from Main import find_distance


class Drone:
    def __init__(self, name, max_load, n_products):
        self.max_load = max_load
        self.loaded = np.zeros(n_products)
        self.current_location = (0, 0)
        self.busy = False
        self.name = name
        self.current_warehouse = 0
        self.current_weight = 0
        self.c_time = 0
        self.free_space = max_load - self.current_weight
        self.loaded_items = [0 for i in range(n_products)]

    def go_to_wh(self):
        pass

    def complete_order(self, order, sim_time):
        pass





