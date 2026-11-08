"""Independent exhaustive check of the zero-field spin-one wheel classification.

Run: python verify_exhaustive.py
Only Python's standard library is needed.
"""
from fractions import Fraction
from itertools import product


def expected(n, d):
    if n % 2:
        return min((-(n - 1) + (n + 1) * d,
                    -(n - 2) + (n - 1) * d, Fraction(0)))
    return min((-n + (n + 1) * d, -n + n * d, Fraction(0)))


def check(n):
    if n % 2:
        threshold = Fraction(n - 2, n - 1)
        trials = sorted(set([Fraction(-2), Fraction(0), Fraction(1, 4),
                             Fraction(1, 2),
                             (Fraction(1, 2) + threshold) / 2,
                             threshold, (threshold + 1) / 2,
                             Fraction(2)]))
    else:
        trials = [Fraction(-2), Fraction(-1, 3), Fraction(0),
                  Fraction(1, 3), Fraction(1), Fraction(2)]
    minima = {d: (None, 0, {}) for d in trials}
    num = 0
    # Direct enumeration: no dynamic programming, transfer matrices, or stored tables.
    for s in product((-1, 0, 1), repeat=n + 1):
        num += 1
        h = s[0]
        rim = s[1:]
        q = sum(x*x for x in s)
        bond = sum(rim[i] * rim[(i + 1) % n] + h * rim[i]
                   for i in range(n))
        for d in trials:
            energy = Fraction(bond) + d * q
            best, count, occ = minima[d]
            if best is None or energy < best:
                minima[d] = (energy, 1, {q: 1})
            elif energy == best:
                occ[q] = occ.get(q, 0) + 1
                minima[d] = (best, count + 1, occ)
    assert num == 3**(n + 1)
    for d, (best, count, occ) in minima.items():
        assert best == expected(n, d), (n, d, best, expected(n,d))
        if n % 2:
            a, b = Fraction(1, 2), Fraction(n-2,n-1)
            if d < a:
                want = {n + 1: 2*n}
            elif d == a == b:
                want = {0: 1, n - 1: 4*n, n + 1: 2*n}
            elif d == a:
                want = {n - 1: 4*n, n + 1: 2*n}
            elif d < b:
                want = {n - 1: 4*n}
            elif d == b:
                want = {0: 1, n - 1: 4*n}
            else:
                want = {0: 1}
        else:
            if d < 0:
                want = {n + 1: 4}
            elif d == 0:
                want = {n: 2, n + 1: 4}
            elif d < 1:
                want = {n: 2}
            elif d == 1:
                want = {0: 1, n: 2}
            else:
                want = {0: 1}
        assert occ == want, (n, d, occ, want)
        assert count == sum(want.values())
    print(f"rim={n}: {num} assignments, {len(trials)} exact parameter samples, PASS")


if __name__ == '__main__':
    for size in range(3, 11):
        check(size)
    print('EXHAUSTIVE PASS')
