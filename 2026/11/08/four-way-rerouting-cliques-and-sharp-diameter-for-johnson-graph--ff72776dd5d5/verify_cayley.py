#!/usr/bin/env python3
"""Independent adjacent-transposition Cayley graph and constructive comparator checks."""
from itertools import permutations
from collections import deque,Counter
from math import factorial,comb
from random import Random

def involution(p,j):
    q=list(p);q[j],q[j+1]=q[j+1],q[j];return tuple(q)

for n in range(1,6):
    perms=list(permutations(range(n)))
    P=len(perms); pos={p:i for i,p in enumerate(perms)}
    moves=[[pos[involution(p,j)] for j in range(n-1)] for p in perms]
    # Group action makes BFS from identity representative exhaustive for eccentricity.
    source=pos[tuple(range(n))]*(P+1)
    seen={source:0}; q=deque([source])
    while q:
      z=q.popleft();a,b=divmod(z,P)
      for j in range(n-1):
        aa=moves[a][j];bb=moves[b][j]
        for nxt in (aa*P+b, a*P+bb, aa*P+bb):
          if nxt not in seen:seen[nxt]=seen[z]+1;q.append(nxt)
    assert len(seen)==P*P
    assert max(seen.values())==comb(n,2)
    # This independent graph uses coordinate swaps alone, not full Johnson sets.
    print('CAYLEY_PASS n=%d states=%d degree=%d eccentricity=%d'%(n,P*P,3*(n-1),max(seen.values())))

r=Random(314159)
for n in range(2,11):
    L=comb(n,2)
    for trial in range(400):
        a=list(range(n));b=list(range(n));r.shuffle(a);r.shuffle(b)
        steps=0
        for stop in range(n-1,0,-1):
            for j in range(stop):
                x,y=a[j]>a[j+1],b[j]>b[j+1]
                if x:a[j],a[j+1]=a[j+1],a[j]
                if y:b[j],b[j+1]=b[j+1],b[j]
                steps+=bool(x or y)
        assert a==list(range(n)) and b==list(range(n)) and steps<=L
    print('COMPARATOR_PASS n=%d trials=400 upper_bound=%d'%(n,L))
print('CAYLEY_ALL_PASS')
