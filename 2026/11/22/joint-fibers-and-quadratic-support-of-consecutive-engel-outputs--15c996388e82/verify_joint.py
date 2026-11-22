#!/usr/bin/env python3
"""Exhaustively verify the joint pair of adjacent Engel-Lie outputs over finite fields."""
from collections import Counter
from itertools import product


def tables(q):
    plus=[[0]*q for _ in range(q)]
    times=[[0]*q for _ in range(q)]
    minus=[0]*q
    for x in range(q):
        a,b=(x%3,x//3) if q==9 else (x,0)
        p=3 if q==9 else q
        minus[x]=(-a)%p + (p*((-b)%p) if q==9 else 0)
        for y in range(q):
            c,d=(y%3,y//3) if q==9 else (y,0)
            plus[x][y]=(a+c)%p+(p*((b+d)%p) if q==9 else 0)
            times[x][y]=(a*c-b*d)%p+(p*((a*d+b*c)%p) if q==9 else 0)
    return plus,times,minus


def test(q):
    add,mul,neg=tables(q); two=add[1][1]
    vec=list(product(range(q),repeat=3)); zero=(0,0,0)
    def sub(a,b):return add[a][neg[b]]
    def comm(x,y):
        a,b,c=x; d,e,f=y
        return (sub(mul[b][f],mul[c][e]),
            mul[two][sub(mul[a][e],mul[b][d])],
            mul[two][sub(mul[c][d],mul[a][f])])
    def quadratic(v):
        a,b,c=v; return add[mul[a][a]][mul[b][c]]
    def inner(u,v):
        a,b,c=u; d,e,f=v
        return add[add[mul[two][mul[a][d]]][mul[b][f]]][mul[c][e]]
    counts=Counter()
    for x in vec:
        for y in vec:
            z=comm(x,comm(x,y))
            w=comm(x,z)
            counts[(z,w)]+=1
    def predicted(z,w):
        if z==zero: return 2*q**4-q**2 if w==zero else 0
        d=quadratic(z)
        if d:
            return q if inner(z,w)==0 and quadratic(w)!=0 else 0
        if w==zero: return (q-1)*q**2
        return q**2 if any(all(w[j]==mul[t][z[j]] for j in range(3)) for t in range(1,q)) else 0
    for z in vec:
        for w in vec:
            got=counts[(z,w)];want=predicted(z,w)
            assert got==want,(q,z,w,got,want)
    assert sum(counts.values())==q**6
    support=sum(1 for n in counts.values() if n)
    assert support==1+q*(q*q-1)*(1+(q-1)**2)
    return {'q':q,'input_pairs':q**6,'output_pairs_tested':q**6,
            'positive_joint_fibers':support,'total_mass':sum(counts.values()),
            'zero_zero':counts[(zero,zero)],
            'nonzero_fiber_sizes':sorted({n for n in counts.values() if n})}
if __name__=='__main__':
    for q in (3,5,7,9):print(test(q),flush=True)
    print('PASS: every prescribed pair (E_2,E_3) checked, incl. extension field F_9')
