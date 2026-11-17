#!/usr/bin/env python3
"""Independent exact-rational checks for continuous cube affine-projection constants.

Requires Python 3.9+; no third-party dependencies.
The universal theorems use analytic arguments given in RESULT.md.
"""
from fractions import Fraction as F
from math import comb, factorial, sqrt, pi


def formula(d):
    assert d >= 1
    return 1 + F(2, 6**d * factorial(d+1)) * sum(
        (-1)**k * comb(d, k) * (3*d-1-6*k)**(d+1)
        for k in range((3*d-1)//6+1)
    )


def integral(d):
    """Exact independent B-spline density integration, including the sign kink."""
    threshold = F(3*d-1, 6)
    c = 3*d-1
    ans = F(0)
    for j in range(d):
        # Uniform[0,1] sum density, polynomial on (j,j+1).
        cuts = sorted({F(j), F(j+1)} |
                      ({threshold} if F(j)<threshold<F(j+1) else set()))
        for lo, hi in zip(cuts, cuts[1:]):
            sign = 1 if 6*(lo+hi)/2 - c > 0 else -1
            for k in range(j+1):
                coef = sign * (-1)**k * comb(d,k)
                def primitive(t):
                    z = t-k
                    return 6*z**(d+1)/F(d+1) + (6*k-c)*z**d/F(d)
                ans += coef*(primitive(hi)-primitive(lo))/factorial(d-1)
    return ans


def density_at_zero(d):
    # Exact Irwin-Hall density of the sum of d symmetric U[-1,1] variables.
    t=F(d,2)
    return F(1,2*factorial(d-1))*sum(
       (-1)**k * comb(d,k)*(t-k)**(d-1)
       for k in range((d-1)//2+1)
    )


def main():
    # Independent B-spline integration versus closed finite sum.
    for d in range(1, 19):
        a, b = formula(d), integral(d)
        assert a == b, (d,a,b)
        assert a > 1
        if d>1:
            assert a > formula(d-1)
    assert formula(1)==F(5,3)
    assert formula(2)==F(233,108)  # square / earlier two-dimensional result
    assert formula(3)==F(415,162)
    print('EXACT_BINOMIAL_FORMULA_AND_INDEPENDENT_SPLINE_INTEGRAL_OK 18 DIMENSIONS')
    print('LOW_DIMENSION_VALUES_OK', [str(formula(d)) for d in range(1,7)])

    # Density comparison across dimension: positive near the level zero.
    for d in range(2,19):
        assert density_at_zero(d)>0
    print('CENTER_DENSITIES_POSITIVE_OK')

    # The analytic proof gives 13/60 as the second asymptotic coefficient.
    # These values are numerical sanity checks only, not proof of asymptotics.
    for d in [20,40,80,120]:
        x=float(formula(d)); target=sqrt(6*d/pi)
        scaled=d*(x/target-1)
        assert abs(scaled-13/60)<0.015
        print('ASYMPTOTIC_CHECK',d, f'{scaled:.12f}')
    print('ALL_CUBE_AFFINE_PROJECTION_CHECKS_PASSED')

if __name__=='__main__': main()
