"""Exact finite checks for orientation-weighted Markov spectrum.
Run with Python 3; no third-party dependencies.
The limit theorem's infinite assertions are proved in RESULT.md, not by this script.
"""
from itertools import product
from random import Random
from math import sqrt, erf


def matmul(A,B):
    return [[sum(a*b for a,b in zip(A[i], (B[k][j] for k in range(len(B)))))
             for j in range(len(B[0]))] for i in range(len(A))]


def charpoly(A):
    """Exact coefficients of det(z I-A), via Faddeev-LeVerrier."""
    n=len(A)
    B=[[int(i==j) for j in range(n)] for i in range(n)]
    co=[1]
    for k in range(1,n+1):
        C=matmul(A,B)
        trace=sum(C[i][i] for i in range(n))
        assert trace%k==0
        c=-(trace//k)
        co.append(c)
        B=[[C[i][j]+(c if i==j else 0) for j in range(n)] for i in range(n)]
    return co


def data(eps):
    n=len(eps)
    u=[0]+[int(eps[j-1]==-1 and eps[j]==1) for j in range(1,n)]
    v=[0]+[int(eps[j-1]==1 and eps[j]==-1) for j in range(1,n)]
    M=[[1-u[i] if j==0 else (1-v[i] if j==n-1 else 1)
        for j in range(n)] for i in range(n)]
    S=[[eps[i]*a for a in row] for i,row in enumerate(M)]
    E=sum(eps); A=sum(u); B=sum(v); a=u[-1]; b=v[-1]
    H=[[E,-A,B],[eps[0],0,0],[eps[-1],-a,b]]
    return S,H,E,A,B,a,b


for n in range(3,10):
    for eps in product((-1,1), repeat=n):
        S,H,E,A,B,a,b=data(eps)
        p=charpoly(S)
        q=charpoly(H)
        assert p==q+[0]*(n-3), (n,eps,p,q)
        assert q==[1,-E-b,A*eps[0]-B*eps[-1]+E*b,
                   -A*b*eps[0]+B*a*eps[0]]
        assert a+b<=1
print('PASS: 1016 orientation words, exact full characteristic polynomials and cubic identities (n=3..9).')

rng=Random(89125)
for n in (100,1000,10000):
    k=200 if n<=1000 else 50
    Z=[]; al=[]; bl=[]; endpoint=[]
    for _ in range(k):
        eps=[1 if rng.getrandbits(1) else -1 for _ in range(n)]
        A=sum(eps[j-1]<eps[j] for j in range(1,n))
        B=sum(eps[j-1]>eps[j] for j in range(1,n))
        Z.append(sum(eps)/sqrt(n));al.append(A/n);bl.append(B/n)
        endpoint.append((eps[0],eps[-1]))
    mean_sq=sum(x*x for x in Z)/k
    avA=sum(al)/k;avB=sum(bl)/k
    assert 0.6 < mean_sq < 1.5
    assert abs(avA-0.25)<0.025 and abs(avB-0.25)<0.025
    print('PASS: n=%d, E(Z_n^2) sample %.4f, mean(A/n) %.4f, mean(B/n) %.4f'
          %(n,mean_sq,avA,avB))
print('Analytic limiting atom mass erf(1)/4 = %.12f' % (erf(1)/4))
print('The Gaussian-mixture limit is a proof consequence, not certified by simulation.')
