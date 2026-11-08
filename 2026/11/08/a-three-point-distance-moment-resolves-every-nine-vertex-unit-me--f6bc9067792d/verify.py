#!/usr/bin/env python3
"""Exact finite verification of unit-edge metric-tree distance-law collisions.
Requires only the Python standard library. Run: python verify.py
"""
from collections import Counter, defaultdict, deque
from fractions import Fraction
from itertools import combinations

# The represented metric tree has length one on every edge.
PAIRS = [
 (
  ((0,1),(0,2),(0,3),(0,4),(0,5),(1,6),(2,7),(3,8)),
  ((0,1),(0,2),(0,3),(0,4),(1,5),(1,6),(1,7),(2,8)),
  (13,12,3,0,0,0,0),
 ),
 (
  ((0,1),(0,2),(0,3),(0,4),(1,5),(2,6),(3,7),(5,8)),
  ((0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(2,7),(4,8)),
  (10,10,6,2,0,0,0),
 ),
]

def adjacency(edges,n):
    a=[[] for _ in range(n)]
    for u,v in edges:
        assert 0<=u<n and 0<=v<n and u!=v
        a[u].append(v);a[v].append(u)
    return a

def canonical(edges,n):
    a=adjacency(edges,n)
    def rooted(u,p):
        return '('+''.join(sorted(rooted(v,u) for v in a[u] if v!=p))+')'
    return min(rooted(v,-1) for v in range(n))

def edge_hist(edges,n):
    """Direct edge-endpoint BFS, unrelated to vertex-distance polynomial."""
    E=tuple(tuple(sorted(e)) for e in edges)
    a=adjacency(E,n); h=Counter()
    for i,(u,v) in enumerate(E):
        ds=[-1]*n;ds[u]=ds[v]=0;Q=deque((u,v))
        while Q:
            z=Q.popleft()
            for w in a[z]:
                if ds[w]==-1:
                    ds[w]=ds[z]+1;Q.append(w)
        for p,q in E[i+1:]:h[min(ds[p],ds[q])]+=1
    assert sum(h.values())==(n-1)*(n-2)//2
    return tuple(h.get(k,0) for k in range(n-2))

def vertex_hist(edges,n):
    """Independent all-pairs shortest vertex distance computation."""
    a=adjacency(edges,n);h=Counter()
    for u in range(n):
        ds=[-1]*n;ds[u]=0;Q=deque((u,))
        while Q:
            z=Q.popleft()
            for w in a[z]:
                if ds[w]==-1:
                    ds[w]=ds[z]+1;Q.append(w)
        for v in range(u+1,n):h[ds[v]]+=1
    assert sum(h.values())==n*(n-1)//2
    return h

def distribution(edges,n,r):
    """Exact CDF by conditioning on ordered edge pairs."""
    r=Fraction(r);m=n-1
    h=edge_hist(edges,n)
    # |U-V| for U,V independent uniform [0,1]
    same=Fraction(0) if r<=0 else (2*r-r*r if r<1 else Fraction(1))
    # U+V for independent uniforms on [0,1]
    def triangle(z):
        if z<=0:return Fraction(0)
        if z<1:return z*z/2
        if z<2:return 1-(2-z)**2/2
        return Fraction(1)
    return same/m+Fraction(2,m*m)*sum(h[k]*triangle(r-k) for k in range(len(h)))

def all_trees(max_n=9):
    """Inductive complete unlabeled-tree census, dedup by AHU rooted canonical code."""
    models={1:[tuple()]}
    for n in range(2,max_n+1):
        found={}
        for E in models[n-1]:
            for v in range(n-1):
                new=tuple(sorted(E+((v,n-1),)))
                found.setdefault(canonical(new,n),new)
        models[n]=list(found.values())
    return models

def main():
    models=all_trees()
    expected_counts={1:1,2:1,3:1,4:2,5:3,6:6,7:11,8:23,9:47}
    assert {n:len(E) for n,E in models.items()}==expected_counts
    collision_classes=[]
    for n,trees in models.items():
        bins=defaultdict(list)
        for E in trees:
            signature=edge_hist(E,n)
            h=vertex_hist(E,n)
            # For any tree, vertex pair distances k+1 match distinct edge-pair gaps k.
            assert all(h.get(k+2,0)==signature[k] for k in range(n-2))
            assert h[1]==n-1
            bins[signature].append(E)
        collisions=[v for v in bins.values() if len(v)>1]
        assert n==9 or not collisions
        if n==9:
            collision_classes=collisions
            assert len(bins)==45
            assert len(collisions)==2
            assert sorted(map(len,collisions))==[2,2]
            got={frozenset(canonical(E,n) for E in C) for C in collisions}
            specified={frozenset((canonical(A,9),canonical(B,9))) for A,B,_ in PAIRS}
            assert got==specified
    for A,B,h in PAIRS:
        assert edge_hist(A,9)==edge_hist(B,9)==h
        assert canonical(A,9)!=canonical(B,9)
        deg=lambda E:sorted(Counter(v for e in E for v in e).values(),reverse=True)
        assert deg(A)!=deg(B)
        for r in map(Fraction,('0','1/4','3/4','1','5/4','3/2','2','5/2','3','4','5','6')):
            assert distribution(A,9,r)==distribution(B,9,r)
        print('COLLISION',h[:4], 'degrees',deg(A),deg(B),'CDF(3/2)',distribution(A,9,Fraction(3,2)))
    print('VERIFY_OK', 'unlabeled_n9=47', 'distinct_distance_laws_n9=45', 'collision_pairs_n9=2', 'smaller_orders_unique=YES')

if __name__=='__main__':main()

# Three-sample distance correlation, including independent formulas.
def distance_matrix(edges,n):
    a=adjacency(edges,n); out=[]
    for u in range(n):
        ds=[-1]*n;ds[u]=0; q=deque((u,))
        while q:
            z=q.popleft()
            for v in a[z]:
                if ds[v]<0:ds[v]=ds[z]+1;q.append(v)
        out.append(ds)
    return out

def integral_square(a,b):
    """Exact integral on [0,1] of (s^2+a*s+b)^2."""
    a=Fraction(a);b=Fraction(b)
    return Fraction(1,5)+a*Fraction(1,2)+(a*a+2*b)*Fraction(1,3)+a*b+b*b

def mixed_moment(edges,n, independent=False):
    """Q=E[d(X,Y)d(X,Z)], where X,Y,Z iid arclength-uniform on metric tree."""
    m=n-1; M=distance_matrix(edges,n); total=Fraction(0)
    for u,v in edges:
        if independent:
            def value(s):
                s=Fraction(s)
                ans=s*s-s+Fraction(1,2)
                for a,b in edges:
                    if (a,b)==(u,v):continue
                    # In a tree, every point along edge (a,b) has a nearest endpoint
                    # from x in edge (u,v); integrate distance along this edge.
                    via_u=min(M[u][a],M[u][b]);via_v=min(M[v][a],M[v][b])
                    # x--u or x--v: only one is possible without traversing (a,b)
                    if via_u<via_v:ans+=s+via_u+Fraction(1,2)
                    elif via_v<via_u:ans+=(1-s)+via_v+Fraction(1,2)
                    else:raise AssertionError('equidistant endpoints')
                return ans
            val0,valm,val1=value(0),value(Fraction(1,2)),value(1)
            # quadratic coefficient is 1 for the same-edge distance integral
            assert val0-2*valm+val1==Fraction(1,2)
            alpha=val1-val0-1;beta=val0
        else:
            a=adjacency(edges,n);comp={u};q=deque((u,))
            while q:
                w=q.popleft()
                for z in a[w]:
                    if (w,z) in ((u,v),(v,u)):continue
                    if z not in comp:comp.add(z);q.append(z)
            EA=[(p,q) for p,q in edges if p in comp and q in comp]
            EB=[(p,q) for p,q in edges if p not in comp and q not in comp]
            la,lb=len(EA),len(EB)
            ca=sum((Fraction(min(M[u][p],M[u][q]))+Fraction(1,2) for p,q in EA),Fraction(0))
            cb=sum((Fraction(min(M[v][p],M[v][q]))+Fraction(1,2) for p,q in EB),Fraction(0))
            alpha=la-lb-1;beta=lb+ca+cb+Fraction(1,2)
        total+=integral_square(alpha,beta)
    return total/Fraction(m**3)

def three_point_main():
    trees=all_trees(9)
    for n,tlist in trees.items():
        if n<2: continue
        bins=defaultdict(list)
        for E in tlist:
            q1=mixed_moment(E,n)
            q2=mixed_moment(E,n,True)
            assert q1==q2,(n,E,q1,q2)
            bins[(edge_hist(E,n),q1)].append(E)
        assert len(bins)==len(tlist),('triple-moment failure',n)
    for A,B,_ in PAIRS:
        ma,mb=mixed_moment(A,9),mixed_moment(B,9)
        print('THREE_POINT_CROSS_MOMENT',ma,mb,'gap',ma-mb)
        assert ma!=mb
    print('THREE_POINT_VERIFY_OK', 'order_leq_9=unique', 'two_point_9_collisions=2', 'exact_cross_moment=checked_twice')

if __name__=='__main__':three_point_main()
