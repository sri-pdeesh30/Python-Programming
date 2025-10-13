'Optimal approach, O(m+n) time complexity'
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        n=0
        while temp:
            n+=1
            temp=temp.next
        if n==0 or n==1:
            return None

        temp=head
        for _ in range(int(n/2)-1):
            temp=temp.next
        temp.next=temp.next.next
        return head
