# TUPLE – Coding Questions

# 1. Max and Min
tup = (5, 10, 1, 85)
print(f"Max: {max(tup)}, Min: {min(tup)}")

# 2. List of tuples to dictionary
list_of_tuples = [("name", "Yash"), ("age", 22), ("city", "Pune")]
result_dict = dict(list_of_tuples)

print(result_dict)

# 3. Count occurrences manually
my_tuple = (1, 2, 3, 2, 4, 2, 5)
tar = 2
def manual_count(tpl, target):
    count = 0
    for item in tpl:
        if item == target:
            count += 1
    return count

print(f"Count of {tar} is :{manual_count(my_tuple, tar)}")

# 4. Modify mutable element inside tuple
my_tuple = ([1, 2, 3], "static")
my_tuple[0].append(4)

print(my_tuple)

# 5. Swap two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple1, tuple2 = tuple2, tuple1

print(f"tuple1: {tuple1}")
print(f"tuple2: {tuple2}")

