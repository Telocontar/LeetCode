from typing import List


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