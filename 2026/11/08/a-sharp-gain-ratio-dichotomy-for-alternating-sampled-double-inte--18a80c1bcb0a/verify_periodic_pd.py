"""Exact symbolic and rational checks for the two-period held-feedback stability theorem.

Run with Python 3 and SymPy. These checks supplement, but do not replace,
the all-parameter proof in RESULT.md.
"""
import sympy as s
from fractions import Fraction
from itertools import product

r,a,b=s.symbols('r a b', positive=True)

def F(t):
    return s.Matrix([[1-r*t*t/2, t-t*t/2],[-r*t, 1-t]])

def identical(x,y):
    assert s.factor(x-y)==0, (x,y)

A=F(a);B=F(b);M=B*A
identical(A.det(),1-a+r*a*a/2)
identical(s.trace(A),2-a-r*a*a/2)
identical(1-A.det(),a-r*a*a/2)
identical(1-s.trace(A)+A.det(),r*a*a)
identical(1+s.trace(A)+A.det(),4-2*a)
D=s.factor(M.det());T=s.factor(s.trace(M))
identical(D,(1-a+r*a*a/2)*(1-b+r*b*b/2))
identical(1-T+D,r*(a+b)*(a+b-a*b))
S=8-4*(a+b)+4*a*b*(1-r)+r*r*a*a*b*b
identical(2*(1+T+D),S)
identical(S.subs(a,2),4*b*(1-2*r)+4*r*r*b*b)
identical(S.subs(a,2/r),4*(b*b+(2/r-3)*b+2-2/r))
identical(S.subs({a:s.Rational(3,4),b:s.Rational(7,4),r:1}),-s.Rational(71,256))
identical((1+T+D).subs({a:s.Rational(3,4),b:s.Rational(7,4),r:1}),-s.Rational(71,512))
identical(S.subs({a:2,b:(2*r-1)/(2*r*r)}),-(2*r-1)**2/r**2)
identical(S.subs({a:2/r,b:s.Rational(3,2)-1/r}),-(r-2)**2/r**2)
identical(S.subs({a:2/r,b:2/r}),8*(1-2/r)**2)
# The relevant boundary minimizers are genuine points of their open edges:
# (2r-1)/(2r^2) lies in (0,2) for 1/2 < r <= 1;
# (3/2 -1/r) lies in (0,2/r) for 1 < r < 2.
identical(s.Rational(3,2)-1/r-2/r,3*(r-2)/(2*r))

# Independent exact rational implementation of the Jury test.
def mm(X,Y):
    return ((X[0][0]*Y[0][0]+X[0][1]*Y[1][0],X[0][0]*Y[0][1]+X[0][1]*Y[1][1]),
            (X[1][0]*Y[0][0]+X[1][1]*Y[1][0],X[1][0]*Y[0][1]+X[1][1]*Y[1][1]))
def frmat(h,r):
    return ((1-r*h*h/2,h-h*h/2),(-r*h,1-h))
def det(X):return X[0][0]*X[1][1]-X[0][1]*X[1][0]
def tr(X):return X[0][0]+X[1][1]
def jury(X):
    T=tr(X);D=det(X)
    return (1-D>0) and (1-T+D>0) and (1+T+D>0)

checks=0
ratios=[Fraction(i,8) for i in range(1,37)]
for rr in ratios:
    L=min(Fraction(2),Fraction(2)/rr)
    steps=[L*Fraction(i,17) for i in range(1,17)]
    for aa,bb in product(steps,repeat=2):
        Fa=frmat(aa,rr);Fb=frmat(bb,rr)
        assert jury(Fa) and jury(Fb)
        J=jury(mm(Fb,Fa))
        Sval=8-4*(aa+bb)+4*aa*bb*(1-rr)+rr*rr*aa*aa*bb*bb
        assert J==(Sval>0)
        if rr<=Fraction(1,2) or rr>=2:
            assert J
        checks+=1
# Explicit destabilizing rational witnesses for every rational ratio in the open window.
for rr in ratios:
    if not (Fraction(1,2)<rr<2):continue
    L=min(Fraction(2),Fraction(2)/rr)
    bb=(2*rr-1)/(2*rr*rr) if rr<=1 else Fraction(3,2)-1/rr
    assert 0<bb<L
    Sboundary=8-4*(L+bb)+4*L*bb*(1-rr)+rr*rr*L*L*bb*bb
    assert Sboundary<0
    eps=L/Fraction(10**8)
    aa=L-eps
    assert not jury(mm(frmat(bb,rr),frmat(aa,rr)))
    checks+=1

print('PASS: derived one-step and two-step identities; exact phase boundary; rational Schur tests:',checks)
