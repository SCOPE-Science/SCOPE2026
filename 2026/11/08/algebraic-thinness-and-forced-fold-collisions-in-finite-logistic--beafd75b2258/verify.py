#!/usr/bin/env python3
"""Exact checks of finite logistic-IFS collision and elimination formulas.
Run: python verify.py  (requires sympy)
This checks finite instances; the all-N proof is in RESULT.md.
"""
from fractions import Fraction
import sympy as s
x,a,b=s.symbols('x a b')

def iterate(k,t):
    v=x
    for _ in range(k):
        v=s.expand(t*v*(1-v))
    return v

def q(k,l,t):
    v=s.Poly(iterate(l,t)-iterate(k,t), x)
    den=s.Poly(x*(1-x if k>=1 else 1),x)
    quot,rem=s.div(v,den)
    assert rem.is_zero
    return s.expand(quot.as_expr())

for k in range(1,4):
    assert s.degree(iterate(k,a),x)==2**k
    assert s.degree(iterate(k,a),a)==2**k-1
    for j in range(k):
        T=q(j,k,a)
        assert s.degree(T,x)<=2**k-1
        assert s.simplify(T.subs({a:2,x:0}))!=0
        assert s.simplify(T.subs({a:2,x:1}))!=0
        assert s.degree(q(j,k,b).subs(x,s.Rational(2,5)),b)==2**k-1
print('POLYNOMIAL_QUOTIENT_DEGREES_OK 6 pairs through n=3')

# Every resultant for N=2 is a genuine, non-identically-zero polynomial:
res=[]
for m,n in [(0,1),(0,2),(1,2)]:
    for p,r in [(0,1),(0,2),(1,2)]:
        R=s.resultant(q(m,n,a),q(p,r,b),x)
        assert R!=0
        res.append((m,n,p,r,R))
print('NONZERO_RESULTANTS_OK',len(res))

def F(t,z):return t*z*(1-z)
A=Fraction(3,2);B=Fraction(3,1)
S={Fraction(1,3),Fraction(2,3)}
assert {F(A,z) for z in S}=={Fraction(1,3)}
assert {F(B,z) for z in S}=={Fraction(2,3)}
assert any(u!=v and u+v==1 for u in S for v in S)
print('TWO_POINT_EXCEPTION_OK',A,B)

S2={Fraction(0),Fraction(1,2),Fraction(1)}
assert {F(Fraction(2),z) for z in S2}|{F(Fraction(4),z) for z in S2}==S2
assert not any(u!=v and u+v==1 and 0<u<1 and 0<v<1 for u in S2 for v in S2)
print('THREE_POINT_BOUNDARY_EXCEPTION_OK')

for N in range(1,6):
    BN=sum(n*(2**n-1) for n in range(1,N+1))
    assert BN==(N-1)*2**(N+1)+2-N*(N+1)//2
print('VERTICAL_SECTION_BOUNDS_OK',[(N,sum(n*(2**n-1) for n in range(1,N+1))**2) for N in range(1,6)])
print('VERIFY_OK')
