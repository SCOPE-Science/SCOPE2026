"""Finite arithmetic diagnostics for the Gaussian projection comparison.

The infinite-dimensional assertions are established analytically, not by this grid.
"""
from fractions import Fraction
from math import asinh, cosh, exp, isclose, log, sqrt


def powers(p, q, C):
    r = 2*q/(1+q*q)
    return C**p * r**p/(1-r**p), (2*C)**p*q**p/(1-q**p)**2


def main():
    F = Fraction
    q, C = F(1, 2), F(5, 4)
    r = 2*q/(1+q*q)
    assert r == F(4, 5)
    assert C*r == 1
    assert 2*C*q == F(5, 4)
    analytic_trace = C*r/(1-r)
    max_trace = 2*C*q/(1-q)**2
    assert analytic_trace == max_trace == 5
    analytic_hs2 = (C*r)**2/(1-r*r)
    max_hs2 = (2*C*q)**2/(1-q*q)**2
    assert analytic_hs2 == max_hs2 == F(25, 9)
    checked = 6
    for iq in range(1, 50):
        qv = iq/50
        for p in (0.1,0.25,0.5,0.75,0.95,1.05,1.2,1.5,1.8,1.95,2.05,2.2,2.5,3.,4.,7.,12.):
            a, b = powers(p, qv, 1.)
            sign = 1 if (p < 1 or p > 2) else -1
            assert (b - a)*sign > -1e-8*max(a,b), (qv,p,a,b)
            checked+=1
    for s in (0.01,0.1,0.4,1.,3.):
        r=1/cosh(s)
        q=exp(-s)
        assert isclose(r, 2*q/(1+q*q), rel_tol=1e-12)
        checked += 1
    # Large-rank spectral profile at small positive Gaussian margin.
    for delta in (1e-3, 1e-4, 1e-5):
        t=1.
        s=asinh(sqrt(delta)/t)
        r=1/sqrt(1+delta/t**2)
        q=exp(-s)
        u=.5
        n=int(u*t*t/delta)
        k=int(u*t*t/delta)
        # Zero-based kth ordered singular value: first shell is m=0.
        m=0
        while (m+1)*(m+2)//2 <= k:
            m+=1
        assert abs(r**n-exp(-u/2)) < .02
        assert abs(q**m-exp(-sqrt(2*u))) < .02
        checked+=2
    print(f"GAUSSIAN_FOCK_SCHATTEN_DIAGNOSTIC_OK {checked}")


if __name__ == "__main__":
    main()
