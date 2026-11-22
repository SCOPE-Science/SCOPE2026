#!/usr/bin/env python3
"""Finite exact checks for chain-polytope difference-body radius and contacts.
Runs under Python 3.9+ with no dependencies. This is not an infinite proof.
"""
from itertools import combinations, product

def orders(n):
    pairs = [(i, j) for i in range(n) for j in range(i+1, n)]
    seen = set()
    for flags in range(1 << len(pairs)):
        reach = [0]*n
        for k, (i, j) in enumerate(pairs):
            if flags >> k & 1: reach[i] |= 1 << j
        for k in reversed(range(n)):
            for i in range(k):
                if reach[i] >> k & 1: reach[i] |= reach[k]
        key=tuple(reach)
        if key not in seen:
            seen.add(key)
            yield key

def antichains(r):
    n=len(r)
    return [m for m in range(1<<n) if all(not (m>>i&1 and m>>j&1) for i in range(n) for j in range(i+1,n) if (r[i]>>j)&1)]

def chains(r):
    n=len(r)
    return [m for m in range(1,1<<n) if all((r[i]>>j)&1 for i in range(n) for j in range(i+1,n) if m>>i&1 and m>>j&1)]

def contact_from_pairs(ants,n):
    points=set()
    for a in ants:
        for b in ants:
            points.add(tuple((a>>i&1)-(b>>i&1) for i in range(n)))
    return points

def direct_signed_chain_points(r,n):
    cm=chains(r)
    return {x for x in product((-1,0,1),repeat=n) if all(abs(sum(x[i] for i in range(n) if m>>i&1))<=1 for m in cm)}

def test():
    posets = checked = total_contacts = 0
    byn={}
    for n in range(1,6):
        count=0
        for r in orders(n):
            ants=antichains(r)
            points=contact_from_pairs(ants,n)
            direct=direct_signed_chain_points(r,n)
            assert points == direct, (n,r,'signed chain integer points')
            # independent two-family census
            w2=max((a|b).bit_count() for a in ants for b in ants if not a&b)
            R2=max(sum(v*v for v in p) for p in points)
            assert R2==w2,(n,r,R2,w2)
            A={p for p in points if sum(v*v for v in p)==R2}
            B=set()
            for a in ants:
                for b in ants:
                    if a&b==0 and (a|b).bit_count()==w2:
                        B.add(tuple((a>>i&1)-(b>>i&1) for i in range(n)))
            assert A==B and all(tuple(-z for z in p) in A for p in A)
            total_contacts+=len(A)
            count+=1
            checked+=len(points)
        byn[n]=count
        posets+=count
    print('POSSET_DIFFERENCE_BODY_PASS', 'posets=',posets,'n_profiles=',byn,'integer_points=',checked,'total_contact_occurrences=',total_contacts)

if __name__=='__main__': test()
