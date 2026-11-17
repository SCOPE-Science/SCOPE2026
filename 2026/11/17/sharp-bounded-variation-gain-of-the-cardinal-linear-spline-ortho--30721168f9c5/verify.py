#!/usr/bin/env python3
"""Exact symbolic and independent finite-Gram diagnostics for cardinal spline BV gain.

Requires Python 3 and SymPy >=1.10. Run: python verify.py.
The infinite-dimensional proof is given in RESULT.md, not by this program.
"""
from fractions import Fraction
import sympy as S

u = S.symbols('u', real=True)
s = S.sqrt(3)
q = s-2
A = (1-2*s*u+3*(s-1)*u**2)/2
B = S.expand(A.subs(u,1-u))
rho = (s-S.sqrt(6-3*s))/(3*(s-1))
assert S.simplify(q+1/q+4)==0
assert S.simplify(s*(1-q)/(1+q)-3)==0  # same as (1-q)/(1+q) = sqrt(3)
assert S.simplify((1-q)/(1+q)-s)==0
assert S.simplify(A.subs(u,rho))==0
assert 0 < float(rho) < 0.5
assert float(A.subs(u,S.Rational(1,2)))<0
assert float(A.subs(u,1))<0
assert S.simplify(1-A-B+(s*(A-B))-(s-3*(s-1)*u**2))==0
assert S.simplify(1-A-B-s*(A+B)-6*u*(1-u))==0
assert S.simplify((A+B)-((s-1)/2-3*(s-1)*u*(1-u)))==0
print('EXACT_GREEN_RECURRENCE_AND_PIECEWISE_STEP_PROFILE_PASS')

# Independent exact finite-interval Galerkin assembly and tridiagonal solve.
def finite_step_tv(m, t):
    # Mesh nodes -m,...,m, endpoints retain half a hat.
    n=2*m+1
    diag=[Fraction(2,3)]*n
    diag[0]=diag[-1]=Fraction(1,3)
    up=[Fraction(1,6)]*(n-1)
    rhs=[]
    for j in range(-m,m+1):
        if j<=-1: rhs.append(Fraction(0))
        elif j==0: rhs.append((1-t)**2/2)
        elif j==1: rhs.append(1-t*t/2)
        elif j==m: rhs.append(Fraction(1,2))
        else: rhs.append(Fraction(1))
    rhs[-1]=Fraction(1,2)
    # Thomas elimination, entirely rational.
    for k in range(1,n):
        factor=up[k-1]/diag[k-1]
        diag[k]-=factor*up[k-1]
        rhs[k]-=factor*rhs[k-1]
    coeff=[Fraction(0)]*n
    coeff[-1]=rhs[-1]/diag[-1]
    for k in range(n-2,-1,-1):
        coeff[k]=(rhs[k]-up[k]*coeff[k+1])/diag[k]
    return sum(abs(coeff[k+1]-coeff[k]) for k in range(n-1))

def formula(t):
    a=float(A.subs(u,S.Rational(t)))
    b=float(B.subs(u,S.Rational(t)))
    return 1-a-b+float(s)*(abs(a)+abs(b))

for t in (Fraction(0),Fraction(1,8),Fraction(1,4),
          Fraction(1,3),Fraction(1,2),Fraction(3,4),Fraction(1)):
    prev=1e3
    for m in (4,8,12):
        value=float(finite_step_tv(m,t))
        if m==12:
            assert abs(value-formula(t)) < 2e-9,(m,t,value,formula(t))
        assert value < 2
        prev=value
print('INDEPENDENT_RATIONAL_FINITE_GRAM_APPROXIMATIONS_PASS 21')

# Directly test the bounded-gradient identities of the claimed
# infinite-line step at each rational subcell position.
for t in (S.Rational(0), S.Rational(1,6),S.Rational(1,4),
          S.Rational(2,5),S.Rational(1,2),S.Rational(7,10),S.Rational(1)):
    av=S.simplify(A.subs(u,t));bv=S.simplify(B.subs(u,t))
    def c(j):
        if j<=0: return av*q**(-j)
        return 1-bv*q**(j-1)
    def rhs(j):
        if j<=-1:return S.Integer(0)
        if j==0:return (1-t)**2/2
        if j==1:return 1-t**2/2
        return S.Integer(1)
    for j in range(-8,9):
        lhs=(c(j-1)+4*c(j)+c(j+1))/6
        assert S.simplify(lhs-rhs(j))==0,(t,j,S.simplify(lhs-rhs(j)))
    Afloat=float(av);Bfloat=float(bv)
    exactgain=1-Afloat-Bfloat+float(s)*(abs(Afloat)+abs(Bfloat))
    assert exactgain<=float(s)+1e-12
    if t not in (0,1):assert exactgain<float(s)-1e-7
print('EXACT_STEP_MOMENT_EQUATIONS_AND_MAXIMUM_PASS 119')
print('ALL_CARDINAL_SPLINE_BV_CHECKS_PASS')
