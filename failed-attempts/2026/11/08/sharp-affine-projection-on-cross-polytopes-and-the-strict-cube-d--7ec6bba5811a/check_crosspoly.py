#!/usr/bin/env python3
"""Exact rational checks for uniform-volume affine projection on cross-polytopes."""
from fractions import Fraction
from math import comb, factorial


def integral_on_segment(a, b, coefficients):
    return sum(k * (b**(j+1)-a**(j+1)) / (j+1) for j,k in enumerate(coefficients))


def density_integral(d, a, b, multiplier):
    """Integrate d*(1-u)^(d-1)*multiplier(u) exactly on [a,b]."""
    density = [d * Fraction((-1)**k * comb(d-1,k)) for k in range(d)]
    product = [Fraction(0)] * (len(density) + len(multiplier) - 1)
    for i, x in enumerate(density):
        for j, y in enumerate(multiplier):
            product[i+j] += x*y
    return integral_on_segment(a, b, product)


def cross_formula(d):
    c = Fraction((d+1)*(d+2), 2)
    q = 1 - 1/c
    return 1 + c/Fraction(d+1)*q**(d+1)


def cross_direct(d):
    c = Fraction((d+1)*(d+2), 2)
    return 1 + density_integral(d, 1/c, Fraction(1), [-1,c])


def cube_formula(d):
    """Integrate the Irwin--Hall CDF of a sum of d uniforms on [0,1]."""
    a = Fraction(3*d-1, 6)
    out = Fraction(0)
    for k in range(int(a)+1):
        out += (-1)**k * comb(d,k) * (a-k)**(d+1)
    return 1 + Fraction(12, factorial(d+1))*out


def run():
    for d in range(1, 64):
        c = Fraction((d+1)*(d+2), 2)
        second = density_integral(d, Fraction(0), Fraction(1), [0,0,1])
        assert second == 1/c, (d,second)
        exact = cross_direct(d)
        assert exact == cross_formula(d), (d, exact, cross_formula(d))
        assert exact - 1 > Fraction(d, 2), d
        if d < 63:
            assert exact < cross_formula(d+1), d
        assert (exact-1)/2 == c/Fraction(2*(d+1))*(1-1/c)**(d+1)
    print('CROSS_POLYTOPE_BETA_AND_MONOTONICITY_IDENTITIES_PASSED 63 DIMENSIONS')
    for d in range(1, 9):
        cross = cross_direct(d)
        cube = cube_formula(d)
        if d <= 2:
            assert cross == cube, (d,cross,cube)
        else:
            assert cross > cube, (d,cross,cube)
        print(f'd={d} cross={cross} cube={cube} gap={cross-cube}')
    print('CUBE_CROSSPOLYTOPE_EXACT_LOW_DIMENSION_GAPS_PASSED')
    print('ALL_CROSSPOLY_AFFINE_CHECKS_PASSED')

if __name__ == '__main__':
    run()
