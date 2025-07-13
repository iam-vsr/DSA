"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array
"""

class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        if n%4==1:
            x=1
        elif n%4==2:
            x=n+1
        elif n%4==3:
            x=0
        else:
            x=n
        ans=0
        for i in range(n):
            ans^=nums[i]
        for i in range(n+1):
            if ans^i==x:
                return i
        return -1
      
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor_all = 0
        xor_nums = 0
        
        for i in range(n + 1):
            xor_all ^= i
        
        for num in nums:
            xor_nums ^= num
        
        return xor_all ^ xor_nums
