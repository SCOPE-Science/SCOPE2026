"""Exact finite Dirichlet-moment checks and high-precision scalar checks.

Standard-library only. Numerical checks supplement, not replace, the analytic proof.
"""
from fractions import Fraction
from itertools import product
from math import factorial, exp, log, sqrt, comb


def compositions(n, count):
    if count == 1:
        yield (n,)
    else:
        for v in range(n + 1):
            for tail in compositions(n - v, count - 1):
                yield (v,) + tail


def rising(x, m):
    out = Fraction(1)
    for j in range(m):
        out *= x + j
    return out


def bernstein_coeff(b):
    n = sum(b)
    out = factorial(n)
    for j in b:
        out //= factorial(j)  # exact because integer factorial products divide n!
    return out


def moment(b, c, theta):
    n = sum(b)
    A = sum(theta)
    num = Fraction(bernstein_coeff(b) * bernstein_coeff(c))
    for h, u, v in zip(theta, b, c):
        num *= rising(h, u + v)
    return num / rising(A, 2 * n)


def trace_tests():
    count = 0
    cases = [
        (1, [1, 1], 5),
        (1, [Fraction(1, 2), Fraction(3, 2)], 4),
        (2, [1, 2, 3], 4),
        (2, [Fraction(1, 2), Fraction(1, 3), Fraction(5, 2)], 3),
        (3, [1, 1, 1, 1], 3),
    ]
    for d, theta, n in cases:
        theta = [Fraction(x) for x in theta]
        A = sum(theta)
        bs = list(compositions(n, d + 1))
        # The normalized Dirichlet moment of B_b is computed with degree zero in c.
        # Unlike moment(), this deliberately uses independent integration formula.
        def average(b):
            out = Fraction(bernstein_coeff(b))
            for h, u in zip(theta, b):
                out *= rising(h, u)
            return out / rising(A, n)
        diagonal = {b: average(b) for b in bs}
        tr = sum(moment(b, b, theta) / diagonal[b] for b in bs)
        tr2 = sum(moment(b, c, theta)**2 / (diagonal[b] * diagonal[c]) for b in bs for c in bs)
        predicted = [Fraction(1)]
        for k in range(1, n + 1):
            predicted.append(predicted[-1] * Fraction(n - k + 1, 1) / (n + A + k - 1))
        expected1 = sum(comb(k + d - 1, d - 1) * predicted[k] for k in range(n + 1))
        expected2 = sum(comb(k + d - 1, d - 1) * predicted[k]**2 for k in range(n + 1))
        assert tr == expected1, (d, theta, n, tr, expected1)
        assert tr2 == expected2, (d, theta, n, tr2, expected2)
        count += 2
    return count


def centered_series_checks():
    # Validate two distinct powers and the cancellation, with small truncation error.
    # Use stable log1p rather than multiplying many nearly-one factors.
    from math import log1p
    checks = 0
    for A in (0.3, 1.0, 2.0, 4.5):
        for k in (1, 2, 3):
            q = k*(k + A - 1)
            D = q*(2*q+(A-1)**2-1)/12
            assert D > 0
            assert abs(D - (2/3)*sum((j+A/2)**3 for j in range(k))) < 1e-10
            checks += 1
            errors = []
            for n in (80, 160, 320):
                N = n+A/2
                v = sum(log1p(-(j+A/2)/N)-log1p((j+A/2)/N) for j in range(k))
                # 5th order residual after center and cubic must be nonnegative.
                remainder = -N*v - q - D/N**2
                assert remainder >= -1e-10
                assert abs(remainder) < 1000*(k+1)**6 / N**4
                errors.append(abs(remainder))
                checks += 2
            assert errors[2] <= errors[0]/12, (A, k, errors)
            checks += 1
    for t in (0.4, 1.3):
        A=3.5
        for n in (40, 100, 300):
            N=n+A/2
            q=2*(2+A-1)
            D=q*(2*q+(A-1)**2-1)/12
            lg=sum(log1p(-(j+A/2)/N)-log1p((j+A/2)/N) for j in range(2))
            actual=exp(t*N*lg)
            heat=exp(-t*q)
            corrected=heat*(1-t*D/N**2)
            assert actual < heat
            assert abs(actual-corrected) <= 20/N**4
            checks += 2
    return checks


def main():
    a=trace_tests()
    b=centered_series_checks()
    print('VERIFIED:', a, 'exact rational finite spectral trace checks,', b, 'analytic expansion numerical cross-checks')

if __name__ == '__main__':
    main()
