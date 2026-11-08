"""Finite exact checks for monomial composition-product identities.

Requires Python 3 and SymPy. All infinite-dimensional conclusions in the
accompanying mathematical proof are analytic and are not certified by tests.
"""
from fractions import Fraction
from math import comb
import sympy as s

checks = 0
for beta in (1, 2, 3, 4):
    def b(k):
        return comb(k + beta, beta)
    for m in range(1, 6):
        for n in range(1, 6):
            c2 = Fraction(1, (m*n)**beta)
            a = Fraction(beta*(beta+1), 2) * (1-Fraction(1, 2*m)-Fraction(1, 2*n))
            t = s.Symbol('t')
            g = s.prod((1+j*t)**2/((1+s.Rational(j,m)*t)*(1+s.Rational(j,n)*t)) for j in range(1,beta+1))
            assert s.simplify(g.subs(t,0) - 1) == 0
            checks += 1
            assert s.simplify(s.diff(g,t).subs(t,0) - 2*s.Rational(a.numerator,a.denominator)) == 0
            checks += 1
            for k in range(0, 11):
                left = Fraction(b(k)**2, b(m*k)*b(n*k))
                # Assemble the two composition coefficients separately;
                # this is the square of the matrix entry of C_(z^m) C_(z^n)^*.
                first_sq = Fraction(b(k), b(n*k))
                second_sq = Fraction(b(k), b(m*k))
                assert left == first_sq * second_sq
                checks += 1
                if k > 0:
                    # Exact identity of the normalized squared weight.
                    rhs = c2
                    for j in range(1,beta+1):
                        rhs *= Fraction((k+j)**2*m*n, (m*k+j)*(n*k+j))
                    assert left == rhs
                    checks += 1
            if m != n:
                for L in range(1, 12):
                    v = [n**(L-i)*m**i*7 for i in range(L+1)]
                    assert len(set(v)) == L+1
                    checks += 1
                    for u,w in zip(v, v[1:]):
                        assert u % n == 0 and (u//n)*m == w
                        checks += 1
print('MONOMIAL_COMPOSITION_EXACT_FINITE_CHECKS_OK', checks)
