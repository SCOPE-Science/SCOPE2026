#!/usr/bin/env python3
"""Independent exhaustive checks for complete-graph evolution-algebra idempotents.

Finite fields are implemented by direct polynomial arithmetic; no dependencies.
"""
from itertools import product
from math import comb

FIELDS = {2:(2,(0,1)),3:(3,(0,1)),4:(2,(1,1,1)),5:(5,(0,1)),7:(7,(0,1)),8:(2,(1,1,0,1)),9:(3,(1,0,1))}

def fld(q):
    p,f = FIELDS[q]
    d=len(f)-1
    def digits(x):
        z=[]
        for _ in range(d): z.append(x%p); x//=p
        return z
    def pack(xs):
        return sum((int(x)%p)*p**i for i,x in enumerate(xs))
    def add(a,b):
        return pack([(x+y)%p for x,y in zip(digits(a),digits(b))])
    def mul(a,b):
        aa,bb=digits(a),digits(b)
        cc=[0]*(2*d-1)
        for i,x in enumerate(aa):
            for j,y in enumerate(bb):cc[i+j]=(cc[i+j]+x*y)%p
        for k in range(2*d-2,d-1,-1):
            t=cc[k]
            for j in range(d):cc[k-d+j]=(cc[k-d+j]-t*f[j])%p
        return pack(cc[:d])
    return p,add,mul

def formula(n,q):
    p,_,_=fld(q)
    if p==2:
        if n%2 or (q.bit_length()-1)%2: return 2**(n-1)
        return 2**n
    if (n-1)%p==0:
        val=sum(comb(n,r) for r in range(1,n) if (2*r-1)%p)
        assert val%2==0
        return 1+val//2
    squares={z*z%q for z in []}  # Character computed directly in the prime-power field.
    _,_,mul=fld(q)
    squares={mul(a,a) for a in range(1,q)}
    def embedded(k):return k%p
    total=0
    for r in range(1,n):
        delta=embedded(1-4*r*(n-r))
        chi=0 if delta==0 else (1 if delta in squares else -1)
        total+=comb(n,r)*(1+chi-(1 if (n+1)%p==0 else 0))
    assert total%2==0
    return 2+total//2

def brute(n,q):
    _,add,mul=fld(q)
    count=0
    for x in product(range(q),repeat=n):
        sx=[mul(a,a) for a in x]
        good=True
        for i,a in enumerate(x):
            v=0
            for j,b in enumerate(sx):
                if i!=j:v=add(v,b)
            if a!=v:good=False;break
        if good:count+=1
    return count

def run():
    cases=[(3,2),(4,2),(5,2),(3,3),(4,3),(5,3),(3,4),(4,4),(5,4),(3,5),(4,5),(5,5),(3,7),(4,7),(3,8),(4,8),(3,9),(4,9)]
    for n,q in cases:
        got,expect=brute(n,q),formula(n,q)
        assert got==expect,(n,q,got,expect)
        print('n=%d q=%d idempotents=%d OK'%(n,q,got))
    print('VERIFY_OK cases=',len(cases))
if __name__=='__main__':run()
