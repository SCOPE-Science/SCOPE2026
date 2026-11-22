#!/usr/bin/env python3
"""Exact and independent finite checks for an axial variational dichotomy.

Requires Python 3 and SymPy. These checks test algebraic steps; the proof of
long-time behavior is analytic and is supplied in RESULT.md.
"""
import sympy as sp

a,b,c,k,s,z0,t=sp.symbols('a b c k s z0 t', real=True, nonzero=True)
x,y,z=sp.symbols('x y z', real=True)
F=sp.Matrix([a*(y-x)+k*x*z,-c*y-x*z,-b+x*y])
J=F.jacobian([x,y,z])
assert F.subs({x:0,y:0,z:z0-b*t}) == sp.Matrix([0,0,-b])
assert J.subs({x:0,y:0,z:-s})[:2,:2] == sp.Matrix([[-a-k*s,a],[s,-c]])

# The equilibrium branches, for a,k,c,b>0 and a-c*k>0.
xe=sp.sqrt(b*(a-c*k)/a)
ye=b/xe
ze=-a*c/(a-c*k)
for sign in [-1,1]:
    assert all(sp.simplify(v)==0 for v in F.subs({x:sign*xe,y:sign*ye,z:ze}))

A=a/k
B=a*(c-a)/k**2-a**2/k**3
r=A/s+B/s**2
riccati=a+(c-a-k*s)*r-s*r**2
res=sp.factor(riccati-b*sp.diff(r,s))
assert sp.simplify(sp.limit(s*res,s,sp.oo))==0
coeff2=sp.simplify(sp.limit(s*s*res,s,sp.oo))
assert sp.simplify(coeff2-((c-a)*B-2*A*B+b*A))==0
assert sp.simplify(B.subs(k,a/c)+c*c)==0
assert sp.simplify((A-c).subs(k,a/c))==0

# Scalar reduction: y'' + P y' + Q y = 0, s=bt-z0.
P=a+c+k*s-b/s
Q=a*c+(c*k-a)*s-b*c/s
Y,Y1,Y2=sp.symbols('Y Y1 Y2')
X=(Y1+c*Y)/s
# y'' = b/s (y'+cy)+ s x' -cy'; substitute x' below.
Y2_from=b*X+s*((-a-k*s)*X+a*Y)-c*Y1
assert sp.simplify(Y2_from+P*Y1+Q*Y)==0
# Wronskian of the scalar equation: W'= -P W.
W=s*sp.exp(-(a+c)*t-k*s*s/(2*b))
W_as_func= (b*t-z0)*sp.exp(-(a+c)*t-k*(b*t-z0)**2/(2*b))
assert sp.simplify(sp.diff(W_as_func,t)/W_as_func+P.subs(s,b*t-z0))==0

# Finite rational evaluations of the Riccati residual and equilibrium identities.
for aa,bb,cc,kk in [(2,3,1,1),(2,3,1,2),(2,3,1,4),(4,5,3,2),(10,100,sp.Rational(56,5),sp.Rational(9,10))]:
    if aa-cc*kk <=0:
        continue
    arg={a:sp.Integer(aa),b:sp.Integer(bb),c:sp.Rational(cc),k:sp.Rational(kk)}
    assert all(sp.simplify(v.subs(arg))==0 for v in F.subs({x:xe,y:ye,z:ze}))
    for ss in [11,29,101,997]:
        R=sp.together(res.subs({**arg,s:sp.Integer(ss)}))
        assert R.is_Rational or R.is_Integer

# Independently derive the first two slow-ratio coefficients by matching powers.
u=sp.symbols('u',positive=True)
L1,L2=sp.symbols('L1 L2')
r_u=L1*u+L2*u**2
balance=sp.expand((a+(c-a-k/u)*r_u-r_u**2/u)+b*u*u*sp.diff(r_u,u))
co0=sp.expand(balance).coeff(u,0)
co1=sp.expand(balance).coeff(u,1)
assert sp.solve(co0,L1)==[A]
assert sp.simplify(sp.solve(co1.subs(L1,A),L2)[0]-B)==0

print('PASS: symbolic identities, equilibrium branches, scalar reduction, Riccati coefficients, and rational evaluations')
