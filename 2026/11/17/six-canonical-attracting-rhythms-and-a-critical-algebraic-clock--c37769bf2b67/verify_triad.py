#!/usr/bin/env python3
"""Exact symbolic cross-checks for a three-harmonic phase-coupled triad.

The checks are finite algebraic tests, not independent proof of the global
classification or of the infinite-time asymptotics.
"""
import sympy as s
r,z,g,u,v=s.symbols('r z g u v', real=True)
t=s.symbols('t')
x=s.symbols('x', real=True)
H=lambda x:s.sin(x)+r*s.sin(2*x)+z*s.sin(3*x)
Hp=lambda x:s.diff(H(x),x)
A=s.simplify(Hp(x).subs(x,0))
B=s.simplify(Hp(x).subs(x,s.pi))
C=s.simplify(Hp(x).subs(x,2*s.pi/3))
assert A==1+2*r+3*z and B==-1+2*r-3*z
assert C==s.Rational(-1,2)-r+3*z
assert s.simplify(C.subs(z,(1+2*r)/6))==0
assert s.simplify(B.subs(z,(2*r-1)/3))==0
assert s.simplify((2*r-1)/3-(1+2*r)/6)==(2*r-3)/6
J=lambda phases:s.Matrix(3,3,lambda i,j: g*Hp(x).subs(x,phases[j]-phases[i]) if i!=j else -g*sum(Hp(x).subs(x,phases[k]-phases[i]) for k in range(3) if k!=i))
for phases,expected in [([0,0,0],[-3*g*A,-3*g*A,0]),([0,2*s.pi/3,4*s.pi/3],[-3*g*C,-3*g*C,0]),([0,0,s.pi],[-g*(2*A+B),-3*g*B,0])]:
    M=s.simplify(J(phases))
    actual=s.factor(M.charpoly(t).as_expr())
    wanted=s.prod(t-q for q in expected)
    assert s.simplify(s.expand(actual-wanted))==0,(phases,actual,wanted)
assert s.simplify(s.diff(H(x),x,3).subs(x,s.pi).subs(z,(2*r-1)/3))==10*r-8
V=lambda arg:s.cos(arg)+r*s.cos(2*arg)/2+z*s.cos(3*arg)/3
W=lambda a,b,c:-V(a-b)-V(a-c)-V(b-c)
U=W(0,2*s.pi/3+t*u,4*s.pi/3+t*v)
assert s.simplify(s.diff(U,t,2).subs(t,0).subs(z,(1+2*r)/6))==0
cubic=s.factor(s.diff(U,t,3).subs(t,0).subs(z,(1+2*r)/6)/6)
assert s.simplify(cubic-s.sqrt(3)*u*v*(4*r-1)*(u-v)/4)==0
Wp=W(v/2,-v/2,s.pi+u).subs(z,(2*r-1)/3)
assert s.simplify(s.diff(Wp,v,2).subs({v:0,u:0})/2-2*r)==0
assert s.simplify(s.diff(Wp,u,4).subs({v:0,u:0})/24-(5*r-4)/6)==0
for rv,zv in [(s.Rational(2),s.Rational(9,10)),(s.Rational(5,2),s.Rational(5,4)),(s.Rational(2),s.Rational(1))]:
    av,bv,cv=[s.simplify(q.subs({r:rv,z:zv})) for q in [A,B,C]]
    rates=[3*av,3*cv,2*av+bv,3*bv]
    print('CASE',rv,zv,'A_B_C',av,bv,cv,'rates/g',rates)
    assert min(rates)>=0
print('VERIFY_OK characteristic_polynomials=3 critical_potential_derivatives=4 strict_examples=2 algebraic_boundary=1')
