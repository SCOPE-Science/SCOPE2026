"""Finite exact consistency checks for cyclic windows and the noise example."""
from collections import Counter
from fractions import Fraction
from math import comb


def check():
    cases = 0
    for n in range(3, 15):
        d = n - 1
        assert sum(comb(d, j)**2 for j in range(n)) == comb(2*d, d)
        for m in range(n, 4*n + 1):
            residual = m - 1
            windows = [{(i + j) % residual for j in range(d)}
                       for i in range(residual)]
            assert all(len(w) == d for w in windows)
            assert Counter(t for w in windows for t in w) == {t: d for t in range(residual)}
            assert (Fraction(residual, 2*d) > 1) == (m >= 2*n)
            cases += 1

    # On an exact finite fixture the design column equals the model's
    # design-dependent error vector when nu=1. The same identity holds for
    # arbitrary complex nodes; this is only a check of column indexing.
    z = [1, 1j, -1, -1j]
    rows = [[zz**k for k in range(3)] for zz in z]
    axis = [0, 1, 0]
    assert [sum(a*b for a, b in zip(row, axis)) for row in rows] == z
    print(f'PASS: {cases} window/threshold cases and the design-column identity')


if __name__ == '__main__':
    check()
