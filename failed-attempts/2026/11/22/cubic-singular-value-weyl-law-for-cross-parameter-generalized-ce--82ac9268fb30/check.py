"""Reproduce finite identities and supplementary diagnostics for Cesaro cross-parameter commutators.
Run: python check.py. Requires NumPy for the optional finite spectral diagnostics.
The infinite-dimensional spectral law is proved in RESULT.md, not by this script.
"""
from fractions import Fraction as F
import math


def mm(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), F(0))
             for j in range(n)] for i in range(n)]


def matrix_c(t, n):
    return [[t**(i-j)/F(i+1) if i >= j else F(0)
             for j in range(n)] for i in range(n)]


def matrices_product(a, b):
    n = len(a)
    return [[a[i][j]-b[i][j] for j in range(n)] for i in range(n)]


def formula_k(t, s, n):
    B = [[(F(1,i+1) if i==j else F(0)) for j in range(n)] for i in range(n)]
    S = [[(F(1) if i==j+1 else F(0)) for j in range(n)] for i in range(n)]
    Q = matrices_product(mm(S,B),mm(B,S))
    def inv_shift(u):
        return [[u**(i-j) if i>=j else F(0) for j in range(n)] for i in range(n)]
    R=mm(inv_shift(t),inv_shift(s))
    return [[(t-s)*z for z in row] for row in mm(mm(mm(B,R),Q),R)]


def exact_tests():
    tests=0
    for s,t in [(F(0),F(1,2)),(F(1,4),F(2,3)),(F(3,7),F(3,5)),(F(1,3),F(1,3))]:
        n=9
        C_t=matrix_c(t,n);C_s=matrix_c(s,n)
        direct=matrices_product(mm(C_t,C_s),mm(C_s,C_t))
        factor=formula_k(t,s,n)
        assert direct==factor
        tests+=n*n
        for k in range(n-1):
            assert direct[k+1][k]==(t-s)*F(1,(k+1)*(k+2)**2)
            tests+=1
        assert all(direct[i][j]==0 for i in range(n) for j in range(i,n))
        tests+=1
    print('exact rational matrix / factor / diagonal assertions:',tests)


def numerical_tests():
    import numpy as np
    from numpy.linalg import svd
    n=300
    j=np.arange(n,dtype=float)
    mask=j[:,None]>=j[None,:]
    delta=np.maximum(j[:,None]-j[None,:],0)
    theta=np.arange(8192)*2*math.pi/8192
    for t,s in [(0.2,0.6),(0,0.5),(0.3,0.7)]:
        C=lambda u: mask*np.power(u,delta)/(j[:,None]+1)
        K=C(t)@C(s)-C(s)@C(t)
        sv=svd(K,compute_uv=False)
        integrand=((1-2*t*np.cos(theta)+t*t)*(1-2*s*np.cos(theta)+s*s))**(-1/3)
        const=abs(t-s)*np.mean(integrand)**3
        ratios=[float((k**3)*sv[k-1]/const) for k in (25,60,100)]
        assert all(0.70 < val < 1.15 for val in ratios), (t,s,ratios)
        assert np.max(np.abs(np.triu(K))) < 1e-12
        print('t,s =',t,s,'Weyl coefficient =',round(float(const),10),
              'finite n^3*s_n/coefficient at n=25,60,100 =',*[round(x,4) for x in ratios])


if __name__=='__main__':
    exact_tests()
    numerical_tests()
    print('PASS: all finite supplementary checks')
