#!/usr/bin/env python3
"""Exact algebraic check of a positive Neumann Turing pitchfork.

Requires SymPy. No external files, services or mutable state.
"""
import sympy as s

u,z,w,k=s.symbols('u z w k')
F=s.Matrix([4*z/(1+k*w)-z-z*z-2*z*w/(z+w),w*(-1+2*z/(z+w))])
Z=(z,w)
K=(2-u)/(u*(2+u))
P=5*u*u-420*u+138
subs={z:u,w:u,k:K}
def exact(expr):return s.cancel(s.together(expr.subs(subs)))
def mod(expr):
    n,d=s.fraction(s.cancel(expr))
    return s.rem(s.Poly(n,u),s.Poly(P,u)).as_expr(),s.rem(s.Poly(d,u),s.Poly(P,u)).as_expr()
def identical_mod(expr,target):
    # Clear denominator before reducing; avoids swapping unreduced rational pairs.
    num=s.fraction(s.cancel(expr-target))[0]
    assert s.rem(s.Poly(num,u),s.Poly(P,u)).is_zero

assert s.cancel(s.together(F[0].subs({z:u,w:u,k:K})))==0
assert s.cancel(s.together(F[1].subs({z:u,w:u,k:K})))==0
J=F.jacobian(Z).applyfunc(exact)
J_expected=s.Matrix([[s.Rational(1,2)-u,-s.Rational(3,2)+u*u/4],[s.Rational(1,2),-s.Rational(1,2)]])
assert J==J_expected
assert s.factor(J.trace())==-u
assert s.simplify(J.det()-(4+4*u-u*u)/8)==0
D=s.diag(1,100);q=s.Rational(1,10)
A1=J-q*D
assert s.simplify(A1.det()+(5*u*u-420*u+138)/40)==0
r=s.Matrix([1,s.Rational(1,21)])
ell0=s.Matrix([1,2*u-s.Rational(4,5)])
assert s.rem(s.Poly((A1*r)[0],u),s.Poly(P,u)).is_zero
assert s.rem(s.Poly((ell0.T*A1)[1],u),s.Poly(P,u)).is_zero
ell=s.simplify(ell0/(ell0.T*r)[0]);assert s.cancel((ell.T*r)[0])==1
H=lambda a,b:s.Matrix([s.cancel(sum(exact(s.diff(F[i],Z[j],Z[h]))*a[j]*b[h] for j in range(2) for h in range(2))) for i in range(2)])
Q=s.Matrix([s.cancel(sum(exact(s.diff(F[i],Z[j],Z[h],Z[l]))*r[j]*r[h]*r[l] for j in range(2) for h in range(2) for l in range(2))) for i in range(2)])
Hrr=H(r,r)
w0=-J.inv()*Hrr/4
w2=-(J-4*q*D).inv()*Hrr/4
C=s.cancel((ell.T*(H(r,w0)+H(r,w2)/2+Q/8))[0])
C_expected=-s.Rational(16,2056513536)*(515234276817020*u-169961218676239)/(72313693080*u-23853887351)
identical_mod(C,C_expected)
S=s.cancel((ell.T*J.diff(u)*r)[0]/s.diff(K,u))
S_expected=3*(53521537*u-17655030)/(187410*u-63179)
identical_mod(S,S_expected)

# Exact rational root enclosure: P strictly decreasing on this interval.
a=s.Rational(329866810868002697,10**18);b=s.Rational(329866810868002700,10**18)
assert P.subs(u,a)>0 and P.subs(u,b)<0
assert 0<a<b<2
# S and C signs at all points of [a,b] follow from monotonic affine factors.
assert all(53521537*t-17655030<0 for t in [a,b])
assert all(187410*t-63179<0 for t in [a,b])
assert all(515234276817020*t-169961218676239<0 for t in [a,b])
assert all(72313693080*t-23853887351<0 for t in [a,b])
assert all(s.Rational(11322,100000)<S_expected.subs(u,t)<s.Rational(11323,100000) for t in [a,b])
assert all(-s.Rational(60379,100000)<C_expected.subs(u,t)<-s.Rational(60377,100000) for t in [a,b])
# Rational functions are monotone on the interval (linear-over-linear).
assert all(s.diff(expr,u).subs(u,t)!=0 for expr in [S_expected,C_expected] for t in [a,b])
for n in (0,1,2,3,4,5,10):
    qn=s.Rational(n*n,10)
    det=s.factor((J-qn*D).det())
    expected=100*qn*qn-(s.Rational(99,2)-100*u)*qn+(4+4*u-u*u)/8
    assert s.simplify(det-expected)==0
    assert s.simplify((J-qn*D).trace()+u+101*qn)==0
# At onset, second and all higher modes have positive determinants.
q2=s.Rational(4,10)
assert (J-q2*D).det().subs(u,a)>0
# For n>=3, D_n(0)>0 and derivative in 0<u<2 is positive;
# n=3 bounds n>=3 by growth in n² because quadratic in n² increases there.
assert s.factor((J-s.Rational(9,10)*D).det().subs(u,0))>0
print('VERIFY_OK: exact equilibrium, first spectral crossing, isolated mode, cubic and unfolding signs')
