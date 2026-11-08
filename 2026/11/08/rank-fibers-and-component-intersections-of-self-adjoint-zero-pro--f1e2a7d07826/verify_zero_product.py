#!/usr/bin/env python3
"""Exhaustively compare self-adjoint zero-product rank fibers with the closed formula.

This standalone program needs Python 3 and NumPy; all computations are finite.
"""
from itertools import product
from math import prod
import numpy as np


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    top = prod(q**(n-i)-1 for i in range(k))
    bot = prod(q**(k-i)-1 for i in range(k))
    return top//bot


def invertible_symmetric_count(m,q):
    # Equivalent to the MacWilliams product, evaluated with integer arithmetic.
    num = q**(m*(m+1)//2)
    num *= prod(q**(2*i-1)-1 for i in range(1,(m+1)//2+1))
    den = prod(q**(2*i-1) for i in range(1,(m+1)//2+1))
    assert num%den == 0
    return num//den


def prediction(n,q):
    return {(a,b): gaussian(n,a,q)*gaussian(n-a,b,q)*
            invertible_symmetric_count(a,q)*invertible_symmetric_count(b,q)
            for a in range(n+1) for b in range(n-a+1)}


def all_symmetric_matrices(n,q):
    inds=[(i,j) for i in range(n) for j in range(i,n)]
    result=np.zeros((q**len(inds),n,n),dtype=np.int64)
    for index, tup in enumerate(product(range(q),repeat=len(inds))):
        for (i,j),val in zip(inds,tup):
            result[index,i,j]=val
            result[index,j,i]=val
    return result


def rank_prime(M,p):
    a=(M%p).astype(np.int64).copy()
    h,w=a.shape
    r=0
    for c in range(w):
        z=next((i for i in range(r,h) if a[i,c]),None)
        if z is None: continue
        a[[r,z]]=a[[z,r]]
        a[r] = a[r] * pow(int(a[r,c]),-1,p) % p
        for i in range(h):
            if i!=r and a[i,c]:
                a[i]=(a[i]-a[i,c]*a[r])%p
        r+=1
        if r==h: break
    return r


def enumerate_prime(n,p,G=None):
    H=all_symmetric_matrices(n,p)
    if G is None:
        mats=H
    else:
        # For these exact tests, n=2, and the supplied matrices are self-inverse.
        assert np.array_equal((G@G)%p,np.eye(n,dtype=np.int64))
        mats=np.einsum('ij,bjk->bik',G,H)%p
        assert all(np.array_equal((G@A).T%p, (G@A)%p) for A in mats)
    ranks=np.array([rank_prime(M,p) for M in mats])
    observed={(a,b):0 for a in range(n+1) for b in range(n-a+1)}
    for a,A in zip(ranks,mats):
        products=np.einsum('ij,bjk->bik',A,mats)%p
        good=~np.any(products!=0,axis=(1,2))
        for b in range(n-a+1):
            observed[(int(a),b)] += int(np.sum(good & (ranks==b)))
    expected=prediction(n,p)
    assert observed==expected,(n,p,observed,expected)
    return sum(observed.values()), sorted((key,v) for key,v in observed.items() if v)


def gf4_mult(x,y):
    raw=0
    for i in range(2):
        if (y>>i)&1:raw ^= x<<i
    for i in (2,):
        if raw&(1<<i): raw ^= 0b111<<(i-2)
    return raw


def gf4_matmul(A,B):
    n=len(A)
    return [[gf4_mult(A[i][k],B[k][j]) ^ gf4_mult(A[i][1-k],B[1-k][j])
             for j in range(n)] for i in range(n) for k in (0,)]


def gf4_rank(M):
    # n=2: nonzero determinant iff full rank.
    if gf4_mult(M[0][0],M[1][1])^gf4_mult(M[0][1],M[1][0]):return 2
    return 1 if any(any(row) for row in M) else 0


def test_gf4_n2():
    matrices=[[[a,b],[b,c]] for a,b,c in product(range(4),repeat=3)]
    ranks=[gf4_rank(A) for A in matrices]
    obs={(a,b):0 for a in range(3) for b in range(3-a)}
    for a,A in zip(ranks,matrices):
        for b,B in zip(ranks,matrices):
            if not any(any(row) for row in gf4_matmul(A,B)):
                obs[(a,b)]+=1
    exp=prediction(2,4)
    assert obs==exp,(obs,exp)
    return sum(obs.values()),obs


if __name__ == '__main__':
    for n,p in [(1,2),(2,2),(3,2),(4,2),(2,3),(3,3),(2,5)]:
        total,profile=enumerate_prime(n,p)
        print('PRIME',n,p,'TOTAL',total,'NONZERO_RANK_FIBERS',profile)
    for p,G in [(2,np.array([[0,1],[1,0]])),(3,np.array([[1,0],[0,2]]))]:
        total,profile=enumerate_prime(2,p,G)
        print('NONSTANDARD_FORM',p,'TOTAL',total,'RANK_FIBERS',profile)
    total,profile=test_gf4_n2()
    print('EXTENSION_GF4',2,'TOTAL',total,'RANK_FIBERS',sorted(profile.items()))
    print('ALL_SELFADJOINT_ZERO_PRODUCT_TESTS_PASS')
