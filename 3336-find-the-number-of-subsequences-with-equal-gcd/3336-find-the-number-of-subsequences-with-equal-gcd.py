from math import gcd
from functools import cache

class Solution:
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        @cache
        def dfs(i, g1, g2):
            if i == n:
                return 1 if g1 == g2 and g1 != 0 else 0

            # Skip current element
            ans = dfs(i + 1, g1, g2)

            # Put in first subsequence
            ng1 = nums[i] if g1 == 0 else gcd(g1, nums[i])
            ans += dfs(i + 1, ng1, g2)

            # Put in second subsequence
            ng2 = nums[i] if g2 == 0 else gcd(g2, nums[i])
            ans += dfs(i + 1, g1, ng2)

            return ans % MOD

        return dfs(0, 0, 0)