"""Numerical checks for a collapsing convex lens mean-chord asymptotic.

Run: python verify.py. Requires NumPy. Finite quadrature is not a proof.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss

def ratio(n, e, kind):
    x, w = leggauss(n)
    if kind == 'tent':
        h = 1 - np.abs(x)
        dh = -np.sign(x)
        aa, bb = -.5, .5
        integral = 2 / 3
    elif kind == 'parabolic':
        h = 1 - x*x
        dh = -2*x
        aa, bb = -.5, .5
        integral = 16 / 15
    elif kind == 'shifted_parabolic':
        h = 1 - x*x
        dh = -2*x
        aa, bb = -.25, .75
        integral = 16 / 15
    else:
        raise ValueError(kind)
    branches = [aa*h, bb*h]
    density = [w*np.hypot(1, e*aa*dh), w*np.hypot(1, e*bb*dh)]
    P = sum(np.sum(d) for d in density)
    dx = x[:, None] - x[None, :]
    total = 0.
    for i in range(2):
        for j in range(2):
            d = np.hypot(dx, e*(branches[i][:, None]-branches[j][None, :]))
            total += np.einsum('ij,i,j->', d, density[i], density[j], optimize=True)
    return total / P**3, integral / 32

def run():
    for kind in ('tent','parabolic','shifted_parabolic'):
        vals=[]
        for eps in (0.04, 0.02):
            r, coeff = ratio(900, eps, kind)
            assert r > 1/6
            vals.append((r-1/6)/(eps*eps))
        estimate=(vals[1]-vals[0])/np.log(2)
        assert abs(estimate-coeff) < .006, (kind, estimate, coeff)
        print(kind, 'logarithmic slope', round(estimate, 8), 'predicted', round(coeff, 8))
    print('Finite quadrature checks passed; proof is analytic.')

if __name__ == '__main__':
    run()
