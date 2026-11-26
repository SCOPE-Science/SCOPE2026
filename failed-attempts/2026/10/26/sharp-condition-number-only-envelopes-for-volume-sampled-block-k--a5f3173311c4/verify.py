"""Independent exact-arithmetic and direct-geometry tests for the volume-projection condition-number envelopes.

Run: python verify.py
Only numerical mathematics is implemented; generality comes from the proof.
"""
from itertools import product, combinations
from math import comb, sqrt
from fractions import Fraction
import numpy as np


def e(values, k):
    if k < 0 or k > len(values):
        return 0
    acc = 0
    for inds in combinations(range(len(values)), k):
        prod_ = 1
        for i in inds:
            prod_ *= values[i]
        acc += prod_
    return acc


def spectrum(values, k):
    denom = e(values,k)
    assert denom > 0
    return [Fraction(values[i] * e(values[:i] + values[i+1:],k-1),denom) for i in range(len(values))]


def bounds(N,k,K):
    # min_mu,max_mu,min_condition,max_condition
    return (
       Fraction(k,k+(N-k)*K),
       Fraction(k*(N-k+(k-1)*K),(N-1)*(N-k+k*K)),
       Fraction(K*(N-1),N-k+(k-1)*K),
       Fraction((N-k)*K+k-1,N-1),
    )


def exact_exhaustive():
    n_checks=0
    tested=0
    for N in range(2,8):
        for K in range(1,6):
            if (K-1)**(N-2)>40000:
                continue
            for interior in product(range(1,K+1),repeat=N-2):
                vals=sorted([1,*interior,K])
                for k in range(1,N+1):
                    p=spectrum(vals,k)
                    assert sum(p)==k
                    assert list(sorted(p))==p
                    mu=min(p)
                    chi=max(p)/min(p)
                    mumin,mumax,chimin,chimax=bounds(N,k,K)
                    assert mumin<=mu<=mumax,(N,K,k,vals,mumin,mu,mumax)
                    assert chimin<=chi<=chimax,(N,K,k,vals,chimin,chi,chimax)
                    n_checks+=4
                tested+=1
            for k in range(1,N+1):
                low=[1]+[K]*(N-1)
                high=[1]*(N-1)+[K]
                Plo=spectrum(low,k)
                Phi=spectrum(high,k)
                mumin,mumax,chimin,chimax=bounds(N,k,K)
                assert min(Plo)==mumin
                assert min(Phi)==mumax
                assert max(Phi)/min(Phi)==chimin
                assert max(Plo)/min(Plo)==chimax
                n_checks+=4
    return tested,n_checks


def geometry_tests():
    rng=np.random.default_rng(20261024)
    count=0
    worst=0.
    for N in range(2,8):
        for rep in range(18):
            eig=np.exp(rng.normal(0,0.6,N))
            Q,_=np.linalg.qr(rng.normal(size=(N,N)))
            V,_=np.linalg.qr(rng.normal(size=(N,N)))
            A=Q@np.diag(np.sqrt(eig))@V.T
            B=A.T@A
            for k in range(1,N+1):
                total=0.
                Pavg=np.zeros((N,N))
                for s in combinations(range(N),k):
                    As=A[list(s),:]
                    G=As@As.T
                    vol=np.linalg.det(G)
                    # independent Gram inverse geometry, no polynomial used
                    proj=As.T@np.linalg.solve(G,As)
                    Pavg+=vol*proj
                    total+=vol
                Pavg/=total
                eigs,Vb=np.linalg.eigh(B)
                ek=sum(np.prod(eigs[list(s)]) for s in combinations(range(N),k))
                desired=np.array([eigs[i]*sum(np.prod(np.delete(eigs,i)[list(s)]) for s in combinations(range(N-1),k-1))/ek for i in range(N)])
                expected=Vb@np.diag(desired)@Vb.T
                err=np.linalg.norm(Pavg-expected,ord='fro')
                worst=max(worst,err)
                assert err<2e-8,(N,k,err)
                assert abs(np.trace(Pavg)-k)<1e-8
                count+=2
    return count,worst


if __name__=='__main__':
    tested,checks=exact_exhaustive()
    geometries,worst=geometry_tests()
    print('Exact integer spectra:',tested,'exact assertions:',checks)
    print('Independent rotated-matrix identities:',geometries,'max Frobenius error:',format(worst,'.3g'))
    print('ALL CHECKS PASS')
