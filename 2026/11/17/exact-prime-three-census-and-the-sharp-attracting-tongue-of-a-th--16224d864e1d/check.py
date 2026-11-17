#!/usr/bin/env python3
"""Reproduce exact identities and selected numerical Floquet diagnostics.
Install the ordinary symbolic dependency listed in requirements.txt.
No claims about infinite parameters are inferred from finite sampling.
"""
import sympy as s

A,u,t,b,L,p,q,r,W=s.symbols('A u t b L p q r W')
f=lambda z: A-z*z
H=s.cancel((f(f(f(u)))-u)/(f(u)-u))
Splus=(1-t)/2
Sminus=(1+t)/2
Qplus=(Splus*Splus+Splus-3*A)/2
Qminus=(Sminus*Sminus+Sminus-3*A)/2
Uplus=(A-2+A*t)/2
Uminus=(A-2-A*t)/2
Cp=u**3-Splus*u**2+Qplus*u-Uplus
Cm=u**3-Sminus*u**2+Qminus*u-Uminus
subs={A:(t*t+7)/4}
assert s.simplify((Cp*Cm-H).subs(subs))==0
assert s.factor(s.discriminant(Cp.subs(subs),u))==(t*t+t+7)**2
assert s.factor(s.discriminant(Cm.subs(subs),u))==(t*t-t+7)**2
prod=u*f(u)*f(f(u))
expr=prod**2+(2-A)*prod-A**3+2*A**2-A+1
assert s.rem(s.Poly(expr,u),s.Poly(H,u)).as_expr()==0
J=lambda y:s.Matrix([[0,-2*y,b],[1,0,0],[0,1,0]])
M=J(p)*J(q)*J(r)
assert s.simplify(M.charpoly(L).as_expr()-((L-b)**3+8*p*q*r*L))==0
c=s.symbols('c')
a1=-3*b;a2=3*b*b+c;a3=-b**3
assert s.simplify(1+a1+a2+a3-((1-b)**3+c))==0
assert s.simplify(1-a1+a2-a3-((1+b)**3+c))==0
assert s.simplify(1-a2+a1*a3-a3*a3-((1-b*b)**3-c))==0
for bv in (s.Rational(0),s.Rational(1,10),s.Rational(1,2),s.Rational(9,10)):
    Am=s.nsolve((A-2+A*s.sqrt(4*A-7))/2-(1+bv)**3/8,1.85)
    Am = s.re(Am)
    for av in (s.Rational(7,4)+s.Rational(1,10000), (s.Rational(7,4)+Am)/2, Am+s.Rational(1,100)):
        Wplus=(av-2+av*s.sqrt(4*av-7))/2
        coeff=(1-bv)**3*8*Wplus
        roots=s.nroots((L-bv)**3+coeff*L, maxsteps=200)
        radius=max(abs(complex(rz)) for rz in roots)
        expect=7/4<float(av)<float(Am)
        assert (radius<1)==expect, (bv,av,roots,expect)
print('PASS: symbolic period-three factorization, discriminants, product elimination, Floquet matrix and Jury identities; 12 numerical regimes.')
