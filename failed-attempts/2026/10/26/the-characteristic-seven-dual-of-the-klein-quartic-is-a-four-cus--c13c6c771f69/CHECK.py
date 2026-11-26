#!/usr/bin/env python3
"""Exact polynomial checks for the characteristic-seven Klein dual quintic.
Run with SymPy 1.14 or later. All polynomial coefficients are reduced modulo 7.
"""
import sympy as s
h,u,v,x,y,z,a,b,c=s.symbols('h u v x y z a b c')
p=7
P=[4*(h+3)**3*(h-2),(h+3)*(h-1)**3,2*(h-1)*(h-2)**3]
L=[2*(h-2)**2*(h-1)**3,-3*(h+3)**2*(h-2)**3,(h-1)**2*(h+3)**3]
F=lambda X,Y,Z:X**3*Y+Y**3*Z+Z**3*X
G=lambda A,B,C:A**3*C**2-3*A**2*B**3+2*B**2*C**3
zero=lambda q,var:hpoly(q,var).is_zero
def hpoly(q,var):return s.Poly(s.expand(q),var,modulus=p)
assert zero(F(*P),h)
assert zero(G(*L),h)
D=[P[1]*s.diff(P[2],h)-P[2]*s.diff(P[1],h),P[2]*s.diff(P[0],h)-P[0]*s.diff(P[2],h),P[0]*s.diff(P[1],h)-P[1]*s.diff(P[0],h)]
for q,ell in zip(D,L):assert zero(q-ell,h)
g=s.gcd(s.gcd(hpoly(L[0],h),hpoly(L[1],h)),hpoly(L[2],h))
assert g.degree()==0
# Only finite critical parameters are -3, 1 and 2.
E=[hpoly(L[i]*s.diff(L[j],h)-L[j]*s.diff(L[i],h),h) for i,j in [(0,1),(0,2),(1,2)]]
g=s.gcd(s.gcd(E[0],E[1]),E[2]);assert g.monic()==hpoly((h+3)*(h-1)*(h-2),h).monic()
# No distinct finite parameter pair has the same dual image.
r,t=s.symbols('r t');Ar=[f.subs(h,r) for f in L];At=[f.subs(h,t) for f in L]
E=[]
for i,j in [(0,1),(0,2),(1,2)]:
 numerator=s.Poly(s.expand(Ar[i]*At[j]-Ar[j]*At[i]),r,t,modulus=p)
 diagonal=s.Poly(r-t,r,t,modulus=p)
 assert s.rem(numerator,diagonal).is_zero
 E.append(numerator.exquo(diagonal).as_expr())
gb=list(s.groebner(E,r,t,modulus=p,order='lex'))
assert gb==[r+3*t**4+3*t, t**6-2*t**3+1]
# The image of infinity, [2:-3:1], is not reached at a finite parameter.
g=s.gcd(hpoly(-3*L[0]-2*L[1],h),hpoly(L[0]-2*L[2],h))
assert g.degree()==0
# Original quartic has a single length-seven Jacobian singular scheme in chart z=1.
f=x**3*y+y**3+x
J=[s.diff(f,x),s.diff(f,y), y**3+3*x]
assert all(s.Poly(A-B,x,y,modulus=p).is_zero for A,B in zip(list(s.groebner(J,x,y,modulus=p)),[x-2*y**3,y**7-4]))
print('VERIFY_OK: characteristic-seven Klein quartic, polar parametrization, irreducible quintic equation, ramification and collision certificate')
