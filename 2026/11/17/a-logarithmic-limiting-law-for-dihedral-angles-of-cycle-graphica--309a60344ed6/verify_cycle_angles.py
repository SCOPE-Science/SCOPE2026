#!/usr/bin/env python3
"""Exact finite verification of cycle graphical zonotope ridge-angle spectrum.
Requires only Python's standard library; checks vertex/facet incidence and rational Gram values.
"""
from itertools import product,combinations
from collections import Counter
from fractions import Fraction
from math import comb

def rank_integer(mat):
    if not mat: return 0
    a=[[Fraction(t) for t in row] for row in mat]; r=0
    for c in range(len(a[0])):
        p=next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        pivot=a[r][c]
        for j in range(c,len(a[0])):a[r][j]/=pivot
        for i in range(r+1,len(a)):
            if a[i][c]:
                q=a[i][c]
                for j in range(c,len(a[0])):a[i][j]-=q*a[r][j]
        r+=1
        if r==len(a): break
    return r

def validate(n):
    assert n>=4
    # Vertices from nonconstant orientations of edges. Each x_i=(sign_i-sign_(i-1))/2.
    verts=set()
    for s in product((-1,1),repeat=n):
        if len(set(s))==1: continue
        verts.add(tuple((s[i]-s[i-1])//2 for i in range(n)))
    assert len(verts)==(1<<n)-2
    verts=tuple(sorted(verts))
    # Every facet normal is the centered indicator of a cyclic interval S,
    # and its exact support value is one.
    sets=[]
    for a in range(n):
        for k in range(1,n):
            S=frozenset((a+j)%n for j in range(k))
            if S not in sets:sets.append(S)
    assert len(sets)==n*(n-1)
    incidences=[]
    for S in sets:
        dotvals=[sum(v[i] for i in S) for v in verts]
        assert max(dotvals)==1
        incidences.append({i for i,t in enumerate(dotvals) if t==1})
    angles=Counter()
    ridge_pairs=0
    for i,j in combinations(range(len(sets)),2):
        common=incidences[i]&incidences[j]
        if len(common)<n-2:continue
        v0=verts[min(common)]
        rank=rank_integer([[verts[k][s]-v0[s] for s in range(n)] for k in common if k!=min(common)])
        if rank!=n-3:continue
        ridge_pairs+=1
        A,B=sets[i],sets[j]
        # exact cosine squared between unit outward normals
        N=n*len(A&B)-len(A)*len(B)
        assert N>0,(n,A,B,N)
        cos2=Fraction(N*N,len(A)*(n-len(A))*len(B)*(n-len(B)))
        angles[cos2]+=1
    predicted=Counter()
    for a in range(1,n-1):
        for b in range(1,n-a):
            c=n-a-b
            cos2=Fraction(a*c,(a+b)*(b+c))
            predicted[cos2]+=2*n
    assert angles==predicted, (n,angles,predicted)
    assert ridge_pairs==n*(n-1)*(n-2)
    p=((n-1)//2)*((n-1+1)//2)
    assert min(angles)==Fraction(1,(n-1)**2)
    assert max(angles)==Fraction(p,p+n)
    assert angles[min(angles)]==2*n
    assert angles[max(angles)]==(2*n if n%2 else 4*n)
    print(f'CYCLE_RIDGE_PASS n={n} vertices={len(verts)} facets={len(sets)} ridges={ridge_pairs} levels={len(angles)}')

if __name__=='__main__':
    for n in range(4,8): validate(n)
