"""Exact finite-dimensional diagnostics for symmetric two-sample spline projection.

Run with Python 3 standard library. All entries are rational for rational t.
The general theorem is established by the separate analytic Green-kernel proof.
"""
from fractions import Fraction as F


def inverse(a):
    n = len(a)
    z = [[F(v) for v in row] + [F(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for j in range(n):
        k = next(k for k in range(j, n) if z[k][j])
        z[k], z[j] = z[j], z[k]
        v = z[j][j]
        z[j] = [x / v for x in z[j]]
        for k in range(n):
            if k != j:
                v = z[k][j]
                if v:
                    z[k] = [u-v*w for u, w in zip(z[k], z[j])]
    return [row[n:] for row in z]


def evaluate(n, t):
    a, b = 1-t, t
    f = [[F(0) for _ in range(n)] for _ in range(2*n)]
    for i in range(n):
        f[2*i][i], f[2*i][(i+1) % n] = a, b
        f[2*i+1][i], f[2*i+1][(i+1) % n] = b, a
    gram = [[sum(f[k][i]*f[k][j] for k in range(2*n))
             for j in range(n)] for i in range(n)]
    inv = inverse(gram)
    c = [[sum(inv[j][k]*f[s][k] for k in range(n))
          for s in range(2*n)] for j in range(n)]
    for row in c:
        assert sum(row) == 1
    return c


def predicted(n, t):
    q = t/(1-t)
    if t == F(1, 2):
        assert n % 2
        return F(n)
    return (1-q**n)/((1-2*t)*(1-(-q)**n))


def test():
    cases = 0
    for n in range(3, 14):
        for t in (F(1, 10), F(1, 4), F(2, 5)):
            c = evaluate(n, t)
            lam = predicted(n, t)
            q = t/(1-t)
            a = 1-t
            for j, row in enumerate(c):
                assert sum(abs(u) for u in row) == lam
                assert sum(u for u in row if u < 0) == (1-lam)/2
                for i in range(n):
                    k = (i-j) % n
                    assert row[2*i] == (-q)**k/(2*a*(1-(-q)**n))
                    assert row[2*i+1] == (-q)**(n-1-k)/(2*a*(1-(-q)**n))
                # Opposing signed nonzero weights forbid edge-interior maxima.
                next_row = c[(j+1) % n]
                assert any(u*v < 0 for u, v in zip(row, next_row))
            cases += 1
    print('EXACT_RATIONAL_GRAM_AND_LEBESGUE_N_3_TO_13_OK', cases, 'CASES')
    for n in (3, 5, 7, 9):
        c = evaluate(n, F(1, 2))
        assert all(sum(abs(u) for u in row) == n for row in c)
    print('ODD_MIDPOINT_LIMIT_AND_ATTAINMENT_OK')
    for n in (3, 4, 5, 6):
        c = evaluate(n, F(0))
        assert all(sum(abs(u) for u in row) == 1 for row in c)
    print('KNOT_SAMPLING_LIMIT_OK')
    print('ALL_DISCRETE_SPLINE_CHECKS_PASSED')


if __name__ == '__main__':
    test()
