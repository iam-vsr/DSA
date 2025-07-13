class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        mask = 0
        for i in range(0, 32, 2):
            mask |= (1 << i)

        if n==0:
            return False
        else:
            return n&(n-1) ==0 and n|mask ==mask
