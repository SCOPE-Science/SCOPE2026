"""Finite independent tests of explicit Jacobi coefficients and beta Gram moments.

Requires sympy; analytic infinite-dimensional claims are proved in RESULT.md.
"""
from math import gamma, pi, isclose
import sympy as sp
from sympy.polys.orthopolys import jacobi_poly

x = sp.Symbol('x')
checked = 0
for L in range(7):
    for K in range(7):
        for j in range(5):
            J = L + j
            r = min(K, L)
            alpha = sp.Rational(2*abs(K-L)-1, 2)
            beta = sp.Rational(2*j-1, 2)
            poly = sp.Poly(sp.expand(jacobi_poly(r, alpha, beta, 1-2*x)), x)
            c = [float(poly.nth(r-m)) for m in range(r+1)]
            def moment(m, n):
                first = K+L-m-n+0.5
                second = j+0.5
                return gamma(first)*gamma(second)/gamma(first+second)/pi
            for k in range(1,r+1):
                value = sum(c[m]*moment(m,k) for m in range(r+1))
                assert abs(value) < 2e-9, (J,K,L,k,value)
                checked += 1
            norm = sum(c[m]*c[n]*moment(m,n) for m in range(r+1) for n in range(r+1))
            if r == 0:
                h = gamma(float(alpha+1))*gamma(float(beta+1))/gamma(float(alpha+beta+2))
            else:
                h = (gamma(float(r+alpha+1))*gamma(float(r+beta+1)) /
                     ((2*r+float(alpha+beta)+1)*gamma(r+1)*gamma(float(r+alpha+beta+1))))
            assert isclose(norm, h/pi, rel_tol=2e-9, abs_tol=2e-9), (J,K,L,norm,h/pi)
            checked += 1
            # Strict positive definiteness of the monomial Gram matrix, tested numerically.
            mat=sp.Matrix([[sp.Float(moment(m,n),15) for n in range(r+1)] for m in range(r+1)])
            for k in range(1,r+2):
                assert float(mat[:k,:k].det()) > -2e-11
                checked += 1
print('HEXABLOCK_JACOBI_CHECK_OK', checked)
