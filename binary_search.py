import random

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

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

def create_item_list():
    return [
        Item("Buku", 5000),
        Item("Pensil", 2000),
        Item("Musang", 50000000),
        Item("Mobil", 20000)
    ]
    
items = create_item_list()
items.sort(key=lambda x: x.name.lower())

target_name = input("Masukkan nama barang yang akan dicari : ")

price_binary = binary_search(items, target_name, 0, len(items) -1 )

if price_binary is not None:
    print(f"Harga {target_name} adalah Rp {price_binary}")
else:
    print(f"{target_name} tidak ditemukan")