"""=================================================================================================
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]

Constraints:

1 <= n <= 20

Wenxuan Dong        2024/9/29
================================================================================================="""
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0
        loop = n//2
        count = 1

        for offset in range(0, loop+1):
            for i in range(starty, n-offset-1):
                nums[startx][i] = count
                count += 1
            for i in range(startx, n-offset-1):
                nums[i][n-starty-1] = count
                count += 1
            for i in range(n-offset-1, startx, -1):
                nums[n-startx-1][i] = count
                count += 1
            for i in range(n-offset-1, starty, -1):
                nums[i][starty] = count
                count += 1
            startx += 1
            starty += 1

        if n % 2 != 0:
            nums[n // 2][n // 2] = count

        return nums


if __name__ == "__main__":
    n = 3
    sol = Solution()
    res = sol.generateMatrix(n)
    print(res)
