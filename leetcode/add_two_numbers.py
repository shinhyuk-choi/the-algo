# https://leetcode.com/problems/add-two-numbers/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    n1 = ""
    n2 = ""
    while l1.next:
        n1 += str(l1.val)
        l1 = l1.next
    while l2.next:
        n2 += str(l2.val)
        l2 = l2.next
    n1 += str(l1.val)
    n2 += str(l2.val)
    n1 = n1[::-1]
    n2 = n2[::-1]
    n3 = str(int(n1) + int(n2))
    n3 = list(n3)
    head = None
    for i in range(len(n3)):
        x = ListNode()
        x.val = int(n3[i])
        x.next = head
        head = x
    return head
