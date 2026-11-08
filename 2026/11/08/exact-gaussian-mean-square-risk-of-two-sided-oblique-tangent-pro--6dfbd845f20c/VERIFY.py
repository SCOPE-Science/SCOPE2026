#!/usr/bin/env python3
"""Reproduce exact finite-dimensional identities and Gaussian risk diagnostics.

The analytic proof is in RESULT.md; Monte Carlo is a sanity check, not proof.
Requires numpy and sympy.
"""
from fractions import Fraction
import numpy as np
import sympy as sp


def deterministic_tests():
    for r, m, n, s in [(1, 3, 4, 2), (1, 4, 3, 3), (2, 5, 4, 4), (2, 4, 5, 5)]:
        U = sp.eye(m)[:, :r]
        V = sp.eye(n)[:, :r]
        UU = U * U.T
        VV = V * V.T
        for shift in range(5):
            # A complete, integer, full-column-rank set of test sketches.
            T = sp.Matrix(s, m, lambda i, j: (i + 1) ** (j % 3) + 2*(i==j) + shift*(i+1)*(j+2))
            O = sp.Matrix(s, n, lambda i, j: (i + 2) ** (j % 3) + 3*(i==j) + shift*(i+3)*(j+1))
            if (T*U).rank() != r or (O*V).rank() != r:
                continue
            Q = U * (T*U).pinv() * T
            R = V * (O*V).pinv() * O
            Z = sp.Matrix(m, n, lambda i,j: (i+2)*(j+1) + shift*(i-j) + (i==j))
            normal = (sp.eye(m)-UU)*Z*(sp.eye(n)-VV)
            base = UU*Z + Z*VV - UU*Z*VV
            sketched = Q*Z+Z*R.T-Q*Z*R.T
            pieces=[Q*normal, normal*R.T, -Q*normal*R.T]
            assert sketched-base == sum(pieces,sp.zeros(m,n))
            for a in range(3):
                for b in range(a+1,3):
                    assert sp.trace(pieces[a].T*pieces[b]) == 0
            assert sketched-base == Q*normal + normal*R.T-Q*normal*R.T
    print('exact rational projection identities: OK')


def gaussian_diagnostics():
    rng = np.random.default_rng(240719)
    for r,s,m,n in ((1,5,4,5),(2,8,5,6),(3,11,7,7)):
        U = np.eye(m)[:,:r]
        V = np.eye(n)[:,:r]
        N = np.zeros((m,n))
        N[r:,r:] = rng.standard_normal((m-r,n-r))
        N /= np.linalg.norm(N)
        trials = 14000
        vals = np.empty(trials)
        for k in range(trials):
            T = rng.standard_normal((s,m))
            O = rng.standard_normal((s,n))
            Q=U@np.linalg.pinv(T@U)@T
            R=V@np.linalg.pinv(O@V)@O
            E=Q@N+N@R.T-Q@N@R.T
            vals[k]=np.sum(E*E)
        exact=2*r/(s-r-1)+(r/(s-r-1))**2
        observed=vals.mean()
        assert abs(observed-exact)<0.17*exact,(r,s,observed,exact)
        print(f'Gaussian check r={r} s={s}: empirical={observed:.6f}; analytic={exact:.6f}')


if __name__=='__main__':
    deterministic_tests()
    gaussian_diagnostics()
    print('VERIFY_OK')
