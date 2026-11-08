"""Exact algebraic checks for symmetric three-variable quadratic norm deficits."""
import sympy as sp
s,u,c,x=sp.symbols('s u c x', real=True)
A=4*u**2-2-s
B=-2*s*u
F=(A-1)**2+B**2+4*A*c**2+2*B*(A+1)*c
h=(s-1)**3*(s+2)/(s-2)
cstar=sp.cancel(-B*(A+1)/(4*A))
xstar=(s**2-s-4)/(4*(s-2))
first=(s+2)*(1-u**2)*(s**2-4*s*u**2-s+8*u**2-4)**2/((s-2)*(s+2-4*u**2))
second=4*(s+2-4*u**2)*(c-cstar)**2
assert sp.cancel(h-F-first-second)==0
assert sp.factor(sp.factor((cstar-u)/u).subs(u**2,xstar))==0
ratio=sp.Rational(9,4)*(s**2-4)/(s-1)**3
assert sp.simplify(sp.diff(ratio,s)+sp.Rational(9,4)*(s**2+2*s-12)/(s-1)**4)==0
r=sp.sqrt(13)-1
assert sp.simplify(ratio.subs(s,r)-(35+13*sp.sqrt(13))/54)==0
print('SA_PHASE_IDENTITY_PASS')
