"""Numerical consistency checks for the finite-abelian biclique-projector theorem.

These checks are supplementary; the analytic proof, not sampling, establishes
universality and the exact equality classification.
"""
from itertools import combinations, product
from math import sqrt
import numpy as np


def chars(moduli):
    points = list(product(*(range(q) for q in moduli)))
    n = len(points)
    U = np.empty((n,n), dtype=complex)
    for i, k in enumerate(points):
        for j, x in enumerate(points):
            U[i,j] = np.exp(-2j*np.pi*sum(a*b/q for a,b,q in zip(k,x,moduli)))/sqrt(n)
    return points, U


def ratio(U, small):
    N = U.shape[0]
    large = [j for j in range(N) if j not in small]
    n = len(large)
    P = np.zeros((N,N), dtype=float)
    P[np.ix_(large,large)] = np.eye(n) - np.ones((n,n))/n
    M = U @ P @ U.conj().T
    return float(np.abs(M).sum()/sqrt(n-1)), M


def subgroup_coset(points, small, moduli):
    B = set(points[i] for i in small)
    b = next(iter(B))
    H = {tuple((x-y)%q for x,y,q in zip(a,b,moduli)) for a in B}
    return all(tuple((x+y)%q for x,y,q in zip(a,b,moduli)) in H for a in H for b in H)


def main():
    cases = 0
    for moduli in [(N,) for N in range(3,12)] + [(2,2),(2,2,2),(3,3),(2,3),(2,4),(2,2,3)]:
        pts,U=chars(moduli)
        N=len(pts)
        for m in range(1,(N-1)//2+1):
            n=N-m
            bound=2*sqrt(n-1)
            for B in combinations(range(N),m):
                got,M=ratio(U,set(B))
                is_coset=subgroup_coset(pts,B,moduli)
                assert got>=bound-2e-9,(moduli,m,B,got,bound)
                assert (abs(got-bound)<2e-9)==is_coset, (moduli,m,B,got,bound,is_coset)
                cases+=1
    # Independent direct two-dimensional Fourier transform normalization.
    pts,U=chars((10,))
    for B in [(0,5),(0,1),(1,3)]:
        n=10-len(B)
        P=np.zeros((10,10))
        C=[x for x in range(10) if x not in B]
        P[np.ix_(C,C)]=np.eye(n)-np.ones((n,n))/n
        v,M=ratio(U,set(B))
        direct=np.fft.fft2(P)/10
        assert abs(np.abs(direct).sum()/np.linalg.norm(P)-v)<1e-9
        assert abs(np.abs(M).sum()-np.abs(direct).sum())<1e-9
    print(f'PASS: {cases} exhaustive subset cases, abelian product examples, and normalization checks')


if __name__=='__main__':
    main()
