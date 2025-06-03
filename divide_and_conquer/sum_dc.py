from typing import List

# Time complexity: O(n)
# Space complexity: O(n)
def sum_dc(arr: List[int]) -> int:
    if (arr == []):
        return 0

    return arr[0] + sum_dc(arr[1:])

# Test cases
print(sum_dc([])) # Output: 0
print(sum_dc([1, 2, 3, 4, 5])) # Output: 15
print(sum_dc([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 55
