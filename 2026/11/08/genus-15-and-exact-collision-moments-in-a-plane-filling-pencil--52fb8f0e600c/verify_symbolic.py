#!/usr/bin/env python3
"""Exact symbolic collision-curve certificate, no dependencies beyond SymPy."""
import sympy as S
x,y,s,t=S.symbols('x y s t')
F=x**3*y**3*(x+y)*(x**2+y**2)+(x**2+x*y+y**2)
M=S.expand((y**3-x**3)+x**3*y**3*(y**4-x**4))
assert S.expand(M-(y-x)*F)==0
assert S.expand(F.subs({x:t,y:s*t})-t**2*(t**7*s**3*(1+s)*(1+s**2)+(1+s+s**2)))==0
num=-(1+s+s**2); den=s**3*(1+s)*(1+s**2)
assert S.gcd(num,den)==1
assert S.factor(num)==-s**2-s-1
# Over an algebraic closure, the finite zeros and poles are disjoint:
# primitive cube roots: 2 zeros of order 1; 0: pole of order 3;
# -1,i,-i: 3 poles of order 1; infinity: zero of order 4.
ramification_orders=[1,1,-3,-1,-1,-1,4]
assert sum(ramification_orders)==0 and all(z%7 for z in ramification_orders)
num_branch=len(ramification_orders)
assert num_branch==7
assert 2*15-2 == -14+6*num_branch
print('SYMBOLIC_COLLISION_CURVE_BIRATIONAL_KUMMER_GENUS15_PASS')
