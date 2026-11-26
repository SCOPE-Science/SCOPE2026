"""Exact checks for diagonal-column Fourier transforms of Schröder paths.

Only standard-library integer arithmetic is used. Run with Python 3.9+.
The finite checks supplement, but do not replace, the all-order proof.
"""
from collections import Counter
from functools import lru_cache
from math import comb


def enumerated_histogram(n):
    hist = [0] * (1 << n)
    def walk(x, y, mask):
        if x == n and y == n:
            hist[mask] += 1
            return
        if y < n:
            walk(x, y+1, mask)
        if x < n and y > x:
            walk(x+1, y, mask)
        if x < n and y < n:
            walk(x+1, y+1, mask | (1 << x))
    walk(0, 0, 0)
    return hist


def walsh_transform(a):
    a = a.copy()
    k = 1
    while k < len(a):
        for i in range(0, len(a), 2*k):
            for j in range(i, i+k):
                u, v = a[j], a[j+k]
                a[j], a[j+k] = u+v, u-v
        k *= 2
    return a


def transfer_coefficient(n, frequency):
    # h=y-x at the start of a vertical column; n columns are traversed.
    dp = [1]
    for i in range(n):
        sign = -1 if frequency & (1 << i) else 1
        cap = n-i-1
        next_dp = [0]*(cap+1)
        for h, ways in enumerate(dp):
            for h_next in range(cap+1):
                if h_next >= h-1:
                    next_dp[h_next] += ways
                if h_next >= h:
                    next_dp[h_next] += sign*ways
        dp = next_dp
    assert len(dp) == 1
    return dp[0]


def schroder_number(n):
    return sum(comb(2*n-k,k)*comb(2*(n-k),n-k)//(n-k+1)
               for k in range(n+1))


def main():
    tested = 0
    counts = []
    for n in range(1, 9):
        hist = enumerated_histogram(n)
        spectrum = walsh_transform(hist)
        assert sum(hist) == schroder_number(n)
        assert all(x > 0 for x in hist)
        for v in range(0, 1 << n, 2):
            assert hist[v] == hist[v+1]
            tested += 1
        for s, observed in enumerate(spectrum):
            expected = transfer_coefficient(n, s)
            assert observed == expected, (n,s,observed,expected)
            assert observed == 0 if s & 1 else observed >= 2
            tested += 1
        assert sum(x != 0 for x in spectrum) == (1 << (n-1))
        survivors = [(s,x) for s,x in enumerate(spectrum) if x != 0]
        assert min(x for _,x in survivors) == 2
        assert [s for s,x in survivors if x == 2] == [(1 << n)-2]
        assert max(x for _,x in survivors) == schroder_number(n)
        assert [s for s,x in survivors if x == schroder_number(n)] == [0]
        counts.append((n,schroder_number(n),len(survivors)))
    # A second range uses the column recurrence without path enumeration.
    for n in range(9, 15):
        spectrum = [transfer_coefficient(n,s) for s in range(1 << n)]
        assert sum(x != 0 for x in spectrum) == (1 << (n-1))
        assert all((x == 0) if (s & 1) else (x >= 2)
                   for s,x in enumerate(spectrum))
        assert [s for s,x in enumerate(spectrum) if x == 2] == [(1 << n)-2]
        assert spectrum[0] == schroder_number(n)
        counts.append((n,schroder_number(n),1 << (n-1)))
        tested += len(spectrum)
    print('PASS: exact path enumeration, integer Walsh transform and independent column transfer')
    print('Coefficient comparisons / histogram equalities:',tested)
    for n,total,rank in counts:
        print(f'n={n:2d} paths={total:<15d} rank={rank:<8d} nullity={rank:<8d} gap=2')


if __name__ == '__main__':
    main()
