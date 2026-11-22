"""Direct finite checks for simultaneous local-square laws of tetrahedral numbers.

Standard-library-only. These checks test finite cases, not the infinite proof.
"""
from fractions import Fraction
from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))


def chi(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def tetra(n):
    return n * (n - 1) * (n - 2) // 6


def trace(p):
    return -sum(chi(n * (n - 1) * (n - 2), p) for n in range(p))


def regular_count(p):
    a = trace(p)
    numerator = p - 6 - chi(-1, p) - 2 * chi(-2, p) - 2 * chi(6, p) * a
    assert numerator % 4 == 0
    return numerator // 4


def formula_counts(p, k):
    a = trace(p)
    r = regular_count(p)
    e = int(chi(-1, p) == 1)
    f = int(chi(-2, p) == 1)
    shell = ((p - 1) // 2) * sum(
        p ** (k - 2 * m - 1) for m in range(1, (k - 1) // 2 + 1)
    )
    joint = r * p ** (k - 1) + 3 + e + (1 + e + 2 * f) * shell
    marginal = ((p - 3 - chi(6, p) * a) // 2) * p ** (k - 1) + 3 * (1 + shell)
    return marginal, joint


def direct_counts(p, k):
    modulus = p ** k
    squares = {x*x % modulus for x in range(modulus)}
    marginal = joint = 0
    for n in range(modulus):
        b = tetra(n) % modulus in squares
        c = tetra(n + 1) % modulus in squares
        marginal += b
        joint += b and c
    return marginal, joint


def densities(p):
    a = trace(p)
    r = regular_count(p)
    e = int(chi(-1, p) == 1)
    f = int(chi(-2, p) == 1)
    mu = Fraction(p - 3 - chi(6, p) * a, 2 * p) + Fraction(3, 2 * p * (p + 1))
    delta = Fraction(r, p) + Fraction(1 + e + 2 * f, 2 * p * (p + 1))
    return mu, delta


def main():
    primes = [p for p in range(5, 102) if is_prime(p)]
    finite = 0
    for p in primes:
        r = regular_count(p)
        assert r == sum(
            chi(tetra(n), p) == 1 and chi(tetra(n+1), p) == 1
            for n in range(p) if n % p not in (0, 1, 2, p-1)
        ), (p, 'regular-character-count')
        assert r > 0, (p, 'existence')
        assert abs(trace(p)) <= 2 * isqrt(p) + 1, (p, 'trace-bound-rounded')
        for k in range(1, 5 if p <= 17 else (4 if p <= 43 else 3)):
            expected = formula_counts(p, k)
            observed = direct_counts(p, k)
            assert observed == expected, (p, k, observed, expected)
            finite += 1
        mu, delta = densities(p)
        assert 0 < delta <= mu < 1
        if p % 4 == 3:
            assert trace(p) == 0
            assert mu == Fraction(p-2, 2*(p+1))
            if p % 8 == 3:
                assert delta == Fraction(p*p-6*p-1, 4*p*(p+1))
                assert delta - mu*mu == Fraction(-p*p-11*p-1, 4*p*(p+1)**2)
            else:
                assert p % 8 == 7
                assert delta == Fraction(p*p-2*p-1, 4*p*(p+1))
                assert delta - mu*mu == Fraction(3*p*p-7*p-1, 4*p*(p+1)**2)
    print(f'PASS: {len(primes)} prime-field checks and {finite} full prime-power histogram tests.')
    print('PASS: exact marginal/joint formulas and the two covariance-sign laws.')
    print('Small prime regular counts:', [(p, regular_count(p)) for p in primes if p < 37])
    print('Example densities:', [(p, str(densities(p)[0]), str(densities(p)[1])) for p in (5,7,11,13)])


if __name__ == '__main__':
    main()
