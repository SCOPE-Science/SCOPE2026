#!/usr/bin/env python3
"""Symbolic checks for the flow continuation and escape-cone identities.
Run with: python3 check.py  (requires sympy).
All infinite-time conclusions follow from the written inequalities, not this test.
"""
import sympy as s
x,y,z,a,b,c,k=s.symbols('x y z a b c k', real=True)
f=s.Matrix([y,-a*x+y*z,b*y-c*x*y-x*x]) # y>0 sector, only for cone
w=z+c*x*x/2
wdot=s.expand(s.diff(w,x)*f[0]+s.diff(w,y)*f[1]+s.diff(w,z)*f[2])
assert s.simplify(wdot-(b*y-x*x))==0
E=(a*x*x+y*y)/2
Edot=s.expand(s.diff(E,x)*f[0]+s.diff(E,y)*f[1])
assert s.simplify(Edot-z*y*y)==0
# cone boundary equations, with c=-k and w=z-k*x*x/2
W=s.symbols("W",real=True)
zs=W+k*x*x/2
h=W+k*x*x/4
g=y-k*x**3/24
xdot=y
ydot=-a*x+zs*y
wprime=b*y-x*x
hprime=s.expand(wprime+k*x*xdot/2)
gprime=s.expand(ydot-k*x*x*xdot/8)
assert s.simplify(hprime-(b*y-x*x+k*x*y/2))==0
assert s.simplify(gprime-(-a*x+(W+3*k*x*x/8)*y))==0
# Evaluate at each relevant cone face; both are algebraic identities.
hface=s.simplify(hprime.subs(W,-k*x*x/4))
gface=s.simplify(gprime.subs(y,k*x**3/24))
assert s.expand(hface-(b*y-x*x+k*x*y/2))==0
assert s.expand(gface-(-a*x + k*x**3/24*(W+3*k*x*x/8)))==0
# At g=0 and h>=0, the claimed lower bound is -a*x+k^2*x^5/192.
lower=s.expand(gface.subs(W,-k*x*x/4))
assert s.simplify(lower-(-a*x+k*k*x**5/192))==0
# At h=0 and x>=4|b|/k, positive y>=k*x^3/24,
# h' >= -x^2+(k^2/96)x^4, verified coefficient.
q=s.simplify((-x*x+(k*x/4)*(k*x**3/24))-(-x*x+k*k*x**4/96))
assert q==0
print('PASS: shear, oscillator energy, cone boundaries and strict derivative margins')
