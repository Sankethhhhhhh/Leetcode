from typing import List

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, idx, val):
        while idx <= self.n:
            self.bit[idx] += val
            idx += idx & -idx

    def query(self, idx):
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        offset = n + 1
        size = 2 * n + 5

        bit = Fenwick(size)

        prefix = 0
        ans = 0

        # Insert prefix sum = 0
        bit.update(offset + 1, 1)

        for x in nums:
            if x == target:
                prefix += 1
            else:
                prefix -= 1

            idx = prefix + offset + 1

            # Count previous prefix sums < current
            ans += bit.query(idx - 1)

            # Insert current prefix sum
            bit.update(idx, 1)

        return ans