"""Exact finite checks for the occupancy-frequency/Hamming-weight covariance theorem.

No external dependencies.  Finite tests complement an analytic all-parameter proof.
"""
from fractions import Fraction
from math import comb, factorial, prod


def compositions(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for a in range(total + 1):
            for rest in compositions(total - a, parts - 1):
                yield (a,) + rest


def direct_covariance(m, n, r):
    denominator = m**n
    ef = eh = efh = total_weight = 0
    for loads in compositions(n, m):
        weight = factorial(n) // prod(factorial(a) for a in loads)
        total_weight += weight
        f = sum(a == r for a in loads)
        h = sum(a % 2 for a in loads)
        ef += weight * f
        eh += weight * h
        efh += weight * f * h
    assert total_weight == denominator
    return Fraction(efh, denominator) - Fraction(ef * eh, denominator**2)


def formula_covariance(m, n, r):
    assert m >= 3 and 1 <= r <= n
    u = Fraction(m - 3, m - 1)
    v = Fraction(m - 2, m)
    p = Fraction(comb(n, r) * (m-1)**(n-r), m**n)
    parity_sign = 1 if r % 2 else -1
    return Fraction(m, 2) * p * (parity_sign - (m-1)*u**(n-r) + m*v**n)


def run_checks():
    cases = 0
    # Independent enumeration, including the m=3 and n=r boundaries.
    for m in range(3, 6):
        for n in range(1, 9 if m <= 4 else 8):
            for r in range(1, n+1):
                assert direct_covariance(m, n, r) == formula_covariance(m, n, r)
                cases += 1

    # Exact rational sign tests: no floating-point comparisons.
    for m in range(3, 21):
        for r in range(1, 16):
            seen_positive = False
            for n in range(r, 101):
                value = formula_covariance(m, n, r)
                if r % 2 == 0:
                    assert value < 0
                elif r == 1:
                    assert value == 0 if n == 1 else value > 0
                else:
                    if n == r:
                        assert value < 0
                    if value > 0:
                        seen_positive = True
                    if seen_positive:
                        assert value > 0
                cases += 1
            if r % 2 == 1 and r >= 3:
                assert seen_positive
    return cases


if __name__ == '__main__':
    print('exact_parameter_cases:', run_checks())
