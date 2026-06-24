class Solution:
    MOD = 10**9 + 7

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        size = 2 * m

        vec = [1] * (m - 1) + [0] + [0] + [1] * (m - 1)

        M = [[0] * size for _ in range(size)]

        for i in range(m):
            for j in range(i + 1, m):
                M[i][m + j] = 1

            for j in range(i):
                M[m + i][j] = 1

        def mat_mul(A, B):
            n = len(A)
            C = [[0] * n for _ in range(n)]

            for i in range(n):
                for k in range(n):
                    if A[i][k] == 0:
                        continue

                    aik = A[i][k]

                    for j in range(n):
                        if B[k][j]:
                            C[i][j] = (C[i][j] + aik * B[k][j]) % self.MOD

            return C

        def mat_vec_mul(A, v):
            n = len(A)
            res = [0] * n

            for i in range(n):
                s = 0
                row = A[i]

                for j in range(n):
                    if row[j]:
                        s = (s + row[j] * v[j]) % self.MOD

                res[i] = s

            return res

        def power_apply(M, vec, exp):
            res = vec[:]

            while exp:
                if exp & 1:
                    res = mat_vec_mul(M, res)

                M = mat_mul(M, M)
                exp >>= 1

            return res

        ans_vec = power_apply(M, vec, n - 1)
        return sum(ans_vec) % self.MOD