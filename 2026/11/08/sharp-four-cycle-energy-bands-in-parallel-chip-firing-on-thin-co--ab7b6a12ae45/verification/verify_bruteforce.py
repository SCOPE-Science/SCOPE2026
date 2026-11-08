"""Exhaustive labelled-state check of primitive four-cycles on K_{2,b}.
Run: python3 verify_bruteforce.py . Uses the invariant 0 <= chips(v) < 2 degree(v)
for each vertex on a nontrivial periodic orbit (Jiang 2010).
"""
from itertools import product
from collections import Counter
from math import comb

def update(state,b):
    u,v,*right=state
    fu=int(u>=b); fv=int(v>=b)
    nr=sum(x>=2 for x in right)
    return (u+nr-b*fu,v+nr-b*fv,*(x+fu+fv-2*(x>=2) for x in right))

def prediction(b):
    C=Counter()
    for r in range(1,b):
        for i in range(r):
            for j in range(b-r):
                C[2*b+i+j] += 4*comb(b,r)
                C[(7*b-2)-(2*b+i+j)] += 4*comb(b,r)
    return C

for b in range(2,8):
    measured=Counter()
    totalstates=0
    for xy in product(range(2*b),repeat=2):
        for y in product(range(4),repeat=b):
            z=(*xy,*y); a=update(z,b); c=update(a,b); d=update(c,b); e=update(d,b)
            if e==z and c!=z:
                measured[sum(z)]+=1
            totalstates+=1
    expected=prediction(b)
    assert measured==expected,(b,measured,expected)
    assert sum(measured.values())==(2**(b+1))*b*(b-1)
    assert min(measured)==2*b and max(measured)==5*b-2
    print(f'b={b} states={totalstates} primitive_four={sum(measured.values())} masses={sorted(measured.items())}')
print('BRUTE_FORCE_OK')
