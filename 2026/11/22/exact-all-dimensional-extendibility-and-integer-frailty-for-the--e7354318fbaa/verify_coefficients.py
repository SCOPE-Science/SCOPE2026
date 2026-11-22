"""Exact checks for the power-series recurrence in a Lomax-distorted copula.

The infinitely many coefficient inequalities are proved analytically; these
finite exact-arithmetic checks test independent expansions and boundary cases.
"""
from fractions import Fraction as Q
from math import factorial


def generalized_binom(p, n):
    out = Q(1)
    for j in range(n):
        out *= (p - j) / (j + 1)
    return out


def independent_coefficients(alpha, theta, N):
    """First N+1 coefficients of f(u) by direct generalized-binomial convolution."""
    s = theta - 1
    return [sum(((-1) ** j * generalized_binom(alpha - 1, j))
                * (generalized_binom(-alpha - 1, n - j) * s ** (n - j))
                for j in range(n + 1)) for n in range(N + 1)]


def recurrence_coefficients(alpha, theta, N):
    """First N+1 coefficients via the first-order rational differential equation."""
    s = theta - 1
    A = Q(2) - (alpha + 1) * theta
    a = [Q(1), A]
    for n in range(1, N):
        a.append(((A + (1 - s) * n) * a[n]
                  + s * (n + 1) * a[n - 1]) / (n + 1))
    return a[:N + 1]


def main():
    valid = [(Q(1, 2), Q(4, 3)), (Q(9, 10), Q(20, 19)),
             (Q(1, 2), Q(1, 2)), (Q(1), Q(1)),
             (Q(1), Q(1, 5)), (Q(1, 3), Q(3, 2))]
    invalid = [(Q(1, 2), Q(7, 5)), (Q(9, 10), Q(11, 10)),
               (Q(1), Q(6, 5))]
    for alpha, theta in valid + invalid:
        assert independent_coefficients(alpha, theta, 26) == recurrence_coefficients(alpha, theta, 26)
    for alpha, theta in valid:
        a = recurrence_coefficients(alpha, theta, 80)
        assert all(v >= 0 for v in a)
        assert theta <= 2 / (alpha + 1)
    for alpha, theta in invalid:
        a = recurrence_coefficients(alpha, theta, 26)
        assert a[1] < 0
        assert theta > 2 / (alpha + 1)
    # Boundary: w_1=2/3, w_2=0, w_3=2/27 exactly.
    alpha, theta = Q(1, 2), Q(4, 3)
    a = recurrence_coefficients(alpha, theta, 5)
    w = [Q(0)] + [alpha * theta * a[k - 1] / k for k in range(1, 6)]
    assert (w[1], w[2], w[3]) == (Q(2, 3), Q(0), Q(2, 27))
    assert recurrence_coefficients(Q(1), Q(1), 10) == [Q(1)] + [Q(0)] * 10
    print('PASS: 9 direct binomial-series/ODE comparisons, exact positivity samples,')
    print('       exact negative quadratic coefficients, and boundary weights.')
    print('Finite checks are supplementary; the theorem uses induction and Laplace uniqueness.')


if __name__ == '__main__':
    main()
