#!/usr/bin/env python3
"""Exact low-order and deterministic nine-state subset-BFS cross-check."""
from collections import deque
from itertools import product
from random import Random
from math import comb, factorial

def rank(b): return len(set(b))

def subset_bfs(b):
    n=len(b)
    full=(1<<n)-1
    q=deque([full]); seen={full}
    while q:
        s=q.popleft()
        if not s & (s-1): return True
        nxt_a=nxt_b=0
        for i in range(n):
            if s >> i & 1:
                nxt_a |= 1<<((i+1)%n)
                nxt_b |= 1<<b[i]
        for t in (nxt_a,nxt_b):
            if t not in seen:
                seen.add(t); q.append(t)
    return False

def orbital_distance_bfs(b):
    n=len(b); k=n//2
    edges=[set() for _ in range(k+1)]
    for d in range(1,k+1):
        for i in range(n):
            t=abs(b[i]-b[(i+d)%n]); edges[d].add(min(t,n-t))
    yes={0}
    while True:
        extra={d for d in range(1,k+1) if edges[d]&yes}
        if extra <= yes: return len(yes)==k+1
        yes |= extra

def main():
    for n in (4,5,6):
        count=0
        for b in product(range(n), repeat=n):
            if rank(b)!=n-2: continue
            assert subset_bfs(b)==orbital_distance_bfs(b)
            count += 1
        print(f'n={n}: independent subset-vs-distance exact comparisons: {count}')
    rng=Random(1729)
    successes=failures=0
    # Positive cases sampled from the full rank-seven population.
    while successes<1500:
        n=9; positions=list(range(n)); rng.shuffle(positions)
        if rng.randrange(2): groups=[positions[:3]]+[[i] for i in positions[3:]]
        else: groups=[positions[:2],positions[2:4]]+[[i] for i in positions[4:]]
        values=rng.sample(range(n),7); b=[0]*n
        for value,g in zip(values,groups):
            for pos in g:b[pos]=value
        assert rank(b)==7
        x=subset_bfs(b)
        assert x==orbital_distance_bfs(b)
        if x:successes+=1
    # Negative cases sampled directly from rank-seven maps preserving mod three.
    while failures<1500:
        b=[0]*9
        permutation=rng.sample(range(3),3)
        profile=rng.choice([(1,3,3),(3,1,3),(3,3,1),(2,2,3),(2,3,2),(3,2,2)])
        for r in range(3):
            available=[permutation[r]+3*k for k in range(3)]
            while True:
                assigned=[rng.choice(available) for _ in range(3)]
                if len(set(assigned))==profile[r]:break
            for k in range(3):b[r+3*k]=assigned[k]
        assert rank(b)==7
        x=subset_bfs(b)
        assert not x
        assert x==orbital_distance_bfs(b)
        failures+=1
    print(f'n=9: direct subset-BFS checks: synchronizing={successes}; nonsynchronizing={failures}')
    f1,f2,f3=3,18,6
    nonsync=factorial(3)*(3*f1*f3**2+3*f2**2*f3)
    total=comb(9,7)*factorial(7)*(comb(9,3)+3*comb(9,4))
    assert (nonsync,total)==(36936,83825280)
    print(f'independent exact counts by residue-class maps: nonsynchronizing={nonsync}; all rank seven maps={total}')
if __name__=='__main__': main()
