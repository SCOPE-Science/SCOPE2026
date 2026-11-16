"""Exact arithmetic checks for palette-independent cycle and cactus Fourier spectra."""
from collections import Counter
from itertools import product
from math import factorial

def balanced_cycle_histogram(q,n):
    # Potential sequence is pinned at zero; this parametrizes balanced frequencies bijectively.
    hist = Counter()
    for tail in product(range(q), repeat=n-1):
        counts = Counter((0,)+tail)
        coefficient = (-1)**n * sum((1-q)**counts[a] for a in range(q))
        assert coefficient % q == 0
        hist[coefficient] += 1
    assert sum(hist.values()) == q**(n-1)
    return hist

def zero_formula(q,n):
    if n < q+1 or n % q != 1:
        return 0
    t = (n-1)//q
    return factorial(n)//(factorial(t+1)*factorial(t)**(q-1))

for q,ns in ((3,range(3,11)),(4,range(3,10)),(5,range(3,8)),(6,range(3,8))):
    for n in ns:
        h=balanced_cycle_histogram(q,n)
        assert h[0]==zero_formula(q,n),(q,n,h[0],zero_formula(q,n))
    print('cycle order',q,'all checked lengths',list(ns),'PASS')

def multiply(h,k):
    out=Counter()
    for a,x in h.items():
        for b,y in k.items(): out[a*b]+=x*y
    return out

def cactus_histogram(q,cycle_lengths,bridge_count=0):
    factors=Counter({1:1})
    for n in cycle_lengths:
        h=balanced_cycle_histogram(q,n)
        factors=multiply(factors,Counter({x//q:c for x,c in h.items()}))
    for _ in range(bridge_count): factors=multiply(factors,Counter({q-1:1,-1:q-1}))
    return Counter({q*x:c for x,c in factors.items()})

# The two graphs have respectively a triangle-square bouquet and a square-square bouquet.
for lengths,bridges in [([3,4],0),([4,4],0),([3,4],1)]:
    hist=cactus_histogram(4,lengths,bridges)
    vertices=1+sum(n-1 for n in lengths)+bridges
    assert sum(hist.values())==4**(vertices-1)
    assert hist[0]==0
    print('cactus lengths',lengths,'bridges',bridges,'balanced',sum(hist.values()),'support',sum(c for v,c in hist.items() if v!=0),'PASS')
