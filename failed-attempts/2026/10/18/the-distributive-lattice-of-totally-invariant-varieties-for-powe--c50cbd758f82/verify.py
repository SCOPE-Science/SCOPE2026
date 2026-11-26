#!/usr/bin/env python3
"""Finite sanity checks for the coordinate-support graph classification.
Not an alternative to the proof or the cited geometric linearity theorem.
"""
from itertools import product,permutations

def det(M):
    n=len(M)
    out=0
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        out+=(-1 if inv%2 else 1)*__import__('math').prod(M[i][p[i]] for i in range(n))
    return out

def masks(M):
    n=len(M)
    direct=set()
    graph=set()
    for mask in range(1<<n):
        good=all(not(mask>>j&1 and not(mask>>i&1) and M[i][j]!=0)
                 for i in range(n) for j in range(n))
        if good: direct.add(mask)
        reach=[set([j]) for j in range(n)]
        for j in range(n):
            q=[j]
            while q:
                u=q.pop()
                for v in range(n):
                    if M[v][u]!=0 and v not in reach[j]:
                        reach[j].add(v)
                        q.append(v)
        if all(not(mask>>j&1) or all(mask>>v&1 for v in reach[j]) for j in range(n)):
            graph.add(mask)
    assert direct==graph
    assert all((a&b) in direct and (a|b) in direct for a in direct for b in direct)
    return direct

for n in range(2,5):
    edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
    seen=0
    for bits in product([0,1],repeat=len(edges)):
        M=[[2 if i==j else 0 for j in range(n)] for i in range(n)]
        for bit,(i,j) in zip(bits,edges): M[i][j]=bit
        if not det(M): continue
        v=masks(M)
        assert 0 in v and (1<<n)-1 in v
        seen+=1
    assert seen>0
    print('N',n,'invertible support patterns checked',seen)

assert len(masks([[2,0,0],[0,2,0],[0,0,2]]))==8
assert len(masks([[2,0,1],[1,2,0],[0,1,2]]))==2
assert len(masks([[2,0,0],[1,2,0],[0,1,2]]))==4
for n in range(2,10):
    for s in range(1,n):
        assert len([(i,j) for i in range(n) for j in range(n)
                    if (j<s and i>=s)])==s*(n-s)
print('VERIFY_OK')
