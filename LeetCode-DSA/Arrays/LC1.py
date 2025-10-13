'Optimal approach with O(n) time complexity:'

def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        noted={}
        for i, num in enumerate(nums):
            diff=target-num
            if diff in noted:
                return [noted[diff],i]
            noted[num]=i
        return []