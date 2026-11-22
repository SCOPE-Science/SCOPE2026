#!/usr/bin/env python3
"""Exact polynomial certificates for a quadratic planar three-cycle census."""
import sympy as S
x,v,c=S.symbols('x v c')
t=x*(1-x); z=c*c*t; H=z**3-(c*c+3)*(z+2)
x1=x+v;x2=x1+c*t
f=S.expand(x2+c*x1*(1-x1)-x)
g=S.expand(c*x2*(1-x2)-v)
R=S.factor(S.resultant(f,g,v))
assert S.simplify(R/(c*c*x*(x-1)*H)) in (-1,1)
sub=S.subresultants(f,g,v)[-2]
y0=-c*t*(z+c*(2*x-1)+1)/(2*(1+z))
assert S.factor(sub.subs(v,y0))==0
for eq in (f,g):
 num=S.together(eq.subs(v,y0)).as_numer_denom()[0]
 assert S.rem(num,H,x)==0
xs=[x,x+y0,x+y0+c*t]
tau=S.factor(1+c*(3-2*sum(xs)))
delta=S.factor(c**3*S.prod(2*u-1 for u in xs))
for expr in ((tau-1)**2-(c*c-24),delta-(c*c+4)*(tau-1)):
 num=S.together(expr).as_numer_denom()[0]
 assert S.rem(num,H,x)==0
s=S.symbols('s')
assert S.expand(s**3-16*s**2-176*s-384)==S.expand((s-24)*(s+4)**2)
q=S.Symbol('Z'); assert S.factor(q**3-27*(q+2))==(q-6)*(q+3)**2
# Numeric checks are only diagnostics, not the proof of exhaustiveness.
for val in (23.9,24.0003,25.0):
 roots=S.nroots(S.Symbol('Z')**3-(val+3)*(S.Symbol('Z')+2),maxsteps=100)
 real_x=sum(2 if (1-4*float(S.re(q))/val)>1e-9 else 1 for q in roots if abs(float(S.im(q)))<1e-7 and (1-4*float(S.re(q))/val)>=-1e-9)
 expected=0 if val<24 else 6
 assert real_x==expected,(val,real_x,expected)
print('PASS: exact resultant, common-root reconstruction, Floquet identities, cubic threshold and finite diagnostics')
