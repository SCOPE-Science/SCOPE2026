#!/usr/bin/env python3
"""Exact algebra checks for three equal-scale logistic density components."""
import sympy as s

u,c,z,a=s.symbols('u c z a', positive=True)
J=1/(u+2)+(c*u+4)/(u+c)**2
H=(c**2-8-c*u)*(u+2)**2-(u+c)**3
nchecks=0

def same(lhs,rhs):
    global nchecks
    assert s.cancel(lhs-rhs)==0, (lhs,rhs)
    nchecks+=1

def truth(condition):
    global nchecks
    assert condition
    nchecks+=1

# Independent exponential representation of the translated logistic components.
G=z/(1+z)**2+z*a/(z+a)**2+z*a/(1+z*a)**2
same(G,J.subs({u:z+1/z,c:a+1/a}))
same(s.diff(J,u),H/((u+2)**2*(u+c)**3))
same(s.discriminant(H,u),4*(c-2)**6*(c+1)*(c**2-16*c-44))
same(H.subs(u,2),-(c+2)*((c-6)**2+32))
same(H.subs(u,-c),2*(c-2)**3*(c+2))
same(H.subs(u,0),-c**3+4*c**2-32)
cc=8+6*s.sqrt(3)
up=4+2*s.sqrt(3)
same(s.expand(H.subs(c,cc)),s.expand(-(9+6*s.sqrt(3))*(u-up)**2*(u+8-2*s.sqrt(3))))
same(s.diff(H,c).subs({c:cc,u:up}),288+192*s.sqrt(3))
same((s.Rational(8,3))**3-4*(s.Rational(8,3))**2+32,s.Rational(608,27))
for cv in [s.Rational(3),s.Rational(6),s.Rational(9),s.Rational(12),s.Rational(18)]:
    p=s.Poly(H.subs(c,cv),u)
    truth(p.count_roots(-s.oo,0)==1)
    truth(p.count_roots(2,s.oo)==0)
for cv in [s.Rational(19),s.Rational(20),s.Rational(50),s.Rational(100)]:
    p=s.Poly(H.subs(c,cv),u)
    truth(p.count_roots(-s.oo,0)==1)
    truth(p.count_roots(2,s.oo)==2)
truth(abs(float(s.acosh(cc/2))-2.908963008819675)<1e-13)
truth(float(2*s.log(2+s.sqrt(3)))<float(s.acosh(cc/2)))
print('PASS:',nchecks,'algebraic and root-count checks')
