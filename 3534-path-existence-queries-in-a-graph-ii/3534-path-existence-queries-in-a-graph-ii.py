from typing import List
import math

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((nums[i], i) for i in range(n))
        vals = [x for x, _ in arr]

        pos = [0] * n
        for i, (_, idx) in enumerate(arr):
            pos[idx] = i

        LOG = n.bit_length() + 1
        jump = [[0] * LOG for _ in range(n)]

        r = 0
        for l in range(n):
            while r + 1 < n and vals[r + 1] - vals[l] <= maxDiff:
                r += 1
            jump[l][0] = r

        for k in range(1, LOG):
            for i in range(n):
                jump[i][k] = jump[jump[i][k - 1]][k - 1]

        def dist(a, b):
            if a == b:
                return 0
            if jump[a][0] >= b:
                return 1
            if jump[a][LOG - 1] < b:
                return -1

            ans = 0
            cur = a
            for k in range(LOG - 1, -1, -1):
                if jump[cur][k] < b:
                    ans += 1 << k
                    cur = jump[cur][k]

            return ans + 1

        res = []
        for u, v in queries:
            a = pos[u]
            b = pos[v]
            if a > b:
                a, b = b, a
            res.append(dist(a, b))

        return res