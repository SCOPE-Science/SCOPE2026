"""Finite diagnostics for the four-point quadratic midpoint-knot interpolant.

The analytic determinant and limiting-norm proof are in RESULT.md. This program
uses exact rational interpolation coefficients and numerical sampling only to
check implementation and representative parameter values.
"""
from fractions import Fraction as F
from math import sqrt


def solve(a, b):
    n = len(b)
    m = [row[:] + [val] for row, val in zip(a, b)]
    for k in range(n):
        p = next(i for i in range(k, n) if m[i][k])
        m[k], m[p] = m[p], m[k]
        v = m[k][k]
        m[k] = [z / v for z in m[k]]
        for i in range(n):
            if i != k:
                v = m[i][k]
                m[i] = [u - v * w for u, w in zip(m[i], m[k])]
    return [row[-1] for row in m]


def equations(e, r):
    k = (1 + e) / 2
    return [
        [F(1), F(0), F(0), F(0), F(0), F(0)],
        [F(1), e, e * e, F(0), F(0), F(0)],
        [F(0), F(0), F(0), F(1), F(1), F(1)],
        [F(0), F(0), F(0), F(1), r, r * r],
        [F(1), k, k * k, F(-1), -k, -k * k],
        [F(0), F(1), 2 * k, F(0), F(-1), -2 * k],
    ]


def value(coeffs, e, t):
    k = (1 + e) / 2
    j = 0 if t <= k else 3
    return coeffs[j] + t * coeffs[j + 1] + t * t * coeffs[j + 2]


def g(r, t):
    if t <= F(1, 2):
        return t - (4 * r - 1) * t * t / (3 * r - 1)
    return (t - 1) * (t - r) / (3 * r - 1)


def lead(r):
    return max((3 * r - 1) / (2 * (4 * r - 1)),
               (r - 1) ** 2 / (2 * (3 * r - 1)))


def run():
    assertions = 0
    for r in [F(11, 10), F(2), F(37, 10), F(4), F(8)]:
        for e in [F(1, 20), F(1, 200), F(1, 2000)]:
            A = equations(e, r)
            cols = [solve(A, [F(int(i == j)) for i in range(6)])
                    for j in range(4)]
            for j, c in enumerate(cols):
                for i, row in enumerate(A):
                    assert sum(v * w for v, w in zip(row, c)) == int(i == j)
                    assertions += 1
            if e == F(1, 2000):
                for t in [F(1, 5), F(2, 5), F(3, 5), F(1), (1+r)/2, r]:
                    assert abs(float(e * value(cols[1], e, t) - g(r, t))) < 0.025
                    assert abs(float(e * value(cols[0], e, t) + g(r, t))) < 0.025
                    assertions += 2
                maximum = 0.0
                for i in range(6001):
                    t = r * i / 6000
                    norm = sum(abs(float(value(c, e, t))) for c in cols)
                    maximum = max(maximum, norm)
                discrepancy = abs(float(e) * maximum - float(lead(r)))
                assert discrepancy < 0.012, (r, discrepancy)
                assertions += 1
    assert 2 + sqrt(3) > 3.7
    assert 2 + sqrt(3) < 3.8
    assertions += 2
    print('QUADRATIC_COLLISION_DIAGNOSTICS_OK', assertions, 'exact and sampled checks')

if __name__ == '__main__':
    run()
