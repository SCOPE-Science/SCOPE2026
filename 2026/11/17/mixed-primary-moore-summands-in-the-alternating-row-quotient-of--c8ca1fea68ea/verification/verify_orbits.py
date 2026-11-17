#!/usr/bin/env python3
"""Exact cell-orbit and Smith verification for the four-by-seven alternating-row quotient."""
from itertools import combinations, permutations
from collections import Counter
from sympy import SparseMatrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

M=4; N=7
rows=range(M); cols=range(N)
def sign(p):
    return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1
A4=[p for p in permutations(rows) if sign(p)==1]
assert len(A4)==12

def orbit_rep(F):
    return min(tuple((c,p[r]) for c,r in F) for p in A4)

cells={}; reps={}; maps={}
for k in range(1,5):
    faces=[]
    for cs in combinations(cols,k):
        for rs in permutations(rows,k):
            faces.append(tuple(zip(cs,rs)))
    cellset=sorted(set(orbit_rep(f) for f in faces))
    cells[k]=cellset
    maps[k]={f:i for i,f in enumerate(cellset)}
    print('dimension',k-1,'labeled_faces',len(faces),'quotient_cells',len(cellset),'orbit_lengths',dict(Counter(sum(orbit_rep(f)==r for f in faces) for r in cellset)))

boundaries={}
for k in (2,3,4):
    data={}
    for j,F in enumerate(cells[k]):
        for i in range(k):
            sub=F[:i]+F[i+1:]
            rid=maps[k-1][orbit_rep(sub)]
            data[(rid,j)]=data.get((rid,j),0)+(-1)**i
    boundaries[k]=SparseMatrix(len(cells[k-1]),len(cells[k]),data)
assert boundaries[2]*boundaries[3]==SparseMatrix(len(cells[1]),len(cells[3]),{})
assert boundaries[3]*boundaries[4]==SparseMatrix(len(cells[2]),len(cells[4]),{})

# Direct orbit coordinate parity checks against independent combinatorial enumeration.
for k in (1,2,3,4):
    by_column=Counter(tuple(c for c,_ in f) for f in cells[k])
    assert set(by_column.values())==({1} if k<=2 else {2})

smith={};rank={}
for k in (2,3,4):
    Mtx=boundaries[k]
    D=smith_normal_form(Mtx, domain=ZZ)
    factors=Counter(abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]!=0)
    assert all(not(D[i,j]) for i in range(D.rows) for j in range(D.cols) if i!=j)
    rank[k]=sum(factors.values())
    smith[k]=dict(sorted(factors.items()))
    print('boundary',k-1,'matrix_size',(Mtx.rows,Mtx.cols),'SNF',smith[k])
assert [len(cells[k]) for k in (1,2,3,4)]==[7,21,70,70]
assert [rank[k] for k in (2,3,4)]==[6,15,55]
assert smith=={2:{1:6},3:{1:15},4:{1:49,3:5,6:1}}, smith
print('homology H0=Z; H1=0; H2=Z/2 plus (Z/3)^6; H3=Z^15; zero above 3')
print('EXACT_A4_QUOTIENT_CHAIN_SNF_PASS')
