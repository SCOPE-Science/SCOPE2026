"""Exact independent checks for the fixed-row dyadic chip-count theorem.

Run with Python 3.10+; standard library only.
"""
from fractions import Fraction
from math import comb, factorial, ceil, floor


def counts(m, max_a, max_b):
    assert isinstance(m, int) and m >= 1
    prev = [m]
    for b in range(1, max_b + 1):
        prev.append(prev[-1] // 2)
    rows = [prev]
    for a in range(1, max_a + 1):
        curr = [m]
        for b in range(1, max_b + 1):
            curr.append((curr[-1] + prev[b]) // 2)
        rows.append(curr)
        prev = curr
    return rows


def q(a, b):
    assert a >= 0 and b >= 0
    return Fraction(comb(b + a, a), 2**a) + sum(
        (Fraction(comb(b + j - 1, j - 1), 2**j) for j in range(1, a + 1)),
        Fraction(0)
    )


def minimum(a, b):
    # A path through a right child requires no more than 2**b labels;
    # this is a proven upper bound from the x=0 route.
    lo, hi = 1, 2**b
    while lo < hi:
        mid = (lo + hi) // 2
        if counts(mid, a, b)[a][b] >= 1:
            hi = mid
        else:
            lo = mid + 1
    return lo


def direct_pairing(depth):
    # Actual labeled-chip dynamics, independent of the floor recurrence.
    k = 2**depth
    sites = {(0, 0): list(range(1, k + 1))}
    seen = {(0, 0): list(range(1, k + 1))}
    for d in range(depth):
        for a in range(d + 1):
            site = (a, d - a)
            incoming = sorted(sites.get(site, []))
            for j in range(0, len(incoming) - 1, 2):
                small, large = incoming[j], incoming[j + 1]
                for dest, x in (((a + 1, d - a), small), ((a, d - a + 1), large)):
                    sites.setdefault(dest, []).append(x)
                    seen.setdefault(dest, []).append(x)
            sites[site] = incoming[len(incoming) // 2 * 2:]
    return seen


def test():
    assertions = 0
    # Independent paths: exact rational closed form versus recurrence;
    # and its global maximum rounding error bound.
    for m in list(range(1, 61)) + [127, 256, 1023]:
        A, B = 6, 16
        table = counts(m, A, B)
        for a in range(A + 1):
            for b in range(B + 1):
                L = Fraction(m, 2**b) * q(a, b)
                assert 0 <= L - table[a][b] <= a + 1, (m, a, b)
                if a >= 1 and b >= 1:
                    R = sum((2**(r-1) *
                        (Fraction(m, 2**r) * q(a-1, r) - table[a-1][r])
                        for r in range(1, b+1)), Fraction(0)) / 2**b
                    assert table[a][b] == (L-R).__floor__(), (m, a, b)
                assertions += 1
    print('EXACT_CONTINUOUS_POLYNOMIAL_AND_NESTED_FLOOR_IDENTITY_PASS', assertions)

    # Independently implement the chip-firing game with real named labels.
    for depth in range(1, 9):
        sites = direct_pairing(depth)
        for a in range(depth + 1):
            for b in range(depth - a + 1):
                assert minimum(a, b) == min(sites[a, b]), (depth, a, b)
    print('DIRECT_LABELLED_FIRING_REACHABILITY_PASS', sum((d+1)*(d+2)//2 for d in range(1, 9)))

    # Non-asymptotic upper/lower estimates at large widths.
    for a in range(0, 6):
        for b in (128, 256, 512, 1024):
            m = minimum(a, b)
            scale = Fraction(factorial(a) * 2**(b+a), b**a)
            ratio = Fraction(m, 1) / scale
            assert 1 <= ratio < Fraction(12, 10), (a, b, float(ratio))
            if a == 0:
                assert m == 2**b
    print('FIXED_ROW_THRESHOLD_ASYMPTOTIC_CROSSCHECK_PASS', 24)

    # Limiting staircase at non-integral levels, using rigorous integer rounding.
    testlevels = [Fraction(1, 2), Fraction(3, 2), Fraction(5, 2), Fraction(11, 2)]
    for a in range(0, 5):
        for b in (256, 512, 1024):
            lam = Fraction(q(a, b), 2**b)
            for t in testlevels:
                m = (t/lam).__ceil__()
                actual = counts(m, a, b)[a][b]
                assert actual == t.__floor__(), (a, b, t, actual)
    print('NONINTEGRAL_FIXED_ROW_STAIRCASE_TEST_PASS', 60)
    print('VERIFY_OK')

if __name__ == '__main__':
    test()
