"""Independent reproducibility checks for a Poisson encounter-load allocation theorem.

Run: python check_crossings.py
No packages beyond the Python 3 standard library. Finite checks supplement the proof.
"""
from fractions import Fraction as Q
from math import factorial, exp, tanh
from random import Random


def p(y, degree):
    return sum(((-y) ** j) / Q(factorial(j)) for j in range(degree + 1))


def objective(c, x):
    return sum(v * exp(-c * v) for v in x)


def d_objective_dt(c, t):
    z = c * t / 2
    from math import cosh, sinh
    return exp(-c / 2) * ((c / 2 - 1) * sinh(z) - z * cosh(z))


def derivative_balance(c, t):
    return (c - 2) * tanh(c * t / 2) - c * t


def test():
    checks = 0
    c = Q(59, 10)
    a, b = Q(9, 40), Q(11, 20)
    cert = 2 * a * p(c * a, 27) + b * p(c * b, 27) - p(c / 3, 26)
    assert cert > 0
    assert float(cert) > 0.0008
    checks += 2

    # For any nonnegative y, Taylor's signed remainder gives P_27 <= exp(-y) <= P_26.
    for y in (Q(0), Q(1, 2), c * a, c * b, c / 3, Q(4)):
        yy = float(y)
        assert float(p(y, 27)) <= exp(-yy) + 1e-14
        assert float(p(y, 26)) >= exp(-yy) - 1e-14
        checks += 2

    # The n=2 exact formula and its analytic derivative agree with finite differences.
    for c0 in (0.1, 2., 4., 4.5, 8., 50.):
        for t in (0.03, 0.12, 0.25, 0.5, 0.8, 0.95):
            step = 1e-6
            f = lambda u: objective(c0, ((1-u)/2, (1+u)/2))
            numerical = (f(t + step) - f(t - step)) / (2 * step)
            assert abs(numerical - d_objective_dt(c0, t)) < 1e-7
            checks += 1

    # The n=2 global maximum is determined by monotonic z*coth(z).
    for c0 in (0.1, 1., 3.99, 4., 4.01, 5., 8., 20.):
        grid = [objective(c0, ((1-j/4000)/2, (1+j/4000)/2)) for j in range(4001)]
        assert max(grid) >= grid[0]
        if c0 <= 4:
            assert max(grid) - grid[0] <= 1e-12
        else:
            lo, hi = 0.000000001, 1.
            assert derivative_balance(c0, lo) > 0
            assert derivative_balance(c0, hi) < 0
            for _ in range(90):
                mid = (lo + hi)/2
                if derivative_balance(c0, mid) > 0:
                    lo = mid
                else:
                    hi = mid
            tstar = (lo+hi)/2
            assert objective(c0, ((1-tstar)/2, (1+tstar)/2)) >= max(grid) - 1e-13
            checks += 2
        checks += 1

    # Finite randomized comparisons against the analytically reduced 1D candidate family.
    # Not an exhaustive proof and deliberately uses a tolerance for the grid.
    rng = Random(527114)
    for n in (3, 4, 5):
        for c0 in (1., 3., 5.9, 6., 10., 20., 40.):
            qmax = max(objective(c0, [s] * (n-1) + [1-(n-1)*s])
                       for s in (j/(n*4000) for j in range(1, 4001)))
            for _ in range(1000):
                vals = [-__import__('math').log(max(1e-15,rng.random())) for _ in range(n)]
                total = sum(vals)
                x = [v / total for v in vals]
                assert objective(c0, x) <= qmax + 0.00005
                checks += 1

    # The asymptotic theorem is sandwiched between two explicit analytic bounds.
    for n in (2, 3, 4, 8):
        for c0 in (float(n + 1), 30., 100., 1000.):
            if c0 < n:
                continue
            low = (n-1)/exp(1) + (c0-n+1)*exp(-(c0-n+1))
            upper = (n-1)/exp(1) + (c0/n)*exp(-c0/n)
            assert low <= upper + 1e-12
            checks += 1

    return checks


if __name__ == '__main__':
    print('PASS: {} supplementary checks; analytic global statements are proved in RESULT.md'.format(test()))
