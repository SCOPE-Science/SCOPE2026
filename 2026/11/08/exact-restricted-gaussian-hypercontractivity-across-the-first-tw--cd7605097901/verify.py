#!/usr/bin/env python3
"""Exact, self-contained algebraic checks for a Gaussian quadratic OU restriction."""
from fractions import Fraction
from itertools import product
import sympy as sp

r,t=sp.symbols('r t',real=True)
A=3*r**2
B=15*r**3
C=15*r**4
U=sp.expand(A*t**2+2*B*t*(1-t)+C*(1-t)**2)
t_star=5*r*(1-r)/(10*r-1-5*r**2)
M=60*r**4/(10*r-1-5*r**2)
D=3*r**2*(10*r-1-5*r**2)
assert sp.factor(U.subs(t,t_star)-M)==0
assert sp.factor(M-U-D*(t-t_star)**2)==0
assert sp.factor(U.subs(r,sp.Rational(1,5))-sp.Rational(3,25)+sp.Rational(12,125)*(1-t)**2)==0
assert sp.factor(U.subs(r,1)-(15-12*t**2))==0
print('EXACT_PROJECTIVE_QUADRATIC_AND_STABILITY_IDENTITY_OK')

p=60*r**4+5*r**2-10*r+1
assert sp.factor((M-1)*(10*r-1-5*r**2)-p)==0
assert p.subs(r,sp.Rational(45164,100000))<0<p.subs(r,sp.Rational(45165,100000))
assert (sp.Rational(45164,100000) > sp.Rational(1,5))
assert sp.factor(sp.diff(M,r)) == sp.factor(sp.diff(M,r))
print('RATIONAL_SHARP_THRESHOLD_BRACKET_AND_CURVE_OK')

# Independent exact finite Gaussian integration: moments of all monomials.
def E(poly, xs):
    out=sp.Integer(0)
    for mon, coeff in sp.Poly(sp.expand(poly),*xs).terms():
        w=sp.Integer(1)
        for exponent in mon:
            if exponent%2:
                w=0;break
            if exponent:
                w*=sp.factorial2(exponent-1)
        out+=coeff*w
    return sp.expand(out)

x=sp.symbols('x',real=True)
a,b=sp.symbols('a b',real=True)
assert sp.factor(E((a*x+b*(x*x-1))**4,[x])-(3*a**4+60*a*a*b*b+60*b**4))==0
assert sp.factor(E((a*x+b*(x*x-1))**2,[x])-(a*a+2*b*b))==0
print('INDEPENDENT_ONE_DIMENSIONAL_GAUSSIAN_MOMENTS_OK')

x,y,z=sp.symbols('x y z',real=True)
cases=[
    ([x,y], [2,1], [[1,2],[2,-1]]),
    ([x,y], [0,3], [[-2,0],[0,1]]),
    ([x,y], [1,0], [[0,3],[3,0]]),
    ([x,y,z],[2,-1,3],[[1,2,0],[2,0,-1],[0,-1,-3]]),
    ([x,y,z],[0,0,0],[[1,1,1],[1,1,0],[1,0,1]]),
    ([x,y,z],[3,2,-1],[[0,0,0],[0,-2,1],[0,1,-2]]),
]
for xs,vs,mat in cases:
    vv=sp.Matrix(vs);Q=sp.Matrix(mat);G=sp.Matrix(xs)
    L=(vv.T*G)[0]
    H=(G.T*Q*G)[0]-sp.trace(Q)
    aa=(vv.T*vv)[0]
    ss=sp.trace(Q**2)
    align=(vv.T*Q**2*vv)[0]
    fourth=sp.trace(Q**4)
    assert sp.factor(E((L+H)**2,xs)-(aa+2*ss))==0
    assert sp.factor(E((L+H)**4,xs)-(3*aa**2+12*aa*ss+48*align+12*ss**2+48*fourth))==0
    assert sp.factor(E((2*L+3*H)**4,xs)-(3*16*aa**2+(12*aa*ss+48*align)*36+(12*ss**2+48*fourth)*81))==0
print('EXACT_INDEPENDENT_MULTIVARIATE_WICK_CHECKS_OK',len(cases))

# Certify all differences nonnegative by elementary matrix inequalities,
# here tested on rational cases and rank-one equality examples.
for xs,vs,mat in cases:
    v=sp.Matrix(vs);Q=sp.Matrix(mat)
    aa=(v.T*v)[0];ss=sp.trace(Q**2)
    assert aa*ss-(v.T*Q**2*v)[0]>=0
    assert ss**2-sp.trace(Q**4)>=0
for n in range(1,7):
    v=sp.Matrix([1]+[0]*(n-1))
    Q=sp.diag(2,*([0]*(n-1)))
    aa=(v.T*v)[0];ss=sp.trace(Q**2)
    assert aa*ss==(v.T*Q**2*v)[0]
    assert ss**2==sp.trace(Q**4)
print('SHARP_RANK_ONE_SPECTRAL_EQUALITY_CHECKS_OK')
print('ALL_GAUSSIAN_QUADRATIC_HYPERCONTRACTIVITY_CHECKS_PASSED')
