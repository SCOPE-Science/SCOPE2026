#!/usr/bin/env python3
"""Deterministic supplementary checks of the sharp row-budget inverse laws.

Only elementary exact rational and finite numerical checks are performed here;
the proofs for arbitrary dimensions and the asymptotic limit are in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import sqrt, floor
import numpy as np


def inverse_rows_of_parent(n, tau, parents):
    """Exact inverse rows of I-G for a parent forest; parent -1 means no edge."""
    out = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for i in range(1, n):
        j = parents[i]
        if j >= 0:
            for h in range(n):
                out[i][h] += tau * out[j][h]
    return out


def frobenius_defect_sq(rows):
    return sum((x-Fraction(int(i==j)))**2 for i, row in enumerate(rows)
               for j,x in enumerate(row))


def sharp_frobenius_sq(n, tau):
    return sum((n-j)*tau**(2*j) for j in range(1,n))


def test_exact_parent_forests():
    checked = 0
    for tau in (Fraction(1, 5), Fraction(1, 2), Fraction(3, 4)):
        for n in range(1, 7):
            full_chain = [-1]+[i-1 for i in range(1,n)]
            bound = sharp_frobenius_sq(n,tau)
            assert frobenius_defect_sq(inverse_rows_of_parent(n,tau,full_chain)) == bound
            for opts in product(*[range(-1,i) for i in range(1,n)]):
                parents = [-1]+list(opts)
                rows = inverse_rows_of_parent(n,tau,parents)
                assert frobenius_defect_sq(rows) <= bound
                for i in range(n):
                    lhs = sum(x*x for x in rows[i])
                    rhs = sum(tau**(2*j) for j in range(i+1))
                    assert lhs <= rhs
                    checked += 1
    return checked


def comb(n,tau,k):
    G = np.zeros((n,n),dtype=float)
    for i in range(1,k+1):
        G[i,i-1]=tau
    for i in range(k+1,n):
        G[i,k]=tau
    # Finite inverse computation for numerical verification.
    T = np.eye(n)-G
    return T


def test_numeric():
    checked=0
    rng=np.random.default_rng(440267)
    for tau in (.15,.4,.7,.92):
        for n in (2,3,4,7,12,26):
            maxfro=sqrt(float(sharp_frobenius_sq(n,tau)))
            for _ in range(15):
                G=np.zeros((n,n))
                for i in range(1,n):
                    r=rng.uniform(0,tau)
                    weights=rng.dirichlet(np.ones(i))
                    G[i,:i]=r*weights*rng.choice((-1,1),size=i)
                T=np.eye(n)-G
                B=np.linalg.inv(T)
                assert np.linalg.norm(T@B-np.eye(n),ord=np.inf)<1e-10
                assert np.linalg.norm(B-np.eye(n),'fro')<=maxfro+1e-10
                assert np.linalg.norm(B,2)<=1+maxfro+1e-10
                checked+=1
    for tau in (.25,.6,.9):
        for n in (16,64,256):
            k=max(1,int(floor(sqrt(n))))
            T=comb(n,tau,k)
            # Probe lower bound using an explicit supported unit vector (no SVD).
            v=np.zeros(n)
            v[:k+1]=np.array([tau**j for j in range(k+1,0,-1)])
            v/=np.linalg.norm(v)
            x=np.linalg.solve(T,v)
            expected=sqrt(n-k-1)*tau*sqrt((1-tau**(2*(k+1)))/(1-tau*tau))
            assert np.linalg.norm(x)+1e-8>=expected
            assert abs(np.linalg.norm(x[k+1:])-expected)<1e-8
            checked+=1
    return checked


if __name__=='__main__':
    exact=test_exact_parent_forests()
    numeric=test_numeric()
    print(f'PASS: {exact} exact-rational parent-forest row assertions; '
          f'{numeric} finite numerical matrix/comb cases')
