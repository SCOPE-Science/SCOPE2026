#!/usr/bin/env python3
"""Reproduce exact Gram predictions for coordinate Fourier frames on invertible matrices."""
from itertools import product
import math
from fractions import Fraction
import numpy as np


def field_add(x, y, q):
    return x ^ y if q == 4 else (x + y) % q


def field_sub(x, y, q):
    return x ^ y if q == 4 else (x - y) % q


def field_mul(x, y, q):
    if q != 4:
        return (x*y) % q
    acc = 0
    while y:
        if y & 1:
            acc ^= x
        y >>= 1
        x <<= 1
        if x & 4:
            x ^= 7  # X^2 = X + 1 over GF(2)
    return acc


def nonzero_determinant(flat, m, q):
    rows = [[flat[i*m+j] for j in range(m)] for i in range(m)]
    rank = 0
    for col in range(m):
        p = next((i for i in range(rank, m) if rows[i][col]), None)
        if p is None:
            return False
        rows[rank], rows[p] = rows[p], rows[rank]
        x = rows[rank][col]
        # Scale-free elimination using invertibility of nonzero field elements.
        for i in range(rank+1,m):
            factor = rows[i][col]
            if not factor:
                continue
            for j in range(col, m):
                rows[i][j] = field_sub(field_mul(x, rows[i][j], q), field_mul(factor, rows[rank][j], q), q)
        rank += 1
    return rank == m


def additive_character(a, q):
    if q == 4:
        square = field_mul(a, a, 4)
        tr = field_add(a, square, 4)
        assert tr in (0,1)
        return -1.0 if tr else 1.0
    return np.exp(2j*math.pi*a/q)


def predicted(m,q):
    alpha = -1.0/(q**m-1)
    beta = 1.0/((q**m-1)*(q**(m-1)-1))
    a=-alpha
    g=-m*math.sqrt(q-1)*a
    b=1+a+(q-1)*(-a*(2*m-1)+beta*(m-1)**2)
    lo,hi=np.linalg.eigvalsh([[1,g],[g,b]])
    contr=1+a
    row=1+a-(q-1)*(a+beta)*(m-1)
    double=1+a+(q-1)*(a+beta)
    spectrum=([lo,hi]+[contr]*(m*m*(q-2))
              +[row]*(2*(m-1))+[double]*((m-1)**2))
    return np.array(sorted(spectrum)), dict(lo=lo,hi=hi,contrast=contr,row=row,double=double,alpha=alpha,beta=beta)


def exact_threshold_sign(q,m):
    e=q**(m-1)-1
    z=(Fraction(q,1)+Fraction(q-1,e))*(2-Fraction(m-2,e))-m
    return z<0


def verify_case(q,m):
    xs=[x for x in product(range(q),repeat=m*m) if nonzero_determinant(x,m,q)]
    expected_size=math.prod(q**m-q**j for j in range(m))
    assert len(xs)==expected_size,(q,m,len(xs),expected_size)
    cols=[np.ones(len(xs),dtype=complex)]
    labels=[('constant',0)]
    for pos in range(m*m):
        for a in range(1,q):
            cols.append(np.array([additive_character(field_mul(a,x[pos],q),q) for x in xs], dtype=complex))
            labels.append((pos,a))
    F=np.column_stack(cols)
    actual_G=(F.conj().T@F)/len(xs)
    a=-1/(q**m-1); b=1/((q**m-1)*(q**(m-1)-1))
    expected_G=np.eye(len(labels),dtype=float)
    for i,(v,av) in enumerate(labels):
        for j,(w,aw) in enumerate(labels):
            if i==j: continue
            if i==0 or j==0 or v==w:
                expected_G[i,j]=a
            elif v//m==w//m or v%m==w%m:
                expected_G[i,j]=a
            else:
                expected_G[i,j]=b
    gramerr=np.max(np.abs(actual_G-expected_G))
    expected_eigs, p=predicted(m,q)
    eigerr=np.max(np.abs(np.linalg.eigvalsh(actual_G)-expected_eigs))
    assert gramerr<2e-11 and eigerr<2e-11, (q,m,gramerr,eigerr)
    assert p['lo']>0
    assert (p['hi']>p['double'])==(m>=2*q)
    return q,m,len(xs),len(labels),float(gramerr),float(eigerr),round(float(p['hi']-p['double']),7)


def main():
    cases=[(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(5,2),(7,2)]
    rows=[verify_case(q,m) for q,m in cases]
    for row in rows:
        print('CASE',row)
    for q in [2,3,4,5,7,8,9,11,16,25,27,32]:
        for m in range(2,50):
            vals,p=predicted(m,q)
            assert p['lo']>0 and min(vals)==p['lo']
            assert exact_threshold_sign(q,m)==(m>=2*q)
    print('VERIFY_OK direct_Gram_and_eigenvalue_cases=%d tested_inequality_pairs=%d fields_include_GF4=YES sharp_transition=PASS'%(len(cases),12*48))

if __name__=='__main__':
    main()
