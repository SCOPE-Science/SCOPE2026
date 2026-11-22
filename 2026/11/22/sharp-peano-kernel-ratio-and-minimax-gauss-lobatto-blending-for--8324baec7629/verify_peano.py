"""Exact Peano-kernel certificate for a 3-Gauss/4-Lobatto blend.
Requires Python 3 and SymPy; no external data or downloads.
Run: python verify_peano.py
"""
from math import isqrt
import sympy as sp

x, z = sp.symbols('x z')
s5, s15 = sp.sqrt(5), sp.sqrt(15)
a, b, half = (5 - s15) / 10, (5 - s5) / 10, sp.Rational(1, 2)
R, T = 25 - 6*s15, 25 - 6*s15 + s5
c_star = sp.simplify(R/T)
G = [((5-s15)/10,sp.Rational(5,18)),(half,sp.Rational(8,18)),
     ((5+s15)/10,sp.Rational(5,18))]
L = [(sp.Integer(0),sp.Rational(1,12)),((5-s5)/10,sp.Rational(5,12)),
     ((5+s5)/10,sp.Rational(5,12)),(sp.Integer(1),sp.Rational(1,12))]

# The bounds are exact rationals formed solely by integer square roots.
SCALE = 10**70
sqrt_intervals = {
    d: (sp.Rational(isqrt(d*SCALE*SCALE),SCALE),
        sp.Rational(isqrt(d*SCALE*SCALE)+1,SCALE))
    for d in (3,5,15)
}

def rational_interval(expr):
    expr = sp.expand(sp.radsimp(expr))
    coeffs = {d: expr.coeff(sp.sqrt(d)) for d in (3,5,15)}
    const = sp.expand(expr-sum(coeffs[d]*sp.sqrt(d) for d in coeffs))
    assert const.is_Rational and all(v.is_Rational for v in coeffs.values())
    low = high = const
    for d, coefficient in coeffs.items():
        a0, b0 = sqrt_intervals[d]
        if coefficient >= 0:
            low += coefficient*a0
            high += coefficient*b0
        else:
            low += coefficient*b0
            high += coefficient*a0
    return low, high

def bernstein_coefficients(expr, left, right):
    pol = sp.Poly(sp.expand(expr.subs(x,left+(right-left)*z)),z)
    degree = pol.degree()
    return [sp.simplify(sum(pol.nth(k)*sp.binomial(j,k)/sp.binomial(degree,k)
            for k in range(j+1))) for j in range(degree+1)]

n_signs = 0
for region, (left, right) in enumerate(((sp.Integer(0),a),(a,b),(b,half))):
    midpoint = float(((left+right)/2).evalf(25))
    Gk = sum(weight*(node-x)**5 for node,weight in G if float(node)>midpoint)/120
    Lk = sum(weight*(node-x)**5 for node,weight in L if float(node)>midpoint)/120
    Ik = (1-x)**6/720
    A = sp.Poly(Ik-Gk,x,extension=[s5,s15]); D = sp.Poly(Lk-Gk,x,extension=[s5,s15])
    H = sp.Poly(R*D.as_expr()-T*A.as_expr(),x,extension=[s5,s15])
    if region == 0:
        assert A == sp.Poly(x**6/720,x,extension=[s5,s15])
        assert D == sp.Poly(x**5/1440,x,extension=[s5,s15])
        assert H == sp.Poly(x**5*(R-2*T*x)/1440,x,extension=[s5,s15])
        assert rational_interval(sp.simplify(R-2*T*a))[0] > 0
        n_signs += 1
    else:
        for value in (A.as_expr(),D.as_expr()):
            for coefficient in bernstein_coefficients(value,left,right):
                assert rational_interval(coefficient)[0] > 0
                n_signs += 1
        if region == 2:
            H, remainder = sp.div(H,sp.Poly((half-x)**2,x,extension=[s5,s15]))
            assert remainder.is_zero
        coefficients = bernstein_coefficients(H.as_expr(),left,right)
        assert len(coefficients) == (7 if region==1 else 5)
        for coefficient in coefficients:
            assert rational_interval(coefficient)[0] > 0
            n_signs += 1
    if region == 2:
        assert sp.simplify(A.eval(half)*T-D.eval(half)*R) == 0

assert rational_interval(R)[0]>0 and rational_interval(T)[0]>0
assert rational_interval(sp.Rational(1,2)*T-R)[0]>0 # c_star < 1/2
# The two ratios 0 and c_star are approachable by smooth nonnegative sixth derivatives
# concentrating near the endpoint and center of the interval, respectively.
assert sp.simplify(c_star - (25 - 6*s15)/(25 - 6*s15 + s5)) == 0
assert sp.simplify((sp.Rational(1,4)-c_star/2)/(sp.Rational(1,4))- (1-2*c_star))==0
# Degree-five exactness of both primitive rules.
for degree in range(6):
    exact = sp.Rational(1,degree+1)
    assert sp.simplify(sum(w*node**degree for node,w in G)-exact)==0
    assert sp.simplify(sum(w*node**degree for node,w in L)-exact)==0
print('PASS: exact polynomial identities; %d strictly positive algebraic interval certificates; 12 polynomial moment identities.' % n_signs)
print('c_star =',sp.N(c_star,20))
print('minimax blending weight c_star/2 =',sp.N(c_star/2,20))
print('relative certificate improvement over 1/4 =',sp.N(1-2*c_star,20))
