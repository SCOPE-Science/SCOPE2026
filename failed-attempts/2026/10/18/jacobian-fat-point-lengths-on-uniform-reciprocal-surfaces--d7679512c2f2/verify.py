#!/usr/bin/env python3
"""Reproducible finite symbolic checks for uniform reciprocal surface local models.

These checks do not substitute for the characteristic-zero invariant-theoretic proof.
"""
from itertools import combinations
from math import comb
import sympy as sp

def check_hankel(r):
    x=sp.symbols('x0:'+str(r+1)); u,v=sp.symbols('u v')
    q=[]
    for a,b in combinations(range(r),2):
        q.append(x[a]*x[b+1]-x[a+1]*x[b])
    J=sp.Matrix([[sp.diff(t,z) for z in x] for t in q])
    k=r-1
    imgs=set()
    subs={x[i]:u**(r-i)*v**i for i in range(r+1)}
    for rows in combinations(range(len(q)),k):
        for cols in combinations(range(r+1),k):
            f=sp.expand(J.extract(rows,cols).det().subs(subs,simultaneous=True))
            if f:
                imgs.add(f)
    vecs=[]
    for f in imgs:
        pp=sp.Poly(f,u,v)
        vecs.append([pp.coeff_monomial(u**(r*k-i)*v**i) for i in range(r*k+1)])
    rank=sp.Matrix(vecs).rank()
    assert rank==r*k+1,(r,rank,r*k+1)
    # Explicit triangular Jacobian determinant
    special=[x[0]*x[j+1]-x[1]*x[j] for j in range(1,r)]
    sub=sp.Matrix([[sp.diff(t,z) for z in x[2:]] for t in special])
    assert sp.expand(sub.det()-x[0]**(r-1))==0
    return len(imgs),rank

def check_inverse_basis(r):
    u,v=sp.symbols('u v')
    # Every pair of the r+1 forms u+j*v is nonproportional.
    L=[u+j*v for j in range(1,r+2)]
    rows=[]
    for j in range(r+1):
        F=sp.prod(L[:j]+L[j+1:])
        P=sp.Poly(sp.expand(F),u,v)
        rows.append([P.coeff_monomial(u**(r-i)*v**i) for i in range(r+1)])
    determinant=sp.Matrix(rows).det()
    assert determinant !=0
    return determinant

def run():
    for r in (2,3,4):
        n=r+2
        cnt,rank=check_hankel(r)
        det=check_inverse_basis(r)
        length=sum(r*d+1 for d in range(r-1))
        expression=(r-1)*(2+r*(r-2))//2
        assert length==expression
        print(f'r={r} n={n} minor_images={cnt} span_rank={rank} inverse_basis_det={det} local_length={length} total_length={n*length}')
    for r in range(2,32):
        assert sum(r*d+1 for d in range(r-1))==(r-1)*(2+r*(r-2))//2
    print('VERIFY_OK: characteristic-zero proof supported; tests are finite only')

if __name__=='__main__':run()
