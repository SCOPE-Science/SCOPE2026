#!/usr/bin/env python3
"""Exact cyclotomic coefficient checks of the Fourier-block identities.

This program tests the derived block determinants independently of the
regular-convolution matrix checker. The infinite-prime proof is in RESULT.md.
"""
from collections import Counter
from itertools import combinations
from math import comb

def zero_in_prime_cyclotomic(p,terms):
    # Sum c_e zeta_p**e is zero iff all p reduced coefficients coincide.
    co=[0]*p
    for exponent,coefficient in terms:
        co[exponent%p]+=coefficient
    return len(set(co))==1

def check(p):
    roots=[t for t in range(2,p) if t*t*t%p==1 and t!=1]
    assert len(roots)==2
    t=roots[0]; H=(1,t,t*t%p)
    assert sum(H)%p==0
    assert len({s*h%p for s in (1,-1) for h in H})==6
    # Every three-element subset of the normal C_p coset has no Fourier zero.
    for u,v in combinations(range(1,p),2):
        for k in range(1,p):
            assert not zero_in_prime_cyclotomic(p,[(0,1),(k*u,1),(k*v,1)])
    # For mixed supports, the cyclic Fourier-block determinant is
    # 3 + sum_{h in H}(zeta^(khu)+zeta^(-khu)), never zero.
    for u in range(1,p):
        for k in range(1,p):
            terms=[(0,3)]+[(s*k*h*u,1) for h in H for s in (-1,1)]
            assert not zero_in_prime_cyclotomic(p,terms)
    # For 3-coset transversals, determinant is 3 - sum_H zeta^(k h d).
    for d in range(p):
        terms=[(0,3)]+[(k*h*d,-1) for h in H for k in (1,)]
        assert zero_in_prime_cyclotomic(p,terms)==(d==0)
    # Count the three coset-occupancy types directly.
    bins=Counter()
    for supp in combinations(range(3*p),3):
        parts=[x//p for x in supp]
        if len(set(parts))!=3:
            bins[3*p]+=1
        else:
            vals={x//p:x%p for x in supp}
            u=(vals[1]-vals[0])%p
            v=(vals[2]-vals[0])%p
            bins[p if (u+t*v)%p==0 else 3*p-2]+=1
    predicted={p:p*p,3*p-2:p*p*(p-1),3*p:p*(p-1)*(7*p-2)//2}
    assert dict(bins)==predicted,(p,bins,predicted)
    assert sum(bins.values())==comb(3*p,3)
    print('PASS p=%d t=%d cyclotomic_zero_tests=exact rank_counts=%s'%(p,t,dict(sorted(bins.items()))))

if __name__=='__main__':
    for p in (7,13,19,31):check(p)
