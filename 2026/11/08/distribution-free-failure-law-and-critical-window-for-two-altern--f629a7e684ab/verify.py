#!/usr/bin/env python3
"""Independent exact checks of the random-threshold two-alternative lottery law."""
from itertools import product
from collections import Counter
from fractions import Fraction
from math import comb

def direct_violation(signs):
    # Ordered, distinct thresholds t_j=(j+1)/(n+1); test all open cells.
    n = len(signs)
    return min(sum(1 for i, s in enumerate(signs) if (i < j and s == -1) or (i >= j and s == 1)) for j in range(n+1))

def reflection_count(n, plus, k):
    if plus < k or plus > n-k:
        return 0
    return comb(n,plus)-comb(n,k-1)

def probability_tail(n,p,k):
    q=1-p
    return sum(Fraction(reflection_count(n,u,k))*p**u*q**(n-u) for u in range(n+1))

def run():
    patterns=0; tails=0; biases=0
    for n in range(1,17):
        by_u_v=Counter()
        for bits in product((-1,1),repeat=n):
            v=direct_violation(bits)
            by_u_v[(bits.count(1),v)] += 1
            patterns+=1
        for u in range(n+1):
            for k in range(1,n//2+2):
                observed=sum(c for (u2,v),c in by_u_v.items() if u2==u and v>=k)
                assert observed==reflection_count(n,u,k),(n,u,k,observed,reflection_count(n,u,k))
                tails+=1
        for p in map(Fraction,('1/4','2/5','1/2','3/4')):
            actual=sum(count*p**u*(1-p)**(n-u) for (u,v),count in by_u_v.items() if v==0)
            closed=sum(p**u*(1-p)**(n-u) for u in range(n+1))
            assert actual==closed,(n,p,actual,closed)
            if n<=10:
                for k in range(1,n//2+2):
                    actual=sum(count*p**u*(1-p)**(n-u) for (u,v),count in by_u_v.items() if v>=k)
                    assert actual==probability_tail(n,p,k),(n,p,k,actual,probability_tail(n,p,k))
                    biases+=1
    print('PASS exhaustive bit strings',patterns,'conditional tail checks',tails,'rational distribution checks',biases)
if __name__=='__main__':run()
