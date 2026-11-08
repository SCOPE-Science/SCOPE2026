#!/usr/bin/env python3
"""Independent orbit enumeration for the (2,3) root divisor under PGL2(F_p).
Finite prime-field tests; not a proof for all prime powers.
"""
from itertools import product
from collections import Counter

def poly_eval(c,x,p):
    a=0
    for z in reversed(c): a=(a*x+z)%p
    return a

def irreducibles(p,d):
    return [(c+(1,)) for c in product(range(p),repeat=d)
            if all(poly_eval(c+(1,),x,p) for x in range(p))]

def primitive(p):
    for a in range(2,p):
        if len({pow(a,i,p) for i in range(1,p)})==p-1:return a
    return 1

def mul(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%p
    return tuple(c)

def shift(c,p):
    # f(T-1), Horner
    res=(c[-1],)
    for a in reversed(c[:-1]):
        res=list(mul(res,(p-1,1),p));res[0]=(res[0]+a)%p
        res=tuple(res)
    return res

def scale(c,l,p):
    d=len(c)-1
    return tuple((v*pow(l,d-i,p))%p for i,v in enumerate(c))

def invert(c,p):
    return tuple(v*pow(c[0],-1,p)%p for v in reversed(c))

def run(p):
    A=irreducibles(p,2);B=irreducibles(p,3)
    assert len(A)==(p*p-p)//2 and len(B)==(p**3-p)//3
    seen=set(); groups=Counter(); total=len(A)*len(B); lam=primitive(p)
    for seed in product(A,B):
        if seed in seen:continue
        queue=[seed];seen.add(seed)
        for x,y in queue:
            for action in (lambda c:shift(c,p),lambda c:scale(c,lam,p),lambda c:invert(c,p)):
                z=(action(x),action(y))
                if z not in seen:seen.add(z);queue.append(z)
        orbit=len(queue); size=p*(p*p-1)
        assert size%orbit==0
        groups[size//orbit]+=1
    expected= (p*(p-1)+4)//6 if p%3==2 else p*(p-1)//6
    assert len(seen)==total and sum(groups.values())==expected,(p,total,groups,expected)
    assert groups.get(3,0)==(1 if p%3==2 else 0)
    assert all(s in (1,3) for s in groups)
    print(f'p={p}: degree2={len(A)} degree3={len(B)} pairs={total} orbits={expected} stabilizers={dict(groups)} OK')

if __name__=='__main__':
    for p in (2,3,5,7,11,13):run(p)
    print('VERIFY_OK')
