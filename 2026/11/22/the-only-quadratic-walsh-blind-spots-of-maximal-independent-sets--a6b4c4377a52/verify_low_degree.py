#!/usr/bin/env python3
"""Exact verification of low-degree Walsh multipliers for cycle independent-dominating sets.

All arithmetic is integer or rational. No dependencies beyond Python's standard library.
"""
from fractions import Fraction


def compositions(k):
    b = [0] * (k + 1)
    b[0] = 1
    for i in range(1, k + 1):
        b[i] = (b[i-2] if i >= 2 else 0) + (b[i-3] if i >= 3 else 0)
    return b


def cycles(n):
    """Independent brute-force membership and domination tests (not a gap-composition generator)."""
    out = []
    for x in range(1 << n):
        if any((x >> i & 1) and (x >> ((i + 1) % n) & 1) for i in range(n)):
            continue
        if any(not ((x >> i & 1) or (x >> ((i - 1) % n) & 1)
                        or (x >> ((i + 1) % n) & 1)) for i in range(n)):
            continue
        out.append(x)
    return out


def fwht(a):
    step = 1
    while step < len(a):
        for start in range(0, len(a), 2 * step):
            for i in range(start, start + step):
                u, v = a[i], a[i + step]
                a[i], a[i + step] = u + v, u - v
        step *= 2
    return a


def check():
    b = compositions(600)
    P = [3, 0, 2] + [0] * 598
    for n in range(3, len(P)):
        P[n] = P[n-2] + P[n-3]
    assertions = 0
    for n in range(3, 18):
        family = cycles(n)
        assert len(family) == P[n]
        assertions += 1
        values = [0] * (1 << n)
        for x in family:
            values[x] = 1
        fwht(values)
        for mask in range(1 << n):
            degree = mask.bit_count()
            if degree > 2:
                continue
            if degree == 0:
                expected = P[n]
            elif degree == 1:
                expected = b[n-3]
            else:
                i, j = (k for k in range(n) if mask >> k & 1)
                d = j - i
                expected = 4*b[d]*b[n-d] - 2*b[n-2] - b[n-3]
            assert values[mask] == expected, (n, mask, values[mask], expected)
            zero_predicted = (n == 4 and degree == 1) or (
                n == 9 and degree == 2 and min(d, n-d) in (3, 4))
            assert (values[mask] == 0) == zero_predicted, (n, mask, values[mask])
            assertions += 2

    # Exact rational enclosures of the positive root of t^3-t-1.
    L = Fraction(1324717957, 1000000000)
    U = Fraction(132471796, 100000000)
    poly = lambda t: t**3-t-1
    assert poly(L) < 0 < poly(U)
    assert L > 1 and U < Fraction(4, 3)
    assertions += 2
    m = Fraction(51, 125)    # 0.408
    M = Fraction(421, 1000)  # 0.421
    for k in (10, 11, 12):
        assert m * U**k < b[k] < M * L**k
        assertions += 1
    assert 4*m*m > M*(2/L**2 + 1/L**3)
    assertions += 1

    # Exact finite sign certificates: every row then propagates by the 2,3 recurrence.
    seed = {
        2: (4, [2, 1, 1]),
        3: (10, [1, 2, 1]),
        4: (10, [-3, -2, -3]),
        5: (10, [5, 2, 5]),
        6: (12, [-3, -1, -1]),
        7: (14, [3, 4, 2]),
        8: (16, [6, 3, 10]),
        9: (19, [5, 1, 3]),
    }
    H = lambda n, d: 4*b[d]*b[n-d] - 2*b[n-2] - b[n-3]
    for d, (start, vals) in seed.items():
        assert [H(n, d) for n in range(start, start+3)] == vals
        assert all(v > 0 for v in vals) or all(v < 0 for v in vals)
        assertions += 2
    assert [H(n, 3) for n in range(6, 10)] == [1, -1, 2, 0]
    assert [H(n, 4) for n in range(8, 10)] == [-2, 0]
    assert H(18, 9) == -2
    assertions += 3

    # Full finite consistency sweep beyond exhaustive Boolean input enumeration.
    for n in range(3, 601):
        assert P[n] == 2*b[n] + b[n-3]
        assertions += 1
        for d in range(1, n // 2 + 1):
            val = H(n, d)
            assert (val == 0) == (n == 9 and d in (3, 4))
            assertions += 1
    print(f"PASSED: {assertions} exact assertions; direct Walsh verification sizes 3..17; recurrence sweep through 600")


if __name__ == '__main__':
    check()
