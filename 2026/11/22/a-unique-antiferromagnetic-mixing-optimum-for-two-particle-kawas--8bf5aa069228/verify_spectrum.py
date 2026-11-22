"""Standalone exact small-system checks for two-particle bipartite Kawasaki dynamics.
Only standard-library fractions and SymPy are needed for exact checks.
"""
from fractions import Fraction
from itertools import combinations
from collections import Counter
import sympy as s


def full_negative_generator(r, p, q):
    """Returns integer q*(-generator), for a=p/q, b=1-a."""
    states = list(combinations(range(2*r), 2))
    index = {z:i for i,z in enumerate(states)}
    M = s.zeros(len(states))
    for k,z in enumerate(states):
        x = set(z)
        for u in range(r):
            for v in range(r,2*r):
                if (u in x)==(v in x):
                    continue
                y=tuple(sorted(x.symmetric_difference({u,v})))
                ell=index[y]
                # AA/BB -> AB has a=p/q; reverse b=(q-p)/q.
                # Determine sector by number of particles on A, not the particular exchange orientation.
                nA=sum(t<r for t in z)
                rate=p if nA in (0,2) else q-p
                M[k,k] += rate
                M[k,ell] -= rate
    return M


def predicted_charpoly(r,p,q,t):
    a=2*r*p
    d=2*(r-1)*(q-p)
    z=2*((r-1)*q+p)
    if r==2:
        return s.Poly(t*(t-a)*(t-z)*(t-d)**3,t)
    quadratic=t*t-(a+d)*t+r*(3*r-2)*p*(q-p)
    return s.Poly(t*(t-a)**(r*(r-3)+1)*(t-z)*(t-d)**((r-1)**2)*quadratic**(2*(r-1)),t)


def run():
    t=s.symbols('t')
    count=0
    for r in (2,3,4):
        for p,q in ((1,3),(1,2),(2,3)):
            M=full_negative_generator(r,p,q)
            assert s.Poly(M.charpoly(t).as_expr(),t)==predicted_charpoly(r,p,q,t), (r,p,q)
            assert M* s.ones(M.rows,1) == s.zeros(M.rows,1)
            count+=1
    print('EXACT_FULL_CHARACTERISTIC_POLYNOMIAL_CHECKS',count)
    import numpy as np
    for r in range(5,9):
        for p,q in ((1,4),(1,2),(3,4)):
            M=full_negative_generator(r,p,q)
            # Reversible similarity: eigenvalues of nonsymmetric integer generator are real.
            vals=np.sort(np.linalg.eigvals(np.array(M,dtype=float)).real)
            ex=[]
            a=2*r*p; d=2*(r-1)*(q-p); z=2*((r-1)*q+p)
            ex.extend([0,z]);ex.extend([a]*(r*(r-3)+1));ex.extend([d]*((r-1)**2))
            eigquad=np.roots([1,-(a+d),r*(3*r-2)*p*(q-p)])
            for v in eigquad: ex.extend([v]*(2*(r-1)))
            ex.sort()
            assert np.allclose(vals,np.array(ex),rtol=1e-9,atol=1e-8), (r,p,q)
            count+=1
    print('TOTAL_SPECTRUM_CHECKS',count)

if __name__=='__main__': run()
