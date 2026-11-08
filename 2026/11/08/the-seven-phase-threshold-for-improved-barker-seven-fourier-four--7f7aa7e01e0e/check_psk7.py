#!/usr/bin/env python3
"""Exact rational interval certificate for seven-symbol PSK autocorrelation energy.
No external packages.  Uses a complete phase-gauge-reduced enumeration.
"""
from fractions import Fraction as F
from math import factorial
from itertools import product

N=7
SCALE=10**15
# arctan(1/z) alternating-series bounds, 23/24 terms

def atan_partial(z, terms):
    return sum(((-1)**k*F(1,(2*k+1)*z**(2*k+1)) for k in range(terms)),F(0))
a5low,a5high=atan_partial(5,24),atan_partial(5,23)
a239low,a239high=atan_partial(239,24),atan_partial(239,23)
pi_low=16*a5low-4*a239high
pi_high=16*a5high-4*a239low
assert F(314159265358979323846,10**20)<pi_low<pi_high
assert F(314159265358979323847,10**20)>pi_high


def floor(x):return x.numerator//x.denominator

def ceil(x):return -floor(-x)

def cos_interval(q,j):
    if j==0:return SCALE,SCALE
    # direct cosine at rational lower endpoint of x; 0 <= x <= pi*2*(q-1)/q < 2pi
    x=F(314159265358979323846,10**20)*F(2*j,q)
    approx=sum(((-1)**k*x**(2*k)/factorial(2*k) for k in range(21)),F(0))
    # all derivatives of cos are bounded by 1: absolute Taylor error <= |x|^42/42!
    err=F(2*j,q)*(pi_high-F(314159265358979323846,10**20))+F(44,7)**42/factorial(42)
    return floor((approx-err)*SCALE),ceil((approx+err)*SCALE)


def profile(q,exponents):
    counts=[0]*q
    for k in range(1,N):
        differences=[(exponents[j+k]-exponents[j])%q for j in range(N-k)]
        for d in differences:
            for e in differences:
                counts[(d-e)%q]+=1
    assert sum(counts)==sum(k*k for k in range(1,N))==91
    assert all(counts[j]==counts[(-j)%q] for j in range(q))
    return tuple(counts)

# Minima claimed as normalized sequences, exact profile, and exact minimizer count.
EXPECTED={
    2:((0,0,0,1,1,0,1),1),
    3:((0,0,1,1,0,1,0),2),
    4:((0,0,0,2,2,0,2),1),
    5:((0,0,1,1,4,0,3),4),
    6:((0,0,0,3,3,0,3),1),
    7:((0,0,2,2,6,1,5),2),
}


def main():
    for q in range(2,8):
        intervals=[cos_interval(q,j) for j in range(q)]
        winner,claimed_count=EXPECTED[q]
        cp=profile(q,winner)
        best_low=sum(x*intervals[j][0] for j,x in enumerate(cp))
        best_high=sum(x*intervals[j][1] for j,x in enumerate(cp))
        equal=0
        n_checked=0
        second_low=None
        for tail in product(range(q),repeat=N-2):
            v=(0,0)+tail
            c=profile(q,v)
            n_checked+=1
            if c==cp:
                equal+=1
            else:
                low=sum(x*intervals[j][0] for j,x in enumerate(c))
                if second_low is None or low<second_low:second_low=low
                assert low>best_high, (q,v,c,cp,low,best_high)
        assert n_checked==q**5
        assert equal==claimed_count,(q,equal,claimed_count)
        print(f'q={q} candidates={n_checked} normalized_minimizers={equal} unnormalized_minimizers={equal*q*q} winner_profile={cp} best_interval=[{best_low},{best_high}]/10^15 next_lower={second_low}/10^15')
    print('SEVEN_PSK_EXACT_ENUMERATION_PASS')

if __name__=='__main__':main()
