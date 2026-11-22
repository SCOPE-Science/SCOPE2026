#!/usr/bin/env python3
"""Exact and finite-check diagnostics for a coupled random-best-response model.

All assertions here are finite checks; the infinite-dimensional convergence
claim is established separately by the mathematical proof.
"""
from fractions import Fraction as F
from math import comb, factorial
from itertools import permutations, product
import random


def exact_common_argmax(k, q):
    q = F(q)
    a = F(0)
    for j in range(k):
        b = F(comb(k - 1, j)) * q**(k - 1 - j) * (1-q)**j
        a += b * (q / (k + j) + 2 * (1-q) / (k * (k+j+1)))
    return a


def enumerate_common_argmax(k):
    """For q=1/2 enumerate all orders of X_i, W_i and all retention flags."""
    good = 0
    tot = 0
    for ranks in permutations(range(2*k)):
        x, w = ranks[:k], ranks[k:]
        imax = max(range(k), key=lambda i: x[i])
        for retained in product((False, True), repeat=k):
            y = tuple(x[i] if retained[i] else w[i] for i in range(k))
            good += int(imax == max(range(k), key=lambda i: y[i]))
            tot += 1
    return F(good, tot)



def exhaustive_game_moments(m, n, q):
    """Exact enumeration of two paired best-response maps by exchangeability."""
    from itertools import product
    from collections import defaultdict
    a = m * exact_common_argmax(m, q)
    b = n * exact_common_argmax(n, q)
    ad = {(i,j): (exact_common_argmax(m,q) if i==j
                    else (1-a)/F(m*(m-1))) for i in range(m) for j in range(m)}
    bd = {(i,j): (exact_common_argmax(n,q) if i==j
                    else (1-b)/F(n*(n-1))) for i in range(n) for j in range(n)}
    sums=[F(0)]*4
    adkeys=list(ad)
    bdkeys=list(bd)
    for acol in product(adkeys, repeat=n):
        pa=F(1)
        for pair in acol:pa*=ad[pair]
        for brow in product(bdkeys, repeat=m):
            p=pa
            for pair in brow:p*=bd[pair]
            e0=sum(acol[j][0]==i and brow[i][0]==j for i in range(m) for j in range(n))
            e1=sum(acol[j][1]==i and brow[i][1]==j for i in range(m) for j in range(n))
            cc=sum(acol[j][0]==i and brow[i][0]==j and
                   acol[j][1]==i and brow[i][1]==j
                   for i in range(m) for j in range(n))
            sums[0]+=p
            sums[1]+=p*e0
            sums[2]+=p*cc
            sums[3]+=p*e0*e1
    return sums

def check():
    checks = 0
    for k in range(1, 20):
        assert exact_common_argmax(k,0) == F(1,k*k); checks+=1
        assert exact_common_argmax(k,1) == F(1,k); checks+=1
        for q in (F(1,4), F(1,2), F(3,4)):
            a=exact_common_argmax(k,q)
            assert F(1,k*k) <= a <= F(1,k); checks+=1
            assert a <= F(1,k); checks+=1
    for k in (1,2,3):
        observed=enumerate_common_argmax(k)
        expected=k*exact_common_argmax(k,F(1,2))
        assert observed == expected, (k, observed, expected);checks+=1
    for k in (10, 25, 100, 200, 500):
        # Exact rational formulas provide asymptotic diagnostics; no inference from this check.
        for q in (F(1,4),F(1,2),F(3,4)):
            p = float(k*exact_common_argmax(k,q))
            target = float(q/(2-q))
            assert abs(p-target) <= 2.5/k, (k,q,p,target);checks+=1
    for m,n in ((2,2),(2,3),(3,3),(3,5),(5,7)):
        for q in (F(0),F(1,4),F(1,2),F(1)):
            p_m,p_n=exact_common_argmax(m,q),exact_common_argmax(n,q)
            common = m*n*p_m*p_n
            old_only=1-common
            assert 0 <= old_only <= 1, (m,n,q); checks+=1
            # For q=0, two copies are independent; a prescribed cell is
            # equilibrium in both with probability 1/(m*n)^2.
            if q==0:
                assert common == F(1,m*n);checks+=1
            if q==1:
                assert common == 1;checks+=1
    for m,n in ((2,2),(2,3)):
        for q in (F(0),F(1,2),F(1)):
            total,mean,common,cross=exhaustive_game_moments(m,n,q)
            a=m*exact_common_argmax(m,q)
            b=n*exact_common_argmax(n,q)
            assert total == 1;checks+=1
            assert mean == 1;checks+=1
            assert common == a*b;checks+=1
            assert cross-1 == (a-F(1,m))*(b-F(1,n));checks+=1
    print('Passed',checks,'exact/finite assertions')
    print('q=1/2: limiting shared equilibrium rate',float((F(1,2)/(2-F(1,2)))**2))
    print('q=1/2: finite 25x25 shared mean',float(25**2*exact_common_argmax(25,F(1,2))**2))
    print('q=1/2: finite 100x100 shared mean',float(100**2*exact_common_argmax(100,F(1,2))**2))

if __name__=='__main__':check()
