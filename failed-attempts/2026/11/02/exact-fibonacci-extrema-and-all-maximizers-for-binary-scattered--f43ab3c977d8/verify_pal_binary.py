"""Finite checks for a theorem on distinct scattered palindromes.

Run: python3 verify_pal_binary.py
This finite checker is not a replacement for the all-length proof.
"""
from functools import lru_cache
from itertools import product
from random import Random


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def bound(n):
    if n % 2:
        return fib((n - 1) // 2 + 5) - 4
    return 2 * fib(n // 2 + 3) - 4


def dp_count(w):
    n = len(w)
    if n == 0:
        return 0
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = 1
            elif w[i] != w[j]:
                dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - (dp[i + 1][j - 1] if j >= i + 2 else 0)
            else:
                lo = i + 1
                hi = j - 1
                while lo <= hi and w[lo] != w[i]:
                    lo += 1
                while lo <= hi and w[hi] != w[i]:
                    hi -= 1
                inside = dp[i + 1][j - 1] if j >= i + 2 else 0
                if lo > hi:
                    dp[i][j] = 2 * inside + 2
                elif lo == hi:
                    dp[i][j] = 2 * inside + 1
                else:
                    dp[i][j] = 2 * inside - (dp[lo + 1][hi - 1] if hi >= lo + 2 else 0)
    return dp[0][n - 1]


@lru_cache(None)
def endpoint_count(w):
    s = 0
    for ch in "01":
        i = w.find(ch)
        if i < 0:
            continue
        s += 1
        j = w.rfind(ch)
        if j > i:
            s += 1 + endpoint_count(w[i + 1:j])
    return s


def brute_set_count(w):
    found = set()
    n = len(w)
    for mask in range(1, 1 << n):
        u = ''.join(w[i] for i in range(n) if (mask >> i) & 1)
        if u == u[::-1]:
            found.add(u)
    return len(found)


def expected_words(n):
    if n == 0:
        return {''}
    alt = ''.join('01'[i % 2] for i in range(n))
    out = {alt, ''.join('10'[i % 2] for i in range(n))}
    if n % 2 == 0:
        for a in '01':
            half = ''.join('01'[(i + int(a)) % 2] for i in range(n // 2))
            out.add(half + half[::-1])
    return out


def main():
    nwords = nsets = 0
    for n in range(0, 17):
        winners = set()
        mx = -1
        for letters in product('01', repeat=n):
            w = ''.join(letters)
            val = dp_count(w)
            assert val == endpoint_count(w), (n, w, val, endpoint_count(w))
            assert val <= bound(n), (n, w, val, bound(n))
            if n <= 9:
                assert val == brute_set_count(w), (n, w)
                nsets += 1
            if val > mx:
                mx = val
                winners = {w}
            elif val == mx:
                winners.add(w)
            nwords += 1
        assert mx == bound(n), (n, mx, bound(n))
        assert winners == expected_words(n), (n, winners, expected_words(n))
    rng = Random(1673)
    random_cases = 4000
    for _ in range(random_cases):
        n = rng.randrange(17, 160)
        w = ''.join(rng.choice('01') for _ in range(n))
        assert endpoint_count(w) == dp_count(w)
        assert endpoint_count(w) <= bound(n)
    for n in range(17, 1000):
        for w in expected_words(n):
            assert endpoint_count(w) == bound(n), (n, w)
    print('VERIFY_OK exhaustive_lengths=0..16 exhaustive_words=%d direct_set_cases=%d random_cases=%d extremal_lengths=17..999 recurrence=endpoint-vs-interval-DP' % (nwords, nsets, random_cases))


if __name__ == '__main__':
    main()
