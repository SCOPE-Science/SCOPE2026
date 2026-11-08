"""Exact finite-field checks for sextic-graph additive energy. Python 3 standard library."""
from collections import Counter

class Field:
    def __init__(self,p,n=None):
        self.p=p;self.n=n;self.q=p if n is None else p*p
        if n is not None:
            assert pow(n,(p-1)//2,p)==p-1, (p,n)
        self.zero=0; self.one=1
    def add(self,x,y):
        p=self.p
        if self.n is None:return (x+y)%p
        return (x%p+y%p)%p+p*((x//p+y//p)%p)
    def neg(self,x):
        return self.sub(0,x)
    def sub(self,x,y):
        p=self.p
        if self.n is None:return (x-y)%p
        return ((x%p-y%p)%p)+p*((x//p-y//p)%p)
    def mul(self,x,y):
        p=self.p
        if self.n is None:return x*y%p
        a,b=x%p,x//p;c,d=y%p,y//p
        return ((a*c+self.n*b*d)%p)+p*((a*d+b*c)%p)
    def pow(self,x,n):
        z=1
        while n:
            if n&1:z=self.mul(z,x)
            x=self.mul(x,x);n//=2
        return z
    def val(self,n):return n%self.p
    def chi(self,x):
        if x==0:return 0
        v=self.pow(x,(self.q-1)//2)
        assert v in (1,self.neg(1)),(x,v)
        return 1 if v==1 else -1
    def polynomial(self,coeffs,x):
        v=0
        for c in reversed(coeffs):v=self.add(self.mul(v,x),self.val(c))
        return v

def check(p,n=None):
    f=Field(p,n);q=f.q
    plus=f.add;mul=f.mul;sub=f.sub;chi=f.chi
    val=f.val
    xs=range(q)
    T1=sum(chi(mul(val(-3),mul(u,f.polynomial([-55,10,1],u)))) for u in xs)
    T2=sum(chi(mul(val(15),mul(z,f.polynomial([11,26,11],z)))) for z in xs)
    root_count=sum(f.polynomial([5,0,10,0,1],r)==0 for r in xs)
    I=2*root_count
    d=chi(val(-3))
    import math
    g=math.gcd(6,q-1)
    model=1+(q-1)*g+(q-1)*(3*q-2-2*d+2*T1+T2-I)
    # Independent direct finite-field count across all original ordered (a,b).
    sums=Counter()
    six=[f.pow(x,6) for x in xs]
    for a in xs:
        for b in xs:
            sums[(plus(a,b),plus(six[a],six[b]))]+=1
    actual=sum(v*v for v in sums.values())
    assert actual==model, (q,actual,model,T1,T2,I)
    # Independently verify the main auxiliary quartic curve and its decomposition.
    B=0
    for r in xs:
        r2=mul(r,r)
        for t in xs:
            t2=mul(t,t)
            if plus(plus(plus(mul(r2,r2),mul(r2,t2)),mul(t2,t2)),plus(mul(val(15),plus(r2,t2)),val(15)))==0:
                B+=1
    Bformula=q-1-2*d+2*T1+T2
    assert B==Bformula,(q,B,Bformula)
    if p!=11:
        assert abs(T1)<=2*q**.5+1e-9,(q,'T1 Hasse',T1)
        assert abs(T2)<=2*q**.5+1e-9,(q,'T2 Hasse',T2)
    print('PASS',q,'energy',actual,'T1',T1,'T2',T2,'intersection',I,'auxiliary',B)

if __name__=='__main__':
    for p in (7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71):check(p)
    for p,n in ((7,3),(11,2),(13,2)):check(p,n)
    print('SEXTIC_GRAPH_EXACT_ENERGY_CHECKS_PASS')
