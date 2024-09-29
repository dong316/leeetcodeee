"""=================================================================================================
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:

1 <= target <= 10*9
1 <= nums.length <= 10*5
1 <= nums[i] <= 10*4

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

Wenxuan Dong        2024/9/28
================================================================================================="""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        size = len(nums)
        left, right = 0, 0
        min_len = float('inf')
        cur_sum = 0

        while right < size:
            cur_sum += nums[right]

            while cur_sum >= target:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1

            right += 1

        return min_len if min_len != float('inf') else 0


if __name__ == "__main__":
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    sol = Solution()
    res = sol.minSubArrayLen(target, nums)
    print(res)
