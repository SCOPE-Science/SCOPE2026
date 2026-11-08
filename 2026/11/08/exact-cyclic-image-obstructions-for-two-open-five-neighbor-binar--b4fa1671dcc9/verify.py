#!/usr/bin/env python3
"""Reproduce exact Boolean and finite-ring computations; no external dependencies."""
from collections import Counter
from itertools import product

def f_a(a,b,c,d,e):
    return b^c^((a^b)&((c&d)^((c^d^1)&e)))

def f_c(a,b,c,d,e):
    return b^((a^b)&((c&d)^(c&e)^c^(d&e)))^(c&(d^e))^(d&e)

def dd(u):
    n=len(u)
    return [(u[i]^u[(i+1)%n]) for i in range(n)]

def hh(u,typ):
    n=len(u)
    if typ=='A':
        return [(u[i]^ (u[(i-1)%n] & (1^u[(i+1)%n]) & u[(i+2)%n])) for i in range(n)]
    return [(u[i]^((1^u[(i-1)%n]) & u[(i+1)%n] & (1^u[(i+2)%n]))) for i in range(n)]

def source_f(u,fun):
    n=len(u)
    return [fun(*[u[(i+j)%n] for j in range(5)]) for i in range(n)]

def composed(u,typ):
    z=hh(dd(u),typ)
    return [z[(i+1)%len(u)] for i in range(len(u))]

def phi(u,typ):
    return sum(hh(u,typ))%2

checks=0
for bits in product((0,1),repeat=5):
    a,b,c,d,e=bits
    u=[a^b,b^c,c^d,d^e]
    # centered H applied to differences produces local rule at site i=0 via shift index 1
    for fun,typ in ((f_a,'A'),(f_c,'C')):
        # direct local composition: H(Dx) at i+1, use its neighbors 0,1,2,3
        # input a,b,c,d,e -> differences p=a+b,q=b+c,r=c+d,s=d+e
        p,q,r,s=u
        h=(q ^ ((p & (1^r) & s) if typ=='A' else ((1^p)&r&(1^s))))
        assert fun(*bits)==h, (typ,bits)
        checks+=1
for n in range(1,11):
    for tup in product((0,1), repeat=n):
        u=list(tup)
        for typ,fun in (('A',f_a),('C',f_c)):
            assert hh(hh(u,typ),typ)==u,(n,typ,u)
            assert source_f(u,fun)==composed(u,typ),(n,typ,u)
            checks+=2
        assert hh(u,'C')==[1^z for z in hh([1^v for v in u],'A')]
        checks+=1
    for typ,fun in (('A',f_a),('C',f_c)):
        pred=Counter()
        for tup in product((0,1), repeat=n):
            u=list(tup)
            pred[tuple(source_f(u,fun))]+=1
        for tup in product((0,1), repeat=n):
            u=list(tup)
            assert pred[tuple(u)] == (2 if phi(u,typ)==0 else 0),(n,typ,u)
            checks+=1
        assert len(pred)==1<<(n-1)
        checks+=1
for n in range(7,13):
    for typ in 'AC':
        for i in range(n):
            u=[int(k==i) for k in range(n)]
            assert (phi(u,typ)==0)==(typ=='C'),(n,typ,'one',i)
            checks+=1
        for i in range(n):
            for j in range(i+1,n):
                u=[int(k==i or k==j) for k in range(n)]
                sep=min(j-i,n-(j-i))
                forbidden=(sep==3 if typ=='A' else sep in (1,2))
                assert (phi(u,typ)==1)==forbidden,(n,typ,i,j,sep)
                checks+=1
print(f'VERIFY_OK checks={checks}')
