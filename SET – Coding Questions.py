# SET – Coding Questions

# 1. Set Operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Union: {set1 | set2}")                 # Elements in either set
print(f"Intersection: {set1 & set2}")          # Elements in both sets
print(f"Difference (1-2): {set1 - set2}")      # In set1 but not set2
print(f"Symmetric Difference: {set1 ^ set2}")  # In one but not both

# 2. Remove common elements
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}
common = s1 & s2
s1 -= common
s2 -= common

print(f"Set 1 updated: {s1}")
print(f"Set 2 updated: {s2}")

# 3. Subset check
small_set = {1, 2}
large_set = {1, 2, 3, 4}
is_subset = small_set.issubset(large_set)

print(f"Is subset? {is_subset}")

# 4. Filter set elements
numbers = {12, 45, 7, 23, 56, 89}
threshold = 30

print(f"Elements greater than {threshold}:")
for num in numbers:
    if num > threshold:
        print(num)

# 5. List to Set back to List (Deduplication)
original_list = [1, 2, 2, 3, 4, 4, 4, 5]
unique_list = list(set(original_list))

print(unique_list)

