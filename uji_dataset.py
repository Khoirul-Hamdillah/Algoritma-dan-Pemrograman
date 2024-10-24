import random
import time

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def linear_search(items, target_name):
    for item in items:
        if item.name.lower() == target_name.lower():
            return item.price
    return None

def binary_search(items, target_name, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    mid_name = items[mid].name.lower()

    if mid_name == target_name.lower():
        return items[mid].price
    elif target_name.lower() < mid_name:
        return binary_search(items, target_name, low, mid - 1)
    else:
        return binary_search(items, target_name, mid + 1, high)

def create_item_list(size):
    items = []
    for i in range(size):
        name = f"Barang {i + 1}"
        price = random.randint(1000, 100000)
        items.append(Item(name, price))
    return items

def measure_time(search_func, *args):
    start_time = time.time()
    search_func(*args)
    return time.time() - start_time

sizes = [100, 1000, 10000]
results = []

for size in sizes:
    items = create_item_list(size)
    items.sort(key=lambda x: x.name.lower())
    target_name = items[random.randint(0, size - 1)].name

    linear_time = measure_time(linear_search, items, target_name)

    binary_time = measure_time(binary_search, items, target_name, 0, size - 1)

    results.append((size, target_name, linear_time, binary_time))

print("Ukuran Dataset | Target Item   | Waktu Linear (s) | Waktu Binary (s)")
for result in results:
    print(f"{result[0]:<15} | {result[1]:<14} | {result[2]:<17.6f} | {result[3]:<15.6f}")