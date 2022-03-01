import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    root = result = ListNode()

    for i, v in enumerate(lists):
        if v:
            heapq.heappush(heap, (v.val, i, v))

    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]

        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))

    return root.next


