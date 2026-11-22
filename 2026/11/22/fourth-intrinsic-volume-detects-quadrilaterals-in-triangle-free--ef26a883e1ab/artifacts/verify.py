#!/usr/bin/env python3
"""Exact finite checks of regular triangle-free graphical-zonotope intrinsic volumes.

No third-party dependencies. Compares direct incidence-column Gram determinants to
component-count formulas, then checks fourth-volume coefficients for several graphs.
Finite checks are illustrative; the included proof handles all admissible graphs.
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb


def binom(n, k):
    return comb(n, k) if n >= k >= 0 else 0


def cycle(n):
    return [(i, (i+1)%n) for i in range(n)]


def biclique(p,q):
    return [(i,p+j) for i in range(p) for j in range(q)]


def circulant_biclique(q, offsets):
    return [(i,q+(i+s)%q) for i in range(q) for s in offsets]


def cube(k):
    return [(i,i^(1<<j)) for i in range(1<<k) for j in range(k) if i<(i^(1<<j))]


def petersen():
    return [(i,(i+1)%5) for i in range(5)] + [(i,i+5) for i in range(5)] + [(i+5,5+(i+2)%5) for i in range(5)]


def determin4(mat):
    total = 0
    for order in permutations(range(4)):
        inv = sum(order[a]>order[b] for a in range(4) for b in range(a+1,4))
        term = 1
        for r,c in enumerate(order): term *= mat[r][c]
        total += (-1 if inv&1 else 1)*term
    return total


def components(edges):
    parent = {}
    for u,v in edges:
        parent.setdefault(u,u)
        parent.setdefault(v,v)
    def find(a):
        while parent[a]!=a:a=parent[a]
        return a
    for u,v in edges:
        parent[find(u)]=find(v)
    sizes=Counter(find(v) for v in parent)
    return tuple(sorted((k-1 for k in sizes.values()),reverse=True)),sizes


def check_graph(label,n,edges):
    ed=[tuple(sorted(x)) for x in edges]
    assert len(set(ed))==len(ed)
    deg=Counter(x for e in ed for x in e)
    assert len(deg)==n
    d=deg[0]
    assert d>=2 and all(deg[i]==d for i in range(n))
    adj=[set() for _ in range(n)]
    for u,v in ed:
        adj[u].add(v);adj[v].add(u)
    assert not any(i in adj[k] for i in range(n) for j in adj[i] for k in adj[j] if i!=k)
    # Count quadrilaterals independently from induced 4-vertex subgraphs.
    c4=0
    for S in combinations(range(n),4):
        if all(len(adj[x].intersection(S))==2 for x in S): c4+=1
    m=len(ed)
    w=n*binom(d,2)
    s=n*binom(d,3)
    t=s+m*(d-1)**2
    e0=n*binom(d,4)+3*n*binom(d,3)*(d-1)+m*(d-1)**3
    d0=t*(m-4*d+3)
    c0=w*(w-9*binom(d,2)+4*(d-1))//2
    b0=w*(binom(m-3*d+2,2)-(n-3)*binom(d,2)+(d-1)*(3*d-4))
    a0=binom(m,4)-b0-c0-d0-e0
    pred={(1,1,1,1):a0+c4,(2,1,1):b0-4*c4,(2,2):c0+2*c4,(3,1):d0+4*c4,(4,):e0-4*c4}
    counts=Counter()
    for F in combinations(ed,4):
        pattern, sizes=components(F)
        nverts=sum(sizes.values())
        # independent incidence-gram determinant, exact integer arithmetic.
        vecs=[]
        for u,v in F:
            vec=[0]*n
            vec[u]=1;vec[v]=-1
            vecs.append(vec)
        gram=[[sum(x*y for x,y in zip(vecs[i],vecs[j])) for j in range(4)] for i in range(4)]
        det=determin4(gram)
        if det==0:
            assert pattern == (3,), (label, F, pattern)
            counts['cycle']+=1
            continue
        assert det>0 and det==__import__('math').prod(sizes.values())
        counts[pattern]+=1
    assert counts['cycle']==c4,(label,c4,counts['cycle'])
    for pat,v in pred.items():assert counts[pat]==v,(label,pat,counts[pat],v)
    assert sum(pred.values())+c4==binom(m,4)
    # Direct check all 3-edge triples, class counts independent of quadrilaterals.
    three=Counter()
    for F in combinations(ed,3):
        pattern,sizes=components(F)
        assert sum(pattern)==3
        three[pattern]+=1
    assert three[(1,1,1)]==binom(m,3)-w*(m-3*d+2)-t
    assert three[(2,1)]==w*(m-3*d+2)
    assert three[(3,)]==t
    assert three.get('cycle',0)==0
    print(f'{label}: n={n} d={d} |E|={m} C4={c4} counts={tuple(counts[x] for x in pred)} PASS')


def main():
    graphs=[('C5',5,cycle(5)),('C6',6,cycle(6)),('C8',8,cycle(8)),('K3,3',6,biclique(3,3)),('K4,4',8,biclique(4,4)),('Cube3',8,cube(3)),('Petersen',10,petersen()),('B(7,{0,1,2})',14,circulant_biclique(7,(0,1,2))),('B(7,{0,1,3})',14,circulant_biclique(7,(0,1,3))),('B(7,{0,2,4})',14,circulant_biclique(7,(0,2,4)))]
    for g in graphs:check_graph(*g)
    print('GRAPHICAL_ZONOTOPE_FOURTH_VOLUME_PASS')

if __name__ == '__main__':main()
