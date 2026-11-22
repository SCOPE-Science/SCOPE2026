"""Exact symbolic and high-precision checks for the two-cell C1 cubic spline quadrature theorem.

Requires Python 3 and SymPy. Run: python verify.py
The analytic sign and uniqueness proofs are in RESULT.md; finite checks are supplementary.
"""
from fractions import Fraction
from math import isfinite
import sympy as sp

s = sp.symbols('s', real=True)
Q = 12*s**3 - 48*s**2 + 64*s - 27
U = (3*s**4 - 6*s**3 - 16*s**2 + 48*s - 27)/Q
V = (3*s**4 - 16*s**3 + 24*s**2 - 9)/(2*Q)
M = [sp.Rational(1, k+1) - sp.Rational(16,27)*s*(s/4)**k for k in range(4)]
checks = 0

def exact(expr, expected=0):
    global checks
    assert sp.cancel(expr - expected) == 0, (expr, expected)
    checks += 1

exact(M[2]-U*M[1]+V*M[0]); exact(M[3]-U*M[2]+V*M[1])
exact(M[0]*M[2]-M[1]**2, -Q/324)
exact(U**2-4*V,
      9*(s-1)**4*(s**4-8*s**3+30*s**2-52*s+27)/Q**2)
exact(s**2-U*s+V, 9*(s-1)**4*(2*s-1)/(2*Q))
exact(1-U+V, -(s-1)**2*(3*s**2-14*s+9)/(2*Q))
exact(M[1]-s*M[0], (2*s-3)*(4*s-3)/18)
exact(M[0]-M[1], (8*s**2-32*s+27)/54)
exact(sp.diff(Q,s),4*(3*s-4)**2)
exact(Q.subs(s,sp.Rational(1,2)),sp.Rational(-11,2))

D = sp.factor(U**2-4*V)
small = (U-sp.sqrt(D))/2
large = (U+sp.sqrt(D))/2
for k, e in enumerate([sp.Rational(1,2),sp.Rational(8,11),sp.Rational(96,121)]):
    exact(sp.simplify(sp.diff(small,s,k).subs(s,sp.Rational(1,2))), e)
for k, e in enumerate([sp.Rational(7,8),sp.Rational(1,4),sp.Rational(6,11)]):
    exact(sp.simplify(sp.diff(large,s,k).subs(s,sp.Rational(1,2))), e)

# The complete first derivative vector is continuous across the reflected knot.
w2=(M[0]*large-M[1])/(large-small)
w3=M[0]-w2
left_rule=[s/4,small,large,sp.Rational(16,27)*s,w2,w3]
expected=[sp.Rational(1,4),sp.Rational(8,11),sp.Rational(1,4),sp.Rational(16,27),0,-sp.Rational(16,27)]
for expr,goal in zip(left_rule,expected):
    exact(sp.simplify(sp.diff(expr,s).subs(s,sp.Rational(1,2))),goal)

# The uniform symmetric rule is exact on the six-dimensional spline basis.
xs=[sp.Rational(1,8),sp.Rational(1,2),sp.Rational(7,8)]
ws=[sp.Rational(8,27),sp.Rational(11,27),sp.Rational(8,27)]
for k in range(4): exact(sum(w*x**k for w,x in zip(ws,xs)),sp.Rational(1,k+1))
for k in (2,3): exact(ws[2]*(xs[2]-sp.Rational(1,2))**k,sp.Rational(1,2)**(k+1)/(k+1))

# Check all moment and endpoint inequalities for a rich fixed rational sample.
# This is not a proof of the continuum statement.
for a in [sp.Rational(k,200) for k in range(1,101)]:
    m=[x.subs(s,a) for x in M]
    q=Q.subs(s,a)
    assert q<0
    l=sp.N(small.subs(s,a),40);r=sp.N(large.subs(s,a),40)
    p1=a/4
    w1=sp.Rational(16,27)*a
    w2=(m[0]*r-m[1])/(r-l)
    w3=m[0]-w2
    assert 0<p1<a<=l<r<1, (a,l,r)
    assert w1>0 and w2>0 and w3>0
    nodes=[sp.N(p1,40),l,r];weights=[sp.N(w1,40),w2,w3]
    for k in range(4):
        diff=sum(weights[i]*nodes[i]**k for i in range(3))-sp.Rational(1,k+1)
        assert abs(diff)<sp.Float('1e-30')
        checks+=1
    for k in (2,3):
        diff=weights[0]*(a-nodes[0])**k-a**(k+1)/sp.Integer(k+1)
        assert abs(diff)<sp.Float('1e-30')
        checks+=1
    checks+=5

# 2-node exactness fails because single nodes on both sides force mass 16/27.
exact(sp.Rational(16,27)*s + sp.Rational(16,27)*(1-s),sp.Rational(16,27))
# Knot-locked 3-node linear moment is (s+4)/9, equal to 1/2 only at s=1/2.
exact(sp.Rational(16,27)*s*(s/4)+sp.Rational(11,27)*s+
      sp.Rational(16,27)*(1-s)*(s+3)/4, (s+4)/9)
print(f'PASS: {checks} symbolic/rational and high-precision assertions; no infinitary claim inferred from finite tests')
