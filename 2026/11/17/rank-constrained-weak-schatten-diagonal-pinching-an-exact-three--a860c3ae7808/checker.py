"""Finite numerical diagnostics for rank-constrained weak-Schatten diagonal pinching.

Analytical proof, not sampling, establishes the theorem for every dimension and exponent.
"""
import math
import numpy as np
from fractions import Fraction


def wnorm(A, p):
    v = np.linalg.svd(A, compute_uv=False)
    q = 1.0 / p
    return max((i+1)**q * x for i, x in enumerate(v))


def norm_diagonal(A, p):
    v = sorted((abs(x) for x in np.diag(A)), reverse=True)
    q = 1.0 / p
    return max((i+1)**q * x for i, x in enumerate(v))


def predicted(n, r, p):
    q = 1.0 / p
    h = sum(j**(-q) for j in range(1, r+1))
    if p < 1:
        return n**(q-1) * h
    if p == 1:
        return h
    return r**(q-1) * h


def fourier(k):
    i = np.arange(k)
    return np.exp(2j * np.pi * np.outer(i, i)/k) / np.sqrt(k)


def witness(n,r,p,k=None):
    if k is None: k = n if p < 1 else r
    assert r <= k <= n
    q=1/p
    z=np.zeros(n,dtype=np.float64)
    z[:r]=np.arange(1,r+1)**(-q)
    F=fourier(k)
    A=np.zeros((n,n),dtype=complex)
    A[:k,:k]=(F * z[:k]) @ F.conj().T
    return A


def exact_rational_boundary(n,r):
    h=sum((Fraction(1,j) for j in range(1,r+1)),Fraction(0))
    h2=sum((Fraction(1,j*j) for j in range(1,r+1)),Fraction(0))
    assert predicted(n,r,1)==float(h) or abs(predicted(n,r,1)-float(h))<1e-12
    assert abs(predicted(n,r,.5)-float(n*h2))<1e-12
    return 2


def main():
    rng=np.random.default_rng(174918)
    tests=0
    for n in range(1,13):
        for r in range(1,n+1):
            tests+=exact_rational_boundary(n,r)
            for p in [0.5,0.75,1.0,1.5,2.,4.]:
                c=predicted(n,r,p)
                A=witness(n,r,p)
                ratio=norm_diagonal(A,p)/wnorm(A,p)
                assert np.isclose(ratio,c,atol=5e-11,rtol=5e-11),(n,r,p,ratio,c)
                tests+=1
                if p==1:
                    for k in range(r,n+1):
                        A=witness(n,r,p,k)
                        ratio=norm_diagonal(A,p)/wnorm(A,p)
                        assert np.isclose(ratio,c,atol=5e-11,rtol=5e-11)
                        tests+=1
                for _ in range(12):
                    X=rng.normal(size=(n,r))+1j*rng.normal(size=(n,r))
                    Y=rng.normal(size=(n,r))+1j*rng.normal(size=(n,r))
                    A=X@Y.conj().T
                    base=wnorm(A,p)
                    if base>1e-12:
                        ratio=norm_diagonal(A,p)/base
                        assert ratio <= c+3e-10,(n,r,p,ratio,c)
                    tests+=1
    for q in [0.02,.2,.5,.99,1.0,1.01,1.5,3.0]:
        previous=0.0
        H=0.0
        for k in range(1,2001):
            H+=k**(-q)
            current=k**(q-1)*H
            assert current>previous-2e-12
            previous=current
            tests+=1
    print('FINITE_WEAK_PINCH_OK',tests,'checks')

if __name__=='__main__': main()
