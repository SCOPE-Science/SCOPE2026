#!/usr/bin/env python3
"""Exact checks for the peak-valley covariance classification in Mallows permutations.
Runs with Python 3 standard library; does not require source downloads."""
from fractions import Fraction
from itertools import permutations

class Poly:
    def __init__(self, coeffs):
        if isinstance(coeffs, int): coeffs=[coeffs]
        coeffs=list(coeffs)
        while len(coeffs)>1 and coeffs[-1]==0: coeffs.pop()
        self.c=tuple(coeffs)
    def __add__(self, other):
        other=pol(other); return Poly([(self.c[i] if i<len(self.c) else 0)+(other.c[i] if i<len(other.c) else 0) for i in range(max(len(self.c),len(other.c)))])
    __radd__=__add__
    def __neg__(self):return Poly([-v for v in self.c])
    def __sub__(self,other):return self+(-pol(other))
    def __rsub__(self,other):return pol(other)+(-self)
    def __mul__(self,other):
        other=pol(other); c=[0]*(len(self.c)+len(other.c)-1)
        for i,a in enumerate(self.c):
            for j,b in enumerate(other.c):c[i+j]+=a*b
        return Poly(c)
    __rmul__=__mul__
    def __pow__(self,n):
        out=Poly(1)
        for _ in range(n):out=out*self
        return out
    def __eq__(self,other):return self.c==pol(other).c
    def at(self,q):return sum(v*q**i for i,v in enumerate(self.c))

def pol(x):return x if isinstance(x,Poly) else Poly(x)
Q=Poly([0,1]); ONE=Poly(1)
class Rat:
    def __init__(self,num,den=1):self.num=pol(num);self.den=pol(den)
    def __add__(self,other):
        other=rat(other);return Rat(self.num*other.den+self.den*other.num,self.den*other.den)
    __radd__=__add__
    def __neg__(self):return Rat(-self.num,self.den)
    def __sub__(self,other):return self+-rat(other)
    def __rsub__(self,other):return rat(other)+-self
    def __mul__(self,other):
        other=rat(other);return Rat(self.num*other.num,self.den*other.den)
    __rmul__=__mul__
    def __truediv__(self,other):
        other=rat(other);return Rat(self.num*other.den,self.den*other.num)
    def __eq__(self,other):
        other=rat(other);return self.num*other.den==other.num*self.den
    def at(self,q):return Fraction(self.num.at(q),self.den.at(q))
def rat(x):return x if isinstance(x,Rat) else Rat(x)
def qfact(n):
    out=ONE
    for j in range(1,n+1):out=out*Poly([1]*j)
    return out

def inv(t):return sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))
def peak(t,i):return t[i]<t[i+1]>t[i+2]
def valley(t,i):return t[i]>t[i+1]<t[i+2]
def weighted_poly(m,pred):
    vals=[0]*(m*(m-1)//2+1)
    for x in permutations(range(m)):
        if pred(x):vals[inv(x)]+=1
    return Poly(vals)
def probability(m,pred):return Rat(weighted_poly(m,pred),qfact(m))

p=probability(3,lambda x:peak(x,0)); v=probability(3,lambda x:valley(x,0))
pv1=probability(4,lambda x:peak(x,0) and valley(x,1))
vp1=probability(4,lambda x:valley(x,0) and peak(x,1))
pv2=probability(5,lambda x:peak(x,0) and valley(x,2))
vp2=probability(5,lambda x:valley(x,0) and peak(x,2))
a=-p*v
b=pv1+vp1-2*p*v
c=pv2+vp2-2*p*v
S3=1+Q+Q**2; S5=sum((Q**j for j in range(5)),Poly(0))
H=(1+Q)**2*S3**2*S5
F5=Poly([2,2,-3,-1,3,-1,-3,2,2])
Lpoly=Poly([1,-1,0,2,0,-1,1])
# Symbolic equalities in Z[q], including all n >= 5 by affine dependence.
assert p==Rat(Q,S3)
assert v==p
assert 2*a+b==Rat(Q*(Q**2-Q-1)*(Q**2+Q-1),(1+Q)**2*S3**2)
assert 3*a+2*b+c==Rat(Q*F5,H)
assert a+b+c==Rat(Q*Lpoly,S3**2*S5)
assert a==Rat(-Q**2,S3**2)
print('Six exact universal polynomial identities: PASS')
# Independent full-permutation enumeration checks, not reusing local-window formulas.
checks=0
for n in range(3,9):
    qs=[Fraction(1,3),Fraction(2,3),Fraction(1),Fraction(2),Fraction(3)] if n<=7 else [Fraction(2)]
    for q in qs:
        denominator=Fraction(0);p_tot=v_tot=pv_tot=Fraction(0)
        for x in permutations(range(n)):
            weight=q**inv(x)
            pp=sum(peak(x,j) for j in range(n-2))
            vv=sum(valley(x,j) for j in range(n-2))
            denominator+=weight;p_tot+=weight*pp;v_tot+=weight*vv;pv_tot+=weight*pp*vv
        cov=pv_tot/denominator-(p_tot/denominator)*(v_tot/denominator)
        calc=(n-2)*a+(n-3)*b+max(n-4,0)*c
        assert cov==calc.at(q),(n,q,cov,calc.at(q))
        if n>=5:
            formula=Rat(Q*(F5+(n-5)*(1+Q)**2*Lpoly),H)
            assert cov==formula.at(q)
        # Exact relation P-V = last descent minus first descent.
        if n>=4:assert cov+Fraction(q,(1+q)**2)==(sum((q**inv(x))*(sum(peak(x,j) for j in range(n-2)))**2 for x in permutations(range(n)))/denominator-(p_tot/denominator)**2)
        checks+=1
print('Independent full-permutation exact covariance cases:',checks,'PASS')
# Positivity certificates in t=q+1/q, u=t-2>=0:
# q^-4 F5 = 2u^4+18u^3+49u^2+37u+3.
# q^-3 Lpoly = u^3+5u^2+5u+2.
def certpoly(coeffs,degree):
    return sum((coeffs[i]*Q**(degree-i)*(Q-1)**(2*i) for i in range(len(coeffs))),Poly(0))
assert F5==certpoly([3,37,49,18,2],4)
assert Lpoly==certpoly([2,5,5,1],3)
print('All deterministic checks passed')
