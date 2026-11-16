"""Separate spherical-moment check for the parity-orthant concentration spectrum.

Uses the monomial Laplacian nullspace rather than the complement-pair proof.
Requires Python 3, numpy, scipy, and sympy.
"""
from itertools import combinations
from math import comb, gamma, pi, prod
import numpy as np
from scipy.linalg import eigh
import sympy as sp


def multiindices(d, k):
    if d == 1:
        return [(k,)]
    return [(i,) + t for i in range(k+1) for t in multiindices(d-1, k-i)]


def harmonic_basis(d, degree):
    xs = multiindices(d, degree)
    if degree < 2:
        return xs, sp.eye(len(xs))
    targets = multiindices(d, degree-2)
    ind = {t:i for i,t in enumerate(targets)}
    L = sp.zeros(len(targets), len(xs))
    for j, a in enumerate(xs):
        for i in range(d):
            if a[i] >= 2:
                b = list(a); b[i] -= 2
                L[ind[tuple(b)],j] += a[i] * (a[i]-1)
    null = L.nullspace()
    return xs, sp.Matrix.hstack(*null)


def full_moment(g):
    if any(i%2 for i in g):
        return 0.
    d=len(g)
    return gamma(d/2) / gamma((d+sum(g))/2) * prod(gamma((a+1)/2) / gamma(.5) for a in g)


def parity_moment(g, r):
    if any(a%2 != 1 for a in g[:r]) or any(a%2 != 0 for a in g[r:]):
        return 0.
    d=len(g)
    return gamma(d/2) / gamma((d+sum(g))/2) * prod(gamma((a+1)/2) / gamma(.5) for a in g)


def check(d, r):
    assert 2 <= r <= d and r % 2 == 0
    m=r//2
    degrees=[]
    basis=[]
    for ell in range(m+1):
        mon, null=harmonic_basis(d,ell)
        for j in range(null.cols):
            v=np.asarray(null[:,j],dtype=float).ravel()
            tup=[(mon[i],v[i]) for i in np.flatnonzero(v)]
            degrees.append(ell)
            basis.append(tup)
    N=len(basis)
    G=np.zeros((N,N)); B=np.zeros((N,N))
    for i in range(N):
        for j in range(i,N):
            Gij=sum(c*cc*full_moment(tuple(a+b for a,b in zip(exps,exps2))) for exps,c in basis[i] for exps2,cc in basis[j])
            Bij=sum(c*cc*parity_moment(tuple(a+b for a,b in zip(exps,exps2)),r) for exps,c in basis[i] for exps2,cc in basis[j])
            G[i,j]=G[j,i]=Gij; B[i,j]=B[j,i]=Bij
    ev=eigh(B,G,eigvals_only=True,check_finite=True)
    rho=(2/pi)**m
    num=comb(r,m)//2
    target=np.array([-rho]*num + [0.]*(N-2*num) + [rho]*num)
    err=np.max(np.abs(ev-target))
    print(f'd={d} r={r} L={m} harmonic_band_dim={N} pair_multiplicity={num} rho={rho:.12f} max_error={err:.3g}')
    assert err < 1e-10
    assert np.linalg.eigvalsh(G)[0]>1e-14
    assert max(abs(z) for z in np.diag(B[:N-num,:N-num])) < 1e-12


for d, r in ((2,2), (3,2), (4,2), (4,4), (5,4), (6,4), (6,6), (7,6)):
    check(d,r)
print('PARITY_ORTHANT_FIRST_SPLITTING_VERIFIED')
