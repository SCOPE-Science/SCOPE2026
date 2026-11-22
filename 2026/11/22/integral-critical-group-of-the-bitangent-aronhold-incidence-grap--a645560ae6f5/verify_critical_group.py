"""Reproduce the integral sandpile calculation for the bitangent–Aronhold graph.
Requires NumPy; run alongside verify_aronhold_octad.py. Integer modular arithmetic only.
"""
import numpy as np
from collections import Counter
from verify_aronhold_octad import graph_family


def reduced_laplacian():
    heptads=sorted(graph_family())
    L=np.zeros((316,316),dtype=np.int64)
    B=np.zeros((28,288),dtype=np.int64)
    for j,h in enumerate(heptads):
        node=28+j
        for bitangent in h:
            B[bitangent,j]=1
            L[bitangent,bitangent]+=1
            L[node,node]+=1
            L[bitangent,node]-=1
            L[node,bitangent]-=1
    assert len(heptads)==288
    assert set(B.sum(axis=1))=={72} and set(B.sum(axis=0))=={7}
    assert np.array_equal(B@B.T,56*np.eye(28,dtype=np.int64)+16*np.ones((28,28),dtype=np.int64))
    assert (L==L.T).all() and np.all(L.sum(axis=1)==0)
    return L


def local_valuations(matrix,prime,precision=10):
    """Smith pivot valuations over Z/(prime^precision) with exact unit operations.

    A unit pivot permits both a row and a column unimodular elimination.
    When all remaining entries are divisible by prime, divide the whole
    residual block and record an additional valuation.  Failure on a
    zero residual block signals insufficient modular precision.
    Integer intermediate products remain below 2^63 for the chosen moduli.
    """
    modulus=prime**precision
    a=(matrix.copy()%modulus).astype(np.int64)
    n=a.shape[0];k=0;valuation=0;found=[]
    while k<n:
        trailing=a[k:,k:]
        nonzero=np.argwhere(trailing%prime != 0)
        if len(nonzero)==0:
            if not trailing.any():raise ArithmeticError('modular precision exhausted')
            a[k:,k:]=trailing//prime
            modulus//=prime;valuation+=1
            continue
        i,j=(nonzero[0]+k).tolist()
        if i!=k:a[[k,i],:]=a[[i,k],:]
        if j!=k:a[:,[k,j]]=a[:,[j,k]]
        inv=pow(int(a[k,k]),-1,modulus)
        if k+1<n:
            col=a[k+1:,k].copy();row=a[k,k+1:].copy()
            correction=((col[:,None]*row[None,:])%modulus*inv)%modulus
            a[k+1:,k+1:]=(a[k+1:,k+1:]-correction)%modulus
            a[k+1:,k]=0;a[k,k+1:]=0
        found.append(valuation)
        k+=1
    assert len(found)==n
    return dict(sorted(Counter(found).items()))


def main():
    L=reduced_laplacian()
    expected={2:{0:288,4:1,6:26},7:{0:54,1:235,2:26}}
    for root in (0,1,28,315):
        minor=np.delete(np.delete(L,root,axis=0),root,axis=1)
        for p,c in expected.items():
            observed=local_valuations(minor,p)
            assert observed==c,(root,p,observed)
    assert sum(e*m for e,m in expected[2].items())==160
    assert sum(e*m for e,m in expected[7].items())==287
    print('ARONHOLD_BITANGENT_CRITICAL_GROUP_SMITH_VERIFIED_OK')
    print('2-primary: Z/16 + (Z/64)^26; 7-primary: (Z/7)^235 + (Z/49)^26')
    print('spanning trees: 2^160 * 7^287')

if __name__=='__main__':main()
