#!/usr/bin/env python3
"""Exact, standard-library check of directed patch threshold classification."""
from itertools import combinations, permutations
from fractions import Fraction
from collections import defaultdict, Counter

def edges_of(n):
    return [(i,j) for i in range(n) for j in range(n) if i != j]

def strongly_connected(n, edges):
    adj = [[] for _ in range(n)]
    for i,j in edges:
        adj[i].append(j)
    for src in range(n):
        seen={src}; todo=[src]
        for u in todo:
            for v in adj[u]:
                if v not in seen:
                    seen.add(v); todo.append(v)
        if len(seen)!=n:
            return False
    return True

def bidegrees(n, edges):
    din=[0]*n; dout=[0]*n
    for i,j in edges:
        din[j]+=1; dout[i]+=1
    return tuple(zip(din,dout))

def polynomial_newton(n, edges):
    a=[[0]*n for _ in range(n)]
    for i,j in edges:a[i][j]=1
    tr=[]; power=[[int(i==j) for j in range(n)] for i in range(n)]
    for k in range(1,n+1):
        power=[[sum(power[i][t]*a[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
        tr.append(sum(power[i][i] for i in range(n)))
    co=[Fraction(1)]
    for k in range(1,n+1):
        x=-sum(co[k-j]*tr[j-1] for j in range(1,k+1))/k
        assert x.denominator==1
        co.append(x)
    return tuple(int(c) for c in co)

def polynomial_permutations(n, edges):
    # Product of monomials from det(t I-A), independently of Newton traces.
    mat=[[int((i,j) in edges) for j in range(n)] for i in range(n)]
    co=[0]*(n+1)
    for perm in permutations(range(n)):
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        terms={0:(-1)**inversions}
        for i,j in enumerate(perm):
            update={}
            for k,val in terms.items():
                if i==j: update[k+1]=update.get(k+1,0)+val
                if mat[i][j]: update[k]=update.get(k,0)-val
            terms=update
        for k,val in terms.items(): co[n-k]+=val
    return tuple(co)

# All loopless strongly connected digraphs through three patches,
# using independently constructed adjacency matrices and characteristic polynomials.
for n in (2,3):
    classes=defaultdict(set); counts=Counter()
    arcs=edges_of(n)
    for mask in range(1<<len(arcs)):
        E=tuple(arcs[j] for j in range(len(arcs)) if mask & (1<<j))
        if not strongly_connected(n,E):continue
        d=tuple(sorted(bidegrees(n,E)))
        poly=polynomial_newton(n,E)
        assert poly==polynomial_permutations(n,E)
        classes[d].add(poly); counts[n]+=1
    assert all(len(v)==1 for v in classes.values()), (n,classes)
    assert counts[n]==({2:1,3:18}[n])
    print('n=',n,'strong_graphs=',counts[n],'degree_profiles=',len(classes),'each_profile_one_polynomial=True')

# The fixed per-patch ordered degree list, 0=(1,2), 1=(2,1), 2=3=(1,1).
target=((1,2),(2,1),(1,1),(1,1))
polys=defaultdict(list)
all_with_profile=0
for E in combinations(edges_of(4),5):
    if bidegrees(4,E)!=target: continue
    all_with_profile+=1
    if not strongly_connected(4,E): continue
    c=polynomial_newton(4,E)
    assert c==polynomial_permutations(4,E)
    polys[c].append(E)
assert all_with_profile==7
P_low=(1,0,0,-1,-1)   # t^4-t-1
P_mid=(1,0,0,-2,0)    # t(t^3-2)
P_high=(1,0,-1,0,-1)  # t^4-t^2-1
assert {p:len(v) for p,v in polys.items()}=={P_low:2,P_mid:1,P_high:2},polys

ex={
 'low':((0,1),(0,2),(1,3),(2,1),(3,0)),
 'middle':((0,2),(0,3),(1,0),(2,1),(3,1)),
 'high':((0,1),(0,2),(1,0),(2,3),(3,1)),
}
for label,E in ex.items():
    assert strongly_connected(4,E)
    assert bidegrees(4,E)==target
    reciprocal=sum((j,i) in E for i,j in E)
    assert reciprocal==({'low':0,'middle':0,'high':2}[label])
    c=polynomial_newton(4,E)
    assert c=={'low':P_low,'middle':P_mid,'high':P_high}[label]
    print(label,'edges=',list(E),'characteristic=',c,'reciprocal_directed_arcs=',reciprocal)
print('n=4, edges=5: fixed_degree_realizations=7, strongly_connected=5, root_types=3')
print('CHECK_OK')
