#!/usr/bin/env python3
"""Definition-level validation of connected mutual visibility in clique-fiber Cartesian products.

Requires only Python 3 standard library.  Checks every subset on selected small instances.
"""
from collections import Counter
from itertools import combinations
from math import comb


def base(n, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        assert a != b and 0 <= a < n and 0 <= b < n
        adj[a].add(b)
        adj[b].add(a)
    return adj


def product(adj_h, q):
    n = len(adj_h)
    adj = [set() for _ in range(n*q)]
    for h in range(n):
        for c in range(q):
            a = h*q+c
            for b in range(q):
                if b != c: adj[a].add(h*q+b)
            for g in adj_h[h]:adj[a].add(g*q+c)
    return adj


def distances(adj):
    N = len(adj)
    result=[]
    for s in range(N):
        d=[N+1]*N;d[s]=0; z=[s]
        for a in z:
            for b in adj[a]:
                if d[b]>N:
                    d[b]=d[a]+1;z.append(b)
        assert len(z)==N
        result.append(d)
    return result


def internal_geodesic_masks(adj,d):
    N=len(adj)
    masks={}
    for a in range(N):
        for b in range(a+1,N):
            length=d[a][b]
            current=[(a,0)]
            for step in range(1,length):
                new=[]
                for u,mask in current:
                    for v in adj[u]:
                        if d[a][v]==step and d[v][b]==length-step:
                            new.append((v,mask|(1<<v)))
                current=new
            masks[a,b]=tuple(dict.fromkeys(mask for _,mask in current))
            assert masks[a,b]
    return masks


def count_actual(adj):
    N=len(adj)
    nb=[sum(1<<v for v in vs) for vs in adj]
    gd=internal_geodesic_masks(adj,distances(adj))
    result=Counter()
    for S in range(1,1<<N):
        # Connectivity by closure of selected-neighbourhoods.
        seen=S & -S
        while True:
            x=seen; neighbors=seen
            while x:
                bit=x&-x;u=bit.bit_length()-1;x-=bit
                neighbors |= nb[u]
            new=seen|(neighbors&S)
            if new==seen:break
            seen=new
        if seen!=S:continue
        members=[i for i in range(N) if S>>i&1]
        good=True
        for a,b in combinations(members,2):
            if not any((mask&S)==0 for mask in gd[a,b]):
                good=False;break
        if good:result[len(members)]+=1
    return result


def count_prediction(n,m,q):
    result=Counter()
    for k in range(1,q+1):result[k]+=n*comb(q,k)
    for u in range(1,q+1):
        result[u+1]+=m*comb(q,u)*u*(2**(u-1))
    return result


def run():
    cases=[
        ('edge',2,[(0,1)],2),
        ('edge',2,[(0,1)],5),
        ('path3',3,[(0,1),(1,2)],3),
        ('path3',3,[(0,1),(1,2)],5),
        ('path4',4,[(0,1),(1,2),(2,3)],3),
        ('star4',4,[(0,1),(0,2),(0,3)],3),
        ('star4',4,[(0,1),(0,2),(0,3)],4),
        ('cycle5',5,[(i,(i+1)%5) for i in range(5)],3),
        ('cycle6',6,[(i,(i+1)%6) for i in range(6)],2),
        ('tree5',5,[(0,1),(0,2),(0,3),(3,4)],3),
    ]
    for name,n,edges,q in cases:
        actual=count_actual(product(base(n,edges),q))
        expected=count_prediction(n,len(edges),q)
        assert actual==expected,(name,q,actual,expected)
        print('EXHAUSTIVE_OK',name,'q',q,'vertices',n*q,'profile',sorted(actual.items()),flush=True)
    print('VERIFY_OK')

if __name__=='__main__':run()
