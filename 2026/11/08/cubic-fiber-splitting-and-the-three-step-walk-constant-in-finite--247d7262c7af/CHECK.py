"""Independent finite-field coefficient tests for a cubic-fold Fourier projector.
Run with Python 3: python CHECK.py (standard library only).
"""
import cmath
import math
import random

class Field:
    def __init__(self,p,D=None):
        self.p,self.D=p,D
        self.elements=list(range(p if D is None else p*p))
        self.q=len(self.elements)
    def pair(self,x):return (x%self.p, x//self.p)
    def val(self,a,b):return a%self.p + self.p*(b%self.p)
    def add(self,x,y):
        if self.D is None:return (x+y)%self.p
        a,b=self.pair(x);c,d=self.pair(y)
        return self.val(a+c,b+d)
    def neg(self,x):
        if self.D is None:return (-x)%self.p
        a,b=self.pair(x);return self.val(-a,-b)
    def mul(self,x,y):
        if self.D is None:return (x*y)%self.p
        a,b=self.pair(x);c,d=self.pair(y)
        if self.p==2:return self.val(a*c+b*d,a*d+b*c+b*d)
        return self.val(a*c+self.D*b*d,a*d+b*c)
    def pow(self,x,k):
        z=1
        while k:
            if k&1:z=self.mul(z,x)
            x=self.mul(x,x);k>>=1
        return z
    def trace(self,x):
        if self.D is None:return x
        # explicit x + x^p, verified to lie in the prime subfield.
        z=self.add(x,self.pow(x,self.p))
        assert z<self.p
        return z


def check(F):
    q,p=F.q,F.p
    E=F.elements
    phases=[cmath.exp(2j*math.pi*j/p) for j in range(p)]
    psi=lambda x: phases[F.trace(x)]
    y3={y:F.pow(y,3) for y in E}
    roots={u:[y for y in E if y3[y]==u] for u in E}
    d=math.gcd(3,q-1)
    assert all(len(v) in (0,1,3) for v in roots.values())
    if d==3:
        mu=roots[1]
        assert len(mu)==3
        H=sum(abs(sum(psi(F.mul(b,z)) for z in mu)) for b in E)
        expected=1+(q-1)**2*H/(3*q*q)
        if p%3==1:
            assert all(z<p for z in mu)
            ap=sum(abs(sum(phases[(t*z)%p] for z in mu)) for t in range(p))/p
        else:
            ap=sum(abs(phases[s]+phases[t]+phases[(-s-t)%p]) for s in range(p) for t in range(p))/(p*p)
        assert abs(H/q-ap)<1e-9,(q,p,H/q,ap)
    else:
        expected=q-1+1/q

    total=0.
    nonzero=0
    # Compute all Fourier coefficients through exact algebraic root sets.
    for c in E:
        for a in E:
            # y solves a+c y^3=0
            yy=[y for y in E if F.add(a,F.mul(c,y3[y]))==0]
            for b in E:
                z=sum(psi(F.mul(b,y)) for y in yy)
                total+=abs(z)/(q*q)
                if abs(z)>1e-9:nonzero+=1
    assert abs(total-expected)<1e-8,(q,total,expected)
    expected_nonzero=1+q*(q-1)+q*(q-1)**2//d
    assert nonzero==expected_nonzero,(q,nonzero,expected_nonzero)

    # Directly evaluate original defining Fourier sums at sampled frequencies.
    R=random.Random(400+q)
    triples=[(a,b,c) for a in E for b in E for c in E]
    sample=triples if q<=13 else R.sample(triples,125)
    for a,b,c in sample:
        slow=sum(psi(F.add(F.add(F.mul(a,x),F.mul(b,y)),F.mul(c,F.mul(x,y3[y])))) for x in E for y in E)
        root=q*sum(psi(F.mul(b,y)) for y in E if F.add(a,F.mul(c,y3[y]))==0)
        assert abs(slow-root)<1e-8,(q,a,b,c,slow,root)
    return q,p,d,len(sample),nonzero,total

def main():
    fields=[Field(p) for p in (2,3,5,7,11,13,19)]+[Field(2,0),Field(3,2),Field(5,2),Field(7,3)]
    for f in fields:
        result=check(f)
        print('FIELD',result)
    print('CHECK_OK fields=%d'%len(fields))

if __name__=='__main__':main()
