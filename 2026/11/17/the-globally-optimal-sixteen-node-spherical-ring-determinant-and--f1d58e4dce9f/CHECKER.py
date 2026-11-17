"""Exact rational certificate for the sixteen-node spherical ring design.

Run with Python 3.10 or later: python CHECKER.py
Uses only the standard library. The determinant factorization and strong
concavity used to interpret the certificate are established in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import permutations

# Rows are ordered by increasing latitude, expressed by ring labels 1,2,3.
# Each height is an exact rational number with denominator 10**10.
DATA = {
    (1, 2, 3): (-7453364257, -1443429094, 5653891177),
    (1, 3, 2): (-7224748987, 7215671467, -629158625),
    (2, 1, 3): (300179852, -6231431047, 5750945098),
    (2, 3, 1): (8685804158, -6042361642, 2022056534),
    (3, 1, 2): (1711718224, 7433256806, -4614491244),
    (3, 2, 1): (8828424289, 3096304714, -4566685205),
}
ORDER = ((2, 3, 1), (3, 2, 1), (1, 3, 2),
         (3, 1, 2), (2, 1, 3), (1, 2, 3))


def determinant_factor(v):
    """D = squared determinant divided by the same positive constant C_4."""
    x = (Q(-1),) + tuple(v)
    d = Q(1)
    for j in range(1, 4):
        d *= (1 - x[j] ** 2) ** (j * (j + 1))
    for i in range(4):
        for j in range(i + 1, 4):
            d *= abs(x[j] - x[i]) ** (2 * (2 * i + 1))
    return d


def gradient(v):
    x = (Q(-1),) + tuple(v)
    return tuple(
        -Q(2 * j * (j + 1)) * x[j] / (1 - x[j] ** 2)
        + sum(Q(2 * (2 * i + 1)) / (x[j] - x[i])
              for i in range(j))
        + sum(Q(2 * (2 * j + 1)) / (x[j] - x[k])
              for k in range(j + 1, 4))
        for j in range(1, 4)
    )


def verify():
    assert set(DATA) == set(permutations((1, 2, 3)))
    d, g2 = {}, {}
    for p, numerators in DATA.items():
        v = tuple(Q(t, 10**10) for t in numerators)
        assert all(-1 < z < 1 for z in v)
        assert tuple(sorted((1, 2, 3), key=lambda i: v[i - 1])) == p
        d[p] = determinant_factor(v)
        assert d[p] > 0
        g = gradient(v)
        g2[p] = sum(t * t for t in g)
        # The bound is exact rational, and implies ||q-x*||_2 < 10^-8.
        assert g2[p] < Q(1, 10**15)
    for better, worse in zip(ORDER[:-1], ORDER[1:]):
        # For F=log D, Hess F <= -4I, hence
        # F(max in chamber) <= F(q)+||grad F(q)||^2/8.
        # The elementary bound exp(u) <= 1+2u for 0<=u<=1/2
        # makes this an exact rational certificate.
        assert d[better] > d[worse] * (1 + g2[worse] / 4)
    a, b = ORDER[:2]
    lower = d[a] / (d[b] * (1 + g2[b] / 4))
    upper = d[a] * (1 + g2[a] / 4) / d[b]
    assert lower > Q(477011, 100000)
    assert upper < Q(477012, 100000)
    assert d[a] > 4 * d[b] * (1 + g2[b] / 4)
    print('PASS: 6 exact chambers, 5 strict ordering certificates')
    print('PASS: each rational point within 10^-8 of its unique chamber optimum')
    print('PASS: optimal/runner-up squared determinant in (4.77011,4.77012)')
    print('PASS: best squared determinant >4 times every other chamber maximum')


if __name__ == '__main__':
    verify()
