"""Exact finite spectral counting diagnostics for a rank-two matrix-ball kernel.

No numerical experiment below establishes the infinite-dimensional asymptotic;
that statement is proved analytically in RESULT.md.
Run: python3 verify_count.py
"""
from fractions import Fraction
from math import log


def eigenvalue(gamma, m, n):
    """Exact eigenvalue for integers m>=n>=0 and rational gamma>0."""
    assert gamma > 0 and m >= n >= 0
    g = gamma
    a = ((g + 1) * (g + 2) * (g + 3) /
         ((m + g + 1) * (m + g + 2) * (m + g + 3)))
    b = ((g) * (g + 1) * (g + 2) /
         ((n + g) * (n + g + 1) * (n + g + 2)))
    return a * b


def count_above(gamma, tau):
    """Exact integer #{eigenvalues > tau}, with squared K-type dimensions."""
    assert gamma > 0 and tau > 0
    n = 0
    total = 0
    while eigenvalue(gamma, n, n) > tau:
        lo, hi = n, max(1, n + 1)
        while eigenvalue(gamma, hi, n) > tau:
            hi = max(hi * 2, hi + 1)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if eigenvalue(gamma, mid, n) > tau:
                lo = mid
            else:
                hi = mid - 1
        k = lo - n + 1
        assert eigenvalue(gamma, lo, n) > tau
        assert eigenvalue(gamma, lo + 1, n) <= tau
        total += k * (k + 1) * (2 * k + 1) // 6
        n += 1
    return total


def naive_count(gamma, tau):
    total = 0
    for n in range(100):
        if eigenvalue(gamma, n, n) <= tau:
            return total
        for m in range(n, 10000):
            if eigenvalue(gamma, m, n) <= tau:
                break
            total += (m - n + 1)**2
    raise AssertionError('naive safety cutoff')


def constants(gamma):
    g = float(gamma)
    A = (g + 1) * (g + 2) * (g + 3)
    B = g * (g + 1) * (g + 2)
    return A * (g + 2) / 6, (A * B)**(2/3) / 6


def main():
    tests = 0
    for g in (Fraction(1, 2), Fraction(1), Fraction(2)):
        for k in (1, 2, 3):
            t = Fraction(1, 10**k)
            exact = count_above(g, t)
            assert exact == naive_count(g, t), (g, k, exact)
            tests += 1
        c0, c1 = constants(g)
        print('gamma', str(g), 'lead_C', format(c0, '.12g'),
              'log_C', format(c1, '.12g'))
        for k in (5, 7, 9, 11, 13):
            t = Fraction(1, 10**k)
            result = count_above(g, t)
            x = float(t)
            model = c0 / x - c1 * x**(-2/3) * log(1/x)
            residual_scaled = (result - model) / x**(-2/3)
            print('  decade', k, 'N=', result,
                  'scaled_remainder=', f'{residual_scaled:.7f}')
            assert result > 0
            tests += 1
    print('PASS', tests, 'exact counting diagnostics')


if __name__ == '__main__':
    main()
