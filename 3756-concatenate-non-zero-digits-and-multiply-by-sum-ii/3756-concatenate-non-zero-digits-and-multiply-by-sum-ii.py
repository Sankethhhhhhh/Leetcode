from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:

        MOD = 10**9 + 7
        n = len(s)

        # prefix sum of digits
        sumD = [0] * (n + 1)

        # count of non-zero digits
        cntNZ = [0] * (n + 1)

        # concatenated non-zero digits modulo MOD
        pref = [0] * (n + 1)

        # powers of 10
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        for i, ch in enumerate(s):
            d = ord(ch) - ord('0')
            sumD[i + 1] = sumD[i] + d
            cntNZ[i + 1] = cntNZ[i]
            pref[i + 1] = pref[i]

            if d != 0:
                cntNZ[i + 1] += 1
                pref[i + 1] = (pref[i] * 10 + d) % MOD

        ans = []

        for l, r in queries:
            nz = cntNZ[r + 1] - cntNZ[l]
            digit_sum = sumD[r + 1] - sumD[l]

            x = (pref[r + 1] - pref[l] * pow10[nz]) % MOD
            ans.append((x * digit_sum) % MOD)

        return ans