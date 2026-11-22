#!/usr/bin/env python3
"""Exact enumeration of all three-colour character sums for complete bipartite two-pole graphs.
No external dependencies. All arithmetic is integral, using coefficient counts of 1, omega, omega^2.
"""
from itertools import product
from collections import Counter
from math import comb
from random import Random


def proper_colours(n):
    for x in product(range(3), repeat=n+2):
        if all(x[2+j] != x[0] and x[2+j] != x[1] for j in range(n)):
            yield x


def formula(n, b):
    if sum(b) % 3 != 0:
        return 0
    z=sum(v==0 for v in b[2:])
    m=n-z
    s=sum(b[2:]) % 3
    exceptional=(b[0]==s and b[1]==s)
    return 3*((-1)**m * 2**z - 1 + 3*exceptional)


def exact_evaluation(b, colours):
    buckets=[0,0,0]
    for x in colours:
        buckets[sum(u*v for u,v in zip(x,b)) % 3] += 1
    assert buckets[1] == buckets[2], (b,buckets)
    return buckets[0] - buckets[1]


def spectral_prediction(n):
    d=Counter({0:2*3**(n+1)})
    for z in range(n+1):
        zcount=comb(n,z)*2**(n-z)
        t=(-1)**(n-z)*2**z
        d[3*(t-1)]+=2*zcount
        d[3*(t+2)]+=zcount
    return +d


def test():
    total=0
    for n in range(1,7):
        colours=list(proper_colours(n))
        assert len(colours)==3*(2**n+2)
        observed=Counter()
        for b in product(range(3),repeat=n+2):
            f=formula(n,b)
            if sum(b)%3==0:
                actual=exact_evaluation(b,colours)
                assert actual==f,(n,b,actual,f)
            else:
                # Global colour translations imply exact character cancellation.
                actual=0
            observed[actual]+=1
            total+=1
        assert observed==spectral_prediction(n),(n,observed,spectral_prediction(n))
        assert observed[0]==2*3**(n+1)+((n+4)*2**(n-1) if n%2==0 else 0)
        assert min(abs(v) for v in observed if v)!=0
        assert min(abs(v) for v in observed if v)==(3 if n%2 else 9)
        assert max(abs(v) for v in observed)==3*(2**n+2)
    rng=Random(712103)
    for n in (7,8,12,18):
        colours=list(proper_colours(n)) if n<=8 else None
        for _ in range(80):
            b=tuple(rng.randrange(3) for _ in range(n+2))
            if colours is not None and sum(b)%3==0:
                assert exact_evaluation(b,colours)==formula(n,b)
            else:
                assert formula(n,b)%3==0
        d=spectral_prediction(n)
        assert sum(d.values())==3**(n+2)
        assert d[0]==2*3**(n+1)+((n+4)*2**(n-1) if n%2==0 else 0)
    print(f'TERNARY_BICLIQUE_FOURIER_EXACT_PASS exhaustive_frequencies={total} random_tests=320')

if __name__=='__main__':
    test()
