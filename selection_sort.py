from typing import List

# Get the index of the minor element in the array
def get_minor(arr: List[int]) -> int:
    minor = arr[0]
    minor_index = 0

    for i in range(1, len(arr)):
        if arr[i] < minor:
            minor = arr[i]
            minor_index = i

    return minor_index

# Sort the array using selection sort
# Time complexity: O(n^2)
# Space complexity: O(n)
def selection_sort(arr: List[int]) -> List[int]:
    ordered_arr = []

    for _ in range(len(arr)):
        minor = get_minor(arr)
        ordered_arr.append(arr.pop(minor))

    return ordered_arr

# Test cases
print(selection_sort([64, 25, 12, 22, 11]))
print(selection_sort([3, 2, 1]))
print(selection_sort([1, 2, 3]))
print(selection_sort([1]))
print(selection_sort([]))
