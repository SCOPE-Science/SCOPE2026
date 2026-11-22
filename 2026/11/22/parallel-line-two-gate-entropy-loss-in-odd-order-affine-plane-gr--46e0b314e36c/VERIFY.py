#!/usr/bin/env python3
"""Independent GF(2) binary-rank checks for two deleted incidence gates.
Only prime orders are sampled computationally; the accompanying proof covers
all finite affine planes of odd order, including non-Desarguesian planes.
"""
from itertools import combinations

def rows_for_prime(q):
    points = [(x,y) for x in range(q) for y in range(q)]
    lines = []
    classes = []
    for a in range(q):
        cls = []
        for b in range(q):
            cls.append(len(lines))
            lines.append(frozenset((x,(a*x+b)%q) for x in range(q)))
        classes.append(cls)
    cls=[]
    for a in range(q):
        cls.append(len(lines))
        lines.append(frozenset((a,y) for y in range(q)))
    classes.append(cls)
    rows=[sum(1<<j for j,L in enumerate(lines) if p in L) for p in points]
    edges=[(i,j) for i,p in enumerate(points) for j,L in enumerate(lines) if p in L]
    directions={j:d for d,cls in enumerate(classes) for j in cls}
    return rows,edges,directions

def gf2_rank(rows):
    pivots={}
    for row in rows:
        while row:
            leading=row.bit_length()-1
            if leading in pivots: row ^= pivots[leading]
            else: pivots[leading]=row;break
    return len(pivots)

def test(q):
    rows,edges,directions=rows_for_prime(q)
    n=q*q
    assert gf2_rank(rows)==n
    for i,j in edges:
        reduced=rows.copy(); reduced[i]^=1<<j
        assert gf2_rank(reduced)==n, (q,'single',i,j)
    counts={n:0,n-1:0}
    for (a,u),(b,v) in combinations(edges,2):
        modified=rows.copy()
        modified[a]^=1<<u
        modified[b]^=1<<v
        rk=gf2_rank(modified)
        predicted=n-1 if u!=v and directions[u]==directions[v] else n
        assert rk==predicted,(q,(a,u),(b,v),rk,predicted)
        counts[rk]+=1
    assert counts[n-1]==(q+1)*q**3*(q-1)//2
    assert sum(counts.values())==len(edges)*(len(edges)-1)//2
    print(f'q={q} points={n} edges={len(edges)} single={len(edges)} two={sum(counts.values())} rank-drop-pairs={counts[n-1]} unaffected={counts[n]} PASS')

if __name__=='__main__':
    for q in (3,5,7):test(q)

# A distinct nonprime prime-power check, without finite-field packages.
def check_order_nine(samples=5000):
    import random
    rng = random.Random(20261119)
    q=9
    def add(u,v):
        return ((u%3+v%3)%3)+3*((u//3+v//3)%3)
    def mul(u,v):
        a,b=u%3,u//3; c,d=v%3,v//3
        return ((a*c-b*d)%3)+3*((a*d+b*c)%3)
    points=[(x,y) for x in range(q) for y in range(q)]
    lines=[]
    for t in range(q):
        for b in range(q):
            lines.append(frozenset((x,add(mul(t,x),b)) for x in range(q)))
    for a in range(q):
        lines.append(frozenset((a,y) for y in range(q)))
    rows=[sum(1<<j for j,L in enumerate(lines) if p in L) for p in points]
    edges=[(i,j) for i,p in enumerate(points) for j,L in enumerate(lines) if p in L]
    assert gf2_rank(rows)==q*q
    for i,j in edges:
        mod=rows[:];mod[i]^=1<<j
        assert gf2_rank(mod)==q*q
    for _ in range(samples):
        (i,j),(k,l)=rng.sample(edges,2)
        mod=rows[:];mod[i]^=1<<j;mod[k]^=1<<l
        expected=q*q-1 if j!=l and (j//q)==(l//q) else q*q
        assert gf2_rank(mod)==expected
    print(f'q=9 points=81 edges={len(edges)} single={len(edges)} two-sample={samples} PASS')

if __name__=='__main__':
    check_order_nine()
