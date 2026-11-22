#!/usr/bin/env python3
"""Standalone finite checks for the cycle general-position homology onset."""
from itertools import combinations, product
from collections import Counter


def graph_dist(i, j, n):
    d = abs(i-j)
    return min(d, n-d)


def gp_triple(t, n):
    for a, b, c in ((t[0],t[1],t[2]),(t[0],t[2],t[1]),(t[1],t[0],t[2])):
        if graph_dist(a,c,n) == graph_dist(a,b,n)+graph_dist(b,c,n):
            return False
    return True


def triangles(n):
    return {t for t in combinations(range(n), 3) if gp_triple(t,n)}


def cross_cycle(n):
    g=[n//3+(1 if j<n%3 else 0) for j in range(3)]
    s=[0,g[0],g[0]+g[1]]
    assert all(gj>=2 for gj in g)
    faces=[]
    for e in product((0,1),repeat=3):
        t=tuple(s[i]+e[i] for i in range(3))
        assert gp_triple(t,n), (n,g,t)
        c=(-1)**sum(e)
        faces.append((t,c))
    bd=Counter()
    for (a,b,c),sgn in faces:
        bd[(b,c)] += sgn
        bd[(a,c)] -= sgn
        bd[(a,b)] += sgn
    assert all(v==0 for v in bd.values())
    assert len(set(t for t,_ in faces))==8
    return g


def peel(n):
    alive=triangles(n)
    steps=0
    while alive:
        degrees=Counter(edge for t in alive for edge in combinations(t,2))
        choices=[(e,t) for t in alive for e in combinations(t,2) if degrees[e]==1]
        if not choices:
            break
        e,t=min(choices)
        alive.remove(t)
        steps+=1
    return steps, len(alive)

for n in range(3, 41):
    tri=triangles(n)
    from_gaps={t for t in combinations(range(n),3)
               if all(x*2<n for x in (t[1]-t[0],t[2]-t[1],n+t[0]-t[2]))}
    assert tri == from_gaps, (n,'gaps')
    for four in combinations(range(n),4):
        assert not all(t in tri for t in combinations(four,3)), (n,'4face',four)
for n in (3,4,5,6,7,8,10):
    done,left=peel(n)
    assert left==0, (n,done,left)
    print(f'vanishing n={n}: free-face removals={done}')
for n in range(9,101):
    if n==10: continue
    assert n%2==1 or n>=12
    g=cross_cycle(n)
print('nonzero n=9..100 (excluding n=10): primitive 8-triangle octahedral cycles checked')
print('complete face test and dimension cap: n=3..40')
print('PASS')
