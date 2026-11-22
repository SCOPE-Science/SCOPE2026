#!/usr/bin/env python3
"""Standalone arithmetic checker for the Schinzel candidate-pole-index fibre theorem."""
from math import gcd

P=11
F=[1,0,-2,-6,-2,0,1]  # ascending coefficients

def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def divrem(a,b):
    a=trim([x%P for x in a]); b=trim([x%P for x in b]);
    q=[0]*max(1,len(a)-len(b)+1)
    inv=pow(b[-1],-1,P)
    while len(a)>=len(b) and a!=[0]:
        t=(a[-1]*inv)%P; k=len(a)-len(b); q[k]=t
        for i in range(len(b)):a[i+k]=(a[i+k]-t*b[i])%P
        a=trim(a)
    return trim(q),trim(a)

def gcdpoly(a,b):
    a=trim(a[:]);b=trim(b[:]);
    while b!=[0]: a,b=b,divrem(a,b)[1]
    if a!=[0]:
        z=pow(a[-1],-1,P);a=[(x*z)%P for x in a]
    return a

def mulmod(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):r[i+j]=(r[i+j]+x*y)%P
    return divrem(r,F)[1]

def powmod(a,k):
    r=[1]
    while k:
        if k&1:r=mulmod(r,a)
        a=mulmod(a,a);k//=2
    return r

x=[0,1]; v=x
for j in range(1,7):
    v=powmod(v,11)
    if j in (2,3):
        target=v[:]+[0]*max(0,2-len(v));target[1]=(target[1]-1)%P
        assert gcdpoly(F,trim(target))==[1],j
    if j==6:assert v==x
print('irreducible modulo 11: Frobenius and GCD tests PASS')

from collections import defaultdict

def direct(H):
    dic=defaultdict(int)
    for k2 in range(H//4+1):
      for k5 in range((H-4*k2)//3+1):
       for k6 in range((H-4*k2-3*k5)//3+1):
        extra=H-4*k2-3*k5-3*k6
        for k3 in range(extra+1):
         k4=extra-k3
         a=2*k2+k4+k5+2*k6
         b=2*k2+k3+2*k5+k6
         dic[a,b]+=1
    return dic

# Product (1-x^2y^2)^-1(1-y)^-1(1-x)^-1(1-xy^2)^-1(1-x^2y)^-1.
def product(H):
    a={(0,0):1}
    for u,v in [(2,2),(0,1),(1,0),(1,2),(2,1)]:
       nxt=defaultdict(int)
       for (r,s),c in a.items():
          for m in range(H//(u+v)+1):
              if r+s+m*(u+v)>H:break
              nxt[(r+u*m,s+v*m)]+=c
       a=nxt
    return a

# Coefficients of 1/(1-t)^2(1-t^3)^2(1-t^4).
def totals(H):
    values=[0]*(H+1)
    for i in range(H//4+1):
      for j in range((H-4*i)//3+1):
       n=H-4*i-3*j
       values[H]+=(j+1)*(n+1)
    return values[H]

whole=product(45)
for h in range(46):
    sub=direct(h)
    assert all(whole.get(k,0)>=v for k,v in sub.items())
    for (a,b),v in sub.items():
        assert whole[a,b]==sum(direct(j).get((a,b),0) for j in range(h+1)) # same weight exactly a+b
    assert sum(sub.values())==totals(h)
    assert all(whole.get((a,h-a),0)>=1 for a in range(h+1))
print('fibres and degree totals through h=45: PASS')
for h in range(12):
    print(h, totals(h), 'fibres', [whole.get((a,h-a),0) for a in range(h+1)])
