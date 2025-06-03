from typing import List

# Time complexity: O(n)
# Space complexity: O(n)
def bigger_num(arr: List[int]) -> int:
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    sub_max = bigger_num(arr[1:])

    return arr[0] if arr[0] > sub_max else sub_max

# Test cases
print(bigger_num([1, 2, 3, 4, 5])) # Output: 5
print(bigger_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 10
print(bigger_num([10, 2, 3, 4, 5])) # Output: 10
print(bigger_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 10
