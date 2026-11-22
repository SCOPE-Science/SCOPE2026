"""Deterministic consistency checks for Lamé boundary-pair near-diameter law.
Scientific numerical checks supplement, but do not replace, local asymptotic proofs.
Requires NumPy and SciPy.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln


def perimeter(p):
    def integrand(t):
        s, c = math.sin(t), math.cos(t)
        if s == 0.0 or c == 0.0:
            return 0.0
        return (8 / p) * math.sqrt(s*s*c**(4/p-2) + c*c*s**(4/p-2))
    return quad(integrand, 0, math.pi / 2, points=[math.pi / 4], epsabs=3e-11, epsrel=3e-11, limit=250)[0]


def coefficient(p):
    L = perimeter(p)
    if p < 1:
        return 2., 8/L**2
    if p == 1:
        return 2., 16/L**2
    if p < 2:
        return 2/p, 16*p**(2/p)*math.exp(2*gammaln(1+1/p)-gammaln(1+2/p))/L**2
    if p == 2:
        return .5, 2/math.pi
    return 1., 8*math.pi*2**(.5-1/p)/(L**2*math.sqrt((p-1)*(p-2)))


def exact_patch_quadrature(p, eps, N=560):
    """Sum over all ordered diameter pairs, integrate their exact local chord geometry.
    Regions outside the patches do not contribute at the small eps used here.
    """
    L = perimeter(p)
    if p <= 1:
        upper = 1.05*eps
        u = (np.arange(N)+.5)*upper/N
        x = 1-u
        w = np.maximum(0, 1-x**p)
        y = w**(1/p)
        ds = np.sqrt(1 + (x**(p-1)*w**(1/p-1))**2)
        acc = 0.
        for sign in (-1, 1):
            length = np.hypot(x[:,None]+x[None,:], y[:,None]-sign*y[None,:])
            acc += np.sum((length > 2-eps)*ds[:,None]*ds[None,:])
        return 8*acc*(upper/N)**2/L**2
    if p < 2:
        upper = 1.05*(p*eps)**(1/p)
        y = (np.arange(N)+.5)*(2*upper/N)-upper
        q = np.maximum(0, 1-np.abs(y)**p)
        x = q**(1/p)
        dx = np.abs(y)**(p-1)*q**(1/p-1)
        ds = np.sqrt(1+dx**2)
        length = np.hypot(x[:,None]+x[None,:], y[:,None]-y[None,:])
        return 4*np.sum((length > 2-eps)*ds[:,None]*ds[None,:])*(2*upper/N)**2/L**2
    if p == 2:
        return 2/math.pi*math.acos(1-eps/2)
    r0 = 2**(.5-1/p)
    upper = 3*math.sqrt(eps/(r0*(p-2)))
    theta = math.pi/4+(np.arange(N)+.5)*(2*upper/N)-upper
    c, s = np.cos(theta), np.sin(theta)
    z = c**p+s**p
    r = z**(-1/p)
    rr = (c**(p-1)*s - s**(p-1)*c)/z
    ds = r*np.sqrt(1+rr**2)
    u = theta-math.pi/4
    length = np.sqrt(r[:,None]**2+r[None,:]**2 + 2*r[:,None]*r[None,:]*np.cos(u[:,None]-u[None,:]))
    return 4*np.sum((length > 2*r0-eps)*ds[:,None]*ds[None,:])*(2*upper/N)**2/L**2


def main():
    for p, per in [(2/3,6.),(1.,4*math.sqrt(2)),(2.,2*math.pi)]:
        assert abs(perimeter(p)/per-1)<1e-10, (p,perimeter(p))
    assert abs(coefficient(2/3)[1]-2/9)<1e-11
    assert abs(coefficient(1.)[1]-.5)<1e-11
    assert abs(coefficient(2.)[1]-2/math.pi)<1e-11
    for p, eps, tol in [(2/3,1e-4,.02),(.8,1e-4,.04),(1.,1e-4,.02),(1.2,1e-5,.06),
                        (1.5,1e-5,.04),(3.,2e-4,.025),(4.,2e-4,.025)]:
        alpha, c = coefficient(p)
        observed = exact_patch_quadrature(p,eps)
        predicted = c*eps**alpha
        rel = abs(observed/predicted-1)
        print(f'p={p:.6g} eps={eps:g} observed={observed:.11g} leading={predicted:.11g} rel={rel:.5g}')
        assert rel < tol, (p,rel,tol)
    # Noncommutation across the diamond: the two one-sided coefficients are half the p=1 coefficient.
    L1 = perimeter(1.)
    assert abs(8/L1**2/.5 - .5) < 1e-12
    # Regular Euclidean circle's exact angular formula gives the claimed exponent.
    for eps in (1e-3,1e-4,1e-5):
        assert abs(exact_patch_quadrature(2.,eps) / (2/math.pi*math.sqrt(eps)) - 1) < 1e-3
    print('ALL_CHECKS_PASSED')

if __name__ == '__main__':
    main()
