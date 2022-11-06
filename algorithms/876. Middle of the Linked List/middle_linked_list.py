"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
  Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
  Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""
from math import ceil
from typing import Optional

from utils.utilities import create_linked_list, ListNode


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:

    first_node = head

    # check how many nodes exist
    node_counter = 0
    while head is not None:
        node_counter += 1
        head = head.next

    # return the second middle node
    if node_counter % 2 == 0:
        node_counter += 1

    # iterate to the middle node
    head = first_node
    middle_node_index = ceil(node_counter / 2)
    for node in range(middle_node_index - 1):
        head = head.next

    return head


test_input_1a = create_linked_list([1,2,3,4,5])
test_input_2a = create_linked_list([1,2,3,4,5,6])

assert middleNode(test_input_1a) == create_linked_list([3,4,5])
assert middleNode(test_input_2a) == create_linked_list([4,5,6])

print("Tests successful.")
