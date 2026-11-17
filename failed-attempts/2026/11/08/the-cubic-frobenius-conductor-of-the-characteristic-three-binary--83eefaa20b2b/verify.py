#!/usr/bin/env python3
"""Exact symbolic identities and finite-field sanity checks for a binary cubic discriminant."""
from itertools import product

P = 3

def clean(p):
    return {k: v % P for k, v in p.items() if v % P}

def add(*polys):
    q = {}
    for p in polys:
        for m, v in p.items(): q[m] = (q.get(m, 0) + v) % P
    return clean(q)

def neg(p):
    return clean({m:-v for m,v in p.items()})

def mul(p,q):
    r={}
    for m,v in p.items():
        for n,w in q.items():
            e=tuple(a+b for a,b in zip(m,n))
            r[e]=(r.get(e,0)+v*w)%P
    return clean(r)

def power(p,k):
    res={tuple([0]*len(next(iter(p)))):1}
    for _ in range(k):res=mul(res,p)
    return res

def der(p,i):
    q={}
    for m,v in p.items():
        if m[i]:
            n=list(m);n[i]-=1;n=tuple(n)
            q[n]=(q.get(n,0)+v*m[i])%P
    return clean(q)

def variable(i,n):
    m=[0]*n;m[i]=1
    return {tuple(m):1}

def substitute(p,imgs):
    n=len(next(iter(imgs[0])))
    z={tuple([0]*n):1}
    r={}
    for exp,coeff in p.items():
        term={tuple([0]*n):coeff}
        for i,v in enumerate(exp):term=mul(term,power(imgs[i],v))
        r=add(r,term)
    return r

A,B,C,D=[variable(i,4) for i in range(4)]
disc=add(mul(power(B,2),power(C,2)), neg(mul(A,power(C,3))), neg(mul(power(B,3),D)))
partials=[neg(power(C,3)),neg(mul(B,power(C,2))),neg(mul(power(B,2),C)),neg(power(B,3))]
assert [der(disc,i) for i in range(4)]==partials
assert all(sum(m[1:3])>=3 for m in disc)
print('DISCRIMINANT_AND_JACOBIAN_IDENTITIES_PASSED')
S,T,U,V=[variable(i,4) for i in range(4)]
para=[mul(power(S,2),U),add(mul(power(S,2),V),neg(mul(S,mul(T,U)))),
      add(mul(power(T,2),U),neg(mul(S,mul(T,V)))),mul(power(T,2),V)]
assert not substitute(disc,para)
lam=add(mul(S,V),neg(mul(T,U)))
assert para[1]==mul(S,lam) and para[2]==neg(mul(T,lam))
print('GLOBAL_PARAMETRIZATION_AND_DIAGONAL_PASSED')
# Affine chart a=1, s=u=1: ring of the normalization k[b,t]
b,t,d=[variable(i,3) for i in range(3)]
c=neg(mul(b,t)); relation=add(power(t,3),mul(b,power(t,2)),neg(d))
# In k[b,t,d]/(relation), cubic equation follows from (b^3)*relation.
r=add(mul(power(b,2),power(c,2)),neg(power(c,3)),neg(mul(power(b,3),d)))
assert r==mul(power(b,3),relation)
# The R-lattice in the free k[b,d]-module S=k[b,d]{1,t,t^2}
# is A*1 + A*(b*t) + A*(b^2*t^2). Multiplication modulo t^3=d-b*t^2
# gives the conductor exactly b^2*S, hence (b^2,b*c,c^2) inside R.
assert mul(power(b,2),t)==neg(mul(b,c))
assert mul(power(b,2),power(t,2))==power(c,2)
print('AFFINE_NORMALIZATION_AND_CONDUCTOR_IDENTITIES_PASSED')

def field(q):
    if q==3:
        els=[(i,0) for i in range(3)]
    elif q==9:
        els=[(i,j) for i in range(3) for j in range(3)]
    else: raise ValueError(q)
    z=(0,0);one=(1,0)
    def plus(a,b):return ((a[0]+b[0])%3,(a[1]+b[1])%3)
    def minus(a,b):return ((a[0]-b[0])%3,(a[1]-b[1])%3)
    def times(a,b):return ((a[0]*b[0]-a[1]*b[1])%3,(a[0]*b[1]+a[1]*b[0])%3)
    def pw(a,n):
        r=one
        while n:
            if n&1:r=times(r,a)
            a=times(a,a);n//=2
        return r
    def div(a,b):return times(a,pw(b,q-2))
    def canonical(t):
        if not any(x!=z for x in t): raise AssertionError
        first=next(x for x in t if x!=z)
        return tuple(div(x,first) for x in t)
    points=[]
    for i in range(4):
        for tail in product(els,repeat=3-i):
            points.append((z,)*i + (one,)+tail)
    def cubic_check(x):
        a,b,c,d=x
        return plus(minus(times(times(b,b),times(c,c)),times(a,pw(c,3))),minus(z,times(pw(b,3),d)))==z
    X={p for p in points if cubic_check(p)}
    p1=[(one,t) for t in els]+[(z,one)]
    imgs=set()
    for s,t in p1:
        for u,v in p1:
            ss=times(s,s);tt=times(t,t)
            a=times(ss,u);b=minus(times(ss,v),times(times(s,t),u))
            c=minus(times(tt,u),times(times(s,t),v));d=times(tt,v)
            imgs.add(canonical((a,b,c,d)))
    assert X==imgs and len(X)==(q+1)**2,(q,len(X),len(imgs))
    print(f'GF({q})_PROJECTIVE_EXHAUSTION_PASSED: {len(X)} discriminant points')

for q in (3,9):field(q)
print('ALL_CHECKS_PASSED')
