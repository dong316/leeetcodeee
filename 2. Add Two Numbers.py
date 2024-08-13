"""=================================================================================================
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Wenxuan Dong        2024/7/23
================================================================================================="""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        total = 0
        next1 = 0
        dummy = ListNode()
        cur = dummy
        while (l1 != None and l2 != None):
            total = l1.val + l2.val + next1
            cur.next = ListNode(total % 10)
            next1 = total // 10
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            total = l1.val + next1
            cur.next = ListNode(total % 10)
            next1 = total // 10
            cur = cur.next
            l1 = l1.next

        while l2 != None:
            total = l2.val + next1
            cur.next = ListNode(total % 10)
            next1 = total // 10
            cur = cur.next
            l2 = l2.next

        if next1 != 0:
            cur.next = ListNode(next1)

        return dummy.next


class Solution:
    # Recursion
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        total = l1.val + l2.val
        next1 = total // 10
        res = ListNode(total % 10)
        if (l1.next or l2.next or next1):
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            l1.val += next1
            res.next = self.addTwoNumbers(l1,l2);
        return res;

def create_linked_list(elements):
    """ Helper function to create a linked list from a list of elements. """
    dummy = ListNode()
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next

def print_linked_list(node):
    """ Helper function to print linked list. """
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()  # For newline at the end

# can solve this question correctly but not in the proper format
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         l1_number = 0
#         for i in range(len(l1)):
#             l1_number = l1_number*10 + l1[len(l1)-i-1]
#         l2_number = 0
#         for i in range(len(l2)):
#             l2_number = l2_number*10 + l2[len(l2)-i-1]
#         sum_numbers = l1_number + l2_number
#         sum_numbers = str(sum_numbers)
#         result = []
#         for i in range(len(sum_numbers)):
#             result.append(sum_numbers[len(sum_numbers)-i-1])
#         return result

if __name__ == '__main__':
    l1 = [2,4,3]
    l2 = [5,6,4]
    l1 = create_linked_list(l1)
    l2 = create_linked_list(l2)
    # l1 = [9,9,9,9,9,9,9]
    # l2 = [9,9,9,9]
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    print_linked_list(result)