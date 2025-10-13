class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=0
        for i in range(m, m+n):
            nums1[i]=nums2[j]
            j+=1
        
        for i in range(n+m):
            for k in range(n+m-i-1):
                if(nums1[k] > nums1[k+1]):
                    temp=nums1[k]
                    nums1[k]=nums1[k+1]
                    nums1[k+1]=temp

        return nums1      