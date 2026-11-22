#!/usr/bin/env python3
"""Exact discriminants and extension-field point counts for two K3 double covers."""
import itertools
import sympy as sp

T,X=sp.symbols('T X')
C=[[6,0,3,0,3],[2,6,6,4,0],[1,2,1,6,6],[5,1,1,3,0],[6,0,3,0,3]]
BT=sum(C[i][j]*T**i*X**j for i in range(5) for j in range(5))
Q1=X**2+1
Q2=2*X**2-X-2
R1=3*(T-3)*(T-5)*(T-6)
R2=6*T*(T-1)*(T-2)*(T-4)
AEKS=R1*Q1**2+R2*Q2**2
P=T**4+T**3+T**2-T+1
Q=T**4+2*T**3+T**2-2*T+1
U=T**2+2
V=T**2+3*T-2

def poly(y):return sp.Poly(y,T,modulus=7)
for f,expected in [(BT,(T**7-T)**2*P*Q),(AEKS,2*(T**7-T)**2*U**2*V**2)]:
    assert poly(sp.discriminant(f,X)-expected).is_zero
for quartic in (P,Q):
    p=poly(quartic)
    assert sp.gcd(p,poly(T**7-T)).degree()==0
    assert sp.gcd(p,poly(T**49-T)).degree()==0
for quad in (U,V):
    assert sp.factor_list(sp.Poly(quad,T,modulus=7),modulus=7)[1][0][0].degree()==2
# Verify all eight rational fibers in both examples have nonsquare times
# the square of a separable irreducible quadratic.
for f in (BT,AEKS):
    for a in range(7):
        factors=sp.factor_list(sp.Poly(f.subs(T,a),X,modulus=7),modulus=7)
        scalar=factors[0]%7
        assert scalar in (3,5,6)
        assert len(factors[1])==1 and factors[1][0][1]==2
        assert factors[1][0][0].degree()==2
    infinity=sp.Poly(sum(C[4][j]*X**j for j in range(5)) if f==BT else 6*Q2**2,X,modulus=7)
    factors=sp.factor_list(infinity,modulus=7)
    assert factors[0]%7 in (3,5,6)
    assert len(factors[1])==1 and factors[1][0][1]==2 and factors[1][0][0].degree()==2
# The quadratic-orbit fibers in AEKS are squares of a separable quadratic.
for factor,scalar in ((U,1-2*T),(V,2-3*T)):
    q0=X**2+X-1
    for j in range(5):
        residual=sp.Poly((AEKS-scalar*q0**2).expand().coeff(X,j),T,modulus=7)
        assert residual.rem(poly(factor)).is_zero
    c_norm=int(sp.resultant(factor,scalar,T))%7
    assert c_norm in (1,2,4)

class GF49:
    """Elements represented by a+b*alpha with alpha**2=d nonsquare modulo 7."""
    d=3
    def __init__(self,a=0,b=0):self.a=a%7;self.b=b%7
    def __add__(self,other):
        if not isinstance(other,GF49):other=GF49(other)
        return GF49(self.a+other.a,self.b+other.b)
    __radd__=__add__
    def __neg__(self):return GF49(-self.a,-self.b)
    def __sub__(self,other):return self+(-other if isinstance(other,GF49) else -GF49(other))
    def __mul__(self,other):
        if not isinstance(other,GF49):other=GF49(other)
        return GF49(self.a*other.a+self.d*self.b*other.b,self.a*other.b+self.b*other.a)
    __rmul__=__mul__
    def __pow__(self,n):
        ans=GF49(1);base=self
        while n:
            if n&1:ans=ans*base
            base=base*base;n//=2
        return ans
    def __eq__(self,other):
        if not isinstance(other,GF49):other=GF49(other)
        return (self.a,self.b)==(other.a,other.b)

def bt(t,x):
    t0,t1=(GF49(0),GF49(1)) if t is None else (GF49(1),t)
    x0,x1=(GF49(0),GF49(1)) if x is None else (GF49(1),x)
    tpow=[t0**(4-i)*t1**i for i in range(5)]
    xpow=[x0**(4-j)*x1**j for j in range(5)]
    return sum((C[i][j]*tpow[i]*xpow[j] for i in range(5) for j in range(5)),GF49(0))

def aeks(t,x):
    z,w=(GF49(1),GF49(0)) if t is None else (t,GF49(1))
    xx,y=(GF49(1),GF49(0)) if x is None else (x,GF49(1))
    q1=xx**2+y**2;q2=2*xx**2-xx*y-2*y**2
    r1=3*w*(z-3*w)*(z-5*w)*(z-6*w)
    r2=6*z*(z-w)*(z-2*w)*(z-4*w)
    return r1*q1**2+r2*q2**2

def count(fun,elems,q):
    result=0
    for t in elems+[None]:
        for x in elems+[None]:
            a=fun(t,x)
            if a==0:result+=1
            elif a**((q-1)//2)==1:result+=2
    return result

for d in (3,5):
    GF49.d=d
    F7=[GF49(i) for i in range(7)]
    F49=[GF49(i,j) for i,j in itertools.product(range(7),repeat=2)]
    assert (count(bt,F7,7),count(aeks,F7,7))==(0,0)
    assert (count(bt,F49,49),count(aeks,F49,49))==(3040,3320)
print('ALL CHECKS PASSED: BT=(0,3040), AEKS=(0,3320)')
