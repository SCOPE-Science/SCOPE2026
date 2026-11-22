#!/usr/bin/env python3
"""Supplementary exact-rational checks for the two-essential-resource patch allocation law.

The infinite-dimensional quantifiers and no-other-maximizers conclusion follow
from the analytic proof, not from these finite experiments.
"""
from fractions import Fraction as F
from math import sqrt
from itertools import product


def phi(x):
    return x / (1 + x)


def g(x):
    return phi(x)**2


def dg(x):
    return 2 * x / (1+x)**3


def merit(T, k):
    return T * T * k / (T + k)**2


def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for first in range(total+1):
            for rem in compositions(total-first, length-1):
                yield (first,)+rem


def verify():
    count = 0
    for a in range(0, 13):
        for b in range(0, 13):
            x,y = F(a,5), F(b,7)
            assert g(x)+g(y)-2*phi(x)*phi(y)==(phi(x)-phi(y))**2
            lhs=dg(x)-dg(y)
            rhs=2*(x-y)*(1-x*y*(3+x+y))/((1+x)**3*(1+y)**3)
            assert lhs==rhs
            count+=2
    for n in range(2, 6):
        for p in range(1,31):
            T=F(p,7)
            # The exact formulas compare without rounding of threshold radicals.
            scores=[merit(T,k) for k in range(1,n+1)]
            for k in range(1,n):
                d=scores[k]-scores[k-1]
                e=T*T-F(k*(k+1))
                assert (d>0)==(e>0)
                assert (d==0)==(e==0)
                assert (d<0)==(e<0)
                count+=3
            winners=[k for k,v in enumerate(scores,1) if v==max(scores)]
            assert all(k == 1 or T*T >= (k-1)*k for k in winners)
            assert all(k == n or T*T <= k*(k+1) for k in winners)
            count+=2
    # Exhaustive finite-mesh checks for two independently distributed budgets,
    # including allocations with different supports or mismatched locations.
    for n in (2,3,4):
        for total in (1,2,3,4,5,6,7,8):
            C=list(compositions(total,n))
            T=F(total,3)
            theoretical=max(merit(T,k) for k in range(1,n+1))
            best=-1
            for one in C:
                c=[F(v,3) for v in one]
                for two in C:
                    q=[F(v,3) for v in two]
                    gain=sum(phi(x)*phi(y) for x,y in zip(c,q))
                    assert gain <= theoretical
                    best=max(best,gain)
                    count+=1
            # Mesh attains the continuum max only when an optimal support k
            # divides this integer mesh evenly; the upper bound is still exact.
            assert best <= theoretical
            count+=1
    # Exact small examples: n=3 and budgets 1,2,3.
    assert merit(F(1),1)==F(1,4)
    assert merit(F(2),2)==F(1,2)
    assert merit(F(3),3)==F(3,4)
    count+=3
    for k in range(1,20):
        T=sqrt(k*(k+1))
        assert abs((T*T*k/(T+k)**2)-(T*T*(k+1)/(T+k+1)**2))<1e-12
        count+=1
    return count

if __name__=='__main__':
    print('PASS: %d supplementary assertions (rational except stated sqrt checks)' % verify())
