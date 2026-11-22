"""Exact finite consistency checks for the signed cusp-contact theorem.

The general theorem is proved by analysis and local algebra, not by this program.
Run: python verify.py
"""
from fractions import Fraction
from math import gcd


def values(p, q, r):
    assert p >= 2 and p % 2 == 0 and q > p and q % 2 == 1
    assert gcd(p, q) == 1 and r > q
    gamma = Fraction(q * (p - 1), p)
    alpha = Fraction(p + q, 2 * p * q)
    beta = Fraction(1, 2) - (gamma - 1) / (2 * r)
    gap = (q * (p - 1) - p) * Fraction(r - q, 2 * p * q * r)
    assert Fraction(0) < alpha < beta < Fraction(1, 2)
    assert beta - alpha == gap
    assert r * (1 - 2 * beta) - gamma == -1
    assert Fraction(q, p) - 2 * q * alpha == -1
    assert Fraction(q * (p - 1) - p, p) / (1 - 2 * beta) == r
    assert q * p < p * r
    return alpha, beta


assert values(2, 3, 4) == (Fraction(5, 12), Fraction(7, 16))
assert values(2, 3, 5) == (Fraction(5, 12), Fraction(9, 20))
assert values(4, 5, 6) == (Fraction(9, 40), Fraction(13, 48))
for p in range(2, 16, 2):
    for q in range(p + 1, 25, 2):
        if gcd(p, q) != 1:
            continue
        a = None
        last_beta = None
        for r in range(q + 1, q + 11):
            alpha, beta = values(p, q, r)
            if a is not None:
                assert alpha == a and beta > last_beta
            a, last_beta = alpha, beta

# For monic x-polynomials that differ only by plus/minus y**r,
# the resultant in x is exactly (2*y**r)**p (up to sign).
try:
    import sympy as sp
except ImportError:
    print('Rational identities passed; optional SymPy resultant checks skipped')
else:
    x, y = sp.symbols('x y')
    for p, q, r in ((2, 3, 4), (2, 3, 7), (4, 5, 6)):
        A = x**p - y**q + y**r
        B = x**p - y**q - y**r
        assert sp.expand(A * B - ((x**p - y**q)**2 - y**(2*r))) == 0
        resultant = sp.factor(sp.resultant(A, B, x))
        assert sp.expand(resultant - (2*y**r)**p) == 0
    print('Rational identities and sample symbolic resultants passed')
