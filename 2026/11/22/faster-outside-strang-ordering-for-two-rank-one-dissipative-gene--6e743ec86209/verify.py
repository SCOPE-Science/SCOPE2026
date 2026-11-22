"""Exact algebra and numerical spot checks for rank-one Strang ordering."""
import sympy as sp
import numpy as np
from scipy.linalg import expm

x,y,z,w,a,b = sp.symbols('x y z w a b', real=True)
P = sp.Matrix([[1,0],[0,0]])
Q = sp.Matrix([[z,w],[w,1-z]])
I=sp.eye(2)
S_A=(I-(1-x)*P)*(I-(1-y*y)*Q)*(I-(1-x)*P)
S_B=(I-(1-y)*Q)*(I-(1-x*x)*P)*(I-(1-y)*Q)
F=(a-b)*x*y-(a+b)*x+(a+b)*y-a+b
T=2*a*P+2*b*Q-(a+b)*I

def reduce(expr):
    num=sp.together(sp.expand(expr))
    return sp.factor(sp.rem(num,w*w-z*(1-z),w))

assert reduce(sp.trace(S_A-S_B))==0
assert reduce(sp.trace(S_A*S_A-S_B*S_B))==0
assert reduce(sp.trace(T*(S_A-S_B))-2*z*(1-z)*(1-x)*(1-y)*F)==0
assert sp.factor(F-(b*(1-x)*(1+y)-a*(1+x)*(1-y)))==0
assert reduce(S_A.det()-S_B.det())==0
print('PASS 5 symbolic identities')

# Exact-rational value substitutions for the matrix-level formulas.
for zz in [sp.Rational(1,9),sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4),sp.Rational(8,9)]:
    for xx in [sp.Rational(1,5),sp.Rational(2,5),sp.Rational(4,5)]:
        for yy in [sp.Rational(1,7),sp.Rational(3,7),sp.Rational(6,7)]:
            ww=sp.sqrt(zz*(1-zz))
            a0=sp.Rational(4,3);b0=sp.Rational(7,5)
            sub={z:zz,x:xx,y:yy,w:ww,a:a0,b:b0}
            assert sp.simplify(sp.trace(T*(S_A-S_B)).subs(sub) - (2*z*(1-z)*(1-x)*(1-y)*F).subs(sub))==0
print('PASS 45 exact-rational matrix contractions')

# Independent high-dimensional checks with genuine matrix exponentials.
rng=np.random.default_rng(721149)
worst=0
for i in range(120):
    d=int(rng.integers(2,9));u=rng.normal(size=d);u/=np.linalg.norm(u)
    v=rng.normal(size=d);v/=np.linalg.norm(v)
    A=float(np.exp(rng.uniform(-2,2)));B=float(np.exp(rng.uniform(-2,2)))
    h=float(np.exp(rng.uniform(-2,2)))
    PP=np.outer(u,u);QQ=np.outer(v,v)
    E=expm(-2*h*(A*PP+B*QQ))
    SA=expm(-h*A*PP)@expm(-2*h*B*QQ)@expm(-h*A*PP)
    SB=expm(-h*B*QQ)@expm(-2*h*A*PP)@expm(-h*B*QQ)
    lhs=np.linalg.norm(SA-E,'fro')**2-np.linalg.norm(SB-E,'fro')**2
    x0=np.exp(-A*h);y0=np.exp(-B*h);zz=float(np.dot(u,v)**2)
    delta=np.sqrt((A-B)**2+4*A*B*zz)
    L=np.exp(-(A+B)*h)*np.sinh(h*delta)/delta
    ff=B*(1-x0)*(1+y0)-A*(1+x0)*(1-y0)
    rhs=4*L*zz*(1-zz)*(1-x0)*(1-y0)*ff
    err=abs(lhs-rhs)
    worst=max(worst,err)
    assert err<2e-11, (i,lhs,rhs)
print('PASS 120 high-dimensional exponential tests; worst absolute discrepancy',worst)
