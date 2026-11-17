#!/usr/bin/env python3
"""Independent domination in central graphs: exact enumeration checks."""
from itertools import combinations,product
from collections import Counter
import random

def central(base):
    n=len(base)
    edges=[(i,j) for i in range(n) for j in range(i+1,n) if j in base[i]]
    m=len(edges)
    H=[set() for _ in range(n+m)]
    def join(i,j):
        H[i].add(j);H[j].add(i)
    for k,(i,j) in enumerate(edges):
        join(i,n+k); join(j,n+k)
    for i in range(n):
        for j in range(i+1,n):
            if j not in base[i]: join(i,j)
    return H

def base_from_mask(n,bits):
    H=[set() for _ in range(n)]
    e=0
    for i in range(n):
        for j in range(i+1,n):
            if bits>>e&1:
                H[i].add(j);H[j].add(i)
            e+=1
    return H

def isconnected(H):
    seen={0}; stack=[0]
    while stack:
        for j in H[stack.pop()]:
            if j not in seen:
                seen.add(j);stack.append(j)
    return len(seen)==len(H)

def brute_poly(base):
    H=central(base); N=len(H)
    c=Counter()
    for s in range(1<<N):
        okay=True
        for v in range(N):
            in_s=bool(s>>v&1)
            if in_s:
                if any(s>>w&1 for w in H[v]): okay=False;break
            else:
                if not any(s>>w&1 for w in H[v]): okay=False;break
        if okay:c[s.bit_count()]+=1
    return c

def clique_poly(base):
    n=len(base)
    edges=[(i,j) for i in range(n) for j in range(i+1,n) if j in base[i]]
    c=Counter()
    for bits in range(1<<n):
        X={i for i in range(n) if bits>>i&1}
        if any(j not in base[i] for i in X for j in X if i!=j): continue
        if any(base[v]==X for v in range(n) if v not in X): continue
        k=len(X)+sum(1 for i,j in edges if i not in X and j not in X)
        c[k]+=1
    return c

def multipartite(sizes):
    parts=[]
    for p,a in enumerate(sizes): parts.extend([p]*a)
    return [set(j for j in range(len(parts)) if parts[i]!=parts[j]) for i in range(len(parts))]

def multipartite_poly(sizes):
    r=len(sizes)
    c=Counter()
    # count a selected original from each chosen part; delete exceptional invalid choices
    for bits in range(1<<r):
        chosen=[i for i in range(r) if bits>>i&1]
        choices=1
        for i in chosen:choices*=sizes[i]
        a=[sizes[i]-(i in chosen) for i in range(r)]
        e=sum(a[i]*a[j] for i in range(r) for j in range(i+1,r))
        c[len(chosen)+e]+=choices
    nontriv=[i for i,a in enumerate(sizes) if a>1]
    if len(nontriv)==1:
        c[r-1]-=1
    elif len(nontriv)==0:
        c[r-1]-=r
    return +c

def run():
    checked=0
    for n in range(1,5):
        for bits in range(1<<(n*(n-1)//2)):
            G=base_from_mask(n,bits)
            want=clique_poly(G); got=brute_poly(G)
            assert want==got,('general',n,bits,want,got)
            checked+=1
    print('ALL_LABELLED_GRAPHS_N1_THROUGH_N4_OK',checked)
    random.seed(66123)
    checked=0
    for n in [5,6]:
        for k in range(14):
            e=n*(n-1)//2
            mask=random.randrange(1<<e)
            G=base_from_mask(n,mask)
            if not isconnected(G):continue
            want=clique_poly(G);got=brute_poly(G)
            assert want==got,(n,mask,want,got)
            checked+=1
    print('SEEDED_RANDOM_CONNECTED_GRAPHS_N5_N6_OK',checked)
    checked=0
    for r in range(2,5):
        for sizes in product((1,2,3),repeat=r):
            if sum(sizes)>10: continue
            G=multipartite(sizes)
            got=clique_poly(G)
            want=multipartite_poly(sizes)
            assert got==want,(sizes,got,want)
            checked+=1
    print('MULTIPARTITE_BOUNDARY_FORMULAS_OK',checked)
    for sizes in [(2,2),(1,2,2),(2,2,2),(1,1,2),(1,1,1),(3,3)]:
        G=multipartite(sizes)
        if len(G)+sum(len(t) for t in G)//2<=19:
            assert brute_poly(G)==multipartite_poly(sizes),sizes
    print('MULTIPARTITE_DIRECT_EXAMPLES_OK')
    checked=0
    for n in range(4,7):
        e=n*(n-1)//2
        for bits in range(1<<e):
            G=base_from_mask(n,bits)
            if min(map(len,G))<2: continue
            if any(len(G[i]&G[j])>0 for i in range(n) for j in G[i]): continue
            m=sum(len(a) for a in G)//2
            c=Counter({m:1})
            for i in range(n): c[m+1-len(G[i])]+=1
            for i in range(n):
                for j in G[i]:
                    if j>i:c[m+3-len(G[i])-len(G[j])]+=1
            assert c==clique_poly(G),(n,bits,c,clique_poly(G))
            checked+=1
    print('TRIANGLE_FREE_MINIMUM_DEGREE_TWO_FORMULA_OK',checked)
    print('VERIFY_OK')
if __name__=='__main__':run()
