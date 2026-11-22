"""Direct finite checks for proper-ternary skip-transposition spheres.

Run: python checker.py
Only Python's standard library is used.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def proper(w):
    return all(w[j] != w[j+1] for j in range(len(w)-1))


def direct_degree(w):
    count = 0
    for j in range(len(w)-2):
        v = list(w)
        v[j], v[j+2] = v[j+2], v[j]
        if tuple(v) != w and proper(v):
            count += 1
    return count


def signed_degree(w):
    s = [1 if (w[j+1]-w[j])%3 == 1 else -1
         for j in range(len(w)-1)]
    d, j = 0, 0
    while j < len(s):
        k = j+1
        while k < len(s) and s[k] == s[j]:
            k += 1
        d += (k-j == 2)
        j = k
    return d


def predicted_distribution(m):
    # Coefficients of A/(1-A), A=z+uz**2+z**3/(1-z):
    # sum over all ordered compositions of m; each part of size two
    # contributes a factor u, all other parts weight one.
    dp = [Counter() for _ in range(m+1)]
    dp[0][0] = 1
    for j in range(1, m+1):
        for size in range(1, j+1):
            mark = int(size == 2)
            for d, count in dp[j-size].items():
                dp[j][d+mark] += count
    return {d: 6*count for d,count in dp[m].items()}


def check():
    total_vertices = 0
    for n in range(2,14):
        got = Counter()
        for w in product(range(3), repeat=n):
            if not proper(w):
                continue
            d = direct_degree(w)
            assert d == signed_degree(w), (n, w, d)
            got[d] += 1
        m = n-1
        expect = predicted_distribution(m)
        assert dict(got) == expect, (n, got, expect)
        assert sum(got.values()) == 3*2**m
        assert set(got) == set(range(m//2+1))
        top_expected = 6 if m%2 == 0 else 6*((m+1)//2)
        assert got[m//2] == top_expected
        if m >= 3:
            mean = Fraction(sum(d*c for d,c in got.items()),3*2**m)
            assert mean == Fraction(m+1,8)
        if m >= 5:
            mean = Fraction(sum(d*c for d,c in got.items()),3*2**m)
            var = Fraction(sum(d*d*c for d,c in got.items()),3*2**m)-mean*mean
            assert var == Fraction(7*m+1,64)
        print('n=%2d vertices=%5d edges=%5d isolated=%5d maxdegree=%d' %
              (n, sum(got.values()), sum(d*c for d,c in got.items())//2,
               got[0], max(got)))
        total_vertices += sum(got.values())
    print('PASS, exact direct checks of',total_vertices,'vertices and all candidate skip swaps')


if __name__ == '__main__':
    check()
