"""Finite exact consistency checks for monomial Gram identities.
The infinite-dimensional theorem follows from the analytic proof, not these checks.
"""
from fractions import Fraction
from math import factorial


def beta(n, j):
    return Fraction(factorial(n) * factorial(j), factorial(n + j + 1))


def gram_norm(n, a, J):
    return sum((Fraction(a * a) ** j * (beta(n, j) / factorial(j)) ** 2
                for j in range(J + 1)), Fraction(0))


def overlap(n, a, J):
    # Aligned ONB tails of z^n and z^{n+1}, through j=J+1.
    val = Fraction(0)
    for k in range(J + 1):
        cn = Fraction((-a) ** (k + 1) * factorial(n),
                      factorial(n + k + 2))
        cn1 = Fraction((-a) ** k * factorial(n + 1),
                       factorial(n + k + 2))
        val += cn * cn1
    return val


def density_moment(n, a, J):
    # The degree-J truncation of I_0 has Beta-product moments.
    return sum((Fraction(a * a) ** j * beta(n, j) ** 2
                / factorial(j) ** 2 for j in range(J + 1)), Fraction(0))


def primitive_moment(n, a, J):
    # F(q) = integral_q^1 rho(t)dt and Fubini.
    return density_moment(n + 1, a, J) / (n + 1)


def run():
    checked = 0
    for a in [0, 1, -1, 2, -3]:
        for n in range(7):
            for J in range(4):
                mn = gram_norm(n, a, J)
                assert mn == density_moment(n, a, J)
                checked += 1
                assert overlap(n, a, J) == -Fraction(a, n + 1) * gram_norm(n + 1, a, J)
                checked += 1
                assert primitive_moment(n, a, J) == gram_norm(n + 1, a, J) / (n + 1)
                checked += 1
    assert gram_norm(0, 0, 0) == 1
    checked += 1
    print(f"PASS: {checked} exact-rational finite identity checks")


if __name__ == '__main__':
    run()
