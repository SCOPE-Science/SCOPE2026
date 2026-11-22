"""Finite-section diagnostics for a remote defect in alternating shifts.

Requires NumPy and SciPy. Diagnostic tests do not establish the infinite-dimensional theorem.
"""
from math import sqrt
import numpy as np
from scipy.linalg import eigh_tridiagonal


def edge(c, u, v):
    if c <= u:
        return u + v
    return (u*u + c*c + sqrt((u*u-c*c)**2 + 4*v*v*c*c))/(2*c)


def finite_top(a, b, c, m, right=260):
    weights = np.fromiter((a if i % 2 == 0 else b for i in range(m+right)), float)
    weights[m] = c
    n = len(weights)+1
    return float(eigh_tridiagonal(np.zeros(n), weights, select='i',
                                  select_range=(n-1, n-1), check_finite=False)[0][0])


def check():
    tests=0
    for a,b,c in [(1,2,1.5),(1,2,3.5),(2,1,1.5),(.8,1.3,1.4),(1,1,2.0),(1,2,.5)]:
        bounds = [edge(c,a,b),edge(c,b,a)]
        for parity in (0,1):
            u = a if parity==0 else b
            v = b if parity==0 else a
            lim = bounds[parity]
            vals=[finite_top(a,b,c,m) for m in (40+parity,80+parity,120+parity)]
            assert vals[0] <= vals[1]+1e-9 and vals[1] <= vals[2]+1e-9, (a,b,c,parity,vals)
            tests+=1
            assert max(vals) <= lim+1e-8,(a,b,c,parity,vals,lim)
            tests+=1
            if c>u:
                assert abs(vals[-1]-lim) < 1e-6,(a,b,c,parity,vals,lim)
                tests+=1
                lam=lim
                assert abs(c*lam*lam-(u*u+c*c)*lam+c*(u*u-v*v))<1e-8
                tests+=1
                rho=u*v/(c*lam-u*u)
                assert 0<rho<1
                tests+=1
            else:
                assert lim==a+b
                tests+=1
    print('REMOTE_DEFECT_PARITY_DIAGNOSTIC_OK',tests)

if __name__=='__main__':
    check()
