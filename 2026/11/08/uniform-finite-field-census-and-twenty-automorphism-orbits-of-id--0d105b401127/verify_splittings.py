#!/usr/bin/env python3
"""Subspace-lattice enumeration independent of Rota-Baxter matrix testing."""
from itertools import product

def ops(q):
    if q==4:
        add=lambda a,b:a^b
        def mul(a,b):
            z=0
            for i in range(2):
                for j in range(2):
                    if ((a>>i)&1) and ((b>>j)&1):
                        z^=1<<(i+j)
            if z&8:z^=0b1001 # x^3=1 modulo x^2+x+1
            if z&4:z^=0b111 # x^2=x+1
            return z
        return add,mul
    return lambda a,b:(a+b)%q,lambda a,b:(a*b)%q

def check(q):
    add,mul=ops(q)
    vs=list(product(range(q),repeat=3))
    z=(0,0,0)
    def plus(x,y):return tuple(add(a,b) for a,b in zip(x,y))
    def scalar(t,v):return tuple(mul(t,x) for x in v)
    def prod(x,y):
        a,d,b=x;A,D,B=y
        return (mul(a,A),mul(d,D),add(mul(a,B),mul(b,D)))
    lines=set();planes=set()
    for v in vs:
        if v==z:continue
        L=frozenset(scalar(t,v) for t in range(q))
        lines.add(L)
    for u in vs:
        if u==z:continue
        for v in vs:
            if v in frozenset(scalar(t,u) for t in range(q)):continue
            planes.add(frozenset(plus(scalar(s,u),scalar(t,v)) for s in range(q) for t in range(q)))
    assert len(lines)==q*q+q+1 and len(planes)==q*q+q+1
    sub1=[L for L in lines if all(prod(x,y) in L for x in L for y in L)]
    sub2=[P for P in planes if all(prod(x,y) in P for x in P for y in P)]
    comp=sum(1 for L in sub1 for P in sub2 if len(L&P)==1)
    assert len(sub1)==2*q+2,(q,len(sub1))
    assert len(sub2)==q+3,(q,len(sub2))
    assert comp==2*q*q+3*q+2,(q,comp)
    print(f'q={q}: subalgebra lines={len(sub1)}, planes={len(sub2)}, ordered rank-one splittings={comp}, all RB projections={2*comp+2}; PASS')
if __name__=='__main__':
    for q in (2,3,4,5):check(q)
    print('ALL_SUBALGEBRA_SPLITTING_CHECKS_PASS')
