#!/usr/bin/env python3
"""Independent exact occupancy computation and birthday-limit consistency checks."""
from math import comb, exp
from itertools import product
from collections import Counter


def exact_unique(n, q):
    # Choose the strict winner color, its number r of votes and the
    # remaining q-1 capped color classes. Integer arithmetic only.
    ans=0
    for r in range(1,n+1):
        counts=[1]+[0]*n
        for color in range(q-1):
            nxt=[0]*(n+1)
            for used in range(n+1):
                if not counts[used]: continue
                for c in range(min(r-1,n-used)+1):
                    nxt[used+c]+=counts[used]*comb(used+c,c)
            counts=nxt
        ans+=comb(n,r)*counts[n-r]
    return q*ans


def enumerate_unique(n, q):
    count=0
    for word in product(range(q),repeat=n):
        freq=Counter(word)
        if list(freq.values()).count(max(freq.values()))==1:
            count+=1
    return count


def birthday_approx(n, q):
    lam=n*(n-1)/(2*q)
    return lam*exp(-lam)


def one_pair_exact(n,q):
    if q<n-1: return 0.0
    acc=comb(n,2)/q**(n-1)
    for j in range(n-2): acc*=q-1-j
    return acc

if __name__=='__main__':
    for q in range(2,7):
        for n in range(1,7):
            got=exact_unique(n,q)
            expect=enumerate_unique(n,q)
            assert got==expect,(q,n,got,expect)
    print('INDEPENDENT OCCUPANCY FORMULA VERIFIED for q=2..6, n=1..6')
    for n,q in [(20,200),(40,800),(60,1800),(80,3200)]:
        # Exact one-pair probability differs from unique winner only
        # through events with at least one triple collision.
        lower=one_pair_exact(n,q)
        theoretical_error=comb(n,3)/q**2
        prediction=birthday_approx(n,q)
        assert abs(prediction-lower)<.045
        print('n=%d q=%d lambda=%.6f one_pair=%.9f Poisson=%.9f triple_union_bound=%.9f'%
              (n,q,n*(n-1)/(2*q),lower,prediction,theoretical_error))
    print('ALL OCCUPANCY CHECKS PASSED')
