"""Exact integer checks for the digit characterization of lcm-binomial equality.

No external dependencies. Not a proof for unbounded inputs.
"""
from fractions import Fraction
from math import comb, gcd, lcm


def primes_up_to(bound):
    out = []
    for value in range(2, bound + 1):
        if all(value % p for p in out if p * p <= value):
            out.append(value)
    return out


def local_data(k, p):
    h = 0
    power = 1
    while power * p <= k:
        power *= p
        h += 1
    digits = []
    v = k
    for _ in range(h):
        digits.append(v % p)
        v //= p
    return digits



def digit_rule(n, k):
    if k <= 1:
        return True
    for p in primes_up_to(k):
        x = n
        for d in local_data(k, p):
            if x % p < d:
                return False
            x //= p
    return True


def density_and_period(k):
    if k <= 1:
        return Fraction(1), 1
    delta = Fraction(1)
    period = 1
    for p in primes_up_to(k):
        digits = local_data(k, p)
        for d in digits:
            delta *= Fraction(p - d, p)
        nz = [i for i, d in enumerate(digits) if d]
        if nz:
            period *= p ** (1 + max(nz))
    return delta, period


def brute_equal(n, k):
    assert 0 <= k <= n
    if k == 0:
        return True
    upper = lcm(*range(n - k + 1, n + 1))
    lower = lcm(*range(1, k + 1))
    assert upper % lower == 0
    return upper // lower == comb(n, k)


def check():
    comparisons = 0
    for n in range(0, 201):
        for k in range(0, min(n, 70) + 1):
            lhs = brute_equal(n, k)
            rhs = digit_rule(n, k)
            assert lhs == rhs, (n, k, lhs, rhs)
            comparisons += 1
    # Verify the density against the exact accepted residues of a full period.
    density_checks = 0
    minimal_period_checks = 0
    for k in range(0, 34):
        delta, T = density_and_period(k)
        if T > 50000:
            continue
        accepted = [digit_rule(n, k) for n in range(k, k + T)]
        assert Fraction(sum(accepted), T) == delta, (k, delta, T)
        density_checks += 1
        # No proper divisor can be a period of the indicator.
        proper = [d for d in range(1, T) if T % d == 0]
        for d in proper:
            assert any(accepted[i] != accepted[(i + d) % T] for i in range(T)), (k, d)
        minimal_period_checks += 1
    # Nontrivial examples for hand checking.
    for k, expected_density, expected_period in (
        (2, Fraction(1), 1),
        (3, Fraction(1, 2), 2),
        (5, Fraction(1, 6), 6),
        (6, Fraction(2, 5), 20),
        (7, Fraction(1, 10), 60),
        (10, Fraction(4, 21), 84),
    ):
        assert density_and_period(k) == (expected_density, expected_period), k
    print('VERIFY_OK', 'direct_lcm_binomial_comparisons=' + str(comparisons),
          'density_period_cases=' + str(density_checks),
          'minimal_period_cases=' + str(minimal_period_checks),
          'exact_integer_arithmetic=True')
    for k in (3, 5, 6, 7, 10, 20):
        d, period = density_and_period(k)
        print('k=%d density=%s period=%d' % (k, d, period))


if __name__ == '__main__':
    check()
