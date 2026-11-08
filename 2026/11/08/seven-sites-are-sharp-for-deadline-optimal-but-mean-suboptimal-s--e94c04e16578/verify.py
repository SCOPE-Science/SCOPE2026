"""Exact certificates for one-site epidemic detection on small trees.
Public reproducibility requires only Python >=3.9 standard library.
"""
from fractions import Fraction
from itertools import product
from functools import lru_cache
from collections import deque
from math import factorial
import heapq


def prufer_tree(seq):
    n=len(seq)+2
    deg=[1]*n
    for x in seq: deg[x]+=1
    leaves=[i for i in range(n) if deg[i]==1]
    heapq.heapify(leaves)
    adj=[set() for _ in range(n)]
    for x in seq:
        y=heapq.heappop(leaves)
        adj[x].add(y); adj[y].add(x)
        deg[x]-=1; deg[y]-=1
        if deg[x]==1: heapq.heappush(leaves,x)
    a,b=leaves
    adj[a].add(b);adj[b].add(a)
    return adj


def distance_profiles(adj):
    n=len(adj)
    ds=[]
    for v in range(n):
        d=[-1]*n;d[v]=0;Q=deque([v])
        while Q:
            w=Q.popleft()
            for z in adj[w]:
                if d[z]<0:
                    d[z]=d[w]+1;Q.append(z)
        assert all(x>=0 for x in d)
        ds.append(d)
    return ds


def coefficients(distance_list):
    n=len(distance_list)
    return tuple(sum(d>k for d in distance_list) for k in range(n-1))


def small_tree_certificate():
    total=0
    counts={}
    for n in range(1,7):
        sequences=[()] if n<=2 else product(range(n),repeat=n-2)
        count=0
        for seq in sequences:
            adj=[set()] if n==1 else prufer_tree(seq)
            ds=distance_profiles(adj)
            sums=list(map(sum,ds))
            med=[u for u in range(n) if sums[u]==min(sums)]
            co=[coefficients(ds[v]) for v in range(n)]
            for v in range(n):
                if v not in med:
                    assert any(all(co[u][k]<=co[v][k] for k in range(n-1)) and
                               any(co[u][k]<co[v][k] for k in range(n-1))
                               for u in med), (n,seq,v,med,co)
            count+=1
        counts[n]=count; total+=count
        assert count==(1 if n<=2 else n**(n-2))
    assert total==1442
    return counts


def broom_certificate():
    # A 5-vertex path 0--1--2--3--4 and two leaves 5,6 attached to 0.
    edges=[(0,1),(1,2),(2,3),(3,4),(0,5),(0,6)]
    adj=[set() for _ in range(7)]
    for a,b in edges: adj[a].add(b);adj[b].add(a)
    ds=distance_profiles(adj)
    sums=list(map(sum,ds))
    assert sums==[12,11,12,15,20,17,17],sums
    co=[coefficients(d) for d in ds]
    # All polynomials below are represented by integer Taylor-coefficient counts c_k
    # with P_v(t)=sum_k c_k*t^k/k!.
    assert co[0]==(6,3,2,1,0,0)
    assert co[1]==(6,4,1,0,0,0)
    assert all(all(co[1][k]<=co[v][k] for k in range(6))
               for v in [2,3,4,5,6])
    assert all(all(co[0][k]<=co[v][k] for k in range(6))
               for v in [3,4,5,6])
    # Special v=2 is strictly dominated by median 1; hence cannot defeat 0 or 1.
    assert sum(ds[1])<sum(ds[0])
    assert (co[0][1]-co[1][1],co[0][2]-co[1][2],co[0][3]-co[1][3])==(-1,1,1)
    # P0-P1=-t+t^2/2+t^3/6: single positive zero (-3+sqrt(33))/2.
    assert co[0][4:]==co[1][4:]
    return adj,co


def laplace_ctmc(adj,s,sentinel):
    n=len(adj)
    @lru_cache(None)
    def F(mask):
        if mask&(1<<sentinel):return Fraction(1)
        den=Fraction(s)
        num=Fraction(0)
        for w in range(n):
            if mask&(1<<w):continue
            rate=sum(bool(mask&(1<<u)) for u in adj[w])
            if rate:
                den+=rate
                num+=rate*F(mask|(1<<w))
        assert den>0
        return num/den
    return sum((F(1<<v) for v in range(n)),Fraction(0))/n


def independent_ctmc_certificate(adj):
    ds=distance_profiles(adj);n=len(adj)
    cases=0
    for s in [Fraction(1),Fraction(2),Fraction(3)]:
        for v in range(n):
            target=sum(((1/(1+s))**d[v] for d in ds), Fraction(0))/n
            check=laplace_ctmc(adj,s,v)
            assert check==target,(s,v,target,check)
            cases+=1
    return cases


if __name__=='__main__':
    counts=small_tree_certificate()
    adj,coefficients_by_vertex=broom_certificate()
    checked=independent_ctmc_certificate(adj)
    print('PASS exhaustive labeled trees:',counts,'total',sum(counts.values()))
    print('PASS broom seven-site symbolic coefficients:',coefficients_by_vertex)
    print('PASS independently computed CTMC Laplace equalities:',checked)
