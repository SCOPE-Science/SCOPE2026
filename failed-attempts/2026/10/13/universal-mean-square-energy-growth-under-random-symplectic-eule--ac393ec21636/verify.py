#!/usr/bin/env python3
"""Exact rational and symbolic reconstruction of oscillator random-step identities."""
import sympy as S
from fractions import Fraction as F
from itertools import combinations
h, a, b, theta, z = S.symbols('h a b theta z', real=True)
m1, m2, m3, m4 = S.symbols('m1 m2 m3 m4', real=True)
A = S.Matrix([[1-h*h,h],[-h,1]])
G = S.Matrix([[1,-h/2],[-h/2,1]])
assert S.simplify(A.T*G*A-G) == S.zeros(2)
assert S.factor(A.det()-1) == 0
assert S.expand((2-h*h)**2-4 - h*h*(h*h-4)) == 0

def moments_to_T(m):
    u,v,w,r = m
    return S.Matrix([[1-2*v+r,2*(u-w),v],[-u+w,1-2*v,u],[v,-2*u,1]])
T = moments_to_T((m1,m2,m3,m4))
x,y = S.symbols('x y')
X = S.Matrix([[x*x,x*y],[x*y,y*y]])
image = S.expand(A*X*A.T)
from_expansion = S.Matrix([S.expand(image[0,0]),S.expand(image[0,1]),S.expand(image[1,1])])
monomials = (x*x,x*y,y*y)
W = S.Matrix([[S.expand(c).coeff(t) for t in monomials] for c in from_expansion])
for i in range(3):
    for j in range(3):
        poly = S.Poly(W[i,j],h)
        moments = (1,m1,m2,m3,m4)
        expected = sum(coef*moments[pow[0]] for pow,coef in poly.terms())
        assert S.expand(expected-T[i,j]) == 0
certificate = m1*m1*m4-2*m1*m2*m3+m2**3
assert S.factor((S.eye(3)-T).det()+2*certificate) == 0
ms = [theta*a**k+(1-theta)*b**k for k in range(1,5)]
assert S.factor(certificate.subs(dict(zip((m1,m2,m3,m4),ms))) - theta*(1-theta)*a*a*b*b*(a-b)**2)==0
assert S.factor((S.eye(3)-moments_to_T(ms)).det()+2*theta*(1-theta)*a*a*b*b*(a-b)**2)==0

# Rational law checks include exact covariance actions for four initial vectors.
values=[F(1,7),F(1,3),F(1,2),F(3,4),F(1),F(4,3),F(7,4)]
probs=[F(1,4),F(1,3),F(1,2),F(2,3),F(3,4)]
initials=[(F(1),F(0)),(F(0),F(1)),(F(2),F(-3)),(F(-2,3),F(5,4))]
count=0
for aa,bb in combinations(values,2):
    for pp in probs:
        mats=[S.Matrix([[1-S.Rational(aa.numerator,aa.denominator)**2,S.Rational(aa.numerator,aa.denominator)],[-S.Rational(aa.numerator,aa.denominator),1]]),S.Matrix([[1-S.Rational(bb.numerator,bb.denominator)**2,S.Rational(bb.numerator,bb.denominator)],[-S.Rational(bb.numerator,bb.denominator),1]])]
        p=S.Rational(pp.numerator,pp.denominator)
        mm=[p*S.Rational(aa.numerator,aa.denominator)**j+(1-p)*S.Rational(bb.numerator,bb.denominator)**j for j in range(1,5)]
        Tnum=moments_to_T(mm)
        assert (S.eye(3)-Tnum).det()==-2*p*(1-p)*(aa*bb*(aa-bb))**2
        for xx,yy in initials:
            x0=S.Matrix([S.Rational(xx.numerator,xx.denominator),S.Rational(yy.numerator,yy.denominator)])
            rhs=p*mats[0]*x0*(mats[0]*x0).T+(1-p)*mats[1]*x0*(mats[1]*x0).T
            v=S.Matrix([x0[0]**2,x0[0]*x0[1],x0[1]**2])
            expected=S.Matrix([rhs[0,0],rhs[0,1],rhs[1,1]])
            assert Tnum*v == expected
            count+=1
Tw=moments_to_T([(S.Rational(1,2)**j+S.Rational(1)**j)/2 for j in range(1,5)])
assert Tw==S.Matrix([[S.Rational(9,32),S.Rational(3,8),S.Rational(5,8)],[-S.Rational(3,16),-S.Rational(1,4),S.Rational(3,4)],[S.Rational(5,8),-S.Rational(3,2),1]])
assert (S.eye(3)-Tw).det() == -S.Rational(1,32)
poly = S.factor((z*S.eye(3)-Tw).det())
assert S.factor(poly-(64*z**3-66*z**2+49*z-49)/64) == 0
assert poly.subs(z,S.Rational(1017,1000)) < 0 and poly.subs(z,S.Rational(1019,1000)) > 0
print('VERIFY_OK',count,'exact-rational covariance identities')
