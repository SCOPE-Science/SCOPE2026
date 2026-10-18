"""Independent finite-field and Fourier checks for the cubic-graph fourth moment.
Uses Python's standard library only. Run: python3 checker.py
No finite test substitutes for the all-field algebraic proof.
"""
from collections import defaultdict
import cmath
from math import isclose, pi, sqrt
import random

class Field:
    def __init__(self,p,degree=1):
        assert p in (5,7,11,13,17,19) and degree in (1,2)
        self.p=p
        self.degree=degree
        self.q=p**degree
        if degree==2:
            self.nonsquare=next(a for a in range(2,p) if pow(a,(p-1)//2,p)==p-1)
    def add(self,x,y):
        p=self.p
        if self.degree==1: return (x+y)%p
        return ((x%p+y%p)%p)+p*((x//p+y//p)%p)
    def neg(self,x):
        p=self.p
        if self.degree==1: return (-x)%p
        return (-x%p)+p*(-(x//p)%p)
    def mul(self,x,y):
        p=self.p
        if self.degree==1:return x*y%p
        a,b=x%p,x//p
        c,d=y%p,y//p
        return ((a*c+self.nonsquare*b*d)%p)+p*((a*d+b*c)%p)
    def cube(self,x):
        return self.mul(self.mul(x,x),x)
    def trace(self,x):
        return x if self.degree==1 else (2*(x%self.p))%self.p
    def minus(self,x,y):
        return self.add(x,self.neg(y))


def fibers(F):
    by_sum=defaultdict(list)
    for x in range(F.q):
        for y in range(x,F.q):
            z=(F.add(x,y),F.add(F.cube(x),F.cube(y)))
            by_sum[z].append((x,y))
    exception=by_sum[(0,0)]
    assert len(exception)==(F.q+1)//2
    assert all(F.add(x,y)==0 for x,y in exception)
    for (s,t),pairs in by_sum.items():
        if s!=0: assert len(pairs)==1
        else: assert (s,t)==(0,0)
    return len(by_sum)


def convolution(F,f):
    conv=defaultdict(complex)
    cubes=[F.cube(x) for x in range(F.q)]
    for x in range(F.q):
        for y in range(F.q):
            z=(F.add(x,y),F.add(cubes[x],cubes[y]))
            conv[z]+=f[x]*f[y]
    return sum(abs(v)**2 for v in conv.values())


def quadratic_identity(F,f):
    S=sum(abs(t)**2 for t in f)
    Q=sum(abs(t)**4 for t in f)
    R=sum(abs(f[x])**2*abs(f[F.neg(x)])**2 for x in range(F.q))
    B=sum(f[x]*f[F.neg(x)] for x in range(F.q))
    return 2*S*S-Q-2*R+abs(f[0])**4+abs(B)**2


def direct_fourier(F,f):
    q=F.q; p=F.p
    c=[F.cube(x) for x in range(q)]
    root=[cmath.exp(2j*pi*k/p) for k in range(p)]
    value=0.
    for u in range(q):
        for v in range(q):
            Ef=sum(f[x]*root[F.trace(F.add(F.mul(u,x),F.mul(v,c[x])))]
                   for x in range(q))/q
            value+=abs(Ef)**4
    return value/(sum(abs(z)**2 for z in f)/q)**2


def run():
    rng=random.Random(261026)
    assertion_count=0
    for p,k in [(5,1),(7,1),(11,1),(13,1),(17,1),(5,2),(7,2)]:
        F=Field(p,k);q=F.q
        nf=fibers(F);assertion_count+=1
        for _ in range(150 if q<=17 else 16):
            f=[complex(rng.randrange(-3,4),rng.randrange(-3,4)) for x in range(q)]
            assert any(f)
            direct=convolution(F,f);identity=quadratic_identity(F,f)
            assert isclose(direct,identity,rel_tol=3e-12,abs_tol=1e-8)
            S=sum(abs(z)**2 for z in f)
            assert direct/S**2 <= 3-6/(2*q+1)+2e-12
            assertion_count+=2
        # Explicit paired-phase optimizer, varying randomly over every orbit.
        f=[0j]*q; f[0]=sqrt(3)
        for x in range(1,q):
            y=F.neg(x)
            if x>y: continue
            angle=rng.uniform(-pi,pi)
            f[x]=sqrt(2)*cmath.exp(1j*angle)
            f[y]=sqrt(2)*cmath.exp(-1j*angle)
        S=sum(abs(z)**2 for z in f)
        assert isclose(S,2*q+1,rel_tol=1e-12)
        ratio=convolution(F,f)/S**2
        assert isclose(ratio,3-6/(2*q+1),rel_tol=1e-12)
        assertion_count+=2
        # Direct characters provide an independent verification of normalization.
        if q in (5,7,25):
            fourier=direct_fourier(F,f)
            assert isclose(fourier,ratio,rel_tol=2e-12,abs_tol=2e-11)
            assertion_count+=1
        print('field',q,'prime',p,'degree',k,'unordered fibers',nf,'sharp constant',ratio)
    print('PASS',assertion_count,'checks; direct Fourier checks for q=5,7,25')

if __name__=='__main__':run()
