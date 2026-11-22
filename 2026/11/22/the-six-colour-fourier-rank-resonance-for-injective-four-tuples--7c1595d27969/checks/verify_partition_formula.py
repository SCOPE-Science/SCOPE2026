"""Exact integer Möbius-character verification for injective four-colour words.

Run: python3 checks/verify_partition_formula.py
Pure Python standard library; no remote data or floating point.
"""
from collections import Counter
from itertools import product, combinations


def group(moduli):
    return list(product(*(range(n) for n in moduli)))


def add(a, b, moduli):
    return tuple((x + y) % m for x, y, m in zip(a, b, moduli))


def neg(a, moduli):
    return tuple((-x) % m for x, m in zip(a, moduli))


def zero(moduli):
    return (0,) * len(moduli)


def multiplier(k, moduli):
    """Finite-partition-lattice character formula, independently from histogram formula."""
    q = 1
    for m in moduli:
        q *= m
    z = zero(moduli)
    if add(add(k[0], k[1], moduli), add(k[2], k[3], moduli), moduli) != z:
        return 0
    ret = q**4 if all(x == z for x in k) else 0
    for i, j in combinations(range(4), 2):
        others = [p for p in range(4) if p not in (i, j)]
        if add(k[i], k[j], moduli) == z and all(k[p] == z for p in others):
            ret -= q**3
    ret += 2 * q**2 * sum(x == z for x in k)
    for (i, j), (r, s) in [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]:
        if add(k[i], k[j], moduli) == z and add(k[r], k[s], moduli) == z:
            ret += q**2
    return ret - 6*q


def predicted(q, t):
    """Seven mutually disjoint cases from the claimed closed-form census."""
    cases = [
        (q*(q-1)*(q-2)*(q-3), 1),
        (-q*(q-2)*(q-3), 6*(q-1)),
        (2*q*(q-3), 4*(q-1)*(q-2)),
        (-6*q, q**3-7*q*q+15*q-8-t),
        (q*(q-6), 3*q*q-12*q+6+3*t),
        (2*q*(q-3), 3*(q-t)),
        (3*q*(q-2), t-1),
    ]
    assert all(count >= 0 for _, count in cases)
    assert sum(count for _, count in cases) == q**3
    out = Counter()
    for value, count in cases:
        out[value] += count
    return +out


def one(moduli):
    xs = group(moduli)
    q = len(xs)
    z = zero(moduli)
    t = sum(add(x, x, moduli) == z for x in xs)
    actual = Counter()
    for a in xs:
        for b in xs:
            for c in xs:
                d = neg(add(add(a, b, moduli), c, moduli), moduli)
                actual[multiplier((a, b, c, d), moduli)] += 1
    assert actual == predicted(q, t), (moduli, actual, predicted(q, t))
    rank = q**3 - actual[0]
    assert rank == (168 if q == 6 else q**3), (moduli, rank)
    print('PASS', moduli, 'q=', q, 'involutions=', t, 'rank=', rank, 'signed_histogram=', sorted(actual.items()))


if __name__ == '__main__':
    for factors in ((4,), (2, 2), (5,), (6,), (7,), (8,), (4, 2), (2, 2, 2), (9,), (3, 3), (10,), (12,), (6, 2)):
        one(factors)
