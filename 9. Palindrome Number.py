"""=================================================================================================
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

-2**31 <= x <= 2**31 - 1

Follow up: Could you solve it without converting the integer to a string?
%取余
//取模
Wenxuan Dong        2024/9/21
================================================================================================="""
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         s = str(abs(x))
#         ss = s[::-1]
#         sss = int(ss)
#         if sss == x:
#             return True
#         else:
#             return False

# without converting integer to string
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#
#         if x < 0:
#             return False
#
#         list = []
#         while x > 0:
#             list.append(x % 10)
#             x //= 10
#
#         return list == list[::-1]

# reduce time complexity? no. But can reduce memory complexity
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Early return on negative numbers or numbers ending in zero (but not zero itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For numbers with an odd digit count, discard the middle digit before comparison
        return x == reversed_half or x == reversed_half // 10



if __name__ == "__main__":
    x = 10
    sol = Solution()
    res = sol.isPalindrome(x)
    print(res)