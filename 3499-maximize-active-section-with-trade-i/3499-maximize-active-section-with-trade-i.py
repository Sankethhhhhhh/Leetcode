class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"
        ones = s.count("1")

        n = len(t)
        i = 0

        zero_blocks = []
        has_middle_one = False

        while i < n:
            if t[i] == '0':
                j = i
                while j < n and t[j] == '0':
                    j += 1
                zero_blocks.append(j - i)
                i = j
            else:
                j = i
                while j < n and t[j] == '1':
                    j += 1
                if i > 0 and j < n and t[i - 1] == '0' and t[j] == '0':
                    has_middle_one = True
                i = j

        if not has_middle_one:
            return ones

        best = 0
        for i in range(len(zero_blocks) - 1):
            best = max(best, zero_blocks[i] + zero_blocks[i + 1])

        return ones + best