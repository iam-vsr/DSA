class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)  # clears the lowest set bit
            count += 1
        return count
"""
Find number of set bits
example-
n = 13 = 1101
Iterations:
1st: n = 1101 → 1100 (count = 1)
2nd: n = 1100 → 1000 (count = 2)
3rd: n = 1000 → 0000 (count = 3)
"""
