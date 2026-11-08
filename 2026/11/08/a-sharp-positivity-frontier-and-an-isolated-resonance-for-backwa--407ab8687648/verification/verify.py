#!/usr/bin/env python3
"""Exact rational identities and Bernstein certificate for a scalar multistep positivity theorem.
No third-party dependencies. Does not replace the analytic spectral argument."""
from fractions import Fraction as F
from math import comb

# Polynomials in the real variable s, stored in ascending coefficient order.
def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:p.pop()
    return tuple(p)
def poly(p):
    if isinstance(p,(int,F)):return (F(p),)
    return trim(tuple(F(x) for x in p))
def add(p,q):
    p,q=poly(p),poly(q)
    return trim(tuple((p[i] if i<len(p) else F(0))+(q[i] if i<len(q) else F(0)) for i in range(max(len(p),len(q)))))
def neg(p):return tuple(-v for v in poly(p))
def sub(p,q):return add(p,neg(q))
def mul(p,q):
    p,q=poly(p),poly(q);r=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return trim(r)
def power(p,n):
    r=poly(1)
    for _ in range(n):r=mul(r,p)
    return r
class Rat:
    def __init__(self,n,d=1):
        if isinstance(n,Rat):self.n,self.d=n.n,n.d;return
        self.n,self.d=poly(n),poly(d)
        if self.d==(F(0),):raise ZeroDivisionError
    @staticmethod
    def get(x):return x if isinstance(x,Rat) else Rat(x)
    def __add__(self,o):
        o=Rat.get(o);return Rat(add(mul(self.n,o.d),mul(o.n,self.d)),mul(self.d,o.d))
    __radd__=__add__
    def __neg__(self):return Rat(neg(self.n),self.d)
    def __sub__(self,o):return self+-Rat.get(o)
    def __rsub__(self,o):return Rat.get(o)+-self
    def __mul__(self,o):
        o=Rat.get(o);return Rat(mul(self.n,o.n),mul(self.d,o.d))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=Rat.get(o);return Rat(mul(self.n,o.d),mul(self.d,o.n))
    def __rtruediv__(self,o):return Rat.get(o)/self
    def __pow__(self,n):return Rat(power(self.n,n),power(self.d,n))
    def equals(self,o):
        o=Rat.get(o);return sub(mul(self.n,o.d),mul(o.n,self.d))==(F(0),)

def verify():
    s=Rat((0,1));one=Rat(1)
    Q=15*s*s-6*s+1
    D=5*s*s-4*s+1
    T=8*s*s-4*s+1
    N=10*s*s-5*s+1
    H=Q-4*s*s*s
    u=s*(6*s-1)/(2*Q)
    rho2=s*s/Q
    v2=rho2-u*u
    assert v2.equals(3*s*s*T/(4*Q*Q))
    t=6*s*s*s/H
    A=(t*t-2*u*t+rho2)/(s*s-2*s*u+rho2)
    Aclosed=(7*s*s-2*s+1)*N*N/(3*D*H*H)
    assert A.equals(Aclosed)
    cv=((1-A)*u-(t-A*s))/2
    E=A*A-(1-A)**2-4*cv*cv/v2
    # P12(s) is printed in the proof.
    P=Rat((1,-32,444,-3668,20235,-78528,219004,-439920,627756,-616752,393500,-146400,24000))
    Eclosed= -(7*s*s-2*s+1)*N*N*P/(3*D*D*T*H**4)
    assert E.equals(Eclosed)
    # Bernstein certificate W(s) = -P12(s) on [2/5,1].
    coefficients=list(neg(P.n))
    lo,span=F(2,5),F(3,5)
    powers=[]
    for k,a in enumerate(coefficients):
        for j in range(k+1):
            if j>=len(powers):powers.append(F(0))
            powers[j]+=a*comb(k,j)*lo**(k-j)*span**j
    degree=12
    bern=[sum(powers[j]*F(comb(i,j),comb(degree,j)) for j in range(i+1)) for i in range(degree+1)]
    assert len(bern)==13 and all(b>0 for b in bern)
    assert min(bern)==F(7443,78125), (min(bern),bern)
    # If the method is started by two backward-Euler steps, the isolated resonance r=3 is exact.
    r=F(3);d=1+F(3,5)*r;ys=[F(1),F(1,4),F(1,16)]
    for k in range(3,101):
        yn=(F(3,2)*ys[-1]-F(3,5)*ys[-2]+F(1,10)*ys[-3])/d
        assert yn==F(1,4)**k
        ys.append(yn)
    # Reproduce two concrete sign-loss witnesses without floating-point error.
    examples=[]
    for r,expected in [(F(1),30),(F(2),10),(F(4),7)]:
        d=1+F(3,5)*r;t=1/(1+r)
        ys=[F(1),t,t*t]
        first_negative=None
        for k in range(3,expected+1):
            yn=(F(3,2)*ys[-1]-F(3,5)*ys[-2]+F(1,10)*ys[-3])/d
            ys.append(yn)
            if yn<0 and first_negative is None:first_negative=k
        assert first_negative==expected
        examples.append((str(r),expected))
    print('VERIFY_OK: exact rational projection-residue identity, 13 positive degree-12 Bernstein coefficients,')
    print('          resonance to n=100, and exact first-negative witnesses',examples)
    print('Bernstein coefficients:',[str(x) for x in bern])

if __name__=='__main__':verify()
