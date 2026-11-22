#!/usr/bin/env python3
"""Standalone checks for coordinate commutators of Bernstein-Durrmeyer operators.

Only Python standard library is required for exact checks. NumPy and SciPy are
optional for finite-dimensional spectra. Finite checks do not prove limits.
"""
from fractions import Fraction
from math import factorial, comb, pi, sqrt, e, gamma


def eigenvalues(n):
    z = [Fraction(1)]
    for k in range(n + 1):
        z.append(z[-1] * Fraction(n-k, n+k+2))
    return z


def weights_squared(n):
    z = eigenvalues(n)
    return [Fraction((k+1)**2, 4*(2*k+1)*(2*k+3)) * (z[k]-z[k+1])**2
            for k in range(n+1)]


def beta_int(i, j):
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))


def direct_kernel_hs_squared(n):
    s = Fraction(0)
    for k in range(n+1):
        for l in range(n+1):
            b = comb(n,k)*comb(n,l)
            a, d = k+l+1, 2*n-k-l+1
            i0=b*beta_int(a,d)
            i1=b*beta_int(a+1,d)
            i2=b*beta_int(a+2,d)
            s += 2 * (i0*i2-i1*i1)
    return s*(n+1)**2


def constant(p):
    return gamma((p+1)/2)**2/(2*sqrt(pi)*gamma(1+p/2)*p**((p+1)/2))


def main():
    count=0
    for n in range(1,12):
        actual = direct_kernel_hs_squared(n)
        spectral = 2*sum(weights_squared(n))
        assert actual == spectral, (n,actual,spectral)
        count += 1
    assert abs(constant(1)-1/pi)<1e-14; count+=1
    assert abs(constant(2)-sqrt(pi)/(16*sqrt(2)))<1e-14; count+=1
    try:
        import numpy as np
        from scipy.linalg import eigh_tridiagonal
    except ImportError:
        print('VERIFIED',count,'exact kernel/spectral and gamma identities; optional SciPy unavailable')
        return
    for n in [16, 64, 256, 1024, 4096]:
        z = np.ones(n+2)
        for k in range(n+1):
            z[k+1] = z[k] * (n-k)/(n+k+2)
        k=np.arange(n+1,dtype=float)
        b=(k+1)/(2*np.sqrt((2*k+1)*(2*k+3)))
        w=b*(z[:-1]-z[1:])
        eigen=eigh_tridiagonal(np.zeros(n+2),w,eigvals_only=True,
                              check_finite=False,lapack_driver='sterf')
        assert abs(np.sum(eigen**2)-2*np.sum(w*w))<2e-11
        assert abs(np.sum(eigen))<2e-11
        assert max(abs(eigen)) <= 2*max(w)+1e-12
        count+=3
        if n==4096:
            for p in [0.5,1,2,3]:
                mass=np.sum(np.abs(eigen)**p)*n**((p-1)/2)
                assert abs(mass/constant(p)-1) < 0.06,(p,mass,constant(p))
                count+=1
            assert abs(sqrt(n)*max(abs(eigen))-1/sqrt(2*e))<0.01
            count+=1
    print('VERIFIED',count,'exact and finite-spectral assertions; asymptotics require the analytic proof')

if __name__=='__main__':
    main()
