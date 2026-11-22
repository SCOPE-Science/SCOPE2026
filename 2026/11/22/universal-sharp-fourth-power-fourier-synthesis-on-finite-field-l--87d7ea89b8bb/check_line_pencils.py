"""Standalone finite-field Fourier checks for exact fourth-norm line-pencil synthesis.
Standard-library only. Run: python check_line_pencils.py
"""
import cmath
import itertools
import math
import random

class Field:
    def __init__(self, q):
        self.q=q
        if q==9:
            self.p=3; self.n=2; self.polynomial="x^2+1"
        elif q in (4,8):
            self.p=2; self.n={4:2,8:3}[q]; self.polynomial={4:0b111,8:0b1011}[q]
        else:
            self.p=q; self.n=1; self.polynomial=None
    def add(self,x,y):
        if self.q==9:
            return (x%3+y%3)%3+3*((x//3+y//3)%3)
        return x^y if self.n>1 else (x+y)%self.p
    def mul(self,x,y):
        if self.n==1:return x*y%self.p
        if self.q==9:
            a,b=divmod(x,3)[1], x//3
            c,d=divmod(y,3)[1], y//3
            return (a*c-b*d)%3+3*((a*d+b*c)%3)
        z=0
        while y:
            if y&1:z^=x
            y>>=1;x<<=1
            if x & self.q:x^=self.polynomial
        return z
    def power(self,x,n):
        r=1
        while n:
            if n&1:r=self.mul(r,x)
            x=self.mul(x,x);n>>=1
        return r
    def trace(self,x):
        if self.n==1:return x
        if self.q==9:return (2*(x%3))%3
        r=0;y=x
        for _ in range(self.n):
            r=self.add(r,y)
            y=self.mul(y,y)
        assert r in (0,1)
        return r
    def character(self,x):
        return cmath.exp(-2j*math.pi*self.trace(x)/self.p)

def span_lines(F, slopes):
    directions=[(1,t) for t in range(F.q)]+[(0,1)]
    S={(0,0)}
    for index in slopes:
        x,y=directions[index]
        for a in range(1,F.q):
            S.add((F.mul(a,x),F.mul(a,y)))
    assert len(S)==1+len(slopes)*(F.q-1)
    return S

def constant_and_coefficients(q,k):
    if k==1:
        return q**(-0.25),1/q,1/q
    if k==q+1:
        return 1.0,1/q**2,1/q**2
    s=((q+1-k)/(k-1))**(1/3)
    den=k-1+k*s
    x=(1+s)/den
    b=x/q
    a=1-k*(q-1)*b
    C=(1+(q-1)*(s/den)**3)**(-0.25)
    return C,a,b

def raw_fourier(F, data):
    for u in range(F.q):
        for v in range(F.q):
            total=0j
            for (x,y),val in data.items():
                dot=F.add(F.mul(u,x),F.mul(v,y))
                total+=val*F.character(dot)
            yield total

def check():
    rng=random.Random(268603)
    tests=0
    for q in (2,3,4,5,7,8,9,11):
        F=Field(q)
        directions=list(range(q+1))
        for k in range(1,q+2):
            chosen=list(itertools.combinations(directions,k))
            if q>5 and len(chosen)>15:
                chosen=rng.sample(chosen,15)
            for slopes in chosen:
                S=span_lines(F,slopes)
                C,a,b=constant_and_coefficients(q,k)
                data={pt:(a if pt==(0,0) else b) for pt in S}
                vals=list(raw_fourier(F,data))
                origin=vals[0]
                assert abs(origin-1)<1e-10,(q,k,origin)
                norm4=sum(abs(x)**4 for x in vals)**.25
                ratio=abs(origin)/norm4
                assert abs(ratio-C)<2e-10,(q,k,slopes,C,ratio)
                assert max(abs(x) for x in vals)<=1+2e-10
                tests+=1
                # Stress test with arbitrary complex coefficient vectors.
                for _ in range(4):
                    data={pt:complex(rng.gauss(0,1),rng.gauss(0,1)) for pt in S}
                    vals=list(raw_fourier(F,data))
                    ratio=max(abs(x) for x in vals)/(sum(abs(x)**4 for x in vals)**.25)
                    assert ratio<=C+1e-9,(q,k,slopes,C,ratio)
                    tests+=1
    # All field sizes above are checked; this is finite validation only.
    print(f'PASS: {tests} Fourier optimizer and random stress checks, fields 2,3,4,5,7,8,9,11; theoretical proof required for all prime powers.')

if __name__=='__main__':check()
