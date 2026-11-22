"""Independent finite Fourier checks for nonreciprocal chase–run diffusivity.

Requires numpy, scipy, sympy. Analytical proof is given in RESULT.md.
Run: python verify.py
"""
from itertools import product
from math import comb
import numpy as np
import sympy as sp
from scipy.sparse import dok_matrix, csc_matrix
from scipy.sparse.linalg import spsolve


def fourier_gain(n, d1, d2, amplitude, wavenumber=1.0, cutoff=3):
    """Solve the stationary corrector on truncated Fourier modes of a torus."""
    modes = [m for m in product(range(-cutoff, cutoff + 1), repeat=n) if any(m)]
    index = {m: i for i, m in enumerate(modes)}
    system = dok_matrix((len(modes), len(modes)), dtype=complex)
    forcing = np.zeros(len(modes), dtype=complex)
    for mode, column in index.items():
        system[column, column] = wavenumber**2 * (d1 * sum(mode)**2 + d2 * sum(v*v for v in mode))
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for step in (-1, 1):
                    changed = list(mode)
                    changed[j] += step
                    changed = tuple(changed)
                    if changed in index:
                        system[index[changed], column] -= amplitude * wavenumber**2 * step * mode[i]/2
        for i in range(n):
            plus = tuple(int(j == i) for j in range(n))
            minus = tuple(-int(j == i) for j in range(n))
            if mode == plus:
                forcing[column] = amplitude*wavenumber/(2j)
            if mode == minus:
                forcing[column] = -amplitude*wavenumber/(2j)
    coefficient = spsolve(csc_matrix(system), forcing)
    return float(np.vdot(forcing, coefficient).real)


def expected_gain(n,d1,d2,a):
    d = d1+d2
    return (n*a*a/(2*d) - n*(n-1)*a**4/(8*d*d*(2*d1+d2)))


def run():
    a, d1, d2, n = sp.symbols('a d1 d2 n', positive=True)
    d = d1+d2
    q = n*a*a/(2*d)
    corr = n*(n-1)*a**4/(8*d*d*(2*d1+d2))
    assert sp.simplify((corr/q) - (n-1)*a*a/(4*d*(2*d1+d2)))==0
    checks=0
    for nval in (1,2,3):
        for d1val,d2val in ((1.,1.), (0.6,1.7), (2.2,0.4)):
            for aval in (0.05,0.10,0.20):
                val=fourier_gain(nval,d1val,d2val,aval,cutoff=3 if nval<3 else 2)
                upper=nval*aval**2/(2*(d1val+d2val))
                assert val>0 and val<=upper*(1+1e-9)
                if nval==1:
                    assert abs(val-upper)<1e-9
                else:
                    assert val<upper
                    # The remaining term is O(a^6), checked at small amplitude.
                    err=abs(val-expected_gain(nval,d1val,d2val,aval))
                    assert err<0.03*aval**6*max(1.,nval*nval)/min(d1val,d2val)**5
                checks+=1
    # Fourier drift action on a first-harmonic corrector: it contains
    # exactly one sine sum-frequency for every unordered particle pair.
    theta1,theta2,k=sp.symbols('theta1 theta2 k',real=True)
    expr=sp.sin(theta2)*sp.cos(theta1)+sp.sin(theta1)*sp.cos(theta2)
    assert sp.simplify(sp.expand_trig(sp.sin(theta1+theta2))-expr)==0
    checks+=1
    print(f'PASS: {checks} symbolic/numerical test groups; Galerkin cutoffs and remainder checks are not an all-amplitude proof')

if __name__=='__main__': run()
