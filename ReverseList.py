# Problem: https://leetcode.com/problems/reverse-linked-list/
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head

        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        return previous
