"""Finite-dimensional checks for the critical discrete Hardy perturbation.

These checks supplement (and do not replace) the infinite-dimensional proof.
Requires numpy and scipy. Run: python CHECKER.py
"""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal


def hardy_weight(n):
    n = np.asarray(n, dtype=float)
    return 2 - np.sqrt(1 + 1/n) - np.sqrt(1 - 1/n)


def form_error(N, seed=13):
    rng = np.random.default_rng(seed + N)
    g = rng.normal(size=N)
    u = np.sqrt(np.arange(1, N+1, dtype=float))*g
    x = np.concatenate(([0.0],u,[0.0]))
    raw = np.sum(np.diff(x)**2)
    weighted = np.dot(hardy_weight(np.arange(1,N+1)),u*u)
    c = np.sqrt(np.arange(1,N+1,dtype=float)*(np.arange(1,N+1,dtype=float)+1))
    energy = np.dot(c, np.diff(np.concatenate((g,[0.0])))**2)
    return abs(raw-weighted-energy)


def lowest_energy(N,t,potential):
    n = np.arange(1,N+1,dtype=float)
    diagonal = 2 - hardy_weight(n)
    for k,v in potential.items():
        diagonal[k-1] -= t*v
    return eigh_tridiagonal(diagonal,np.full(N-1,-1.0),
                           select='i',select_range=(0,0),eigvals_only=True)[0]


def verify():
    for N in [2,3,5,9,25,120]:
        err = form_error(N)
        assert err <= 2e-12*(1+N), (N,err)

    # Direct finite-section checks of the min-max eigenvalue calculations.
    for potential in ({1:1.0},{1:0.4,3:0.2}):
        for t in (0.3,0.4,0.6,1.0):
            E = lowest_energy(5000,t,potential)
            assert E < 0, (potential,t,E)
    # The single-site weak-binding coefficient tends towards 2 (not a
    # numerical proof of this limiting statement).
    lims=[]
    for t in (0.6,0.4,0.3):
        E = lowest_energy(5000,t,{1:1.0})
        lims.append(t*math.log(1/(-E)))
    assert lims[0] < lims[1] < lims[2] < 2.0
    print('PASS: six ground-state identities, eight negative finite-section spectra, three weak-binding trend checks')
    print('One-site diagnostic t*log(1/|E|):',*[round(v,7) for v in lims])


if __name__=='__main__':
    verify()
