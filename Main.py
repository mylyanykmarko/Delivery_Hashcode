"""All drones
Якшо дрон на складі, то він бере максимум продуктів які треба найближчому ордеру
Якшо дрон на ордері, то він летить до найближчого не пустого складу

"""
from Warehouse import Warehouse
from Drone import Drone
from Order import Order
from math import ceil

n_rows = int(input())
n_cols = int(input())
n_drones = int(input())
deadline = int(input())
drone_maxload = int(input())
n_products = int(input())
products_weights = input().split(" ")
products_weights = [int(i) for i in products_weights]
n_warehouses = int(input())

warehouses = []
for i in range(n_warehouses):
    a, b = input().split(" ")
    products = input().split(" ")
    w = Warehouse(i, n_products, [int(j) for j in products], (int(a), int(b)))
    warehouses.append(w)

n_orders = int(input())
orders = []
for i in range(n_orders):
    a, b = input().split(" ")
    n_ordered = int(input())
    order_list = input().split(" ")
    order_list = [int(j) for j in order_list]
    o = Order(i, (int(a), int(b)), order_list, n_ordered, n_products)
    orders.append(o)

total_commands = 0

drones = []
for i in range(n_drones):
    drones.append(Drone(i, drone_maxload, n_products))


def find_distance(drone, warehouse):
    return ((warehouse.coordinates[0] - drone.current_location[0]) ** 2 + (warehouse.coordinates[1] - drone.current_location[1]) ** 2) ** 0.5


def find_closest_warehouses(drone, warehouses):
    "Returns sorted list of warehouses from closest to farest"
    closest = sorted(warehouses, key=lambda x: find_distance(drone, x))
    return closest


def find_closest_order(drone, orders):
    "returns closest order to drone( Order type)"
    closest = sorted(orders, key=lambda x: find_distance(drone, x))
    return closest


def put_products(drone: Drone, order: Order, warehouse: Warehouse):
    """
    adding maximal number of items which are needed to closest order
    """
    global drone_maxload, n_products, products_weights, total_commands
    item_list = order.items_list
    for i in range(n_products):
        if drone.current_weight < drone_maxload and item_list[i] and warehouse.items_list[i]:
            if item_list[i] > warehouse.items_list[i]:
                if drone.current_weight + (warehouse.items_list[i]*products_weights[i]) < drone_maxload:
                    drone.loaded_items[i] += warehouse.items_list[i]
                    drone.current_weight += warehouse.items_list[i]*products_weights[i]
                    warehouse.items_list[i] = 0
                    print(drone.name, " L ", warehouse.index, i, warehouse.items_list[i])
                    print("1")

                else:
                    items_to_add = drone.free_space//products_weights[i]
                    drone.loaded_items[i] += items_to_add
                    drone.current_weight += items_to_add*products_weights[i]
                    warehouse.items_list[i] -= items_to_add
                    print(drone.name, " L ", warehouse.index, i, items_to_add)
                    print("2")

            else:
                if drone.current_weight + (item_list[i]*products_weights[i]) < drone_maxload:
                    drone.loaded_items[i] += item_list[i]
                    drone.current_weight += item_list[i]*products_weights[i]
                    warehouse.items_list[i] -= item_list[i]
                    print(drone.name, " L ", warehouse.index, i, item_list[i])
                    print("3")
                else:
                    items_to_add = drone.free_space//products_weights[i]
                    drone.loaded_items[i] += items_to_add
                    drone.current_weight += items_to_add*products_weights[i]
                    warehouse.items_list[i] -= items_to_add
                    print(drone.name, " L ", warehouse.index, i, items_to_add)

    total_commands += 1


def deliver(drone: Drone, order: Order):
    "substract items from order and drone baggage"
    items = order.items_list
    for i in drone.loaded_items:
        items[i] -= drone.loaded_items[i]
        drone.loaded_items[i] = 0
        print(drone.name, " D ", order.name, i, drone.loaded_items[i])
    drone.current_weight = 0
    order.items_list = items
    drone.current_location = order.coordinates


for i in drones:
    print(i.name)

    while i.c_time < deadline:
        "What drone should do if it is in warehouse"
        if not i.busy:
            closest_wh = find_closest_warehouses(i, warehouses)
            closest_o = find_closest_order(i, orders)
            j = 0
            k = 0
            while closest_wh[j].is_empty() and j < n_warehouses:
                j += 1
            while not closest_o[k].active and k < n_orders:
                k += 1
            put_products(i, closest_o[k], closest_wh[j])
           # print(i.name, i.loaded_items)
            i.c_time += 1
            #print(i.c_time)
            "Next will be time to deliver products"
            if i.c_time + ceil(find_distance(i, closest_o[k])) < deadline:
                deliver(i, closest_o[k])
                i.current_location = closest_o[k].coordinates
                i.c_time += ceil(find_distance(i, closest_o[k]))
                i.busy = True
        else:
            closest_wh = find_closest_warehouses(i, warehouses)
            j = 0
            while closest_wh[j].is_empty():
                j += 1
            if i.c_time + find_distance(i, closest_wh[j]) < deadline:
                i.current_location = closest_wh[j].coordinates
                i.c_time += ceil(find_distance(i, closest_wh[j]))
                i.busy = False


















