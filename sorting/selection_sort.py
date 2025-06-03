from typing import List

# Selection sort is a sorting algorithm that repeatedly selects the minimum element from an unsorted list and swaps it with the first element

# Time complexity: O(n^2)
# Space complexity: O(n)

def selection_sort(arr: List[int]) -> List[int]:
    ordered_arr = []

    for _ in range(len(arr)):
        minor = get_minor(arr)
        ordered_arr.append(arr.pop(minor))

    return ordered_arr

# Get the index of the minor element in the array
def get_minor(arr: List[int]) -> int:
    minor = arr[0]
    minor_index = 0

    for i in range(1, len(arr)):
        if arr[i] < minor:
            minor = arr[i]
            minor_index = i

    return minor_index

# Test cases
print(selection_sort([64, 25, 12, 22, 11])) # Output: [11, 12, 22, 25, 64]
print(selection_sort([3, 2, 1])) # Output: [1, 2, 3]
print(selection_sort([1, 2, 3])) # Output: [1, 2, 3]
print(selection_sort([1])) # Output: [1]
print(selection_sort([])) # Output: []
