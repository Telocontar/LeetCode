"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
  Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:
Input: head = [1,2]
Output: [2,1]
Example 3:
Input: head = []
Output: []
  Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
  Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next})"

    def __eq__(self, other):
        return str(self) == str(other)


def create_linked_list(input_list: List) -> ListNode:

    if len(input_list) == 0:
        return ListNode()
    # last element in list
    elif len(input_list) == 1:
        return ListNode(val=input_list[0])
    else:
        return ListNode(val=input_list[0], next=create_linked_list(input_list[1:]))


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:

    previous_node = None
    while head is not None:
        # store the next node
        next_node = head.next
        # reverse order
        head.next = previous_node
        # we reversed the current node, so our current node is our previous node
        previous_node = head
        # continue with the next node
        head = next_node

    return previous_node


test_input_1a = create_linked_list([1,2,3,4,5])
test_input_2a = create_linked_list([1,2])
test_input_3a = create_linked_list([])

assert reverseList(test_input_1a) == create_linked_list([5,4,3,2,1])
assert reverseList(test_input_2a) == create_linked_list([2,1])
assert reverseList(test_input_3a) == create_linked_list([])

print("Tests successful.")
