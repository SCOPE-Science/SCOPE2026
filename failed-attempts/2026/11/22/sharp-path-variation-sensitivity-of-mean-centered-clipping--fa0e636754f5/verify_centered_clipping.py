#!/usr/bin/env python3
"""Exact-rational checks for centered clipping in finite-path variation."""
from fractions import Fraction as F
from itertools import product
import random


def var(z):
    return sum((abs(b-a) for a,b in zip(z,z[1:])),F(0))


def clip(a, t=F(1)):
    return max(-t,min(t,a))


def transform(x,t=F(1)):
    mu=sum(x,F(0))/len(x)
    return [mu+clip(a-mu,t) for a in x]


def sharp(n):
    return F(2*(n*n//4),n)


def active_mask(n,j):
    # j is cut position (1..n-1); boundary sites j-1,j are both active.
    return [((j-1-i)%2==0) if i<j else ((i-j)%2==0) for i in range(n)]


def base_point(n,j):
    mask=active_mask(n,j)
    clipped=[i for i,d in enumerate(mask) if not d]
    c=len(clipped)
    x=[F(0)]*n
    if c==1:
        x[clipped[0]]=F(3,2)
        for i,d in enumerate(mask):
            if d:x[i]=-F(3,2*(n-1))
    elif c>=2:
        a=(c+1)//2; b=c-a
        for i in clipped[:a]:x[i]=F(2)
        for i in clipped[a:]:x[i]=-F(2*a,b)
    assert sum(x)==0
    assert all((abs(z)<1 if d else abs(z)>1) for z,d in zip(x,mask))
    return x


def witness(n):
    j=n//2
    x=base_point(n,j)
    h=[F(0) if i<j else F(1) for i in range(n)]
    eps=F(1,1000*n)
    y=[a+eps*b for a,b in zip(x,h)]
    lhs=var([a-b for a,b in zip(transform(y),transform(x))])
    rhs=var([a-b for a,b in zip(y,x)])
    assert lhs==sharp(n)*rhs,(n,lhs,rhs,sharp(n))
    return lhs/rhs


def exhaustive(n):
    best=F(0)
    for j in range(1,n):
        mu=F(n-j,n)
        cutbest=F(0)
        for mask in product((False,True),repeat=n):
            a=[(F(0) if mask[i] else mu) if i<j else (F(1) if mask[i] else mu) for i in range(n)]
            cutbest=max(cutbest,var(a))
        assert cutbest==F(2*j*(n-j),n),(n,j,cutbest)
        best=max(best,cutbest)
    assert best==sharp(n)


def random_stress():
    rng=random.Random(20261116)
    trials=2400
    for _ in range(trials):
        n=rng.randint(2,36)
        t=F(rng.randint(1,9),rng.randint(1,7))
        x=[F(rng.randint(-31,31),rng.randint(1,8)) for _ in range(n)]
        y=[F(rng.randint(-31,31),rng.randint(1,8)) for _ in range(n)]
        tx=transform(x,t);ty=transform(y,t)
        assert var(tx)<=var(x)
        assert var(ty)<=var(y)
        lhs=var([u-v for u,v in zip(tx,ty)])
        rhs=var([u-v for u,v in zip(x,y)])
        assert lhs<=sharp(n)*rhs
        c=F(rng.randint(-9,9),rng.randint(1,6))
        assert transform([z+c for z in x],t)==[z+c for z in tx]
    return trials


if __name__=='__main__':
    for n in range(2,11): exhaustive(n)
    print('EXACT_ALL_ACTIVE_MASKS_AND_STEP_CUTS_PASS n=2..10')
    for n in range(2,101): witness(n)
    print('EXACT_STRICT_MASK_LOCAL_WITNESSES_PASS n=2..100')
    k=random_stress()
    print('RANDOM_RATIONAL_TWO_INPUT_AND_ONE_INPUT_PASS trials='+str(k))
    print('CENTERED_CLIPPING_VARIATION_ALL_CHECKS_PASS')
