#!/usr/bin/env python3
"""Exact checks for source--sink covariance in independently oriented trees.

Python 3 standard library only. This finite checker corroborates, but does not
replace, the all-orders proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter

checks = 0

def insist(cond):
    global checks
    checks += 1
    assert cond, f"Assertion {checks} failed"

def prufer_edges(code, n):
    deg = [1] * n
    for x in code:
        deg[x] += 1
    edges = []
    for x in code:
        leaf = next(i for i in range(n) if deg[i] == 1)
        edges.append((leaf, x))
        deg[leaf] -= 1
        deg[x] -= 1
    last = [i for i in range(n) if deg[i] == 1]
    edges.append(tuple(last))
    return edges

def formula(n, edges):
    d = [0] * n
    for u, v in edges:
        d[u] += 1; d[v] += 1
    a = [F(1, 2**q) for q in d]
    c = 2 * sum((a[u]*a[v] for u,v in edges), F(0)) - sum((q*q for q in a), F(0))
    energy = sum(((d[v]-1)*a[v]*a[v] for v in range(n)), F(0)) - sum(((a[u]-a[v])**2 for u,v in edges), F(0))
    insist(c == energy)
    return c, d

def direct(n, edges):
    m = len(edges)
    s_total = 0; t_total = 0; st_total = 0
    for k in range(1 << m):
        indeg = [0]*n; outdeg = [0]*n
        for j, (u,v) in enumerate(edges):
            if (k >> j) & 1: u,v = v,u
            outdeg[u]+=1; indeg[v]+=1
        s = sum(x==0 for x in indeg)
        t = sum(x==0 for x in outdeg)
        s_total += s; t_total += t; st_total += s*t
    D = 1 << m
    return F(st_total,D) - F(s_total,D)*F(t_total,D)

def spider(arms):
    edges=[]; v=1
    for length in arms:
        prev=0
        for _ in range(length):
            edges.append((prev,v))
            prev=v; v+=1
    return v,edges

# Every labelled tree with 3 through 6 vertices: direct 2^(n-1)
# orientation enumeration and the explicit degree formula.
for n in range(3,7):
    for code in product(range(n), repeat=n-2):
        edges = prufer_edges(code,n)
        c,d = formula(n,edges)
        insist(c == direct(n,edges))
        gap = F(n-4,16) - c
        insist(gap >= 0)
        if max(d) > 2:
            insist(gap >= F(13,64))
            insist(gap > F(13,64)) # Three arms of length >=2 need n>=7.
        else:
            insist(gap == 0)

# Exhaustive symbolic inequality and equality case on all labelled
# trees with seven vertices (there are 7^5 codes).
n=7
for code in product(range(n), repeat=n-2):
    edges=prufer_edges(code,n)
    c,d=formula(n,edges)
    gap=F(n-4,16)-c
    insist(gap >= 0)
    if max(d)>2:
        insist(gap>=F(13,64))
        leaves=sum(t==1 for t in d)
        equality=(leaves==3 and max(d)==3 and
                  all(d[v]==2 for u,v in edges if d[u]==3) and
                  all(d[u]==2 for u,v in edges if d[v]==3))
        insist((gap==F(13,64))==equality)
    else:
        insist(gap==0)

# Construct extremizers at arbitrary orders; n>=7 is exactly feasible.
for n in range(7,51):
    size,edges=spider((2,2,n-5))
    insist(size==n)
    c,_=formula(n,edges)
    insist(F(n-4,16)-c==F(13,64))

print(f"VERIFY_OK {checks} exact assertions; all labelled trees n<=7, orientations n<=6")
