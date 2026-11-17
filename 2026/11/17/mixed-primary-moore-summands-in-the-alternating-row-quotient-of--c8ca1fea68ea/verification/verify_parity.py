#!/usr/bin/env python3
"""Independent parity-cell formula for the A4 row quotient of the 4x7 chessboard."""
from itertools import combinations
from collections import Counter
from sympy import SparseMatrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
N=7
cells={1:list(combinations(range(N),1)),2:list(combinations(range(N),2))}
for k in (3,4): cells[k]=[(S,e) for S in combinations(range(N),k) for e in (+1,-1)]
idx={k:{a:i for i,a in enumerate(v)} for k,v in cells.items()}
mat={}
for k in (2,3,4):
    a={}
    for j,t in enumerate(cells[k]):
        if k<=2: S=t; epsilon=None
        else: S,epsilon=t
        for i in range(k):
            T=S[:i]+S[i+1:]
            if k<=3:
                sub=T if k==2 or k==3 else None
            else: sub=(T,epsilon*((-1)**(3-i)))
            row=idx[k-1][sub]
            a[(row,j)]=a.get((row,j),0)+(-1)**i
    mat[k]=SparseMatrix(len(cells[k-1]),len(cells[k]),a)
assert mat[2]*mat[3]==SparseMatrix(7,70,{})
assert mat[3]*mat[4]==SparseMatrix(21,70,{})
assert [len(cells[k]) for k in range(1,5)]==[7,21,70,70]
expect=[{1:6},{1:15},{1:49,3:5,6:1}]
for k,expected in zip([2,3,4],expect):
    d=smith_normal_form(mat[k],domain=ZZ)
    inv=dict(sorted(Counter(abs(int(d[i,i])) for i in range(min(d.shape)) if d[i,i]!=0).items()))
    assert inv==expected, (k,inv)
    print('PARITY d_%d Smith %s'%(k-1,inv))
print('PARITY_CELL_SNF_PASS')
