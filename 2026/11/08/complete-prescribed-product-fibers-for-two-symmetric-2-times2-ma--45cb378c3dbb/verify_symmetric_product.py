"""Reproducible exhaustive multiplication-fiber check for symmetric 2x2 matrices.
Only Python standard library. Fields are prime fields or GF(2^f) from explicit
irreducible binary polynomials, so extension field checks are not prime-ring checks.
"""
from collections import Counter
from itertools import product

class Field:
    def __init__(self,q,polynomial=None):
        self.q=q; self.polynomial=polynomial
        self.characteristic=2 if polynomial is not None else (3 if q==9 else q)
        if polynomial is not None:
            assert q in (4,8)
            assert polynomial in (0b111,0b1011)
        self.add=lambda a,b: (a^b) if polynomial is not None else ((a%3+b%3)%3+3*((a//3+b//3)%3) if q==9 else (a+b)%q)
        self.neg=lambda a: a if polynomial is not None else ((-a%3)%3+3*((-(a//3))%3) if q==9 else (-a)%q)
        self.mul=self._mul
    def _mul(self,a,b):
        if self.q==9:
            x,y=a%3,a//3;u,v=b%3,b//3
            return (x*u-y*v)%3+3*((x*v+y*u)%3)
        if self.polynomial is None:return (a*b)%self.q
        v=0
        while b:
            if b&1:v^=a
            a<<=1
            if a&self.q:a^=self.polynomial
            b>>=1
        return v
    def sub(self,a,b):return self.add(a,self.neg(b))

def multiply_symmetric(A,B,F):
    a,b,c=A;d,e,f=B
    m=F.mul;s=F.add
    return (s(m(a,d),m(b,e)),s(m(a,e),m(b,f)),
            s(m(b,d),m(c,e)),s(m(b,e),m(c,f)))

def formula(C,F):
    q=F.q;a,b,c,d=C;m=F.mul;s=F.add
    trace=s(a,d)
    determinant=F.sub(m(a,d),m(b,c))
    if C==(0,0,0,0):return 3*q**3-q**2-q
    if determinant==0:return 2*q*(q-1) if trace==0 else (q-1)*(2*q-1)
    if a==d and b==0 and c==0:return q*q*(q-1)
    roots=sum(s(F.sub(m(x,x),m(trace,x)),determinant)==0 for x in range(q))
    return ((q-1)**2 if roots==2 else q*(q-1) if roots==1 else q*q-1)

def verify(q,poly=None):
    F=Field(q,poly)
    symmetric=list(product(range(q),repeat=3))
    counts=Counter(multiply_symmetric(A,B,F) for A in symmetric for B in symmetric)
    categories=Counter()
    for C in product(range(q),repeat=4):
        f=formula(C,F)
        assert counts[C]==f,(q,C,counts[C],f)
        categories[f]+=1
    assert sum(counts.values())==q**6
    print(f'PASS field={q} polynomial={poly} targets={q**4} pairs={q**6} fibers={dict(sorted(categories.items()))}')

if __name__=='__main__':
    for q,poly in [(2,None),(3,None),(4,0b111),(5,None),(7,None),(8,0b1011),(9,None)]:verify(q,poly)
    print('ALL_SYMMETRIC_PRODUCT_FIBERS_PASS')
