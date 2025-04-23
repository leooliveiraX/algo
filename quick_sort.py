# Quick sort -> O(n log n) time complexity, O(log n) space complexity
def quick_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    # Recursive case
    # 1. Choose a pivot
    # 2. Partition the array into two sub-arrays based on the pivot
    # 3. Recursively apply the same logic to the left and right sub-arrays
    # 4. Combine the sorted left and right sub-arrays with the pivot
    pivot = arr[0]
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

# Test cases
print(quick_sort([3, 6, 8, 10, 1, 2, 1])) # [1, 1, 2, 3, 6, 8, 10]
print(quick_sort([1, 2, 3, 4, 5])) # [1, 2, 3, 4, 5]
print(quick_sort([5, 4, 3, 2, 1])) # [1, 2, 3, 4, 5]
print(quick_sort([])) # []
print(quick_sort([1])) # [1]
