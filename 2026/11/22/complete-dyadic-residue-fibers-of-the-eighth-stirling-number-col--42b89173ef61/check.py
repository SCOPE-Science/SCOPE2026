"""Exact finite checks for the eight-block Stirling residue theorem.

The infinite statement is proved analytically in RESULT.md; this script only
checks representative modular identities and finite periods.
"""
from collections import Counter
from math import comb


def stirling_column(nmax, k, modulus):
    row = [0] * (k + 1)
    row[0] = 1
    values = []
    for n in range(nmax + 1):
        values.append(row[k])
        for j in range(min(k, n + 1), 0, -1):
            row[j] = (j * row[j] + row[j - 1]) % modulus
        row[0] = 0
    return values


def f(n, bits):
    mod = 1 << bits
    numerator = (pow(7, n, mod << 4) + 7 * pow(5, n, mod << 4)
                 + 7 * pow(3, n, mod << 4) + 1) % (mod << 4)
    assert numerator % 16 == 0
    return (-numerator // 16) * pow(315, -1, mod) % mod


def v2(n):
    assert n
    return (n & -n).bit_length() - 1


def run():
    count = 0
    for k in range(1, 11):
        m = 1 << k
        period = m * 2
        start = max(8, k + 5)
        values = stirling_column(start + period * 3, 8, m)
        for n in range(start, start + period * 2):
            assert values[n] == f(n, k)
            assert values[n] == values[n + period]
            count += 2
        histogram = Counter(values[start:start + period])
        for y in range(m):
            expected = 1 + (4 if (k >= 2 and y % 4 == 0) else (2 if k == 1 and y == 0 else 0))
            assert histogram[y] == expected
            count += 1
        # The even-parity subsequence is a full permutation.
        assert len({f(2 * t, k) for t in range(m)}) == m
        count += 1
        if k >= 2:
            assert len({f(2 * t + 1, k) for t in range(m)}) == m // 4
            count += 1
    for k in range(4, 13):
        mod = 1 << k
        for t in range(32):
            for s in range(t):
                for shift in (0, 1):
                    diff = (f(2*t+shift, k) - f(2*s+shift, k)) % mod
                    val = v2(t-s) + (2 if shift else 0)
                    if val < k:
                        assert diff and v2(diff) == val
                        count += 1
    # Binomial-series first coefficients and divisibility conditions.
    a0 = [1] + [sum(c * (a*a-1)**j for c,a in ((1,7),(7,5),(7,3))) // 16
          for j in range(1,8)]
    a1 = [1] + [sum(c * (a*a-1)**j for c,a in ((7,7),(35,5),(21,3))) // 64
          for j in range(1,8)]
    assert a0[:3] == [1,17,424]
    assert a1[:3] == [1,21,588]
    count += 2
    print('CHECK_OK', count)

if __name__ == '__main__':
    run()
