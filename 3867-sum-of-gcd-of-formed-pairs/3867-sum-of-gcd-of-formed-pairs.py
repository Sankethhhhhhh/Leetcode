from math import gcd
from typing import List

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        prefixGcd = []
        mx = 0

        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(gcd(num, mx))

        prefixGcd.sort()

        ans = 0
        n = len(prefixGcd)

        for i in range(n // 2):
            ans += gcd(prefixGcd[i], prefixGcd[n - 1 - i])

        return ans