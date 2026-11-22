"""Independent finite checks for the exact weighted Bergman first-jet projection.

Only Python's standard library is required.  Finite checks corroborate an
analytic all-order argument; they are not a substitute for that proof.
"""
from fractions import Fraction as Q
from math import comb, exp, gamma, lgamma, log, log1p, sqrt


def a_int(n, beta):
    return Q(comb(n + beta - 1, n))


def projection_closed(n, beta, x):
    a = a_int(n, beta)
    h = n + beta
    return a * x ** (n - 1) * (1 - x) ** beta * (x + Q((n - h * x) ** 2, beta))


def projection_independent_gram(n, beta, x):
    # Eliminate the common sqrt(x) and sqrt(a_n) from the value/jet Gram inverse.
    a = a_int(n, beta)
    S0 = (1 - x) ** (-beta)
    S1sq = beta * beta * x * (1 - x) ** (-2 * beta - 2)
    S2 = beta * (1 + beta * x) * (1 - x) ** (-beta - 2)
    mixed = beta * n * x ** n * (1 - x) ** (-beta - 1)
    numerator = S2 * x ** n - 2 * mixed + S0 * n * n * x ** (n - 1)
    determinant = S0 * S2 - S1sq
    assert determinant > 0
    return a * numerator / determinant


def derivative_direct(n, beta, x):
    a = a_int(n, beta)
    h = n + beta
    b = x + (n - h * x) ** 2 / Q(beta)
    db = 1 - Q(2 * h * (n - h * x), beta)
    return a * x ** (n - 2) * (1 - x) ** (beta - 1) * ((n - 1) * (1 - x) * b - beta * x * b + x * (1 - x) * db)


def derivative_factored(n, beta, x):
    a = a_int(n, beta)
    h = n + beta
    quad = h * (h + 1) * x * x - 2 * n * h * x + n * (n - 1)
    return a / beta * x ** (n - 2) * (1 - x) ** (beta - 1) * (n - h * x) * quad


def roots(n, beta):
    h = n + beta
    t = sqrt(n * (beta + 1) / h)
    return (n - t) / (h + 1), n / h, (n + t) / (h + 1)


def floating_projection(n, beta, x):
    h = n + beta
    return exp(lgamma(n + beta) - lgamma(beta) - lgamma(n + 1) + (n - 1) * log(x) + beta * log1p(-x) + log(x + (n - h * x) ** 2 / beta))


def gamma_limit(beta):
    t = sqrt(beta + 1)
    c = beta + 1 + t
    return exp(log(2) + (beta + 1) * log(c) - c - lgamma(beta + 1))


def main():
    checks = 0
    for n in range(2, 19):
        for beta in range(1, 8):
            for x in [Q(1, 11), Q(2, 7), Q(3, 5), Q(8, 9)]:
                exact = projection_closed(n, beta, x)
                gram = projection_independent_gram(n, beta, x)
                assert exact == gram and 0 < exact < 1, (n, beta, x, exact, gram)
                checks += 1
                assert derivative_direct(n, beta, x) == derivative_factored(n, beta, x)
                checks += 1
    for n in (2, 3, 5, 20, 200):
        for beta in (1.001, 1.5, 2.0, 3.75, 20.0):
            rm, rz, rp = roots(n, beta)
            assert 0 < rm < rz < rp < 1
            checks += 1
            # Strictly positive independent projection energies, two candidate peaks.
            pm = floating_projection(n, beta, rm)
            pp = floating_projection(n, beta, rp)
            pz = floating_projection(n, beta, rz)
            assert 0 < pz < min(pm, pp) <= 1.0000000001
            checks += 1
    for beta in (1.001, 2, 4, 15):
        n = 10000
        rm, _, rp = roots(n, beta)
        L = gamma_limit(beta)
        assert abs(n * floating_projection(n, beta, rm) / L - 1) < 0.011
        assert floating_projection(n, beta, rm) > floating_projection(n, beta, rp)
        checks += 2
    print('PASS:', checks, 'checks; Gram inversion, factored derivative, extrema, gamma boundary law')


if __name__ == '__main__':
    main()
