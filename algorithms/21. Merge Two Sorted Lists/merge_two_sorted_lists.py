"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
  Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:
Input: list1 = [], list2 = []
Output: []
Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
  Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional

from utils.utilities import create_linked_list, ListNode


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

    curr_node_list_1 = list1
    curr_node_list_2 = list2

    # pointer to the head of the new list
    header = ListNode()
    curr_node_new_list = header

    while curr_node_list_1 and curr_node_list_2:
        if curr_node_list_1.val < curr_node_list_2.val:
            # change pointer of current node to smaller node
            curr_node_new_list.next = curr_node_list_1
            # continue with next node
            curr_node_list_1 = curr_node_list_1.next
        else:
            # change pointer of current node to smaller node
            curr_node_new_list.next = curr_node_list_2
            # continue with next node
            curr_node_list_2 = curr_node_list_2.next

        # continue with next node
        curr_node_new_list = curr_node_new_list.next

    # either list1 or list 2 has finished
    if curr_node_list_1 is None:
        curr_node_new_list.next = curr_node_list_2
    else:
        curr_node_new_list.next = curr_node_list_1

    # skip the first node which we initialized
    header = header.next

    return header


test_input_1a = create_linked_list([1,2,4])
test_input_1b = create_linked_list([1,3,4])
test_input_2a = create_linked_list([])
test_input_2b = create_linked_list([])
test_input_3a = create_linked_list([])
test_input_3b = create_linked_list([0])


assert mergeTwoLists(test_input_1a, test_input_1b) == create_linked_list([1,1,2,3,4,4])
assert mergeTwoLists(test_input_2a, test_input_2b) == create_linked_list([])
assert mergeTwoLists(test_input_3a, test_input_3b) == create_linked_list([0])

