"""Elementary finite checks for a ternary elated-number density bound.

The asymptotic theorem is established by the accompanying proof, not by this script.
"""
from fractions import Fraction
from math import exp


def leading_base3(n):
    assert n > 0
    while n >= 3:
        n //= 3
    return n


def elated(n):
    lead = leading_base3(n)
    x = n
    squares = 0
    while x:
        x, d = divmod(x, 3)
        squares += d*d
    return lead*squares


def is_elated(n):
    seen = set()
    while n not in seen:
        if n == 1:
            return True
        seen.add(n)
        n = elated(n)
    return False


def verify():
    for n in range(1, 10001):
        t = elated(n)
        assert (t & 1) == ((n & 1) * (leading_base3(n) & 1))
        if leading_base3(n) == 2:
            assert not is_elated(n)
        if leading_base3(n) == 1 and leading_base3(t) == 2:
            assert not is_elated(n)
    for r in range(3, 51):
        B = 3 ** r
        k = (3 * B - 1) // 2
        M = k // 20
        low_mean = Fraction(5 * (k-M) - 2, 3)
        high_mean = Fraction(5 * k - 2, 3)
        assert low_mean >= Fraction(9*B, 4)
        assert high_mean <= Fraction(11*B, 4)
        assert k-1 < Fraction(3*B, 2)
        assert M >= 1
    print('VERIFY_OK parity_obstruction=10000 mean_bounds_r=3..50 Hoeffding_constant=192')
    for r in (3, 4, 5):
        B = 3 ** r
        k = (3 * B - 1) // 2
        M = k // 20
        print('r=%d B=%d k=%d M=%d upper_fraction_bound=%g' % (r, B, k, M, 3.0**(-M) + 2*exp(-B/192)))


if __name__ == '__main__':
    verify()
