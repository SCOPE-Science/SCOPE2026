#!/usr/bin/env python3
"""Exact arithmetic checks for spanning-tree-polytope Euclidean inballs.

Only standard Python modules are used. Finite checks corroborate the proof;
they are not a certificate for the all-dimension theorem.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, isclose, sqrt

checks = 0

def check(flag):
    global checks
    assert flag
    checks += 1

def sqnorm_projected(size, m):
    return F(size * (m - size), m)

def radius_squared(n):
    m = comb(n, 2)
    rcoord = F(4, n*n) / (1 - F(1, m))
    rcut = F(n-2, n*(n-1))
    return min(rcoord, rcut)

def cut_sq(n, k):
    return F(2*(n-1)*(k-1)*(n-k), n*k*(n+k-1))

def rank(mat):
    if not mat:
        return 0
    a = [[F(t) for t in row] for row in mat]
    i = 0
    for j in range(len(a[0])):
        pivot = next((r for r in range(i, len(a)) if a[r][j]), None)
        if pivot is None:
            continue
        a[pivot], a[i] = a[i], a[pivot]
        fac = a[i][j]
        a[i] = [v/fac for v in a[i]]
        for r in range(len(a)):
            if r != i and a[r][j]:
                fac = a[r][j]
                a[r] = [v-fac*w for v,w in zip(a[r], a[i])]
        i += 1
        if i == len(a):
            break
    return i

for n in range(4, 501):
    m = comb(n, 2)
    rcoord = F(4*(n-1),n*(n-2)*(n+1))
    rcut = F(n-2,n*(n-1))
    check(radius_squared(n) == (rcut if n <= 5 else rcoord))
    check((rcut < rcoord) == (n<=5))
    check(rcoord == F(4,n*n) / (1-F(1,m)))
    for k in range(2,n):
        a=comb(k,2)
        slack=F((k-1)*(n-k),n)
        d2=slack**2/sqnorm_projected(a,m)
        check(d2==cut_sq(n,k))
        check(d2>=rcut)
        if k < n-1:
            check(d2>rcut)
    # The k=2 end of the cut-distance spectrum is farther than k=n-1.
    check(cut_sq(n,2)>cut_sq(n,n-1))

for n in range(4,11):
    edges=list(combinations(range(n),2))
    m=len(edges)
    # Projected singleton-cut normals have rank n-1 in the affine hyperplane.
    incid=[[int(v in e) for e in edges] for v in range(n)]
    check(rank(incid)==n)
    check(rank([list(row) for row in zip(*incid)])==n)
    ones=[1]*m
    project_cut=[[F(v)-F(n-1,m) for v in row] for row in incid]
    check(rank(project_cut)==n-1)
    # Projected coordinate facet normals span the full affine direction space.
    projected_coord=[[F(int(i==j))-F(1,m) for j in range(m)] for i in range(m)]
    check(rank(projected_coord)==m-1)
    # The centered sphere has precisely n cut contacts for n=4,5;
    # and precisely m coordinate contacts for n>=6.
    cut_contacts=sum(cut_sq(n,k)==radius_squared(n)*1 for k in range(2,n))
    check((cut_contacts==1) if n<=5 else (cut_contacts==0))

# Reconstruct all spanning trees of K_n for n=4,5 via Prufer codes;
# each subset inequality is checked at each vertex, independently of the
# abstract matroid base-polytope theorem.
def tree_edges(code, n):
    deg=[1]*n
    for v in code: deg[v]+=1
    E=[]
    for v in code:
        leaf=min(i for i in range(n) if deg[i]==1)
        E.append(tuple(sorted((leaf,v))))
        deg[leaf]-=1
        deg[v]-=1
    u,v=[i for i in range(n) if deg[i]==1]
    E.append(tuple(sorted((u,v))))
    return set(E)

for n in (4,5,6):
    E=list(combinations(range(n),2)); m=len(E)
    c=F(2,n)
    for seq in product(range(n), repeat=n-2):
        tree=tree_edges(seq,n)
        check(len(tree)==n-1)
        for k in range(2,n):
            for S in combinations(range(n), k):
                q=set(S)
                check(sum(u in q and v in q for u,v in tree)<=k-1)
    # Explicit nonuniform degree-preserving center at n=4,5.
    if n<=5:
        X={e:c for e in E}
        for e,delta in [((0,1),F(1,1000)),((2,3),F(1,1000)),
                        ((0,2),-F(1,1000)),((1,3),-F(1,1000))]:
            X[e]+=delta
        check(sum(X.values())==n-1)
        check(all(sum(val for e,val in X.items() if v in e)==F(2*(n-1),n)
                  for v in range(n)))
        r=sqrt(float(radius_squared(n)))
        for e,val in X.items():
            check(float(val)>r*sqrt(float(sqnorm_projected(1,m))))
        for k in range(2,n-1):
            for S in combinations(range(n),k):
                q=set(S)
                sumval=sum(val for (u,v),val in X.items() if u in q and v in q)
                check(float(sumval)+r*sqrt(float(sqnorm_projected(comb(k,2),m)))<k-1)

print('VERIFICATION_OK', checks)
