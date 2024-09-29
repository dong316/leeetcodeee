"""=================================================================================================

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
