def fibonacci(n):
    # Base case 1: if n is 0, return 0
    if n <= 0:
        return 0
    # Base case 2: if n is 1, return 1
    elif n == 1:
        return 1
    # Recursive case: if n is greater than 1, return the sum of the two preceding numbers
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test cases
print(fibonacci(0))  # Output: 0
print(fibonacci(1))  # Output: 1
print(fibonacci(2))  # Output: 1
print(fibonacci(5))  # Output: 5
print(fibonacci(10))  # Output: 55
print(fibonacci(12))  # Output: 144

# The time complexity of the fibonacci function is O(2^n)
# The space complexity of the fibonacci function is O(n)

# The fibonacci function is a recursive function that calculates the nth number in the fibonacci sequence
# The fibonacci sequence is a sequence of numbers where each number is the sum of the two preceding ones, starting from 0 and 1

# Example of the fibonacci sequence:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
