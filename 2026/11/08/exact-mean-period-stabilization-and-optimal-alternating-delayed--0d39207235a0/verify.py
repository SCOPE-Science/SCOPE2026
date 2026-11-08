#!/usr/bin/env python3
"""Reproduce symbolic identities and finite sanity checks for delayed sample-and-hold pairing.
The proof in RESULT.md, not the finite tests below, covers the continuum of parameters.
"""
import math
from fractions import Fraction
import sympy as sp

checks = 0

def eq(lhs, rhs):
    global checks
    assert sp.simplify(lhs-rhs) == 0, (lhs, rhs)
    checks += 1

def check(condition, description):
    global checks
    assert condition, description
    checks += 1

a,b,S,p,m=sp.symbols('a b S p m', real=True)
L=sp.Symbol('L')
M=lambda h: sp.Matrix([[1,-h],[1,0]])
F=M(b)*M(a)
check(F==sp.Matrix([[1-b,-a],[1,-a]]), 'two-step transition matrix')
eq(sp.trace(F),1-a-b)
eq(F.det(),a*b)
eq(F.charpoly(L).as_expr(),L**2-(1-a-b)*L+a*b)
eq(1-sp.trace(F)+F.det(),a+b+a*b)
eq(1+sp.trace(F)+F.det(),2-a-b+a*b)

root=sp.sqrt(4*m-1)
a_star=m+root/2
b_star=m-root/2
eq(a_star+b_star,2*m)
eq(a_star*b_star,(2*m-1)**2/4)
F_star=F.subs({a:a_star,b:b_star}, simultaneous=True)
eq(sp.trace(F_star),1-2*m)
eq(F_star.det(),(2*m-1)**2/4)
eq(F_star.charpoly(L).as_expr(),(L+(2*m-1)/2)**2)

m0=sp.Rational(5,4)
a0=sp.simplify(a_star.subs(m,m0))
b0=sp.simplify(b_star.subs(m,m0))
check((a0,b0)==(sp.Rational(9,4),sp.Rational(1,4)), 'optimal pair')
F0=F.subs({a:a0,b:b0})
eq(F0.charpoly(L).as_expr(),(L+sp.Rational(3,4))**2)
const=M(m0)
eq(const.charpoly(L).as_expr(),L**2-L+sp.Rational(5,4))
check(F0 != sp.eye(2)*(-sp.Rational(3,4)), 'defective optimal Floquet matrix')
check((F0+sp.eye(2)*sp.Rational(3,4))**2==sp.zeros(2), 'Jordan square')

# Compare direct eigenvalue moduli with analytic Jury region at rational grid points.
for ia in range(1,37):
    for ib in range(1,37):
        aa=Fraction(ia,16); bb=Fraction(ib,16)
        ss=aa+bb; pp=aa*bb
        tr=1-float(ss)
        discr=tr*tr-4*float(pp)
        if discr>=0:
            rho=max(abs((tr+math.sqrt(discr))/2),abs((tr-math.sqrt(discr))/2))
        else:
            rho=math.sqrt(float(pp))
        stable=(pp<1 and pp>ss-2)
        if abs(rho-1)>1e-10:
            check((rho<1)==stable, ('Jury classification',ia,ib,rho))

for num in range(20,30):
    mm=num/20 # 1.0..1.45
    astar=mm+math.sqrt(4*mm-1)/2
    bstar=mm-math.sqrt(4*mm-1)/2
    check(astar>0 and bstar>0, ('positive optimizer',mm))
    optimum=mm-0.5
    for j in range(1,150):
        aa=2*mm*j/150
        bb=2*mm-aa
        pp=aa*bb
        tr=1-2*mm
        disc=tr*tr-4*pp
        rho=math.sqrt(pp) if disc < 0 else max(abs((tr+math.sqrt(disc))/2),abs((tr-math.sqrt(disc))/2))
        check(rho>=optimum-1e-12, ('global rate lower bound',mm,aa))

print('PASS:',checks,'symbolic, rational, and finite numerical assertions.')
print('Sufficient proof is analytic: exact transition polynomial, degree-two Jury test, eigenvalue-trace bound, and discriminant equality.')
print('Example: mean=5/4; lengths=(9/4,1/4); alternating Floquet spectral factor=3/4; uniform two-step factor=5/4.')
