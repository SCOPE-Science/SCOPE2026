#!/usr/bin/env python3
"""Finite exact-rational and floating-point checks for a signed cyclic feedback chain.

Requires Python 3 and NumPy for the independent eigenvalue comparisons.
The arbitrary-order claims are proved analytically in RESULT.md, not by this script.
"""
from fractions import Fraction as F
from itertools import combinations
from math import cos, pi


def cheb_u(k, z):
    assert k >= 0
    if k == 0: return z * 0 + 1
    a, b = z * 0 + 1, 2 * z
    for _ in range(2, k + 1): a, b = b, 2 * z * b - a
    return b


def interval(n, mu, a=F(1)):
    z = mu / a
    den = cheb_u(n - 2, z)
    num = cheb_u(n - 1, z)
    return a * (1 - num) / den, a * (1 + num) / den


def minor_determinant(A):
    n = len(A)
    if n == 0: return F(1)
    A = [list(row) for row in A]
    sign = 1
    det = F(1)
    for i in range(n):
        pivot = next((r for r in range(i, n) if A[r][i]), None)
        if pivot is None: return F(0)
        if pivot != i:
            A[i], A[pivot] = A[pivot], A[i]
            sign *= -1
        v = A[i][i]
        det *= v
        for r in range(i + 1, n):
            mult = A[r][i] / v
            for c in range(i + 1, n):
                A[r][c] -= mult * A[i][c]
            A[r][i] = F(0)
    return sign * det


def minus_symmetric_part(n, mu, a, b):
    # Exact symmetric matrix - (J+J^T)/2.
    A = [[F(0) for _ in range(n)] for __ in range(n)]
    for i in range(n): A[i][i] = mu
    for i in range(n-1):
        A[i][i+1] = A[i+1][i] = -a/2
    A[0][n-1] = A[n-1][0] = b/2
    return A


def is_psd(A):
    n = len(A)
    for k in range(1, n+1):
        for inds in combinations(range(n), k):
            B = [[A[i][j] for j in inds] for i in inds]
            if minor_determinant(B) < 0:
                return False
    return True


def main():
    import numpy as np
    # These rational mu/a values lie strictly between cos(pi/n) and cos(pi/(n+1)).
    pairs = [(3, F(3,5)), (4,F(3,4)), (5,F(5,6)),
             (6,F(8,9)), (7,F(11,12)), (8,F(15,16))]
    exact = 0
    for n,mu in pairs:
        assert cos(pi/n) < float(mu) < cos(pi/(n+1))
        lo,hi=interval(n,mu)
        assert 0 < lo < 1 < hi
        # Independent PSD test using every principal minor, including endpoints.
        for b,expected in [(lo/2,False),(lo,True),((lo+hi)/2,True),
                           (F(1),True),(hi,True),(hi+F(1,5),False)]:
            assert is_psd(minus_symmetric_part(n,mu,F(1),b)) == expected, (n,mu,b)
            exact+=1
        # Exact equality of endpoint full determinants to zero.
        assert minor_determinant(minus_symmetric_part(n,mu,F(1),lo))==0
        assert minor_determinant(minus_symmetric_part(n,mu,F(1),hi))==0
    numerical=0
    for n in range(3,17):
        a=1.
        z=(cos(pi/n)+cos(pi/(n+1)))/2
        lo,hi=interval(n,z)
        for b in (0.,float(lo),float((lo+hi)/2),1.,float(hi),float(hi)+0.2):
            J = -z*np.eye(n)
            for i in range(n-1): J[i+1,i]=a
            J[0,n-1]=-b
            omega=np.linalg.eigvalsh((J+J.T)/2)[-1]
            should_nonamp=(b>=float(lo)-1e-9 and b<=float(hi)+1e-9)
            assert (omega<=1e-8)==should_nonamp, (n,b,omega)
            # Root formula for spectral abscissa at b>0.
            if b>0:
                exact_abscissa = -z + b**(1/n)*cos(pi/n)
                vals=np.linalg.eigvals(J)
                assert abs(max(vals.real)-exact_abscissa)<2e-10
            numerical +=1
        # Check projected top-eigenspace lower bounds for arbitrary feedback strengths.
        omega_star = -z+cos(pi/n)
        for b in (0.,0.1,0.9,1.2,2.,4.):
            J=-z*np.eye(n)
            for i in range(n-1):J[i+1,i]=a
            J[0,n-1]=-b
            omega = np.linalg.eigvalsh((J+J.T)/2)[-1]
            bound = omega_star + ((b-1)*(1+cos(pi/n))/n if b>=1
                                    else (1-b)*(1-cos(pi/n))/n)
            assert omega >= bound-2e-10, (n,b,omega,bound)
            numerical+=1
    print('PASS: exact PSD decisions',exact,'; independent numerical comparisons',numerical,
          '; exact endpoint determinants',2*len(pairs))

if __name__=='__main__': main()
