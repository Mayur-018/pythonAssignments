# LIST – Coding Questions

# 1. Remove duplicates without set
nums = [1, 2, 2, 3, 4, 4, 5]
def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

print(remove_duplicates(nums))

# 2. List comprehension for even numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in nums if n % 2 == 0]
print(evens)

# 3. Second largest element
nums = [10, 20, 4, 45, 99, 20]
unique_nums = list(set(nums))
unique_nums.sort()
print(f"Second Largest: {unique_nums[-2]}")

# 4. Sum of inner lists
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
inner_sums = [sum(inner) for inner in nested_list]
print(inner_sums)

# 5. Shallow vs Deep Copy
import copy
original = [[1, 2], [3, 4]]
# Shallow copy
shallow = original.copy()
# Deep copy
deep = copy.deepcopy(original)
# Modifying the original's first sublist
original[0][0] = 'X'

print(f"Original: {original}")
print(f"Shallow:  {shallow}")
print(f"Deep:     {deep}")

