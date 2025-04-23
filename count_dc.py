from typing import List

# Time complexity: O(n)
# Space complexity: O(n)
def count_dc(arr: List[int]) -> int:
    if (arr == []):
        return 0

    return 1 + count_dc(arr[1:])

# Test cases
print(count_dc([])) # 0
print(count_dc([1, 2, 3, 4, 5])) # 5
print(count_dc([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 10
