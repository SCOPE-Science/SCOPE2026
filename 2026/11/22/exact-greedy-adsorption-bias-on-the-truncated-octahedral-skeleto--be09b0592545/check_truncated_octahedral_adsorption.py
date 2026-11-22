"""Exact enumeration of random greedy monomer occupancy on the truncated octahedral 1-skeleton.
All calculations use Python standard library and rational arithmetic.
"""
from itertools import permutations, product
from functools import lru_cache
from fractions import Fraction
from collections import Counter, defaultdict

V = sorted(set(tuple(0 if x == 0 else s*x for x,s in zip(t,signs))
               for t in set(permutations((0,1,2)))
               for signs in product((-1,1), repeat=3)))
n=len(V)
assert n==24
neigh=[sum(1<<j for j,y in enumerate(V)
           if sum((x[k]-y[k])**2 for k in range(3))==2)
       for x in V]
assert all(m.bit_count()==3 for m in neigh)
assert sum(x.bit_count() for x in neigh)==72
assert all(bool(neigh[i] & (1<<j))==bool(neigh[j] & (1<<i))
           for i in range(n) for j in range(n))
ALL=(1<<n)-1

# Exact total-probability recursion, conditioning on the first inspected vertex.
@lru_cache(None)
def jam(mask):
    if not mask:
        return (Fraction(1),)
    out=defaultdict(Fraction)
    m=mask
    while m:
        bit=m&-m; m-=bit
        i=bit.bit_length()-1
        child=jam(mask & ~(bit|neigh[i]))
        for k,p in enumerate(child):
            out[k+1]+=p/mask.bit_count()
    return tuple(out[j] for j in range(max(out)+1))

# Independent depth-first enumeration of all independent dominating sets,
# i.e. all maximal independent sets. This has no probability recursion.
maximal=Counter()
def enum(remaining,selected,dominated):
    if remaining==0:
        if dominated==ALL:
            maximal[selected.bit_count()]+=1
        return
    bit=remaining & -remaining
    i=bit.bit_length()-1
    enum(remaining ^ bit,selected,dominated)
    enum(remaining & ~(bit|neigh[i]),selected|bit,dominated|bit|neigh[i])
enum(ALL,0,0)

P={k:p for k,p in enumerate(jam(ALL)) if p}
assert P=={
 8: Fraction(7666301,62208000),
 9: Fraction(926336912,1915538625),
 10: Fraction(51963221287,178319232000),
 12: Fraction(57033471421,560431872000)}
assert maximal=={8:117,9:208,10:36,12:2}
assert sum(P.values())==1 and sum(maximal.values())==363
assert sum(k*p for k,p in P.items())==Fraction(1161395055131,122594472000)
Q={k:Fraction(c,363) for k,c in maximal.items()}
for t in (9,10,12):
    assert sum((p for k,p in P.items() if k>=t),Fraction(0)) > sum((p for k,p in Q.items() if k>=t),Fraction(0))
assert Fraction(P[12],Q[12])==Fraction(627368185631,33965568000)
print('PASS: graph=24 vertices, 36 edges; exact terminal distribution',sorted(P.items()))
print('PASS: 363 maximal independent sets',sorted(maximal.items()))
print('PASS: greedy jamming stochastically dominates uniform maximal-set size')
print('PASS: perfect packing probability amplification',P[12]/Q[12])
print('cache',jam.cache_info())
