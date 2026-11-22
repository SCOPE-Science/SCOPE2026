"""Finite-model checks for cone--parallel-plane Fourier multipliers.

Pure Python 3, standard library only.  Tests fields of prime order and GF(9).
The analytic proof for all odd prime powers is in RESULT.md.
"""
from __future__ import annotations
import cmath, math

class Field:
    def __init__(self, p, extension=1):
        assert (extension == 1 and p in (3, 5, 7)) or (p == 3 and extension == 2)
        self.p = p
        self.m = extension
        self.q = p ** extension
        self.zero, self.one = 0, 1
        self.E = range(self.q)
    def add(self, x, y):
        p = self.p
        return ((x % p + y % p) % p + (p * ((x // p + y // p) % p) if self.m == 2 else 0))
    def neg(self, x):
        return self.sub(0, x)
    def sub(self, x, y):
        p = self.p
        return ((x % p - y % p) % p + (p * ((x // p - y // p) % p) if self.m == 2 else 0))
    def mul(self, x, y):
        p = self.p
        if self.m == 1: return (x*y)%p
        a,b = x%p,x//p; c,d = y%p,y//p
        # i**2 = -1 over GF(3); X**2 + 1 irreducible.
        return ((a*c-b*d)%p)+p*((a*d+b*c)%p)
    def power(self,x,n):
        z=1
        while n:
            if n&1: z=self.mul(z,x)
            x=self.mul(x,x);n>>=1
        return z
    def div(self,x,y):
        assert y!=0
        return self.mul(x,self.power(y,self.q-2))
    def trace(self,x):
        if self.m==1: return x%self.p
        return self.add(x,self.power(x,self.p))%self.p
    def psi(self,x):
        return cmath.exp(-2j*math.pi*self.trace(x)/self.p)
    def chi(self,x):
        if x==0:return 0
        return 1 if self.power(x,(self.q-1)//2)==1 else -1
    def addmany(self,*xs):
        v=0
        for x in xs:v=self.add(v,x)
        return v


def check(p,m):
    F=Field(p,m);q=F.q
    V=[(x,y,z) for x in F.E for y in F.E for z in F.E]
    cone={(x,y,z) for x,y,z in V if F.sub(F.mul(x,y),F.mul(z,z))==0}
    gauss=sum(F.chi(t)*F.psi(t) for t in F.E)
    assert abs(abs(gauss)-math.sqrt(q))<1e-8
    count=0
    for c in (0,1,2):
        H={(x,c,z) for x in F.E for z in F.E}
        S=cone | H
        assert len(S)==2*q*q-q
        zeros=0
        small=float('inf')
        for u,v,w in V:
            xi0=u==v==w==0
            inner=F.sub(F.mul(u,v),F.div(F.mul(w,w),F.addmany(1,1,1,1)))
            FC=(q*q if xi0 else 0)+q*F.chi(F.neg(inner))
            FH=q*q*F.psi(F.mul(v,c)) if u==w==0 else 0
            if c==0:FI=q if u==0 else 0
            elif u==0:
                FI=q*F.psi(F.mul(v,c)) if w==0 else 0
            else:
                quad=F.div(F.mul(c,F.mul(w,w)),F.mul(F.addmany(1,1,1,1),u))
                ph=F.sub(F.mul(v,c),quad)
                FI=F.chi(F.div(u,c))*gauss*F.psi(ph)
            predicted=FC+FH-FI
            actual=sum(F.psi(F.addmany(F.mul(u,x),F.mul(v,y),F.mul(w,z))) for x,y,z in S)
            assert abs(actual-predicted)<1e-6,(q,c,u,v,w,actual,predicted)
            if abs(actual)<1e-6:zeros+=1
            else:small=min(small,abs(actual))
            count+=1
        assert zeros==(2*q*(q-1) if c==0 else 0),(q,c,zeros)
        assert abs(small-(q if c==0 else math.sqrt(q)))<1e-6,(q,c,small)
        print('GF(%d), plane y=%d: %d multipliers checked; zeros=%d; min positive modulus=%.12g'%(q,c,q**3,zeros,small))
    return count

if __name__=='__main__':
    n=sum(check(p,m) for p,m in [(3,1),(5,1),(7,1),(3,2)])
    print('PASS: %d exact-field indexed Fourier identity comparisons.'%n)
