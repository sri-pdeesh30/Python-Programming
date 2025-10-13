'Iterative approach:'

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        current=head

        while current:
            third=current.next
            current.next=prev
            prev=current
            current=third

        return prev