#!/usr/bin/env python3
"""Exact small-field verification of the two-Engel image and its disjoint rulings."""
from collections import Counter
from itertools import product

class Field:
    def __init__(self, q):
        self.q=q
        if q==4:
            self.add=lambda a,b: a^b
            self.neg=lambda a:a
            def mul(a,b):
                out=0
                for i in range(2):
                    for j in range(2):
                        if (a>>i)&1 and (b>>j)&1:out^=1<<(i+j)
                if out&4:out^=7  # t^2 = t + 1
                return out
            self.mul=mul
        else:
            self.add=lambda a,b:(a+b)%q
            self.neg=lambda a:(-a)%q
            self.mul=lambda a,b:(a*b)%q
    def sqmult(self,a,b,c):return self.mul(self.mul(a,b),c)
    def twice(self,a):return self.add(a,a)

def value(x,y,F):
    d=len(x)
    a,n,m=F.add,F.neg,F.sqmult
    return tuple(a(a(m(x[i],x[j],y[k]),n(F.twice(m(x[i],y[j],x[k])))),m(y[i],x[j],x[k]))
           for i in range(d) for j in range(d) for k in range(d))

def test(d,q):
    F=Field(q)
    V=list(product(range(q),repeat=d))
    zero=(0,)*(d**3)
    fibers=Counter(value(x,y,F) for x in V for y in V)
    zcount=q**d+(q**d-1)*q
    nval=1+(q**d-1)*(q**(d-1)-1)//(q-1)
    assert fibers[zero]==zcount
    assert len(fibers)==nval
    assert set(fibers.values())=={zcount,q*(q-1)}
    # Equivalent projective representatives: first nonzero coordinate exactly 1.
    reps=[]
    for x in V[1:]:
        first=next(a for a in x if a)
        if first==1: reps.append(x)
    assert len(reps)==(q**d-1)//(q-1)
    images=[set(value(x,y,F) for y in V) for x in reps]
    assert all(len(s)==q**(d-1) for s in images)
    assert all(images[i]&images[j]=={zero} for i in range(len(images)) for j in range(i))
    print('PASS d=%s q=%s pairs=%s projective_rulings=%s image=%s zero_fiber=%s nonzero_fiber=%s' %
           (d,q,q**(2*d),len(reps),len(fibers),zcount,q*(q-1)))

if __name__=='__main__':
    for d,q in [(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2)]:test(d,q)
