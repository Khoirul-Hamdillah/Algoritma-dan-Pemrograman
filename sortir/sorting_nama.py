def sort_names(data): n
    return sorted(data)

data_input = input("masukkan nama :")
data = data_input.split()

sorted_names = sort_names(data)

print("nama yang sudah terurut :")
for i, nama in enumerate(sorted_names, 1):
    print(f"{i}.{nama}")
