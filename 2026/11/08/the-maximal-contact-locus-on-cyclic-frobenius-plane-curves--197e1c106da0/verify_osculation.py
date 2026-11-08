#!/usr/bin/env python3
"""Exact finite-field check of osculating points on cyclic Frobenius curves.

No symbolic-algebra packages. GF(2^6), GF(3^6), GF(2^12), GF(5^6) are built
from explicitly checked irreducible defining polynomials.
"""

from itertools import product

def is_irreducible(p, coefficients):
    """Exhaustively exclude all monic polynomial factors of degree <= n/2."""
    n = len(coefficients)-1
    for degree in range(1,n//2+1):
        for low in product(range(p),repeat=degree):
            divisor=list(low)+[1]
            rem=list(coefficients)
            for j in range(n-degree,-1,-1):
                top=rem[degree+j]
                if top:
                    for i in range(degree+1):
                        rem[i+j]=(rem[i+j]-top*divisor[i])%p
            if not any(rem[:degree]):
                return False
    return True

class FField:
    def __init__(self,p,n,coeff):
        assert len(coeff)==n+1 and coeff[-1]==1
        assert is_irreducible(p,coeff)
        self.p,self.n,self.coeff=p,n,coeff
        self.size=p**n
    def unpack(self,x):
        a=[]
        for _ in range(self.n):a.append(x%self.p);x//=self.p
        return a
    def pack(self,a):
        z=0
        for t in reversed(a):z=z*self.p+(t%self.p)
        return z
    def add(self,*xs):
        if self.p==2:
            z=0
            for x in xs:z ^= x
            return z
        a=[0]*self.n
        for x in xs:
            b=self.unpack(x)
            for i in range(self.n):a[i]=(a[i]+b[i])%self.p
        return self.pack(a)
    def mul(self,x,y):
        if self.p==2:
            result=0
            poly=sum(bit<<i for i,bit in enumerate(self.coeff))
            while y:
                if y&1: result^=x
                y>>=1
                x<<=1
                if x & (1<<self.n):x^=poly
            return result
        a=self.unpack(x);b=self.unpack(y)
        c=[0]*(2*self.n-1)
        for i in range(self.n):
            for j in range(self.n):c[i+j]=(c[i+j]+a[i]*b[j])%self.p
        for k in range(2*self.n-2,self.n-1,-1):
            m=c[k]
            for j in range(self.n):c[k-self.n+j]=(c[k-self.n+j]-m*self.coeff[j])%self.p
        return self.pack(c[:self.n])
    def pow(self,x,n):
        assert n>=0
        a=1
        while n:
            if n&1:a=self.mul(a,x)
            x=self.mul(x,x); n>>=1
        return a
    def inv(self,x):
        assert x
        return self.pow(x,self.size-2)
    def curve(self,P,q):
        x,y,z=P
        return self.add(self.mul(self.pow(x,q),y),self.mul(self.pow(y,q),z),self.mul(self.pow(z,q),x))
    def fixed_point_count(self,q):
        assert self.size==q**6
        good=0
        classes=set()
        for a in range(1,self.size):
            b=self.pow(a,q**3+1)
            trace=self.add(b,self.pow(b,q),self.pow(b,q**2))
            if trace!=0:continue
            good+=1
            P=(a,self.pow(a,q**4),self.pow(a,q**2))
            assert self.curve(P,q)==0
            # Directly check tangent intersection with the residual point.
            R=(self.pow(P[1],q**2),self.pow(P[2],q**2),self.pow(P[0],q**2))
            assert self.mul(P[0],self.inv(R[0]))==self.mul(P[1],self.inv(R[1]))==self.mul(P[2],self.inv(R[2]))
            z=self.inv(a)
            classes.add((1,self.mul(P[1],z),self.mul(P[2],z)))
        assert good == (q*q-1)*(q**3+1),(q,good)
        assert len(classes)==q**3+1,(q,len(classes))
        orbit_profile={1:0,2:0,3:0,6:0}
        for P in classes:
            degree=next(d for d in (1,2,3,6) if tuple(self.pow(t,q**d) for t in P)==P)
            orbit_profile[degree]+=1
        h=1 if q%3==0 else (2 if q%3==1 else 0)
        expected={1:h,2:0,3:q+1-h,6:q**3-q}
        assert orbit_profile==expected,(q,orbit_profile,expected)
        print(f'q={q}: representatives={good}, projective maximal-osculation points={len(classes)}, degree-profile={orbit_profile}')

# Polynomial irreducibility checked by exhaustive monic factor division.
# GF64: T^6+T+1; GF729: T^6+T+2; GF4096: T^12+T^3+1.
# GF15625: T^6+T^2+T+1.
FField(2,6,[1,1,0,0,0,0,1]).fixed_point_count(2)
FField(3,6,[2,1,0,0,0,0,1]).fixed_point_count(3)
FField(2,12,[1,0,0,1,0,0,0,0,0,0,0,0,1]).fixed_point_count(4)
FField(5,6,[1,1,1,0,0,0,1]).fixed_point_count(5)
print('OSCULATING_VERIFY_OK')
