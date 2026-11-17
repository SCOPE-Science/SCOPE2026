"""Exact identities and finite diagnostics for a delayed rational map."""
from fractions import Fraction
import math
import numpy as np
import sympy as sp

x, y, z, u, v, a, b, r, t = sp.symbols('x y z u v a b r t', positive=True)
F = (u + a*(x+z))/(v + b*(x+z) + r*y)
D = v+(2*b+r)*t
Q = (r+2*b)*t*t + (v-2*a)*t-u
assert sp.simplify((F.subs({x:t,y:t,z:t})-t)*D+Q) == 0
J = sp.Matrix([[sp.diff(F,w).subs({x:t,y:t,z:t}) for w in (x,y,z)],[1,0,0],[0,1,0]])
alpha = (a-b*t)/D
omega = r*t/D
Js = sp.Matrix([[alpha,-omega,alpha],[1,0,0],[0,1,0]])
for i in range(3):
    assert sp.simplify((J-Js)[0,i].subs(u,(r+2*b)*t*t+(v-2*a)*t)) == 0
lam=sp.symbols('lam')
assert sp.factor(Js.charpoly(lam).as_expr()-(lam**3-alpha*lam**2+omega*lam-alpha)) == 0
A,B=sp.symbols('A B',positive=True)
e1=A*(v+2*b*B+r*A)-u-2*a*B
e2=B*(v+2*b*A+r*B)-u-2*a*A
assert sp.simplify((e1-e2)-(A-B)*(v+2*a+r*(A+B))) == 0

cases=[(1,1,3,2),(2,5,sp.Rational(1,10),7),(4,sp.Rational(1,5),10,sp.Rational(1,10)),
       (1,30,2,12),(17,2,1,1),(3,4,7,1)]
for U,V,AA,BB in cases:
    for R in (sp.Rational(1,5),1,13,250,10000):
        U,V,AA,BB,R=map(sp.Rational,(U,V,AA,BB,R))
        T=sp.factor((2*AA-V+sp.sqrt((V-2*AA)**2+4*U*(R+2*BB)))/(2*(R+2*BB)))
        DD=V+(R+2*BB)*T
        al=(AA-BB*T)/DD; om=R*T/DD
        assert abs(float(al)) < .5 and 0<float(om)<1
        assert float(1-2*al+om)>0 and float(1+2*al+om)>0 and float(1-om)>0
        roots=np.roots([1.,-float(al),float(om),-float(al)])
        assert max(abs(w) for w in roots)<1.0000000001
        assert abs(float(((R+2*BB)*T*T+(V-2*AA)*T-U).evalf(30))) < 1e-12
for U,V,AA,BB in cases:
    U,V,AA,BB=map(float,(U,V,AA,BB))
    for R in (10**6,10**8):
        T=(2*AA-V+math.sqrt((V-2*AA)**2+4*U*(R+2*BB)))/(2*(R+2*BB))
        DD=V+(R+2*BB)*T
        al=(AA-BB*T)/DD; om=R*T/DD
        rho=max(abs(z) for z in np.roots([1.,-al,om,-al]))
        scaled=math.sqrt(R)*(1-rho)
        predicted=V/(2*math.sqrt(U))
        if R==10**8:
            assert abs(scaled-predicted) < max(.01, .012*predicted)
print('PASS: exact polynomial identities; 30 rational-parameter Schur cases; singular-gap diagnostics')
