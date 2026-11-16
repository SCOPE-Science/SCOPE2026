"""Reproducible exact checks for the two-torus Poisson modulation theorem.

Run: python checker.py. Finite checks supplement, but cannot replace, the proof.
"""
from fractions import Fraction as Q
from itertools import product
import sympy as sp


def qpow(z, j):
    return z ** abs(j)


def shifted_coefficient(r, s, a, b, m, n):
    base = qpow(r, m) * qpow(s, n)
    plus = (qpow(r, m - 1) * qpow(s, n - 1) +
            qpow(r, m + 1) * qpow(s, n + 1))
    minus = (qpow(r, m - 1) * qpow(s, n + 1) +
             qpow(r, m + 1) * qpow(s, n - 1))
    return base + a * plus / 2 + b * minus / 2


def grouped_ratio(r, s, a, b, m, n):
    u = 1 / (r * s) + r * s
    v = s / r + r / s
    if m != 0 and n != 0:
        if m * n > 0:
            return 1 + (a * u + b * v) / 2
        return 1 + (a * v + b * u) / 2
    if m == 0 and n == 0:
        return 1 + r * s * (a + b)
    if m == 0:
        return 1 + (a + b) * r * (s + 1 / s) / 2
    return 1 + (a + b) * s * (r + 1 / r) / 2


def gram_apex(r, s, xs, ys):
    u = 1 / (r * s) + r * s
    v = s / r + r / s
    a = -2 / (u + v)
    # angles in a rational-cosine set: x in {0, pi}, y in {0, 2pi/3, 4pi/3}
    points = list(product(xs, ys))
    def cos_diff(t, z, d):
        k = (t - z) % d
        if d == 2:
            return sp.Integer(1) if k == 0 else sp.Integer(-1)
        return sp.Integer(1) if k == 0 else sp.Rational(-1, 2)
    vals = []
    for x, y in points:
        row = []
        for x2, y2 in points:
            cx = cos_diff(x, x2, 2)
            cy = cos_diff(y, y2, 3)
            px = (1 - r*r) / (1 - 2*r*cx + r*r)
            py = (1 - s*s) / (1 - 2*s*cy + s*s)
            row.append(px * py * (1 + 2*a*cx*cy))
        vals.append(row)
    return sp.Matrix(vals)


def main():
    checks = 0
    for r, s in [(Q(1, 3), Q(2, 5)), (Q(3, 4), Q(1, 2)), (Q(2, 7), Q(5, 9))]:
        u = 1/(r*s) + r*s
        v = s/r + r/s
        apex = -2/(u+v)
        for a,b in [(Q(0), Q(0)), (Q(1, 5), Q(-1, 10)), (apex,apex), (Q(2),Q(-3,2))]:
            for m,n in product(range(-5, 6), repeat=2):
                c = shifted_coefficient(r,s,a,b,m,n)
                expected = qpow(r,m)*qpow(s,n)*grouped_ratio(r,s,a,b,m,n)
                assert c == expected, (r,s,a,b,m,n,c,expected)
                checks += 1
        assert grouped_ratio(r,s,apex,apex,0,1) == (1-r*r)/(1+r*r)
        assert grouped_ratio(r,s,apex,apex,1,0) == (1-s*s)/(1+s*s)
        assert grouped_ratio(r,s,apex,apex,0,0) > 0
        assert grouped_ratio(r,s,apex,apex,1,1) == 0
        assert grouped_ratio(r,s,apex,apex,1,-1) == 0
        G = gram_apex(sp.Rational(r.numerator,r.denominator), sp.Rational(s.numerator,s.denominator), [0,1], [0,1,2])
        assert G.shape == (6,6)
        assert G.rank() == 4, (G.rank(), G)
        assert all(t >= 0 for t in G.eigenvals().keys())
        checks += 5
    print('CHECK_OK exact_Fourier_coefficient_cases=',checks-15,'graph_Gram_cases=3','apex_axes_cases=15')

if __name__ == '__main__':
    main()
