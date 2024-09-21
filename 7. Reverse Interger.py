"""=================================================================================================
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:
-2**31 <= x <= 2**31 - 1
Wenxuan Dong        2024/9/21
================================================================================================="""
class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))
        ss = s[::-1]
        sss = int(ss)
        if sss < (2**31)-1 and sss > -(2**31):
            if x > 0:
                return sss
            else:
                return sss*-1
        else:
            return 0

if __name__ == "__main__":
    x = 321
    solution = Solution()
    result = solution.reverse(x)
    print(result)