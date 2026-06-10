# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        if not head:
            return False
        while head.next != None:
            if head.val in visited:
                return True
            visited.add(head.val)
            head = head.next
        return False
        