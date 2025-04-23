# https://leetcode.com/problems/roman-to-integer/
# Given a roman numeral, convert it to an integer.
# O(n) time complexity
# O(1) space complexity
class Solution:
    dictionary = {
        "I":1,
        "IV":4,
        "V":5,
        "IX":9,
        "X":10,
        "XL":40,
        "L":50,
        "XC":90,
        "C":100,
        "CD":400,
        "D":500,
        "CM":900,
        "M":1000
    }
    def roman_to_int_recursion(self, s: str) -> int:
        if len(s) == 1 or len(s) == 2 and self.dictionary.get(s):
            return self.dictionary.get(s)

        # if self.dictionary.get(s[0]) < self.dictionary.get(s[1]):
        #     return self.dictionary.get(s[0] + s[1]) + self.roman_to_int_recursion(s[2:])

        if self.dictionary.get(s[0] + s[1]):
            return self.dictionary.get(s[0] + s[1]) + self.roman_to_int_recursion(s[2:])

        return self.dictionary.get(s[0]) + self.roman_to_int_recursion(s[1:])

    def roman_to_int_iterative(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and self.dictionary.get(s[i] + s[i + 1]):
                total += self.dictionary.get(s[i] + s[i + 1])
                i += 2
            else:
                total += self.dictionary.get(s[i])
                i += 1
        return total


# Test cases
print(Solution().roman_to_int_recursion("III")) # 3
print(Solution().roman_to_int_recursion("IV")) # 4
print(Solution().roman_to_int_recursion("IX")) # 9
print(Solution().roman_to_int_recursion("LVIII")) # 58
print(Solution().roman_to_int_recursion("MCMXCIV")) # 1994

print(Solution().roman_to_int_iterative("III")) # 3
print(Solution().roman_to_int_iterative("IV")) # 4
print(Solution().roman_to_int_iterative("IX")) # 9
print(Solution().roman_to_int_iterative("LVIII")) # 58
print(Solution().roman_to_int_iterative("MCMXCIV")) # 1994
