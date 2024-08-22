"""=================================================================================================
Given a string s, return the longest *palindromic substring* in s.
A string is palindromic if it reads the same forward and backward.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

Wenxuan Dong        2024/8/21
================================================================================================="""

# Brute Force

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#
#         self.len = 0
#         res = []
#         for i in range(len(s)):
#             for j in range(i+1, len(s)+1):
#                 sub = s[i:j]
#                 if sub == sub[::-1] and len(sub) > self.len:
#                     self.len = len(sub)
#                     res = sub
#         return res

# expand from center
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        res = ""
        for i in range(len(s)):
            # Odd length palindromes
            tmp = expand_from_center(i, i)
            if len(tmp) > len(res):
                res = tmp

            # Even length palindromes
            tmp = expand_from_center(i, i + 1)
            if len(tmp) > len(res):
                res = tmp

        return res


if __name__ == '__main__':
    s = "babad"
    solution = Solution()
    result = solution.longestPalindrome(s)
    print(result)