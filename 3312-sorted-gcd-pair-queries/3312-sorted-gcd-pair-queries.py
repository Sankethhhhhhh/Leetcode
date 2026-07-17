from collections import Counter
from itertools import accumulate
from bisect import bisect_right
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = Counter(nums)

        # cnt_g[g] = number of pairs with gcd exactly g
        cnt_g = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            multiples = 0

            for x in range(g, mx + 1, g):
                multiples += freq[x]
                cnt_g[g] -= cnt_g[x]

            cnt_g[g] += multiples * (multiples - 1) // 2

        prefix = list(accumulate(cnt_g))

        return [bisect_right(prefix, q) for q in queries]