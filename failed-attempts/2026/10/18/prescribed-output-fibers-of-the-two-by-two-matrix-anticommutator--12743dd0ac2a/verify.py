#!/usr/bin/env python3
"""Direct finite-field check of the full Jordan anticommutator fiber law.

This checks every ordered pair of two-by-two matrices over F_2,F_3,F_5,F_4.
The latter field is represented by F_2[t]/(t^2+t+1).
"""
from itertools import product
from collections import defaultdict,Counter

class Field:
    def __init__(self,q):
        self.q=q
    def add(self,x,y):
        return (x^y) if self.q==4 else (x+y)%self.q
    def neg(self,x):
        return x if self.q==4 else (-x)%self.q
    def mul(self,x,y):
        if self.q!=4: return x*y%self.q
        z=0
        for i in range(2):
            for j in range(2):
                if ((x>>i)&1) and ((y>>j)&1):z^=1<<(i+j)
        if z&8:z^=0b1100  # impossible for degree <=2 product
        if z&4:z^=0b111 # t^2=t+1
        return z
    def inv(self,x):
        assert x!=0
        return next(t for t in range(1,self.q) if self.mul(t,x)==1)

def calc(q):
    F=Field(q); add=F.add; mul=F.mul
    mats=list(product(range(q),repeat=4))
    def matrix_prod(x,y):
        a,b,c,d=x;e,f,g,h=y
        return (add(mul(a,e),mul(b,g)),add(mul(a,f),mul(b,h)),add(mul(c,e),mul(d,g)),add(mul(c,f),mul(d,h)))
    def anti(x,y):
        p=matrix_prod(x,y);r=matrix_prod(y,x)
        return tuple(add(p[i],r[i]) for i in range(4))
    def scalar(x):return x[1]==0 and x[2]==0 and x[0]==x[3]
    def trace(x):return add(x[0],x[3])
    def lines():return [(1,t) for t in range(q)]+[(0,1)]
    def action(x,v):return (add(mul(x[0],v[0]),mul(x[1],v[1])),add(mul(x[2],v[0]),mul(x[3],v[1])))
    def proportional(v,w):return add(mul(v[0],w[1]),F.neg(mul(v[1],w[0])))==0
    def predicted(C):
        if q%2==0:
            if trace(C)!=0:return 0
            if C==(0,0,0,0):return q**6+q**5-q**3
            return q**5-q**3
        b=q*(q-1)*(q*q-q-1)
        if scalar(C):
            if C==(0,0,0,0):return b+q*q*(q**3-1)+q*q*(q*q-1)+q**4
            return b+q*q*(q**3-1)
        k=e=0
        for v in lines():
            w=action(C,v)
            if w==(0,0):k+=1
            elif proportional(v,w):e+=1
        return b+q*q*(q-1)+q*(q-1)*(q+1+(q-1)*k-e)
    observed=Counter()
    for x in mats:
        for y in mats:observed[anti(x,y)]+=1
    for C in mats:
        p=predicted(C)
        assert observed[C]==p,(q,C,observed[C],p)
    assert sum(observed.values())==q**8
    hist=Counter(observed[C] for C in mats)
    print(f'q={q}: targets={q**4} ordered_pairs={q**8} fiber_histogram={dict(sorted(hist.items()))} VERIFY_OK')

if __name__=='__main__':
    for q in (2,3,4,5):calc(q)
    print('VERIFY_OK')
