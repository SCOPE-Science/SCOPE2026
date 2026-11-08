#!/usr/bin/env python3
"""Exact finite checks for the square-gap-root profile theorem.

Requires only the Python standard library.  Finite checks are not an
infinite proof; the analytic argument is given separately.
"""
import math
import cmath


def in_semigroup_bruteforce(m, z):
    return any((z - (m+1)*y) % m == 0 for y in range(z//(m+1)+1))


def gap_formula(m, j):
    q, r = divmod(j*j, m)
    return r > q


def count(m, a=0, b=None):
    if b is None: b=m
    return sum(gap_formula(m, j) for j in range(a, b))


def main():
    instances=0
    for m in range(2, 101):
        for j in range(0,m+2):
            assert gap_formula(m,j)==(not in_semigroup_bruteforce(m,j*j)), (m,j)
            instances+=1
    print('exact semigroup-membership comparisons:',instances)
    # Fourier/correlation bound on normalized quadratic point sets.
    gauss_checks=0
    for m in range(2,65):
        for r in (-3,-1,0,1,3):
            for s in (-3,-1,1,3):
                val=sum(cmath.exp((2j*math.pi/m)*(s*j*j+r*j)) for j in range(m))
                bound=m*math.gcd(2*s,m)
                assert abs(val)**2<=bound+1e-6, (m,r,s,val,bound)
                gauss_checks+=1
    print('Gauss-sum quadratic upper-bound comparisons:',gauss_checks)
    print('m, square_gaps, square_gaps/m, density_prediction')
    for m in (100, 200, 500, 1000, 2000, 5000, 10000, 50000, 100000):
        n=count(m)
        print(f'{m},{n},{n/m:.7f},0.6666667')
    print('all finite checks passed; infinite asymptotic comes from proof')

if __name__=='__main__': main()
