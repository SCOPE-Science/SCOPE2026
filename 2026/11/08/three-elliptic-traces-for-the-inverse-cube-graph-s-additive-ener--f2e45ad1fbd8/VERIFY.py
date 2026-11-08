#!/usr/bin/env python3
"""Exact finite-field checks for the inverse-cube graph energy formula."""
from collections import Counter


def primes_up_to(n):
    return [p for p in range(2, n+1) if all(p%d for d in range(2,int(p**.5)+1))]


class FiniteField:
    def __init__(self, p, degree=1):
        assert degree in (1, 2)
        self.p, self.degree, self.q = p, degree, p**degree
        if degree == 2:
            self.d = next(i for i in range(2,p) if pow(i,(p-1)//2,p) == p-1)

    def from_int(self, n):
        return n%self.p

    def add(self,x,y):
        p=self.p
        if self.degree==1:return (x+y)%p
        return ((x%p+y%p)%p)+p*((x//p+y//p)%p)

    def mul(self,x,y):
        p=self.p
        if self.degree==1:return x*y%p
        a,b=x%p,x//p
        c,d=y%p,y//p
        return ((a*c+self.d*b*d)%p)+p*((a*d+b*c)%p)

    def pow(self,a,n):
        r=1
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a)
            n>>=1
        return r

    def chi(self,a):
        if a==0:return 0
        return 1 if self.pow(a,(self.q-1)//2)==1 else -1

    def f(self,kind,x):
        m=self.mul;add=self.add;v=self.from_int
        xx=m(x,x)
        if kind==0:
            return m(add(1,x),add(add(1,x),m(v(4),xx)))
        R=add(add(m(v(4),xx),m(v(5),x)),v(10))
        return m(add(x,v(2)) if kind==1 else add(x,v(-2)), R)

    def traces(self):
        return tuple(-sum(self.chi(self.f(j,x)) for x in range(self.q)) for j in range(3))

    def direct_energy(self):
        q=self.q;add=self.add;mul=self.mul
        invc=[None]*q
        for x in range(1,q):
            y=self.pow(x,q-2)
            invc[x]=mul(mul(y,y),y)
        reps=Counter()
        for x in range(1,q):
            for y in range(1,q):
                reps[(add(x,y),add(invc[x],invc[y]))]+=1
        return sum(c*c for c in reps.values())

    def predicted_energy(self):
        q=self.q;a0,ap,am=self.traces()
        eps=self.chi(self.from_int(-3));eta=self.chi(self.from_int(-1))
        return (q-1)*(4*q-14-6*eps-3*eta-2*eps*a0-ap-am)


def main():
    count=0
    for p in primes_up_to(101):
        if p<7:continue
        F=FiniteField(p)
        actual=F.direct_energy();pred=F.predicted_energy()
        assert actual==pred,(p,actual,pred,F.traces())
        count+=1
    extensions=[]
    for p in (7,11,13,17):
        F=FiniteField(p,2)
        actual=F.direct_energy();pred=F.predicted_energy()
        assert actual==pred,(p,actual,pred,F.traces())
        a=FiniteField(p).traces()
        a2=F.traces()
        assert all(a2[j]==a[j]*a[j]-2*p for j in range(3)),(p,a,a2)
        extensions.append((p,actual))
    print('VERIFY_OK prime_fields=%d quadratic_extensions=%d extension_energies=%s three_elliptic_traces=PASS'%(count,len(extensions),extensions))

if __name__=='__main__':main()
