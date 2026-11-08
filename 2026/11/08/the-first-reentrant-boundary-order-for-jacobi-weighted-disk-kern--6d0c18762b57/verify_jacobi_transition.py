#!/usr/bin/env python3
"""Exact Cayley/Routh identities for the first Jacobi-kernel reentrance."""
from fractions import Fraction
import sympy as sp

x, u, t, k = sp.symbols('x u t k', real=True)


def kernel_numerator(m):
    """Return P=(1-x)^(m+2) sum_(k>=0) (k+t)_(m+1)x^k/t."""
    f = sp.expand(sp.prod(k + t + j for j in range(m + 1)))
    sums = [1/(1-x)]
    for _ in range(m + 1):
        sums.append(sp.factor(x * sp.diff(sums[-1], x)))
    series = sum(f.coeff(k, j) * sums[j] for j in range(m+2))
    return sp.factor(sp.cancel(series * (1-x)**(m+2) / t))


def cayley(m):
    p = kernel_numerator(m)
    return sp.factor(sp.cancel((1+u)**(m+1)*p.subs(x,(u-1)/(u+1))))


def routh_first_col(poly):
    """Construct exact Routh array (for polynomials without zero pivots)."""
    coeff = sp.Poly(poly, u).all_coeffs()
    deg = len(coeff)-1
    width = (deg+2)//2
    row0 = coeff[::2] + [sp.Integer(0)]* (width-len(coeff[::2]))
    row1 = coeff[1::2] + [sp.Integer(0)]* (width-len(coeff[1::2]))
    tab = [row0, row1]
    for j in range(2,deg+1):
        b, a = tab[-1][0], tab[-2][0]
        assert b != 0
        row = [sp.factor(sp.cancel((b*tab[-2][i+1]-a*tab[-1][i+1])/b))
               for i in range(width-1)] + [sp.Integer(0)]
        tab.append(row)
    return [sp.factor(row[0]) for row in tab]


R = [
    u + 2*t-1,
    u**2 + 2*t*u + 2*t**2-1,
    3*u**3+(6*t+3)*u**2+(6*t*t+6*t-3)*u+(4*t**3+6*t*t-4*t-3),
    3*u**4+6*(t+1)*u**3+6*t*(t+2)*u**2
        +(4*t**3+12*t*t+2*t-6)*u
        +(2*t**4+8*t**3+4*t*t-8*t-3)
]
scales = [t, t/2, t/2, t/8]
for m in range(4):
    actual = sp.expand(sp.cancel(scales[m]*cayley(m)))
    assert sp.simplify(actual-R[m]) == 0

expected_columns = [
    [sp.Integer(1), 2*t-1],
    [sp.Integer(1), 2*t, 2*t*t-1],
    [sp.Integer(3),6*t+3,4*t*(t+1),(2*t+1)*(2*t*t+2*t-3)],
    [sp.Integer(3),6*(t+1),(2*t+1)*(2*t+3),
       4*t*(t+1)*(t+2)*(t*t+2*t+3)/((2*t+1)*(2*t+3)),
       2*t**4+8*t**3+4*t*t-8*t-3]
]
for m in range(4):
    actual = routh_first_col(R[m])
    assert len(actual) == len(expected_columns[m])
    for a,b in zip(actual,expected_columns[m]):
        assert sp.simplify(a-b) == 0

T3 = sp.sqrt(2+sp.sqrt(10)/2)-1
assert sp.simplify(R[3].subs(u,0).subs(t,T3)) == 0
assert sp.simplify(R[3].subs(u,0).subs(t,sp.Rational(1,2))) < 0
assert sp.simplify(R[3].subs(u,0).subs(t,sp.Integer(1))) > 0

Q4_at_half = 30*(8*u**5+32*u**4+44*u**3+16*u**2-17*u-20)
Q4_at_one = 120*(u+1)**5
Q4_at_four = 30*(u**5+11*u**4+58*u**3+198*u**2+501*u+1023)
for v,expected in [(sp.Rational(1,2),Q4_at_half),(sp.Integer(1),Q4_at_one),(sp.Integer(4),Q4_at_four)]:
    assert sp.simplify(cayley(4).subs(t,v) - expected) == 0
assert routh_first_col(Q4_at_half/30) == [8,32,40,sp.Rational(128,5),sp.Rational(77,4),-20]
assert routh_first_col(Q4_at_four/30) == [1,11,40,sp.Rational(429,5),-sp.Rational(896,13),1023]

# Rational-parameter numerical checks illustrate, but do not prove, the universal claims.
import numpy as np
checks=0
for m in range(4):
    p = sp.Poly(kernel_numerator(m), x)
    tp = [sp.Rational(j,20) for j in range(1,81) if j not in (20,)]
    critical = [sp.Rational(1,2),1/sp.sqrt(2),(sp.sqrt(7)-1)/2,T3][m]
    for v in tp:
        coeff = [float(c.subs(t,v)) for c in p.all_coeffs()]
        # Remove leading coefficients that vanish at special rational parameters.
        while len(coeff)>1 and abs(coeff[0]) < 1e-11:
            coeff.pop(0)
        roots = np.roots(coeff)
        observed = sum(abs(z)<1-1e-7 for z in roots)
        expected = int(float(v)<float(critical))
        assert observed == expected,(m,v,roots,observed,expected)
        checks+=1
print(f"JACOBI_FIRST_REENTRANCE_PASS exact_cayley=4 exact_routh=4 exact_witnesses=3 sampled_cases={checks}")
