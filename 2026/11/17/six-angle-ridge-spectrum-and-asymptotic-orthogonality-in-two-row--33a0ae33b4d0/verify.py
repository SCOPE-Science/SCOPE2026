"""Standalone finite checks of the two-row generalized Pitman--Stanley ridge law.
Run with Python 3, numpy, scipy and sympy: python verify.py.
These finite tests supplement, but do not replace, the all-m proof.
"""
from collections import Counter
from itertools import combinations
import numpy as np
from scipy.optimize import linprog
from sympy import Matrix, Rational


def inequalities(m):
    d = 2*m
    rows, bounds, names = [], [], []
    def add(name, entries, rhs=0):
        r = [0]*d
        for coordinate, coefficient in entries:
            r[coordinate] += coefficient
        rows.append(r); bounds.append(rhs); names.append(name)
    add('A',[(m-1,-1)])
    for j in range(m):add(f'B{j+1}',[(m+j,-1)])
    for j in range(m-1):add(f'C{j+1}',[(j,-1),(j+1,1)])
    for j in range(m-1):add(f'D{j+1}',[(j,-1),(m+j,-1),(j+1,1),(m+j+1,1)])
    add('E',[(0,1)],1)
    add('F',[(0,1),(m,1)],2)
    return np.array(rows,dtype=int), np.array(bounds,dtype=int), names


def predicted_nonridges(m):
    forbidden = {frozenset(('B1','F'))}
    for j in range(1,m):
        forbidden.add(frozenset((f'B{j}',f'C{j}')))
        forbidden.add(frozenset((f'B{j+1}',f'D{j}')))
    return forbidden


def spectrum(m):
    A,b,names=inequalities(m)
    excluded=predicted_nonridges(m)
    h=Counter()
    for i,j in combinations(range(len(names)),2):
        if frozenset((names[i],names[j])) in excluded:continue
        dot=int(A[i]@A[j]);normproduct=int((A[i]@A[i])*(A[j]@A[j]))
        # Distinguished classes of outer-normal cosines.
        if dot==0:key='0'
        elif dot==-1 and normproduct==2:key='-sqrt2/2'
        elif dot==-1 and normproduct==4:key='-1/2'
        elif dot==-2 and normproduct==16:key='-1/2'
        elif dot==-1 and normproduct==8:key='-sqrt2/4'
        elif dot==-2 and normproduct==8:key='-sqrt2/2'
        elif dot==1 and normproduct==4:key='1/2'
        elif dot==2 and normproduct==8:key='sqrt2/2'
        elif dot==1 and normproduct==2:key='sqrt2/2'
        else:raise AssertionError((m,names[i],names[j],dot,normproduct))
        h[key]+=1
    expected={'0':(9*m*m-13*m+8)//2,
              '-1/2':2*m-1,'-sqrt2/2':3,'-sqrt2/4':2*m-4,
              '1/2':m-1,'sqrt2/2':m}
    assert all(h[k]==v for k,v in expected.items()),(m,h,expected)
    assert sum(h.values())==(9*m*m-m+2)//2
    return h


def ridge_lp(m):
    a,b,names=inequalities(m)
    n=2*m; not_ridges=set()
    for i,j in combinations(range(len(names)),2):
        rest=[k for k in range(len(names)) if k not in (i,j)]
        # Maximize common slack for all other listed facets while imposing both equalities.
        # Variables (x_1,...,x_2m,t) have unrestricted x, t in [0,1].
        U=np.column_stack([a[rest].astype(float),np.ones(len(rest))])
        E=np.column_stack([a[[i,j]].astype(float),np.zeros(2)])
        objective=np.r_[np.zeros(n),-1.]
        sol=linprog(objective,A_ub=U,b_ub=b[rest],A_eq=E,b_eq=b[[i,j]],
                    bounds=[(None,None)]*n+[(0,1)],method='highs')
        if sol.status==2: not_ridges.add(frozenset((names[i],names[j]))); continue
        assert sol.success,(m,i,j,sol.message)
        if sol.x[-1]<1e-7:not_ridges.add(frozenset((names[i],names[j])))
    assert not_ridges==predicted_nonridges(m),(m,not_ridges)


def exact_vertices(m):
    A,b,names=inequalities(m)
    d=2*m
    out=set()
    for idx in combinations(range(len(names)),d):
        M=Matrix(A[list(idx)].tolist())
        if M.det()==0:continue
        x=M.inv()*Matrix(b[list(idx)].tolist())
        if all((Matrix([int(v) for v in row]).dot(x)<=int(rhs)) for row,rhs in zip(A,b)):
            out.add(tuple(x))
    return out

def exact_ridge_incidence(m):
    A,b,names=inequalities(m)
    vertices=exact_vertices(m)
    expected=predicted_nonridges(m)
    for i,j in combinations(range(len(names)),2):
        face=[v for v in vertices if sum(int(z)*w for z,w in zip(A[i],v))==b[i]
              and sum(int(z)*w for z,w in zip(A[j],v))==b[j]]
        affine_rank=(Matrix([[w[k]-face[0][k] for k in range(2*m)] for w in face[1:]]).rank()
                     if face else -1)
        is_ridge=affine_rank==2*m-2
        assert is_ridge == (frozenset((names[i],names[j])) not in expected), (m,names[i],names[j],affine_rank)
    print(f'EXACT_VERTEX_AND_RIDGE_PASS m={m} vertices={len(vertices)}')

if __name__=='__main__':
    for m in range(2,33):spectrum(m)
    for m in range(2,9):ridge_lp(m)
    for m in (2,3):exact_ridge_incidence(m)
    print('TWO_ROW_PS_RIDGE_ANGLE_PASS angle_counts_m=2..32 strict_LP_m=2..8 exact_vertices_m=2,3')
