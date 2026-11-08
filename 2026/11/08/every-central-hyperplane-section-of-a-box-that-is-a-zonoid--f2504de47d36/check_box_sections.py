"""Exact finite checks of central symmetry of offset box slices.
No numerical tolerance, external dependencies, or proof by sampling is used.
"""
from fractions import Fraction
from itertools import product


def vertices(b, t):
    r = len(b)
    out = set()
    for j in range(r):
        others = [i for i in range(r) if i != j]
        for signs in product((-1, 1), repeat=r - 1):
            x = [None] * r
            for i, sign in zip(others, signs):
                x[i] = Fraction(sign)
            x[j] = Fraction(t - sum(b[i] * x[i] for i in others), b[j])
            if -1 <= x[j] <= 1:
                out.add(tuple(x))
    return out


def centrally_symmetric(b, t):
    vs = vertices(b, t)
    assert len(vs) >= len(b), (b, t, vs)
    n = len(vs)
    center = tuple(sum(v[i] for v in vs) / n for i in range(len(b)))
    return all(tuple(2 * center[i] - v[i] for i in range(len(b))) in vs for v in vs)


def theorem(b, t):
    return any(2 * a >= abs(t) + sum(b) for a in b)


def run():
    count = 0
    for r in (3, 4, 5):
        for b in product((1, 2, 3), repeat=r):
            for t in range(1, sum(b)):
                actual = centrally_symmetric(b, t)
                predicted = theorem(b, t)
                assert actual == predicted, (b, t, actual, predicted)
                assert centrally_symmetric(b, -t) == predicted, (b, -t)
                count += 2
    for m in (4, 5, 6):
        for a in product((1, 2, 3), repeat=m):
            if max(a) * 2 < sum(a):
                # Every active-coordinate facet of the central section is full-dimensional,
                # and must be noncentrally symmetric (the decisive obstruction).
                i = a.index(min(a))
                b = a[:i] + a[i + 1:]
                assert sum(b) > a[i]
                assert not centrally_symmetric(b, -a[i]), a
                count += 1
    assert centrally_symmetric((1, 1, 1), 0)
    assert centrally_symmetric((2, 2, 2, 2), 0)
    print('EXACT_ENUMERATED_CASES', count)
    print('ALL_DIMENSION_BOX_ZONOID_CHECKS_PASSED')

if __name__ == '__main__':
    run()
