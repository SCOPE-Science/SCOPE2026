#!/usr/bin/env python3
"""Finite-field enumeration for a cubic-moment-curve and its tangent.
Run: python3 checker.py. Uses only the Python standard library.
This is finite corroboration, not a substitute for the all-fields proof.
"""
from collections import Counter

class Field:
    def __init__(self, p, degree=1):
        self.p, self.degree = p, degree
        self.q = p ** degree
        if degree == 2:
            self.nonresidue = next(a for a in range(2, p) if pow(a, (p-1)//2, p) == p-1)
        elif degree != 1:
            raise ValueError('Only prime and quadratic-extension fields are implemented')
    def add(self, x, y):
        p = self.p
        if self.degree == 1: return (x+y)%p
        return ((x%p+y%p)%p) + p*((x//p+y//p)%p)
    def neg(self, x):
        p = self.p
        if self.degree == 1: return (-x)%p
        return (-x%p) + p*(-(x//p)%p)
    def sub(self, x, y): return self.add(x, self.neg(y))
    def mul(self, x, y):
        p = self.p
        if self.degree == 1: return x*y%p
        a,b = x%p, x//p
        c,d = y%p, y//p
        return (a*c+self.nonresidue*b*d)%p + p*((a*d+b*c)%p)
    def pow(self, x, e):
        r=1
        while e:
            if e & 1: r=self.mul(r,x)
            x=self.mul(x,x);e//=2
        return r
    def chi(self, x):
        if x==0:return 0
        return 1 if self.pow(x,(self.q-1)//2)==1 else -1
    def scale(self, x, k): return self.mul(x,k%self.p)
    def inv2(self):return pow(2,-1,self.p)

def run(p,degree):
    F=Field(p,degree);q=F.q
    add,sub,mul,powr=F.add,F.sub,F.mul,F.pow
    curve={(t,powr(t,2),powr(t,3)) for t in range(q)}
    line={(t,0,0) for t in range(q)}
    signal=curve|line
    r=Counter((add(a[0],b[0]),add(a[1],b[1]),add(a[2],b[2]))
              for a in signal for b in signal)
    phase=(p!=3 and F.chi(F.neg(2%p))==1)
    # The exceptional phase is absent in characteristic three even though -2 is a square.
    hist=Counter(r.values())
    predicted={1:q-1,2:(q-1)*(3*q-2-4*int(phase))//2,q:q}
    if phase:predicted[4]=q-1
    assert hist==predicted,(q,hist,predicted)
    assert sum(r.values())==(2*q-1)**2
    energy=sum(a*a for a in r.values())
    assert energy==q**3+6*q**2-9*q+3+8*(q-1)*int(phase)
    assert len(r)==(3*q*q-q)//2-(q-1)*int(phase)
    yz_to_t={(powr(t,2),powr(t,3)):t for t in range(q)}
    assert len(yz_to_t)==q
    inv2=F.inv2()
    for x in range(q):
        for y in range(q):
            for z in range(q):
                if y==0 and z==0: v=q
                elif (y,z) in yz_to_t:
                    t=yz_to_t[y,z]
                    v=4 if phase and x==F.neg(F.scale(t,2)) else 2
                elif z==F.scale(sub(F.scale(mul(x,y),3),powr(x,3)),inv2):
                    v=1+F.chi(sub(F.scale(y,2),powr(x,2)))
                else:v=0
                assert r[(x,y,z)]==v,(q,(x,y,z),r[(x,y,z)],v)
    return f'q={q} char={p}: epsilon={int(phase)} |S|={len(signal)} |S+S|={len(r)} E={energy} histogram={dict(sorted(hist.items()))}'

if __name__=='__main__':
    cases=[(3,1),(3,2),(5,1),(5,2),(7,1),(7,2),(11,1),(13,1),
           (17,1),(19,1),(23,1),(29,1),(31,1),(37,1)]
    for args in cases: print(run(*args))
    print('PASS: exact convolution at every target over 14 finite fields')
