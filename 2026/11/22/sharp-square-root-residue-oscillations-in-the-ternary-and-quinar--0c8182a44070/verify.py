#!/usr/bin/env python3
"""Exact-integer regression checks for projective Calkin-Wilf row identities.

Run: python3 verify.py
No third-party dependencies. Finite checking supports, but does not replace,
the all-depth transfer-matrix proof and analytic spectral argument.
"""
from collections import Counter

# Infinity is represented by None.
def project(a, b, p):
    a, b = a % p, b % p
    assert (a, b) != (0, 0)
    return None if b == 0 else (a * pow(b, -1, p)) % p


def direct_rows(p, maximum=15):
    current = [(1, 1)]
    for n in range(maximum + 1):
        counts = Counter(project(a, b, p) for a, b in current)
        yield n, counts
        if n < maximum:
            current = [child for a, b in current
                       for child in ((a, a + b), (a + b, b))]


def reduced_rows(p, maximum=80):
    if p == 3:
        A, B, C = 0, 1, 0
        for n in range(maximum + 1):
            yield n, {None: A, 0: A, 1: B, 2: C}
            A, B, C = A + C, 2 * A, 2 * B
    elif p == 5:
        A, B, C, D = 0, 1, 0, 0
        for n in range(maximum + 1):
            yield n, {None: A, 0: A, 1: B, 2: C, 3: C, 4: D}
            A, B, C, D = A + D, 2 * A, B + C, 2 * C
    else:
        raise ValueError('only 3 and 5 are considered')


def genfunc_coeffs(den, num, maximum):
    # den[0]=1 and den is in ascending powers of z.
    values = [0] * (maximum + 1)
    for n in range(maximum + 1):
        values[n] = ((num[n] if n < len(num) else 0)
                     - sum(den[j] * values[n-j]
                           for j in range(1, min(n, len(den)-1)+1)))
    return values


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def verify():
    assertions = 0
    denominators = {
        3: mul([1, -2], [1, 1, 2]),
        5: mul(mul([1, -2], [1, 1]), [1, -1, 2]),
    }
    numerators = {
        3: {0: [0, 0, 2], 1: [1, -1], 2: [0, 2, -2]},
        5: {0: [0, 0, 0, 2], 1: [1, -2, 1],
            2: [0, 1, -1], 4: [0, 0, 2, -2]},
    }
    for p in (3, 5):
        expected = dict(reduced_rows(p, 80))
        for n, observed in direct_rows(p, 15):
            assert all(observed.get(state, 0) == count
                       for state, count in expected[n].items())
            assertions += p+1
        for n, row in expected.items():
            assert sum(row.values()) == 2**n
            assert row[None] == row[0]
            if p == 5:
                assert row[2] == row[3]
                assertions += 1
            assertions += 2
        assert all(expected[3].get(state, 0) == 0 for state in ([2] if p==3 else [1]))
        assert all(v > 0 for v in expected[4].values())
        assertions += 2
        for state, numerator in numerators[p].items():
            vals = genfunc_coeffs(denominators[p], numerator, 80)
            for n in range(81):
                assert vals[n] == expected[n][state]
                assertions += 1
    assert denominators[3] == [1,-1,0,-4]
    assert denominators[5] == [1,-2,1,0,-4] # (1-2z)(1+z)(1-z+2z^2)
    assertions += 2
    print(f'PASS: {assertions} exact assertions; direct rows n=0..15 for p=3,5;')
    print('generating functions n=0..80; both levels first complete at n=4.')


if __name__ == '__main__':
    verify()
