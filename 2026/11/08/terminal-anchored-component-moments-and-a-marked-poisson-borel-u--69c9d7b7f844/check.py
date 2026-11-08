#!/usr/bin/env python3
"""Exact finite checks for terminal components of uniform labeled trees.
Run with standard-library Python 3: python check.py
"""
from itertools import product
from fractions import Fraction
from math import comb, factorial
import heapq

def cayley_tree(n, code):
    degree = [1] * n
    for x in code: degree[x] += 1
    leaves = [i for i in range(n) if degree[i] == 1]
    heapq.heapify(leaves)
    adj = [set() for _ in range(n)]
    for x in code:
        y = heapq.heappop(leaves)
        adj[x].add(y); adj[y].add(x)
        degree[y] -= 1; degree[x] -= 1
        if degree[x] == 1: heapq.heappush(leaves, x)
    a = heapq.heappop(leaves); b = heapq.heappop(leaves)
    adj[a].add(b); adj[b].add(a)
    return adj

def components(adj, removed):
    avail = set(range(len(adj))) - removed
    groups = []
    while avail:
        root = min(avail); todo=[root]; avail.remove(root); group={root}
        while todo:
            x=todo.pop()
            for y in adj[x]:
                if y in avail:
                    avail.remove(y); group.add(y); todo.append(y)
        groups.append(group)
    return groups

def rooted_deficit(adj, d):
    n=len(adj); groups=components(adj,set(range(n-d,n)))
    return (n-d)-next(len(s) for s in groups if 0 in s)

def anchored_marks(adj,D):
    n=len(adj); B=set(range(n-D)); out={}
    for j in range(1,D+1):
        h=n-j
        for s in components(adj,{h}):
            if s.issubset(B): out[j,len(s)]=out.get((j,len(s)),0)+1
    return out

def falling(a,s):
    x=1
    for j in range(s): x*=a-j
    return x

def expected_mark_product(n,D,typ):
    # typ: mapping (j,r)-> factorial exponent
    R=sum(r*m for (j,r),m in typ.items())
    if R>n-D: return None
    remaining=n-R
    factor=falling(n-D,R) * (remaining**(remaining-2) if remaining>=2 else 1)
    for (_,r),m in typ.items(): factor*=Fraction(r**((r-1)*m),factorial(r)**m)
    return Fraction(factor,n**(n-2))

def measured_product(mark,typ):
    out=1
    for key,m in typ.items(): out*=falling(mark.get(key,0),m)
    return out

checks=0
for n in range(3,8):
    tree_count=n**(n-2)
    marked_total={}
    root_total={}
    distances=[0]*n
    specs=[]
    for D in (1,2):
        if D>=n:continue
        candidates=[{(1,1):1},{(1,1):2},{(1,2):1}, {(1,1):1,(1,2):1}]
        if D==2:
            candidates += [{(1,1):1,(2,1):1},{(1,2):1,(2,1):1},{(2,2):1}]
        for typ in candidates:
            if expected_mark_product(n,D,typ) is not None:
                specs.append((D,tuple(sorted(typ.items()))))
                marked_total[(D,tuple(sorted(typ.items())))]=0
        for j in range(n-D): root_total[D,j]=0
    for code in product(range(n),repeat=n-2):
        adj=cayley_tree(n,code)
        for D in (1,2):
            if D>=n:continue
            root_total[D,rooted_deficit(adj,D)]+=1
            marks=anchored_marks(adj,D)
            for specD,typ in specs:
                if specD==D:
                    marked_total[specD,typ]+=measured_product(marks,dict(typ))
        dist={0:0}; queue=[0]
        for x in queue:
            for y in adj[x]:
                if y not in dist:dist[y]=dist[x]+1;queue.append(y)
        distances[dist[1]]+=1
    for D,typ in specs:
        actual=Fraction(marked_total[D,typ],tree_count)
        expected=expected_mark_product(n,D,dict(typ))
        assert actual==expected,(n,D,typ,actual,expected)
        checks+=1
    for (D,j),value in root_total.items():
        k=n-D;m=k-j
        expected=Fraction(comb(k-1,j)*m**(m-1)*(D+j)**j,n**(k-1))*Fraction(D,D+j)
        assert Fraction(value,tree_count)==expected,(n,D,j,value,expected)
        checks+=1
    for ell in range(1,n):
        want=Fraction(falling(n-2,ell-1)*(ell+1),n**ell)
        assert Fraction(distances[ell],tree_count)==want,(n,ell)
        checks+=1
print(f'PASS: {checks} exact rational checks of anchored factorial moments, root deficits and two-vertex distances on all Cayley trees with 3<=n<=7')
