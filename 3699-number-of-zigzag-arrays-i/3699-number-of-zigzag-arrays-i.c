#define MOD 1000000007

int zigZagArrays(int n, int l, int r) {
    int m = r - l + 1;

    long long *up = calloc(m, sizeof(long long));
    long long *down = calloc(m, sizeof(long long));

    for (int i = 0; i < m; i++) {
        up[i] = 1;
        down[i] = 1;
    }

    for (int len = 2; len <= n; len++) {
        long long *newUp = calloc(m, sizeof(long long));
        long long *newDown = calloc(m, sizeof(long long));

        long long pref = 0;
        for (int i = 0; i < m; i++) {
            newDown[i] = pref;
            pref = (pref + up[i]) % MOD;
        }

        long long suff = 0;
        for (int i = m - 1; i >= 0; i--) {
            newUp[i] = suff;
            suff = (suff + down[i]) % MOD;
        }

        free(up);
        free(down);

        up = newUp;
        down = newDown;
    }

    long long ans = 0;
    for (int i = 0; i < m; i++) {
        ans = (ans + up[i] + down[i]) % MOD;
    }

    free(up);
    free(down);

    return (int)ans;
}