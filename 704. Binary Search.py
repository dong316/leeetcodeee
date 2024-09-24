"""=================================================================================================
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
1 <= nums.length <= 10**4
-10**4 < nums[i], target < 10**4
All the integers in nums are unique.
nums is sorted in ascending order.

Wenxuan Dong        2024/9/22
================================================================================================="""

# this is for [left, right]
# class Solution:
#     def search(self, nums: list[int], target: int) -> int:
#
#         left, right = 0, len(nums) - 1
#
#         while left <= right:
#             middle = left + (right - left)//2
#
#             if nums[middle] > target:
#                 right = middle - 1
#             elif nums[middle] < target:
#                 left = middle + 1
#             else:
#                 return middle
#         return -1

# this is for [left, right)
class Solution:
    def search(self, nums: list[int], target: int) -> int:

        left, right = 0, len(nums)-1

        while left < right:
            middle = left + (right - left)//2

            if nums[middle] > target:
                right = middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1


if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 3
    sol = Solution()
    res = sol.search(nums, target)
    print(res)