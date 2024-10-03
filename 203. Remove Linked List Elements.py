"""=================================================================================================
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []

Constraints:

The number of nodes in the list is in the range [0, 10**4].
1 <= Node.val <= 50
0 <= val <= 50

Wenxuan Dong        2024/10/1
================================================================================================="""
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(next=head)
        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy_head.next

def build_linked_list(values):
    """ Helper function to build a linked list from a list of values """
    dummy_head = ListNode()
    current = dummy_head
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy_head.next

def print_linked_list(head):
    """ Helper function to print the linked list values """
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(values)

if __name__ == "__main__":
    # Create a linked list from a list
    head = build_linked_list([1, 2, 6, 3, 4, 5, 6])
    val = 6

    # Remove elements with value 6
    sol = Solution()
    res = sol.removeElements(head, val)

    # Print the modified linked list
    print_linked_list(res)  # Expected Output: [1, 2, 3, 4, 5]
