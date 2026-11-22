#!/usr/bin/env python3
"""Pure standard-library exhaustive nonisomorphic connected cubic bipartite census through 12 vertices."""
from itertools import combinations,combinations_with_replacement,permutations
from collections import deque

# All row multisets enumerate arbitrary bipartite graphs after ordering the left shore.
def connected(rows,m):
    seen={0}; q=deque([0])
    while q:
        v=q.popleft()
        if v<m: adj=[m+j for j in range(m) if rows[v]&(1<<j)]
        else: adj=[i for i in range(m) if rows[i]&(1<<(v-m))]
        for w in adj:
            if w not in seen:seen.add(w);q.append(w)
    return len(seen)==2*m

def relabel(rows,m,p):
    return tuple(sorted(sum(((r>>p[j])&1)<<j for j in range(m)) for r in rows))

def canonical(rows,m):
    # Swap bipartition shores and/or permute one shore; the other side can be sorted.
    trans=tuple(sum(((r>>j)&1)<<i for i,r in enumerate(rows)) for j in range(m))
    return min(relabel(a,m,p) for a in (rows,trans) for p in permutations(range(m)))

def graph6(rows,m):
    n=2*m
    neighbors=[set() for _ in range(n)]
    for i,r in enumerate(rows):
        for j in range(m):
            if r&(1<<j):neighbors[i].add(m+j);neighbors[m+j].add(i)
    bits=[int(i in neighbors[j]) for j in range(1,n) for i in range(j)]
    bits.extend([0]*((-len(bits))%6))
    return chr(n+63)+''.join(chr(63+sum(bit<<(5-k) for k,bit in enumerate(bits[t:t+6]))) for t in range(0,len(bits),6))

def run():
    for m in range(3,7):
        supports=[sum(1<<j for j in c) for c in combinations(range(m),3)]
        uniques={}; raw=0
        for rows in combinations_with_replacement(supports,m):
            if any(sum((r>>j)&1 for r in rows)!=3 for j in range(m)) or not connected(rows,m):continue
            raw+=1; c=canonical(rows,m)
            uniques[c]=c
        print('order',2*m,'connected sorted matrices',raw,'nonisomorphic',len(uniques))
        for c in sorted(uniques):print(' ',graph6(c,m))
if __name__=='__main__':run()
