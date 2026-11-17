"""Finite consistency checks for the one-sided Dirac numerical-range formulas.

Run with Python 3 and NumPy. These checks do not establish the analytical theorem.
"""
import math
import numpy as np

SIGMA1 = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA3 = np.diag([1, -1]).astype(complex)


def symbol(M, c, k):
    return M * SIGMA3 - 1j * c * (1 - np.exp(-1j*k)) * SIGMA1


def support(M, c, theta):
    return math.sqrt(M*M*math.cos(theta)**2 + c*c*(1+abs(math.sin(theta)))**2)


def radius(M, c):
    return 2*c if M <= math.sqrt(2)*c else M*M/math.sqrt(M*M-c*c)


def inradius(M, c):
    return math.sqrt(M*M+c*c) if M <= math.sqrt(3)*c else 2*c


def run():
    checks = 0
    ks = np.linspace(-math.pi, math.pi, 1001)
    thetas = np.linspace(0, 2*math.pi, 101)
    for c in [0.25, 1.0, 2.5]:
        for M in [0., .1*c, .7*c, math.sqrt(2)*c, 1.6*c, 2.5*c, 8*c]:
            for th in thetas:
                matrices = np.array([symbol(M, c, k) for k in ks])
                herm = (np.exp(-1j*th)*matrices + np.exp(1j*th)*matrices.conj().transpose(0, 2, 1))/2
                eig_max = np.linalg.eigvalsh(herm)[:, -1].max()
                h = support(M, c, th)
                assert -1e-9 <= h-eig_max <= 2.0e-5*c, (M,c,th,h,eig_max)
                checks += 1
            hs = [support(M, c, x) for x in np.linspace(0,2*math.pi,20001)]
            w = radius(M,c)
            assert abs(max(hs)-w) < 2e-7*c, (M,c,max(hs),w)
            checks += 1
            r = inradius(M,c)
            assert abs(min(hs)-r) < 2e-7*c, (M,c,min(hs),r)
            checks += 1
            u = math.sqrt(M*M+c*c)
            half_height = c*c/u
            eps=1e-6
            derivative_plus = (support(M,c,eps)-u)/eps
            derivative_minus = (support(M,c,-eps)-u)/(-eps)
            assert abs(derivative_plus-half_height)<1e-5*c
            assert abs(derivative_minus+half_height)<1e-5*c
            checks += 2
    assert support(1,1,math.pi/2)==2
    checks += 1
    print('DIRAC_NUMERICAL_RANGE_DIAGNOSTICS_OK',checks)

if __name__ == '__main__':
    run()
