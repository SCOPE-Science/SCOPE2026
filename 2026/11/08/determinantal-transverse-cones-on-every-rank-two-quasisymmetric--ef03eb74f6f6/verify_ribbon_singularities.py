#!/usr/bin/env python3
"""Independent finite lattice and finite-field checks for rank-two ribbon charts.
The geometric proof of the all-parameter theorem is separate.
"""
from fractions import Fraction
from itertools import product
from math import comb

def rank(matrix):
    if not matrix: return 0
    m=[[Fraction(v) for v in row] for row in matrix]
    rows, cols=len(m),len(m[0]); rr=0
    for cc in range(cols):
        k=next((i for i in range(rr,rows) if m[i][cc]!=0),None)
        if k is None: continue
        m[rr],m[k]=m[k],m[rr]
        c=m[rr][cc]
        for j in range(cc,cols): m[rr][j]/=c
        for i in range(rows):
            if i!=rr and m[i][cc]:
                c=m[i][cc]
                for j in range(cc,cols): m[i][j]-=c*m[rr][j]
        rr+=1
        if rr==rows: break
    return rr

def vector(n,i,j):
    z=[0]*n; z[i]+=1;z[j]-=1;return z

def rank_columns(cs):
    return rank([[col[i] for col in cs] for i in range(len(cs[0]))])

cases=0
for a in range(1,9):
    for b in range(1,9):
        n=a+b+1
        left=list(range(b));center=b;right=list(range(b+1,n))
        # Plucker weights are e_i+e_j. Every affine generator is the difference of two weights.
        def difference(pair1,pair2):
            z=[0]*n
            for i in pair1:z[i]+=1
            for i in pair2:z[i]-=1
            return z
        U=[difference((i,center),(left[0],center)) for i in left[1:]]
        V=[difference((center,j),(left[0],center)) for j in right]
        W=[difference((left[0],j),(left[0],center)) for j in right]
        assert rank_columns(U+V+W)==a+b
        assert rank_columns(V+W)==a+1
        # Their relations are precisely 2 by a rank-one minors, of independent rank a-1.
        rel=[]
        for j in range(1,a):
            z=[V[0][i]+W[j][i]-V[j][i]-W[0][i] for i in range(n)]
            assert z==[0]*n
            rel.append(j)
        assert len(rel)==a-1
        # A chart with W_(first-left, first-right) nonzero is a polynomial affine space.
        B=[difference((i,right[0]),(left[0],right[0])) for i in left[1:]]
        B += [difference((left[0],j),(left[0],right[0])) for j in right[1:]]
        B += [difference((left[0],center),(left[0],right[0])),
              difference((center,right[0]),(left[0],right[0]))]
        assert len(B)==a+b and rank_columns(B)==a+b
        cases+=1
print('LATTICE_CHART_RANKS_OK',cases,'(a,b) pairs; all chart generators checked')
for a in range(1,8):
    actual=0
    for data in product((0,1),repeat=2*a):
        v=data[:a];w=data[a:]
        if all((v[i]*w[j]-v[j]*w[i])%2==0 for i in range(a) for j in range(i+1,a)):
            actual+=1
    expected=1+3*(2**a-1)
    assert actual==expected,(a,actual,expected)
    # Cone over P1 x P^(a-1) has degree a (computed from its graded Hilbert function).
    hs=[(d+1)*comb(d+a-1,a-1) for d in range(a+3)]
    diff=hs[:]
    for _ in range(a):diff=[diff[j+1]-diff[j] for j in range(len(diff)-1)]
    assert all(x==a for x in diff)
print('GF2_RANK_ONE_CONES_OK a=1..7; Segre Hilbert multiplicity matches a')
print('RIBBON_SINGULARITY_CHART_VERIFIER_OK')
