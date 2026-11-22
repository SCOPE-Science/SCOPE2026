#!/usr/bin/env python3
"""Finite exact KKT and direct spectral diagnostics for equal-arm spiders.

Requires Python 3 standard library; NumPy is optional for the eigenspectrum check.
These finite tests support, but do not establish, the infinite-family theorem.
"""
import math
from fractions import Fraction


def coefficients(k, L):
    return {j: (L-j+1)*((k-1)*L+j) for j in range(1,L+1)}


def design(k, L):
    c=coefficients(k,L)
    e=sum(c[j] for j in range(2,L+1,2))
    o=sum(c[j] for j in range(3,L+1,2))
    u=math.sqrt(e)/(math.sqrt(e)+math.sqrt(o))
    w=[None,1/k]+[u if j%2==0 else 1-u for j in range(2,L+1)]
    n=k*L+1
    f=k/n*(k*c[1]+(math.sqrt(e)+math.sqrt(o))**2)
    return c,e,o,u,w,f


def exact_check(k,L):
    c,e,o,u,w,f=design(k,L)
    assert k>=3 and L>=3 and e>0 and o>0
    assert e < 2*o  # a strict bound guaranteeing free first junction
    for j in range(2,L):
        he=sum(c[t] for t in range(2,j+1,2))
        ho=sum(c[t] for t in range(3,j+1,2))
        if j%2==0:
            assert he*o > ho*e, (k,L,j,'even KKT')
        else:
            assert ho*e > he*o, (k,L,j,'odd KKT')
    # Check the increasing pairwise likelihood ratios as integer inequalities.
    pairs=[(c[j],c[j+1]) for j in range(2,L,2)]
    for (a,b),(d,e2) in zip(pairs,pairs[1:]):
        assert a*e2 < d*b
    assert 1/k + u < 1
    assert 0<u<1
    assert f>0


def numeric_spectral_check(k,L):
    import numpy as np
    c,e,o,u,w,f=design(k,L)
    n=k*L+1
    P=np.zeros((n,n),dtype=float)
    for arm in range(k):
        for j in range(1,L+1):
            a=0 if j==1 else 1+arm*L+(j-2)
            b=1+arm*L+(j-1)
            P[a,b]=P[b,a]=w[j]
    np.fill_diagonal(P,1-P.sum(axis=1))
    assert np.min(P)>-1e-12
    assert np.max(abs(P.sum(axis=1)-1))<1e-12
    assert np.max(abs(P-P.T))<1e-12
    z=np.linalg.eigvalsh(np.eye(n)-P)
    assert abs(z[0])<1e-10 and z[1]>1e-11
    spectral=float(sum(1/val for val in z[1:]))
    assert math.isclose(spectral,f,rel_tol=1e-9,abs_tol=1e-8), (k,L,spectral,f)
    # A feasible maximum-degree uniform-edge comparator.
    max_deg = k
    uniform=k*k/n*sum(c.values())
    assert uniform>f + 1e-10
    # exact equality of all interior depth>=2 row sums
    for arm in range(k):
        for j in range(2,L):
            idx=1+arm*L+(j-1)
            assert abs(P[idx,idx])<1e-11
        idx=1+arm*L # depth-one junction
        assert P[idx,idx]>0


def main():
    n_exact=0
    for k in range(3,61):
        for L in range(3,101):
            exact_check(k,L)
            n_exact+=1
    n_spectral=0
    for k in range(3,9):
        for L in range(3,13):
            numeric_spectral_check(k,L)
            n_spectral+=1
    print(f'PASS: {n_exact} exact-inequality parameter pairs; {n_spectral} spectral comparator cases.')
    print('Finite diagnostics are not a proof for all parameters.')

if __name__=='__main__':
    main()
