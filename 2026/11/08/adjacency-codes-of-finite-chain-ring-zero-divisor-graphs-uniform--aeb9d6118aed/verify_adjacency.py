#!/usr/bin/env python3
"""Finite calculations for adjacency row spaces of chain-ring zero-divisor graphs.

Requires Python 3 and NumPy. Enumerates polynomial-quotient ring elements and
uses direct quotient multiplication for adjacency, not the valuation shortcut.
These checks are finite illustrations; the accompanying proof is uniform.
"""
from itertools import product
import numpy as np


def mul_f(a, b, q):
    if q != 4:
        return (a*b) % q
    # GF(4)=GF(2)[u]/(u^2+u+1), coefficient bit encoding.
    c=0
    for i in range(2):
        for j in range(2):
            if ((a>>i)&1) and ((b>>j)&1):
                c ^= (1<<(i+j))
    if c & 4:
        c ^= 7  # u^2 = u+1; u^3 never appears in a degree <=2 product.
    return c


def is_zero_product(a,b,q):
    e=len(a)
    c=[0]*e
    if q==4:
        for i,x in enumerate(a):
            for j,y in enumerate(b[:e-i]):
                c[i+j]^=mul_f(x,y,q)
    else:
        for i,x in enumerate(a):
            for j,y in enumerate(b[:e-i]):
                c[i+j]=(c[i+j]+mul_f(x,y,q))%q
    return not any(c)


def valuation(a):
    return next(i for i,x in enumerate(a) if x)


def row_basis(a,p):
    a=(np.asarray(a,dtype=np.int64)%p).copy()
    rows,cols=a.shape
    pivot=[]
    r=0
    for c in range(cols):
        hits=np.flatnonzero(a[r:,c])
        if not len(hits):
            continue
        j=r+int(hits[0]); a[[r,j]]=a[[j,r]]
        a[r]=(a[r]*pow(int(a[r,c]),-1,p))%p
        for i in range(rows):
            if i!=r and a[i,c]:
                a[i]=(a[i]-a[i,c]*a[r])%p
        pivot.append(c);r+=1
        if r==rows:
            break
    return a[:r,:],pivot


def in_span(vec,basis,piv,p):
    v=np.asarray(vec,dtype=np.int64).copy()%p
    for row,c in zip(basis,piv):
        if v[c]:v=(v-v[c]*row)%p
    return not np.any(v)


def case(q,e):
    p=2 if q==4 else q
    all_vectors=product(range(q),repeat=e)
    v=[x for x in all_vectors if x[0]==0 and any(x)]
    v.sort(key=valuation)
    n=len(v)
    assert n==q**(e-1)-1
    val=[valuation(x) for x in v]
    h0=(e+1)//2
    lows=[i for i,z in enumerate(val) if z<h0]
    highs=[i for i,z in enumerate(val) if z>=h0]
    L=len(lows);M=len(highs)
    assert L==q**(e-1)-q**(e//2) and M==q**(e//2)-1
    assert L>=2
    A=np.zeros((n,n),dtype=np.int64)
    for i in range(n):
        for j in range(i+1,n):
            raw=int(is_zero_product(v[i],v[j],q))
            assert raw==int(val[i]+val[j]>=e)
            A[i,j]=A[j,i]=raw
    basis,piv=row_basis(A,p)
    rank=len(basis)
    assert rank==q**(e//2),(q,e,rank)
    rank2=len(row_basis(A@A%p,p)[0])
    assert rank-rank2==1,(q,e,rank,rank2)
    # Check exact dual/kernel parametrization from direct A.
    B=A[np.ix_(lows,highs)]
    for i in range(min(L,10)):
        z=np.zeros(L,dtype=np.int64);z[i]=1;z[(i+1)%L]=-1
        y=B.T@z%p
        w=np.concatenate([z%p,y])
        assert not np.any(A@w%p)
    # Verify complete code-parametrization on independent test generators.
    one=np.ones(L,dtype=np.int64)
    c0=np.concatenate([one,np.zeros(M,dtype=np.int64)])
    assert in_span(c0,basis,piv,p)
    assert not np.any(A@c0%p)
    for j in range(M):
        y=np.zeros(M,dtype=np.int64);y[j]=1
        c=np.concatenate([(-B@y)%p,y])
        assert in_span(c,basis,piv,p)
    # All and only predicted coordinates support weight-one codewords.
    predicted=[idx for idx in highs if (not np.any(B[:,idx-L])) or np.all(B[:,idx-L])]
    actual=[]
    for idx in range(n):
        v1=np.zeros(n,dtype=np.int64);v1[idx]=1
        if in_span(v1,basis,piv,p):actual.append(idx)
    assert actual==predicted,(q,e,actual,predicted)
    expected=(q-1)+(q-1)*q**(e//2-1) if e%2==0 else q-1
    assert len(actual)==expected
    return (q,e,n,rank,rank2,len(actual),p)


def main():
    configs=[(2,e) for e in range(3,9)] + [(3,e) for e in range(3,7)] + [(4,e) for e in range(3,5)] + [(5,e) for e in range(3,5)]
    for q,e in configs:
        result=case(q,e)
        print('CASE q=%d length=%d graph_vertices=%d rank=%d square_rank=%d weight_one_supports=%d char=%d'%result)
    print('VERIFY_OK configurations=%d direct_ring_multiplication=yes rank_hull_code_dual_weight_one_checks=yes'%len(configs))

if __name__=='__main__':main()
