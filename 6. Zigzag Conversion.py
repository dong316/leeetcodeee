"""=================================================================================================
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"


Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000


Wenxuan Dong        2024/8/22
================================================================================================="""


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        # List of empty strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Place each character in the appropriate row
        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        # Join all rows to form the final string
        return ''.join(rows)

if __name__ == "__main__":
    s = 'PAYPALISHIRING'
    numRows = 3
    solution = Solution()
    result = solution.convert(s, numRows)
    # expected "PAHNAPLSIIGYIR" numRows = 3
    # expected "PINALSIGYAHRPI" numRows = 4
    print(result)
