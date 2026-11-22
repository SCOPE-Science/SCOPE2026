#!/usr/bin/env python3
"""Symbolic checks for the three-site wrapped Cauchy mode threshold.
Requires Python 3 and SymPy; executes exact rational operations.
"""
import sympy as s
r, x, w = s.symbols('r x w', real=True)
D1 = 1+r**2-2*r*x
T3 = 4*x**3-3*x
D3 = 1+r**6-2*r**3*T3
Q = 1-r**2+r**4+2*r*(1+r**2)*x+4*r**2*x**2
S = 1+r**2+r**4
H = 9*r**2*S*(1-4*x**2)/Q**2
F = 9*r**2*S/(1-r**2)**3
checks=0
def same(a,b):
    global checks
    assert s.cancel(a-b)==0
    checks+=1
same(D3,D1*Q)
same(s.diff(H,x),-36*r**2*S*(r+2*x)*(1+2*r*x)*D1/Q**3)
same(H.subs(x,-r/2),F)
same(s.diff(F,r),18*r*(1+2*r**2)**2/(1-r**2)**4)
same(s.diff(H,x,2).subs(x,-r/2),-72*r**2*S*(1+2*r**2)/(1-r**2)**5)
same(s.cancel(2*s.diff(F,r)/(-s.diff(H,x,2).subs(x,-r/2))),
    (1-r**2)*(1+2*r**2)/(2*r*S))
# The full derivative has the sign of (w-1-H(x)) in the middle sector.
# Outside the middle sector, (4*x*x-1) is nonnegative.
for rv in [s.Rational(1,5),s.Rational(1,3),s.Rational(1,2),s.Rational(3,4)]:
    poly=s.together((w-1-H)*Q**2).subs({r:rv,w:2}).expand()
    poly=s.Poly(poly,x)
    count=poly.count_roots(-s.Rational(1,2),s.Rational(1,2))
    should=2 if F.subs(r,rv)>1 else 0
    assert count==should, (rv,count,should)
    checks+=1
q=s.symbols('q',real=True)
same(s.expand(9*q*(1+q+q*q)-(1-q)**3),10*q**3+6*q**2+12*q-1)
assert s.Poly(10*q**3+6*q**2+12*q-1,q).count_roots(0,1)==1
checks+=1
print('PASS:',checks,'exact symbolic, interval-root and algebra assertions')
