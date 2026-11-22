"""Finite exact-arithmetic diagnostics for parity-perturbed sign moments.

The infinite-dimensional statements and their asymptotics use analytic proofs.
"""
from fractions import Fraction
from itertools import product
from math import prod
from math import comb, factorial


def indep_moment(a):
    n = len(a)
    return sum(sum(ai * si for ai, si in zip(a, eps)) ** n
               for eps in product((-1, 1), repeat=n)) // (2 ** n)


def numerator_theta(a, theta):
    n = len(a)
    total = sum((sum(ai * si for ai, si in zip(a, eps)) ** n)
                * (1 + theta * prod(eps))
                for eps in product((-1, 1), repeat=n))
    return total / (2 ** n)


def uniform_moment(n):
    return sum(comb(n, j) * (n - 2 * j) ** n
               for j in range(n + 1)) // (2 ** n)


def run():
    checks = 0
    for n in (4, 6, 8):
        m = uniform_moment(n)
        assert m > factorial(n)
        checks += 1
        vectors = [(1,) * n, tuple(-1 if i == 0 else 1 for i in range(n)),
                   (0,) + (1,) * (n - 1), tuple(range(1, n + 1)),
                   tuple(1 + (i % 2) for i in range(n)),
                   tuple((-1) ** i * (i + 1) for i in range(n)),
                   tuple(i % 3 - 1 for i in range(n)),
                   tuple(3 if i == 0 else 1 for i in range(n))]
        for a in vectors:
            base = indep_moment(a)
            prod_a = prod(a)
            assert Fraction(factorial(n) * abs(prod_a), base) <= Fraction(factorial(n), m)
            checks += 1
            equality = factorial(n) * abs(prod_a) * m == factorial(n) * base
            assert equality == (len(set(map(abs, a))) == 1 and 0 not in a)
            checks += 1
            for theta in (Fraction(-1), Fraction(-1, 3), Fraction(0),
                          Fraction(2, 5), Fraction(1)):
                shifted = numerator_theta(a, theta)
                assert shifted == base + theta * factorial(n) * prod_a
                checks += 1
                lower = 1 - abs(theta) * Fraction(factorial(n), m)
                upper = 1 + abs(theta) * Fraction(factorial(n), m)
                assert lower <= shifted / base <= upper
                checks += 1
    assert Fraction(factorial(4), uniform_moment(4)) == Fraction(3, 5)
    assert Fraction(factorial(6), uniform_moment(6)) == Fraction(15, 47)
    checks += 2
    print(f"PARITY_NTH_RELATIVE_EXACT_OK {checks}")
    print("SHARP_LAMBDA_4_6_8", [str(Fraction(factorial(n), uniform_moment(n))) for n in (4, 6, 8)])


if __name__ == '__main__':
    run()
