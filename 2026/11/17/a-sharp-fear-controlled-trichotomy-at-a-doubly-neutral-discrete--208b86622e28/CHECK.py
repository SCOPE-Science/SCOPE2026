#!/usr/bin/env python3
"""Check the exact analytic jets and finite numerical diagnostics."""
import math
import sympy as sp
s,y=sp.symbols('s y')
A,B,H,J,k=sp.symbols('A B H J k')
def truncate(expr,degree):
    P=sp.Poly(sp.expand(expr),s,y)
    return sp.Add(*[co*s**t[0]*y**t[1] for t,co in P.terms() if sum(t)<=degree])
x=s-B*y/2
E=truncate(-2*x*sum((-k*y)**j for j in range(4))-B*y*sum((-H*x)**j for j in range(4)),3)
F=truncate((1+x)*sum(truncate(E**j,3)/sp.factorial(j) for j in range(4))-1,3)
D=truncate(-A*y*sum((-J*x)**j for j in range(3)),3)
G=truncate(y*sum(truncate(D**j,3)/sp.factorial(j) for j in range(3)),3)
S=truncate(F+B*G/2,3)
S2=truncate(S.subs({s:S,y:G},simultaneous=True),3)
P=sp.Poly(S2,s,y)
assert sp.simplify(P.coeff_monomial(s)-1)==0
assert sp.simplify(P.coeff_monomial(s**3)+sp.Rational(4,3))==0
assert sp.simplify(P.coeff_monomial(s*y)+2*(2*k+B*(1+H)))==0
assert sp.simplify(P.coeff_monomial(s**2*y))==0
assert sp.simplify(P.coeff_monomial(y**2))==0
# At y=0, the original prey map has multiplier -1. Its second iterate has no quartic term.
z=sp.symbols('z')
f=sp.series((1+z)*sp.exp(-2*z)-1,z,0,5).removeO()
f2=sp.series(f.subs(z,f),z,0,5).removeO()
assert sp.expand(f2).coeff(z,4)==0
print('Symbolic two-step jets: PASS')
K=gamma=beta=b=c=1.;a=10.;A0=a/(b*K+c);B0=beta/(K+gamma);H0=K/(K+gamma)
for kval in (0.25,0.875,1.5):
    L0=2*kval+B0*(1+H0); p=L0/A0
    yy=0.001;ss=0.1;xx=ss-B0*yy/2
    for n in range(1,200001):
        xn=(1+xx)*math.exp(-2*xx/(1+kval*yy)-beta*yy/(K*(1+xx)+gamma))-1
        yn=yy*math.exp(-a*yy/(b*K*(1+xx)+c))
        xx,yy=xn,yn
    zz=xx+B0*yy/2
    assert zz>0 and abs(A0*n*yy-1)<0.02
    if p<0.5:
        scaled=math.sqrt(n)*zz
        target=math.sqrt(3*(1-2*p))/2
        assert abs(scaled/target-1)<0.05,(p,scaled,target)
    elif p==0.5:
        scaled=math.sqrt(n*math.log(n))*zz
        assert 0.7 < scaled/(math.sqrt(3)/2) < 1.5
    else:
        assert 0 < (n**p)*zz < 10
    print('Finite diagnostic:', 'k=',kval,'p=',p,'A*n*v=',A0*n*yy)
print('All finite checks: PASS (not an infinite-time certificate)')
