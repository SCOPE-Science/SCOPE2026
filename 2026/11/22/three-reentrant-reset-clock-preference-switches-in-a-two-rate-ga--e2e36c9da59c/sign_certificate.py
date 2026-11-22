"""Exact-rational sign certificate for the two-mode Gaussian reset-clock example.

Uses only the Python standard library. All comparisons are exact; no
floating-point arithmetic or numerical integration establishes a sign.
"""
from fractions import Fraction as Q
from math import factorial

# At age t, the two covariance ratios to the reset state are
# 2 - exp(-rate*t), for rates 1 and 10000.
RATES = (Q(1), Q(10000))
RESET_RATES = (Q(1), Q(5), Q(300), Q(30000))
# For every nonnegative z: E(exp(-n*lambda*T)) = z/(z+n).
# The nonnegative geometric-series remainder is bounded by 2^(-N-2).
N = 70

def mode_divergence(v):
    """Jeffreys divergence for one centered Gaussian variance mode."""
    return (Q(1, 2-v) - v)/2

def expectation_bounds(z):
    lower = -z / (2*(z+1))
    lower += sum((z/(z+n) if n else Q(1))/(Q(4)*2**n)
                 for n in range(N+1))
    return lower, lower+Q(1, 2**(N+2))

def expminus_bounds(p):
    assert p > 0
    if p <= 1:
        # Alternating-series bounds with decreasing term magnitudes.
        lower = sum((-p)**k/factorial(k) for k in range(22))
        upper = sum((-p)**k/factorial(k) for k in range(21))
    else:
        # log(1+x) <= x implies exp(-p) <= (1+p/20)^(-20).
        lower = Q(0)
        upper = (1+p/20)**(-20)
    assert Q(0) <= lower <= upper <= Q(1)
    return lower, upper

def signed_difference_interval(r):
    # D(r)=E[S(T)]-S(1/r); T is exponential with rate r.
    low, high = Q(0), Q(0)
    for lam in RATES:
        elo, ehi = expectation_bounds(r/lam)
        vlo, vhi = expminus_bounds(lam/r)
        # mode_divergence is decreasing in v on [0,1].
        low += elo-mode_divergence(vlo)
        high += ehi-mode_divergence(vhi)
    return low, high

def verify():
    expected = (-1,1,-1,1)
    for r, s in zip(RESET_RATES, expected):
        low, high = signed_difference_interval(r)
        assert (high<0) if s < 0 else (low>0)
        # Rational upper/lower inequalities are exact certificates.
        print(f'r={r}: sign={"negative" if s<0 else "positive"}; '
              f'interval=({float(low):+.12f}, {float(high):+.12f}); '
              f'exact bounds: {low.numerator}/{low.denominator} < D < '
              f'{high.numerator}/{high.denominator}')
    print('PASS: four alternating exact-rational signs; at least three positive roots by continuity.')

if __name__=='__main__':
    verify()
