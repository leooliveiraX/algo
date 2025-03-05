# Creating an array (list in Python) with different data types
mixed_array = [
    42,               # integer
    "Hello",          # string
    3.14,             # float
    True,             # boolean
    [1, 2, 3],        # nested list
    {"name": "John"}, # dictionary
    (1, 2),           # tuple
    {1, 2, 3}         # set
]

# Display each element and its type
print("Array elements and their types:")
for item in mixed_array:
    print(f"{item} ({type(item).__name__})")

# You can also access elements by index
print("\nAccessing elements by index:")
print(f"First element: {mixed_array[0]}")
print(f"Second element: {mixed_array[1]}")

# You can modify elements with different types
print("\nModifying elements:")
mixed_array[0] = "Changed to string"  # Changed from int to string
mixed_array[1] = 100                  # Changed from string to int
print(f"After modification: {mixed_array[0]} ({type(mixed_array[0]).__name__})")
print(f"After modification: {mixed_array[1]} ({type(mixed_array[1]).__name__})")

# Adding new elements of different types
mixed_array.append(lambda x: x*2)  # Even functions can be stored!
print("\nArray after adding a function:")
for i, item in enumerate(mixed_array):
    print(f"Index {i}: {item} ({type(item).__name__})")
