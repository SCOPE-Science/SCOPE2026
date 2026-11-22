#!/usr/bin/env python3
"""Exact finite-state verification of a correlated five-habitat reserve theorem.

Python 3 standard library only; no randomness or numerical tolerance is used.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def reached_size(bits, protected):
    n = len(bits)
    functional = {i for i, bit in enumerate(bits) if bit} | set(protected)
    seen = set(protected)
    stack = list(protected)
    while stack:
        i = stack.pop()
        for j in ((i - 1) % n, (i + 1) % n):
            if j in functional and j not in seen:
                seen.add(j)
                stack.append(j)
    return len(seen)


def enumerate_table(n, protected):
    ans = Counter()
    for bits in product((0, 1), repeat=n):
        equal = sum(bits[i] == bits[(i + 1) % n] for i in range(n))
        ans[(equal, reached_size(bits, protected))] += 1
    assert sum(ans.values()) == 2 ** n
    return ans


def add(a, b):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    return trim(out)


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i + j] += x * y
    return trim(out)


def pow_poly(a, n):
    out = [1]
    for _ in range(n): out = mul(out, a)
    return out


def trim(a):
    while len(a) > 1 and a[-1] == 0: a.pop()
    return a


def weighted(t, n, f):
    return sum_poly([mul(pow_poly([0, 1], j), pow_poly([1, -1], n - j))
                     for (j, k), multiplicity in t.items()
                     for _ in range(multiplicity * f(k))])


def sum_poly(items):
    out = [0]
    for item in items: out = add(out, item)
    return out


def exact_expectation(t, n, q):
    z = 1 + (2 * q - 1) ** n
    return sum(Fraction(k * count) * q ** j * (1 - q) ** (n - j)
               for (j, k), count in t.items()) / z


def exact_tail(t, n, q, at_least):
    z = 1 + (2 * q - 1) ** n
    return sum(Fraction(count) * q ** j * (1 - q) ** (n - j)
               for (j, k), count in t.items() if k >= at_least) / z


def main():
    A = enumerate_table(5, {0, 1})
    S = enumerate_table(5, {0, 2})
    expected_A = {1: (3, 2, 5, 0), 3: (4, 6, 7, 3), 5: (1, 0, 0, 1)}
    expected_S = {1: (1, 4, 4, 1), 3: (2, 8, 8, 2), 5: (1, 0, 0, 1)}
    for j in (1, 3, 5):
        assert tuple(A[j, k] for k in (2, 3, 4, 5)) == expected_A[j]
        assert tuple(S[j, k] for k in (2, 3, 4, 5)) == expected_S[j]

    ZA = weighted(A, 5, lambda k: 1)
    ZS = weighted(S, 5, lambda k: 1)
    Z = add([1], pow_poly([-1, 2], 5))
    assert ZA == ZS == Z
    mean_A_numer = weighted(A, 5, lambda k: k)
    mean_S_numer = weighted(S, 5, lambda k: k)
    full_A_numer = weighted(A, 5, lambda k: int(k == 5))
    full_S_numer = weighted(S, 5, lambda k: int(k == 5))
    assert add(mean_S_numer, [-x for x in mean_A_numer]) == \
           mul(mul([0, 1], pow_poly([1, -1], 2)), [3, -6, 4])
    assert add(full_A_numer, [-x for x in full_S_numer]) == \
           mul(mul([0, 1], pow_poly([1, -1], 2)), [-1, 2])
    assert mul([2], mean_S_numer) == mul([7], Z)
    assert weighted(A, 5, lambda k: int(k >= 4)) == \
           weighted(S, 5, lambda k: int(k >= 4))

    # There is only one dihedral two-refuge placement for a triangle.
    assert enumerate_table(3, {0, 1}) == enumerate_table(3, {0, 2})
    # On a square the spin-complement involution gives total reachability 6.
    for d in (1, 2):
        for bits in product((0, 1), repeat=4):
            inv = tuple(1 - bit for bit in bits)
            assert reached_size(bits, {0, d}) + reached_size(inv, {0, d}) == 6
        for q in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
            assert exact_expectation(enumerate_table(4, {0, d}), 4, q) == 3

    for q in (Fraction(1, 10), Fraction(1, 3), Fraction(1, 2),
              Fraction(3, 4), Fraction(9, 10)):
        z = 1 + (2 * q - 1) ** 5
        gap_mean = exact_expectation(S, 5, q) - exact_expectation(A, 5, q)
        gap_full = exact_tail(A, 5, q, 5) - exact_tail(S, 5, q, 5)
        assert gap_mean == q * (1 - q) ** 2 * (4 * q * q - 6 * q + 3) / z
        assert gap_full == q * (1 - q) ** 2 * (2 * q - 1) / z
        assert gap_mean > 0
        assert (gap_full > 0) == (q > Fraction(1, 2))
        assert (gap_full == 0) == (q == Fraction(1, 2))
    q = Fraction(3, 4)
    assert exact_expectation(A, 5, q) == Fraction(305, 88)
    assert exact_expectation(S, 5, q) == Fraction(7, 2)
    assert exact_tail(A, 5, q, 5) == Fraction(27, 88)
    assert exact_tail(S, 5, q, 5) == Fraction(25, 88)
    print('PASS: exact enumeration, polynomial identities, minimality and rational example')


if __name__ == '__main__':
    main()
