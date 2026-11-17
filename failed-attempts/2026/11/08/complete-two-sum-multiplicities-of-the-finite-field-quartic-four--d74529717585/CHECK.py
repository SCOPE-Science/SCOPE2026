#!/usr/bin/env python3
"""Exact small-field checks for quartic sum-fiber theorem.
Uses only Python standard library. No external data or claims of infinite certification.
"""
from collections import Counter


def primes_upto(n):
    return [m for m in range(5, n+1) if all(m%d for d in range(2,int(m**.5)+1))]


class Field:
    def __init__(self,p,modpoly=None):
        self.p=p
        self.poly=modpoly or [0,1]
        self.n=len(self.poly)-1
        assert self.poly[-1]==1
        self.q=p**self.n
        self.digits=[self.decode(i) for i in range(self.q)]
        self.enc={x:i for i,x in enumerate(self.digits)}
        self.one=self.enc[(1,)+(0,)*(self.n-1)]

    def decode(self,i):
        r=[]
        for _ in range(self.n):r.append(i%self.p);i//=self.p
        return tuple(r)

    def add(self,a,b):
        return self.enc[tuple((x+y)%self.p for x,y in zip(self.digits[a],self.digits[b]))]

    def neg(self,a):
        return self.enc[tuple((-x)%self.p for x in self.digits[a])]

    def mul(self,a,b):
        da,db=self.digits[a],self.digits[b]
        out=[0]*(2*self.n-1)
        for i,x in enumerate(da):
            for j,y in enumerate(db):out[i+j]=(out[i+j]+x*y)%self.p
        for k in range(len(out)-1,self.n-1,-1):
            x=out[k]
            if x:
                for j in range(self.n):out[k-self.n+j]=(out[k-self.n+j]-x*self.poly[j])%self.p
        return self.enc[tuple(out[:self.n])]

    def power(self,a,n):
        out=self.one
        while n:
            if n&1:out=self.mul(out,a)
            a=self.mul(a,a);n//=2
        return out

    def chi(self,a):
        if a==0:return 0
        return 1 if self.power(a,(self.q-1)//2)==self.one else -1

    def constant(self,n):
        return self.enc[(n%self.p,)+(0,)*(self.n-1)]


def check(F):
    q=F.q; add=F.add;mul=F.mul
    fourth=[F.power(x,4) for x in range(q)]
    r=Counter((add(x,y),add(fourth[x],fourth[y])) for x in range(q) for y in range(q))
    chi1=F.chi(F.constant(-1));chi3=F.chi(F.constant(-3));eta=F.chi(F.constant(-6))
    g=4 if (q-1)%4==0 else 2
    a=(q-4-chi1-2*chi3-2*eta)//8
    b=(q+chi1+2*chi3)//4
    assert a>=0 and b>=0 and 8*a==q-4-chi1-2*chi3-2*eta and 4*b==q+chi1+2*chi3
    expected0={1:1, g:(q-1)//g}
    expected1={2:b,4:a,2+eta:1}
    expected0={k:v for k,v in expected0.items() if v}
    expected1={k:v for k,v in expected1.items() if v}
    total=Counter()
    for s in range(q):
        obs=Counter(c for (ss,t),c in r.items() if ss==s)
        exp=expected0 if s==0 else expected1
        assert obs==exp, (q,s,obs,exp)
        total+=obs
    sumset=1+(q-1)//g+(q-1)*(a+b+1)
    assert len(r)==sumset
    energy=sum(c*c for c in r.values())
    expected_energy=3*q*q-q-1-(q-1)*(1+chi3)**2
    assert energy==expected_energy, (q,energy,expected_energy)
    if q>3:
        for s in range(1,q):
            # The distinguished odd fiber is at t=s^4/8.
            t=mul(fourth[s],F.power(F.constant(8),q-2))
            assert r[(s,t)]==2+eta
    return q,q*q,sumset,energy,(chi1,chi3,eta),dict(sorted(total.items()))


def main():
    fields=[Field(p) for p in primes_upto(193)]
    # Irreducible quadratic / cubic polynomial quotients.
    fields += [Field(5,[2,0,1]),Field(7,[1,0,1]),Field(11,[1,0,1]),Field(5,[1,1,0,1])]
    targets=0
    for F in fields:
        q,k,S,E,chars,distr=check(F)
        targets+=k
        if q in (5,7,11,13,17,25,49,121,125):print('FIELD',q,'char',chars,'sumset',S,'energy',E,'r-spectrum',distr)
    print('CHECK_OK fields=%d prime_fields=%d extension_fields=%d exact_target_entries=%d' % (len(fields),len(fields)-4,4,targets))

if __name__=='__main__':main()
