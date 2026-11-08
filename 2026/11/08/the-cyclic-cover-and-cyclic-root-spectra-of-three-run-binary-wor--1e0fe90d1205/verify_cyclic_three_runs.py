#!/usr/bin/env python3
"""Definition-driven cyclic occurrence enumeration against a closed-form spectrum."""
from itertools import product
import random

def direct(s):
    n=len(s)
    lengths=[]; factor_counts={}; roots=[]
    for ell in range(1,n+1):
        pat=s[:ell]
        rots={pat[t:]+pat[:t] for t in range(ell)}
        starts=[j for j in range(n-ell+1) if s[j:j+ell] in rots]
        mask=0
        for j in starts:
            mask |= ((1<<ell)-1)<<j
        if mask==(1<<n)-1:
            lengths.append(ell)
            factor_counts[ell]=len({s[j:j+ell] for j in starts})
        if n%ell==0 and all(s[j:j+ell] in rots for j in range(0,n,ell)):
            roots.append(ell)
    return lengths, factor_counts, roots

def predicted(a,b,c):
    n=a+b+c
    if a==c:
        ell0=a+(b+1)//2
    else:
        ell0=b+max(a,c)
    lengths=list(range(ell0,n+1))
    counts={}
    for ell in lengths:
        if a==c and ell<a+b:
            counts[ell]=2
        else:
            counts[ell]=n-ell+1
    roots=[n//2,n] if (a==c and b%2==0) else [n]
    total=(min(a,c)+1)*(min(a,c)+2)//2
    if a==c:
        total+=2*(b//2)
    assert sum(counts.values())==total
    return lengths,counts,roots

def run():
    cases=0;compared=0
    for a,b,c in product(range(1,11), repeat=3):
        x='0'*a+'1'*b+'0'*c
        got=direct(x); want=predicted(a,b,c)
        assert got==want,(a,b,c,got,want)
        cases+=1;compared+=len(x)
    rng=random.Random(521972)
    for z in range(250):
        a,b,c=(rng.randrange(1,26) for _ in range(3))
        x='0'*a+'1'*b+'0'*c
        got=direct(x); want=predicted(a,b,c)
        assert got==want,(a,b,c,got,want)
        cases+=1;compared+=len(x)
    print(f'PASS: {cases} nontrivial run triples; {compared} full-length cyclic-cover, factor-count, and root tests.')
    for p in ((2,3,2),(2,3,3),(3,8,3),(3,8,4),(4,1,4)):
        print(p, predicted(*p))
if __name__=='__main__': run()
