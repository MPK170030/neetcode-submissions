# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Understand:
Input: head of list, integer n
Output: A head of list with nth node removed
Edge case: If list is empty or of size 1 and n==1 return empty list

Match:
Linked list and fast and slow pointers

Plan:
Have two pointers slow and fast pointing at head
Move fast pointer by n positions so when fast is at the end (fast.next is None)slow will be at n-1 and we can point slow.next to slow.next.next
return the head of list

'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n==1 and head.next == None:
            return None
        
        slow = head
        fast = head

        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head
