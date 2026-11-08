#!/usr/bin/env python3
"""Finite-field checks for a Fermat dual-curve calculation; no external libraries."""
from itertools import product

class Field:
    def __init__(self,p,nonresidue):
        self.p=p; self.n=p*p; self.c=nonresidue
        self.elems=tuple((a,b) for a in range(p) for b in range(p))
        self.zero=(0,0); self.one=(1,0)
    def add(self,x,y): return ((x[0]+y[0])%self.p,(x[1]+y[1])%self.p)
    def neg(self,x): return ((-x[0])%self.p,(-x[1])%self.p)
    def sub(self,x,y): return self.add(x,self.neg(y))
    def mul(self,x,y):
        a,b=x; c,d=y
        return ((a*c+b*d*self.c)%self.p,(a*d+b*c)%self.p)
    def pow(self,x,n):
        r=self.one
        while n:
            if n&1:r=self.mul(r,x)
            x=self.mul(x,x); n//=2
        return r
    def div(self,x,y):return self.mul(x,self.pow(y,self.n-2))
    def projective(self,x):
        for z in x:
            if z!=self.zero:
                return tuple(self.div(v,z) for v in x)
        raise ValueError('zero triple')
    def points(self):
        for a,b in product(self.elems,repeat=2):yield (self.one,a,b)
        for b in self.elems:yield (self.zero,self.one,b)
        yield (self.zero,self.zero,self.one)
    def sum(self,*xs):
        s=self.zero
        for x in xs:s=self.add(s,x)
        return s

def compute(p,c):
    f=Field(p,c); q=p; d=2*q+1; m=d-2
    two=(2%p,0)
    def Fermat(x):return f.sum(*(f.pow(t,d) for t in x))
    def G(x):
        a,b,z=(f.pow(t,d) for t in x)
        pos=f.sum(f.mul(a,a),f.mul(b,b),f.mul(z,z))
        pairs=f.sum(f.mul(a,b),f.mul(a,z),f.mul(b,z))
        return f.sub(pos,f.mul(two,pairs))
    def partials(x):
        a,b,z=(f.pow(t,d) for t in x)
        dcoef=(2*d%p,0)
        vals=(a,b,z)
        return tuple(f.mul(dcoef,f.mul(f.pow(x[i],d-1),f.sub(vals[i],f.sum(vals[(i+1)%3],vals[(i+2)%3])))) for i in range(3))
    C={f.projective(pt) for pt in f.points() if Fermat(pt)==f.zero}
    D={f.projective(pt) for pt in f.points() if G(pt)==f.zero}
    squares={f.projective(tuple(f.pow(t,2) for t in pt)) for pt in C}
    frob_gauss={f.projective(tuple(f.pow(t,2*q) for t in pt)) for pt in C}
    assert D==squares==frob_gauss, (p,len(C),len(D),len(squares),len(frob_gauss))
    assert len(C)==len(squares)
    singular={pt for pt in D if all(g==f.zero for g in partials(pt))}
    expected={pt for pt in D if any(v==f.zero for v in pt)}
    assert singular==expected,(p,len(singular),len(expected))
    assert len(singular)==3, (p,len(singular)) # gcd(d,p^2-1)=1 for p=3,5
    for pt in C:
        if all(t!=f.zero for t in pt):
            u=f.projective(tuple(f.pow(t,2) for t in pt))
            grad=partials(u)
            expo=tuple(f.pow(t,m) for t in pt)
            assert f.projective(grad)==f.projective(expo)
    print(f'p={p} q={q} d={d} field_size={f.n} projective_points={f.n*f.n+f.n+1} Fermat_points={len(C)} dual_points={len(D)} singular_points={len(singular)} check=PASS')

if __name__=='__main__':
    compute(3,2) # X^2+1 irreducible in F_3; alpha^2=2
    compute(5,2) # X^2-2 irreducible in F_5; alpha^2=2
    print('ALL_DUAL_AND_BIDUAL_FINITE_CHECKS_PASSED')
