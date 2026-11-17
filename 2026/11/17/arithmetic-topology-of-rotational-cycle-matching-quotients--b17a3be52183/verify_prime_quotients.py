#!/usr/bin/env python3
"""Exact cellular integral homology of free prime rotation quotients of cycle matching complexes."""
from collections import defaultdict
from itertools import combinations
from sympy import ZZ, Matrix
from sympy.matrices.normalforms import smith_normal_form

def independent(face,p):
    return all((face[(i+1)%len(face)]-face[i])%p>1 for i in range(len(face))) if len(face)>=2 else True

def valid(face,p):
    s=set(face)
    return all((i+1)%p not in s for i in s)

def canonical(face,p):
    # canonical rotation of a simplex and orientation parity
    f=tuple(sorted(face))
    shifted=[tuple(sorted((a+k)%p for a in f)) for k in range(p)]
    minimum=min(shifted)
    k=shifted.index(minimum)
    unsorted=[(a+k)%p for a in f]
    inversions=sum(unsorted[i]>unsorted[j] for i in range(len(f)) for j in range(i+1,len(f)))
    return minimum, (-1)**inversions

def verify(p):
    cells=defaultdict(dict)
    for length in range(1,(p//2)+1):
        for f in combinations(range(p),length):
            if valid(f,p):
                canon,_=canonical(f,p)
                cells[length-1][canon]=len(cells[length-1]) if canon not in cells[length-1] else cells[length-1][canon]
    # correct indexing: insertion is repeated but positions stable
    dimensions=sorted(cells)
    mats={}
    for k in dimensions[1:]:
        mat=[[0]*len(cells[k]) for _ in range(len(cells[k-1]))]
        for t,j in cells[k].items():
            for a in range(len(t)):
                sub=t[:a]+t[a+1:]
                can,sgn=canonical(sub,p)
                mat[cells[k-1][can]][j]+=(-1)**a*sgn
        mats[k]=Matrix(mat)
    for k in dimensions[2:]:
        assert mats[k-1]*mats[k]==Matrix.zeros(len(cells[k-2]),len(cells[k]))
    dims={}
    for k in dimensions[1:]:
        D=smith_normal_form(mats[k],domain=ZZ)
        diag=[int(D[i,i]) for i in range(min(D.rows,D.cols)) if D[i,i]]
        diag=sorted([abs(s) for s in diag]); dims[k]=diag
    betti={}; tors={}
    for k in dimensions:
        rank_in=len(dims.get(k+1,[]));rank_out=len(dims.get(k,[]))
        betti[k]=len(cells[k])-rank_in-rank_out
        tors[k]=[x for x in dims.get(k+1,[]) if x>1]
    d=(p-2)//3
    for k in dimensions:
        assert betti[k]==(1 if k in (0,d) else 0),(p,k,betti)
        expected=[p] if k%2==1 and 0<k<d else []
        assert tors[k]==expected,(p,k,tors)
    print(f'p={p}; quotient cells={[len(cells[k]) for k in dimensions]}; Betti={betti}; torsion={tors}')
if __name__=='__main__':
    for p in (5,7,11,13):verify(p)
    print('PRIME_CYCLE_ORBIT_SMITH_CHECK_PASS p=5,7,11,13')
