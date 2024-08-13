"""=================================================================================================
Given a string s, find the length of the longest
substring
 without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Wenxuan Dong        2024/8/12
================================================================================================="""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        maxLength = 0

        for right in range(len(s)):
            # If character is in set, it means we have a repeating character.
            # We need to shrink the window from the left until we can remove that character.
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            # Add the current character to the set and update the max length if necessary.
            charSet.add(s[right])
            maxLength = max(maxLength, right - left + 1)

        return maxLength

# # Time Limit Exceeded
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         sub = []
#         finallen = 0
#         for i in range(len(s)):
#             for j in range(i+1, len(s)+1):
#                 sub = s[i:j]
#
#             visited = [0] * (256)
#             sublen = 0
#             for i in range(len(sub)):
#                 if (visited[ord(sub[i])] == True):
#                     break
#                 visited[ord(sub[i])] = True
#                 sublen += 1
#             if sublen > finallen:
#                 finallen = sublen
#
#         return finallen

if __name__ == '__main__':
    s = "pwwkew"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)
