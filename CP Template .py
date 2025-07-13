import sys
import math
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from itertools import permutations, combinations
from functools import lru_cache

input = sys.stdin.readline
sys.setrecursionlimit(2 * 10**5)

# Input helpers
def ni(): return int(input())                            # single integer
def mi(): return map(int, input().split())               # multiple integers
def nf(): return float(input())                          # single float
def mf(): return map(float, input().split())             # multiple floats
def li(): return list(map(int, input().split()))         # list of integers
def lf(): return list(map(float, input().split()))       # list of floats
def lsi(): return list(input().strip())                  # list of characters from string
def inp(): return input().strip()                        # single string
def lss(): return input().strip().split()                # list of strings (space-separated)
def mat(n): return [list(map(int, input().split())) for _ in range(n)]  # 2D int matrix

def solve():
    t = ni()
    for _ in range(t):
        

if __name__ == "__main__":
    solve()
