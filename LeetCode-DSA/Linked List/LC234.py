'Approach 1: O(n) Time complexity and O(n) space complexity'

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mylist=[]
        ptr=head
        while ptr!=None:
            mylist.append(ptr.val)
            ptr=ptr.next
        return mylist==mylist[::-1]
    
'Approach 2: '