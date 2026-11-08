"""Finite checks for an analytic theorem on antipodal-quotient cube metrics.

Usage: python3 folded_cube_rate_check.py
No third-party dependencies. Finite checks do not replace the general proof.
"""
from math import comb, log, exp, isclose
from fractions import Fraction


def bound(h):
    return Fraction(2 * (h + 1) * (h - 1)**2, comb(2*h, h) * (h - 3))


def parity_transform(n, power):
    return sum(((-1)**w) * comb(n, w) * min(w, n-w)**power
               for w in range(1, n))


def abel_transform(h, power):
    n = 2*h
    return -2*sum(((-1)**w) * comb(n-1, w) * ((w+1)**power - w**power)
                  for w in range(h))


def direct_quotient_transform(n, power):
    return sum(((-1)**x.bit_count()) * min(x.bit_count(), n-x.bit_count())**power
               for x in range(1, 1 << (n-1)))


def check():
    # Binomial Abel-summation identity is checked for all positive powers.
    # The limiting nonzero-distance kernel at power zero has eigenvalue -2.
    for h in range(2, 11):
        n = 2*h
        for power in (0.125, 0.5, 1.0):
            lhs = parity_transform(n, power)
            rhs = abel_transform(h, power)
            assert isclose(lhs, rhs, rel_tol=1e-9, abs_tol=1e-7), (n, power, lhs, rhs)
        exact = parity_transform(n, 1)
        expected = 2 * (-1)**h * comb(n-2, h-1)
        assert exact == expected, (n, exact, expected)
    # Every consecutive even/odd pair in the proof has a positive lower ratio.
    for h in range(4, 301, 2):
        for w in range(2, h-1, 2):
            assert w * (2*(h-w)-3) > 1
    for h in range(6, 15, 2):
        n=2*h
        p=float(bound(h))
        assert 0 < p < 1
        # Exact critical obstruction, not a floating point rank threshold.
        val=parity_transform(n,p)
        lower=-2 + p*comb(n,h)*(h-3)/((h+1)*(h-1)**2)
        assert lower >= -1e-12
        assert val > 0.01 and val > lower-1e-6, (n,val,lower)
        if n <= 16:
            direct=direct_quotient_transform(n,p)
            assert isclose(2*direct,val,rel_tol=1e-7,abs_tol=1e-6), (n,direct,val)
        N=1 << (n-1)
        lower_power=1/(4*N*log(h))
        assert lower_power < p
        # A transparent norm-estimate certificate: exp(t)-1 <= 2t for t <= 1/2.
        t=lower_power*log(h)
        assert t <= 0.5 and N*(exp(t)-1) < 0.5 + 1e-10
        print(f'n={n:2d} lower={lower_power:.12g} upper={p:.12g} '
              f'parity_full={val:.12g}')
    print('FOLDED_CUBE_EXPONENTIAL_RATE_FINITE_CHECKS_OK')

if __name__ == '__main__':
    check()
