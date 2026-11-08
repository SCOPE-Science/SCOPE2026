#!/usr/bin/env python3
"""Independent finite verification of optimal palindromic-cut multiplicity.
Only uses Python standard library. No mathematical claim of infinite exhaustion.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations

@lru_cache(None)
def optimal(w):
    """Dynamic program returns minimum number of nonempty palindromic factors and number of minimizing cut tuples."""
    n=len(w)
    score=[n+1]*(n+1); multiplicity=[0]*(n+1)
    score[0]=0; multiplicity[0]=1
    for j in range(1,n+1):
        for i in range(j):
            piece=w[i:j]
            if piece!=piece[::-1]:
                continue
            t=score[i]+1
            if t<score[j]: score[j]=t; multiplicity[j]=multiplicity[i]
            elif t==score[j]: multiplicity[j]+=multiplicity[i]
    return score[n],multiplicity[n]

def direct_count_four(w):
    """Independent brute-force cut triples, not using the DP recurrence."""
    n=len(w); k=0
    for i,j,h in combinations(range(1,n),3):
        pieces=(w[:i],w[i:j],w[j:h],w[h:])
        if all(p==p[::-1] for p in pieces): k+=1
    return k

def condition(a,b,c,d):
    return b!=c and min(a,d)>max(b,c)

def coeff_from_rational(n):
    # H(z,1)=2*z^8 / ((1-z)^2*(1-z^3)*(1-z^4))
    k=n-8; count=0
    if k>=0:
        for u in range(k//3+1):
            for v in range((k-3*u)//4+1):
                count+=2*(k-3*u-4*v+1)
    return count

def coeff_from_bivariate(n):
    # H(z,y)=2*z^8*y^3 / ((1-z)^2*(1-z^3*y)*(1-z^4*y^2))
    k=n-8; out=defaultdict(int)
    if k>=0:
        for u in range(k//3+1):
            for v in range((k-3*u)//4+1):
                out[3+u+2*v]+=2*(k-3*u-4*v+1)
    return dict(out)

if __name__=='__main__':
    tested=0; four_direct=0
    for n in range(3,25):
        observed=defaultdict(int)
        for p,q,r in combinations(range(n),3):
            a=p; b=q-p-1; c=r-q-1; d=n-r-1
            w='0'*a+'1'+'0'*b+'1'+'0'*c+'1'+'0'*d
            pl,k=optimal(w)
            expect=condition(a,b,c,d)
            assert (pl==4)==expect,(n,(a,b,c,d),pl)
            if expect:
                assert k==b+c+2,(w,k,b+c+2)
                if n<=18:
                    assert direct_count_four(w)==k,(w,k,direct_count_four(w))
                    four_direct+=1
                observed[k]+=1
            tested+=1
        assert sum(observed.values())==coeff_from_rational(n),(n,observed)
        assert dict(observed)==coeff_from_bivariate(n),(n,observed,coeff_from_bivariate(n))
    # Longer coefficient tests use two independently parameterized summations.
    for n in range(25,101):
        counts=defaultdict(int)
        for h in range(1,(n-5)//3+1):
            for l in range(h):
                outer_sum=n-3-h-l
                # a,d>=h+1. If possible, # ordered positive-offset pairs is
                # n-3-h-l-2*(h+1)+1 = n-4-3h-l
                placements=outer_sum-2*(h+1)+1
                if placements>0: counts[h+l+2]+=2*placements
        assert dict(counts)==coeff_from_bivariate(n),(n,counts,coeff_from_bivariate(n))
    print(f'VERIFY_OK words={tested} direct_four_cut_checks={four_direct} bivariate_lengths=3..100')

# Analytic checks on the two branches of the limiting density:
# f(t) = 36*t - 90*t*t, 0<=t<=1/3;
# f(t) = 18*(1-2*t)**2, 1/3<t<=1/2.
# Each moment uses exact rational polynomial integration.
from fractions import Fraction

def definite_integral_poly(coeffs, low, high):
    return sum(Fraction(c,j+1)*(high**(j+1)-low**(j+1)) for j,c in enumerate(coeffs))

f1=[0,36,-90]
f2=[18,-72,72]
for j,expect in [(0,Fraction(1)),(1,Fraction(5,24)),(2,Fraction(19,360))]:
    mass=definite_integral_poly([Fraction(0)]*j+f1,Fraction(0),Fraction(1,3)) + definite_integral_poly([Fraction(0)]*j+f2,Fraction(1,3),Fraction(1,2))
    assert mass==expect,(j,mass,expect)
assert Fraction(19,360)-Fraction(5,24)**2==Fraction(3,320)
for n in range(8,101):
    observed=coeff_from_bivariate(n)
    assert set(observed)=={k for k in range(3,n+1) if (2*k+2 if k%2 else 2*k+3)<=n},(n,set(observed))
print('MOMENT_AND_SHARP_SPECTRUM_OK')
