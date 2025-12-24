# STRING - Coding Questions

# 1. Count types of characters
text = "Python 3.12 @ 2025!"
v, c, d, s = 0, 0, 0, 0
for char in text:
    if char.isalpha():
        if char.lower() in 'aeiou': v += 1
        else: c += 1
    elif char.isdigit(): d += 1
    elif not char.isspace(): s += 1
print(f"Vowels: {v}, Consonants: {c}, Digits: {d}, Special: {s}")

# 2. Reverse each word individually
text = "Hello World"
def reverse_words(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

print(reverse_words(text))

# 3. Palindrome using slicing
text="Racecar"
def is_palindrome(s):
    # Standardize string: lowercase and remove non-alphanumeric
    clean_s = "".join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]

print(is_palindrome(text))

# 4. Frequency of characters
text="apple"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(f"Frequency: {freq}")

# 5. String Immutability
s = "Hello"
try:
    s[0] = "Y"
except TypeError as e:
    print(f"Immutability Error: {e}")
