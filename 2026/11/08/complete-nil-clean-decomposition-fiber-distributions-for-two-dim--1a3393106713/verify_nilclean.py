#!/usr/bin/env python3
"""Standalone exhaustive verification of nil-clean decomposition fibers in M_2(F_q).
GF(4) encoded with polynomial t^2+t+1; primes use integer residues.
"""
from itertools import product
from collections import Counter

def field(q):
    if q == 4:
        add=lambda a,b:a^b
        def mul(a,b):
            r=0
            for i in range(2):
                for j in range(2):
                    if (a>>i)&1 and (b>>j)&1: r^=1<<(i+j)
            if r&8: r^=0b1110
            if r&4: r^=0b111
            return r
        char=2
    else:
        add=lambda a,b:(a+b)%q
        mul=lambda a,b:(a*b)%q
        char=q
    neg=lambda a:next(b for b in range(q) if add(a,b)==0)
    sub=lambda a,b:add(a,neg(b))
    return add,mul,neg,sub,char

def matmul(A,B,z,add,mul):
    return tuple(add(mul(A[2*i],B[j]),mul(A[2*i+1],B[2+j])) for i in range(2) for j in range(2))

def expected(A,q,add,mul,neg,sub,char):
    a,b,c,d=A
    t=add(a,d);det=sub(mul(a,d),mul(b,c))
    nil=(t==0 and det==0)
    trtwo=add(1,1)
    shifted=(t==trtwo and sub(add(det,1),t)==0) # det(A-I)=det(A)-tr(A)+1
    out=int(nil)+int(shifted)
    if t!=1:return out
    if det==0:return out+2*q-1
    eiglines=0
    for v in [(1,x) for x in range(q)]+[(0,1)]:
        Av=(add(mul(a,v[0]),mul(b,v[1])),add(mul(c,v[0]),mul(d,v[1])))
        if sub(mul(v[0],Av[1]),mul(v[1],Av[0]))==0:eiglines+=1
    return out+q+1-eiglines

def run(q):
    add,mul,neg,sub,char=field(q)
    mats=list(product(range(q),repeat=4))
    nil=[];idem=[]
    for P in mats:
        P2=matmul(P,P,q,add,mul)
        if P2==P:idem.append(P)
        if add(P[0],P[3])==0 and sub(mul(P[0],P[3]),mul(P[1],P[2]))==0:nil.append(P)
    fibers=Counter()
    hist=Counter()
    for P in idem:
        for N in nil:
            A=tuple(add(P[i],N[i]) for i in range(4))
            fibers[A]+=1
    for A in mats:
        actual=fibers[A]
        predicted=expected(A,q,add,mul,neg,sub,char)
        assert actual==predicted,(q,A,actual,predicted)
        hist[actual]+=1
    assert len(idem)==q*(q+1)+2
    assert len(nil)==q*q
    assert sum(k*v for k,v in hist.items()) == len(idem)*len(nil)
    # All positive traces (0,1,2) and the discriminant splitting law.
    count_nonzero=sum(v for k,v in hist.items() if k>0)
    assert count_nonzero==q**3+2*q*q-(char!=2)
    assert max(hist)==2*q-1
    print(f'q={q} matrices={q**4} idempotents={len(idem)} nilpotents={len(nil)} nilclean={count_nonzero} maxfiber={max(hist)} histogram={dict(sorted(hist.items()))} PASS')

if __name__=='__main__':
    for q in [2,3,4,5,7]:run(q)
    print('ALL_NILCLEAN_FIBER_HISTOGRAM_CHECKS_PASS')
