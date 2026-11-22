#!/usr/bin/env python3
"""Directly enumerate Italian dominating functions on small leaf-coronas.
Compare with the subset-boundary transform, and check the domination threshold.
"""
from itertools import product
from collections import Counter
from math import comb

def subsets(mask,n):
    return [v for v in range(n) if mask>>v & 1]

def gamma(adj):
    n=len(adj)
    return min(mask.bit_count() for mask in range(1<<n)
               if all((mask>>v & 1) or (adj[v]&mask) for v in range(n)))

def transform(adj):
    n=len(adj); p=Counter()
    for mask in range(1<<n):
        a=mask.bit_count()
        boundary=sum(bool(adj[v]&mask) for v in range(n) if not(mask>>v&1))
        # coeff of x^(2n-boundary)*(2+2x+x^2)^a*(1+x)^boundary
        coeff=Counter({0:1})
        for j in range(a):
            cc=Counter()
            for k,z in coeff.items():
                for d,w in enumerate((2,2,1)):
                    cc[k+d]+=z*w
            coeff=cc
        for j in range(boundary):
            cc=Counter()
            for k,z in coeff.items():
                cc[k]+=z;cc[k+1]+=z
            coeff=cc
        for d,z in coeff.items():p[2*n-boundary+d]+=z
    return +p

def direct(adj):
    n=len(adj); ad=[0]*(2*n)
    for v in range(n):
        ad[v]=sum((1<<u) for u in range(n) if adj[v]>>u&1)|(1<<(n+v))
        ad[n+v]=1<<v
    out=Counter()
    for f in product((0,1,2),repeat=2*n):
        if all(f[v]!=0 or sum(f[u] for u in range(2*n) if ad[v]>>u&1)>=2 for v in range(2*n)):
            out[sum(f)]+=1
    return +out

def adj_graph(n,mask):
    adj=[0]*n; e=0
    for i in range(n):
        for j in range(i+1,n):
            if mask>>e&1:adj[i]|=1<<j;adj[j]|=1<<i
            e+=1
    return adj

def run():
    total=0
    for n in range(1,5):
        graphs=1<<comb(n,2)
        for g in range(graphs):
            adj=adj_graph(n,g)
            a=direct(adj);b=transform(adj)
            assert a==b,(n,g,a,b)
            assert min(a)==n+gamma(adj),(n,g,a)
            # leading-coefficient formula
            max_boundary=max(sum(bool(adj[v]&P) for v in range(n) if not(P>>v&1)) for P in range(1<<n))
            mul=sum(2**P.bit_count() for P in range(1<<n) if sum(bool(adj[v]&P) for v in range(n) if not(P>>v&1))==max_boundary)
            assert a[n+gamma(adj)]==mul,(n,g,a,mul)
            total+=1
        print(f'ORDER_{n} GRAPHS_{graphs} PASS',flush=True)
    for n,edges in ((5,[(i,i+1) for i in range(4)]),(5,[(i,(i+1)%5) for i in range(5)]),
                    (5,[(0,i) for i in range(1,5)]),(5,[(i,j) for i in range(5) for j in range(i+1,5)])):
        adj=[0]*n
        for u,v in edges:adj[u]|=1<<v;adj[v]|=1<<u
        a=direct(adj);b=transform(adj)
        assert a==b and min(a)==n+gamma(adj),(edges,a,b)
        print(f'ORDER_5_EDGES_{len(edges)} MIN_{min(a)} TOTAL_{sum(a.values())} PASS',flush=True)
    print('VERIFY_OK',total,'all_graphs_and_4_order_5_families')
if __name__=='__main__': run()
