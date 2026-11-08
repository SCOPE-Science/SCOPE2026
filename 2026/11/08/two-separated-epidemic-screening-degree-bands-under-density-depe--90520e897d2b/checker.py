#!/usr/bin/env python3
"""Exact checks for a two-band SIS metapopulation degree-screening theorem.

Only Python standard library is required. All threshold comparisons use
rational interval enclosures, never floating-point approximations.
"""
from fractions import Fraction as F


def icuberoot_floor(n: int) -> int:
    assert n >= 0
    lo, hi = 0, 1
    while hi**3 <= n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**3 <= n:
            lo = mid
        else:
            hi = mid
    return lo


def cube_interval(k: int, scale=10**12):
    a = icuberoot_floor(k*scale**3)
    lo, hi = F(a, scale), F(a+1, scale)
    assert lo**3 <= k < hi**3
    return lo, hi


def ratio_interval(k, c, A, mu=F(5), b=F(1)):
    lo, hi = cube_interval(k)
    def denominator(x):
        return mu+b*(x*x-c/(x**4))
    assert denominator(lo) > 0
    # Q(x) is strictly increasing: Q'(x)=b(2*x+4*c/x**5)>0.
    return A*lo/denominator(hi), A*hi/denominator(lo)


def G_interval(k, c):
    lo, hi = cube_interval(k)
    # G(k) = t^2+5c/t^4 with t=k^(1/3); outward rational bounds
    return lo*lo +5*c/hi**4, hi*hi +5*c/lo**4


def main():
    counter = 0
    H2 = sum((F(1, k*k) for k in range(3, 21)), F(0))
    H3 = sum((F(1, k**3) for k in range(3, 21)), F(0))
    c = 1/H2
    A = F(1250, 281)
    assert c == F(10838475198270720,3751881733704241)
    counter += 1
    assert F(2888,1000)<c<F(2889,1000)
    counter += 1
    # Uncorrelated annealed distribution: p(k) proportional to k^-3.
    assert sum((F(1,k**3)/H3 for k in range(3,21)),F(0))==1
    counter += 1
    for k in range(3, 21):
        p=F(1,k**3)/H3
        mean_degree=H2/H3
        p_same=k*p/mean_degree
        assert p_same == c/F(k*k) and 0<p_same<1
        counter += 1
    # Exact derivative sign for alpha=2, gamma=3:
    # for t=k^(1/3), R(t)=A*t/(5+t^2-c*t^-4)
    # R'(t)=A*(5-t^2-5c*t^-4)/(5+t^2-c*t^-4)^2.
    # G(k)=k^(2/3)+5c*k^(-4/3) has its single minimum at sqrt(10c).
    assert F(5)**3*4>135*c
    counter+=1
    assert 3*3<10*c<6*6
    counter+=1
    # First derivative zero in (3,4), second in (8,9).
    for k, sign in [(3,1),(4,-1),(8,-1),(9,1),(20,1)]:
        low, high = G_interval(k,c)
        if sign==1: assert low>5
        else: assert high<5
        counter+=1
    # Exactly two disconnected sets of integer degree classes satisfy R(k)>1.
    bands = {3} | set(range(5,14))
    margins=[]
    for k in range(3,21):
        lower, upper = ratio_interval(k,c,A)
        assert lower > 1 if k in bands else upper < 1, (k,lower,upper)
        margins.append((k,lower-1 if k in bands else 1-upper))
        counter+=1
    # Compare every one of the 18 scores to threshold by exact intervals.
    assert len(margins)==18 and min(v for _,v in margins)>0
    counter+=1
    # The spectral sufficient condition follows from a strictly positive
    # infected-block diagonal when any R(k)>1; no eigenvalue claimed here.
    # At k=3, the positive diagonal condition is equivalent to R(3)>1.
    low,hi = ratio_interval(3,c,A)
    assert low>1
    counter+=1
    print('PASS', counter, 'exact rational assertions')
    print('c =',c)
    print('certified integer degree bands: {3} and {5,...,13}')
    print('smallest certified threshold margin >', min(v for _,v in margins))


if __name__=='__main__':
    main()
