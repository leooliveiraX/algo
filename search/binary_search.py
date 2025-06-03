# Binary search is a search algorithm that finds the position of a target value within a sorted array

# It compares the target value to the middle element of the array
# If the target value is equal to the middle element, the index of the middle element is returned
# If the target value is less than the middle element, the search continues in the left half of the array
# If the target value is greater than the middle element, the search continues in the right half of the array

# Time complexity: O(log2 n)
# Space complexity: O(1)

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            # Return statement inside a while loop will break the loop and return the value to the function caller
            return mid

        # If the target is greater than the middle element, move the left pointer to the right of the middle element
        if arr[mid] < target:
            left = mid + 1
        else:
            # If the target is less than the middle element, move the right pointer to the left of the middle element
            right = mid - 1

    # If the target is not found, return -1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Test cases
print(binary_search(arr, 9)) # Output: 8
print(binary_search(arr, 11)) # Output: -1
print(binary_search(arr, 0)) # Output: -1
print(binary_search(arr, 5)) # Output: 4
