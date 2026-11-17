"""Independent numerical checks of the odd-prism edge-polytope ellipsoid.
Requires Python 3, numpy and scipy. All computations are finite corroboration.
"""
import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar


def incidence_rows(m):
    rows = []
    for layer in range(2):
        for j in range(m):
            row = np.zeros(2*m)
            row[layer*m+j] = row[layer*m+(j+1)%m] = 1
            rows.append(row)
    for j in range(m):
        row = np.zeros(2*m)
        row[j] = row[m+j] = 1
        rows.append(row)
    return np.array(rows)


def implicit_u(m):
    assert m >= 3 and m % 2
    def f(u):
        return ((1-u)/(1+u))**m - (1-2*u)/(1+2*u)
    return brentq(f, 0.24, 0.5, xtol=5e-15)


def check(m):
    V = incidence_rows(m)
    mu = np.full(2*m, 1/m)
    centered = V-mu
    _, singular, vh = np.linalg.svd(centered, full_matrices=False)
    basis = vh[singular > 1e-9].T
    d = 2*m-1
    assert basis.shape == (2*m, d)
    Z = centered @ basis
    def matrix(x):
        w = np.r_[np.full(2*m, (1-x)/(2*m)), np.full(m, x/m)]
        return Z.T @ (w[:,None]*Z)
    u = implicit_u(m)
    x = u*u
    C = matrix(x)
    sign, ld = np.linalg.slogdet(C)
    assert sign > 0
    f = (1+u)**m+(1-u)**m
    expected = (2*math.log(f)+m*math.log1p(-x)-d*math.log(2*m))
    assert abs(ld-expected) < 2e-7, (m,ld,expected)
    leverage = np.einsum('ij,jk,ik->i', Z, np.linalg.inv(C), Z)
    max_contact = float(np.max(np.abs(leverage-d)))
    assert max_contact < 3e-6, (m,max_contact)
    assert np.max(np.abs(V.mean(axis=0)-mu)) < 1e-14
    # Numerical logdet optimization is independent of the implicit root.
    opt = minimize_scalar(lambda t: -np.linalg.slogdet(matrix(t))[1],
                          bounds=(0.02,0.98),method='bounded',
                          options={'xatol':1e-12})
    assert opt.success
    assert abs(opt.x-x) < 5e-7, (m,opt.x,x)
    # Fourier eigenvalue multiset independent of SVD and determinant identity.
    modes = []
    for k in range(1,m):
        theta=2*math.pi*k/m
        modes.append(((1-x)*(1+math.cos(theta))+2*x)/m)
    for k in range(m):
        theta=2*math.pi*k/m
        modes.append((1-x)*(1+math.cos(theta))/m)
    assert np.allclose(sorted(modes),np.linalg.eigvalsh(C),atol=8e-13,rtol=5e-10)
    return x, max_contact

if __name__=='__main__':
    for m in range(3,20,2):
        x,err=check(m)
        print('m=%d spoke_weight=%.12g max_leverage_error=%.3g'%(m,x,err))
    for m in range(5,18,2):
        u=implicit_u(m)
        print('asymptotic_check m=%d normalized_defect=%.9f'%
              (m,(0.5-u)*3**m))
    print('ODD_PRISM_LOEWNER_PASS nine_orders=3..19 determinant_spectrum_contacts=PASS')
