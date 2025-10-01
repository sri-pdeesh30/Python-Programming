class Solution(object):
    def isSameAfterReversals(self, num):
        if num==0:
            return True
        def reverse(n):
            rev=0
            while n>0:
               N=n%10
               rev=rev*10 + N
               n=n//10
            return rev
        first=reverse(num)
        second=reverse(first)
        if second==num:
            return True
        else:
            return False
