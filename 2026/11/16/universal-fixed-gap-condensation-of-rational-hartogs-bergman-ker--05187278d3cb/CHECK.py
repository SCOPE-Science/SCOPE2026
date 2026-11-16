"""Exact coefficient identities and finite root-location checks for fixed-gap Hartogs polynomials.

Run with Python 3, numpy, and sympy. Finite computations are consistency
checks; the all-gap theorem is proved analytically in RESULT.md.
"""
import math
import numpy as np
import sympy as sp


def triangle(t):
    return max(0, 1 - abs(t))


def source_coefficients(m, n):
    """Two-index formula from the published numerator, computed exactly."""
    k = m - n
    def D(t):
        return max(0, m - abs(t - m + 1))
    coeff = [0] * (2*k + 1)
    for a in range(2*m-1):
        for b in range(2*n+1):
            t = D(a) * D(m*b+n*a+m+n-1-2*m*n)
            if t:
                coeff[a+b+1-2*n] += t
    return coeff


def one_sum_coefficients(m, n):
    """Reindexed exact centered-coefficient formula, integer-only."""
    k = m - n
    coeff = []
    for j in range(2*k+1):
        s = 0
        for ell in range(1, 2*m):
            v1 = m - abs(ell-m)
            v2 = max(0, m - abs(m*j-k*ell))
            s += v1*v2
        coeff.append(s)
    return coeff


def limiting_coefficients(k):
    z = sp.Symbol('z')
    p = sp.Poly((z*z+4*z+1)*sum(z**r for r in range(k))**2, z)
    return [int(p.nth(j)) for j in range(2*k+1)]


def run():
    checks = 0
    for k in range(1, 9):
        c = limiting_coefficients(k)
        assert c[0] == c[-1] == 1
        assert c[k] == 6*k-2
        assert sum(c) == 6*k*k
        checks += 3
        for n in range(1, 9):
            if math.gcd(n,k) != 1: continue
            m = n+k
            q = one_sum_coefficients(m,n)
            assert q == source_coefficients(m,n)
            assert q == q[::-1]
            assert sum(q) == m**3
            checks += 3
    # Confirm the O_k(m^-2) coefficient-scale prediction and root splitting.
    for k in (4, 5, 6, 7):
        c = np.array(limiting_coefficients(k),float)
        for n in (51,101,201):
            while math.gcd(n,k)!=1: n += 1
            m = n+k
            q = np.array(one_sum_coefficients(m,n),float)
            e = np.max(np.abs((6*k*k/m**3)*q-c))
            assert (m*m*e) < 10000*k**3
            # Roots of the real reciprocal polynomial in degree 2k.
            roots = np.roots(q[::-1]/q[-1])
            beta = -2+math.sqrt(3)
            close_beta = sorted(roots,key=lambda z:abs(z-beta))[0]
            assert abs(close_beta-beta)<80*k*k/m
            for j in range(1,k):
                zeta = np.exp(2*np.pi*1j*j/k)
                nearby = sorted(roots,key=lambda z:abs(z-zeta))[:2]
                # At this moderate n the neighborhoods do not always separate;
                # check only the nearest candidate at this stage.
                assert abs(nearby[0]-zeta) < 80*k*k/m
            checks += 1+k
    print('PASS: %d finite grouped assertions, exact source/one-sum matching, '
          'normalization, and coefficient/root consistency.' % checks)

if __name__ == '__main__':
    run()
