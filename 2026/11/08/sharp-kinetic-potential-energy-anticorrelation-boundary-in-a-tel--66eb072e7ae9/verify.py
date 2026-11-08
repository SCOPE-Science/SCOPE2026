"""Exact rational checks for a telegraph-driven inertial harmonic oscillator.

Use Python 3.10+ standard library. No simulation or numerical integration is needed.
The checks independently solve each degree of the stationary generator.
"""
from fractions import Fraction as F


def linear_solve(a, b):
    """Gauss-Jordan elimination on a rational system."""
    n = len(b)
    a = [[F(v) for v in row] + [F(b[i])] for i, row in enumerate(a)]
    for col in range(n):
        piv = next((r for r in range(col, n) if a[r][col]), None)
        assert piv is not None, 'singular stationary moment recurrence'
        a[col], a[piv] = a[piv], a[col]
        div = a[col][col]
        a[col] = [z / div for z in a[col]]
        for r in range(n):
            if r == col:
                continue
            fac = a[r][col]
            a[r] = [a[r][j] - fac * a[col][j] for j in range(n + 1)]
    return [a[i][-1] for i in range(n)]


def moments(k, g, order=4):
    """Exact generator solution, not a hardcoded formula for the answer."""
    k, g = F(k), F(g)
    assert k > 0 and g > 0
    m = {(0, 0, 0): F(1), (0, 0, 1): F(0)}
    for n in range(1, order + 1):
        e = n % 2
        mon = [(i, n - i, e) for i in range(n + 1)]
        ids = {q: z for z, q in enumerate(mon)}
        a = [[F(0) for _ in mon] for _ in mon]
        b = [F(0) for _ in mon]
        for row, (i, j, e) in enumerate(mon):
            a[row][row] += 2 * j + 2 * g * e
            terms = [(-i, (i - 1, j + 1, e)),
                     (j * k, (i + 1, j - 1, e)),
                     (-j, (i, j - 1, 1 - e))]
            for c, key in terms:
                if not c:
                    continue
                if key in ids:
                    a[row][ids[key]] += c
                else:
                    b[row] -= c * m.get(key, F(0))
        sol = linear_solve(a, b)
        m.update(zip(mon, sol))
    return m


def direct_mixed_covariance(k, g):
    m = moments(k, g)
    return m[(2, 2, 0)] - m[(2, 0, 0)] * m[(0, 2, 0)]


def closed_form(k, g):
    k, g = F(k), F(g)
    d0 = 4*g*g + 4*g + k
    d9 = 4*g*g + 12*g + 9*k
    d8 = 4*g*g + 12*g + k + 8
    p = (48*g**4 + 384*g**3 + (104*k+1152)*g*g
         + (272*k+1104)*g - 3*(k-24)*(3*k+4))
    return -g*p/(2*(k+3)*d0*d0*d9*d8)


def check():
    count = 0
    ks = [F(1, 5), F(1), F(4), F(16), F(24), F(25), F(36), F(100), F(1000)]
    gs = [F(1, 100), F(1, 10), F(1, 2), F(1), F(3), F(10), F(40)]
    for k in ks:
        for g in gs:
            m = moments(k, g)
            d0 = 4*g*g + 4*g + k
            assert m[(2, 0, 0)] == (g+1)/(k*d0)
            count += 1
            assert m[(0, 2, 0)] == g/d0
            count += 1
            assert m[(1, 1, 0)] == 0
            count += 1
            exact = direct_mixed_covariance(k, g)
            formula = closed_form(k, g)
            assert exact == formula, (k, g, exact, formula)
            count += 1
            p = (48*g**4+384*g**3+(104*k+1152)*g*g
                 +(272*k+1104)*g-3*(k-24)*(3*k+4))
            assert (exact > 0) == (p < 0)
            assert (exact < 0) == (p > 0)
            count += 2
            if k <= 24:
                assert exact < 0
                count += 1
    assert direct_mixed_covariance(F(36), F(1,10)) == F(5795375, 30528348533124)
    assert direct_mixed_covariance(F(36), F(1)) == F(-127, 32089200)
    count += 2
    assert closed_form(F(24), F(1)) < 0
    assert closed_form(F(36), F(1,10)) > 0
    assert closed_form(F(36), F(1)) < 0
    count += 3
    print(f'PASS: {count} exact-rational checks of the independent generator system and closed form')


if __name__ == '__main__':
    check()
